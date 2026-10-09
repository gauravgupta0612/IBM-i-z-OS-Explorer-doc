# Architecture (for contributors)

The extension is written in TypeScript, bundled with esbuild into one file (`dist/extension.js`), and has a single runtime dependency, **ssh2**, for IBM i. The z/OS side uses only Node's `https` module.

## Overview

```text
                 ┌──────────────────────── VS Code ────────────────────────┐
  Activity bar → │ ZosTree / IbmiTree (ui/trees.ts)                         │
                 │   └ Node(ctx = contextValue, pid = connection id, data)  │
  Commands     → │ commands.ts · zos/zosCommands.ts · ibmi/ibmiCommands.ts │
                 │ general.ts (favorites, compare, export/import)          │
  Editors      → │ MainframeFS  "mf:"     (fsProvider.ts) read/write files │
                 │ SpoolProvider "mfspool:" read-only spool, job logs      │
                 └───────────────┬────────────────────────────┬────────────┘
                                 │ Sessions (one client per connection)
                     ┌───────────▼──────────┐       ┌─────────▼──────────┐
                     │ ZosmfClient          │       │ IbmiClient         │
                     │ zos/zosmf.ts (HTTPS) │       │ ibmi/ibmiClient.ts │
                     └───────────┬──────────┘       │ SSH exec + SFTP    │
                                 │                  └─────────┬──────────┘
                           z/OSMF REST                 IBM i SSH daemon
```

## Key modules

| File | Responsibility |
|---|---|
| `extension.ts` | Activation: registers the file systems, tree views, commands, status bar |
| `profiles.ts` | `Profile` model, `ProfileStore` (globalState + SecretStorage), connection wizard |
| `sessions.ts` | Creates and caches one `ZosmfClient` / `IbmiClient` per connection; `reset()` after edits |
| `fsProvider.ts` | `mf:` file system, URI builders (`uris.*`), `parseUri()`, language extension mapping |
| `ui/trees.ts` | Tree data providers. Every node has `ctx` (used in `package.json` menus), `pid` and `data` |
| `ui/helpers.ts` | `Ui`: command registration, connection picker, confirmations, history input |
| `ui/sqlView.ts` | SQL result grid (webview) |
| `log.ts` | Output channel, `guard()` = progress + error handling for every host call |

## z/OS: `ZosmfClient`

All methods are `async` and throw `ZosmfError` (with `status` and `body`) for HTTP errors ≥ 400.

| Method | z/OSMF call |
|---|---|
| `info()` | `GET /zosmf/info` |
| `listDatasets(filter)` | `GET /restfiles/ds?dslevel=` |
| `listMembers(ds, pattern?)` | `GET /restfiles/ds/{ds}/member` |
| `readDataset(ds, member?)` → `{text, etag}` | `GET /restfiles/ds/{ds(member)}` |
| `writeDataset(ds, member, text, etag?)` | `PUT` with `If-Match` |
| `createDataset(ds, options)` / `deleteDataset(ds, member?)` | `POST` / `DELETE` |
| `copyMember(fromDs, fromMbr, toDs, toMbr, replace)` | `PUT {request: "copy"}` (`'*'` copies all members) |
| `renameMember()` / `renameDataset()` | `PUT {request: "rename"}` |
| `datasetAttributes(ds)` | `GET ds?dslevel=` with `X-IBM-Attributes: base,total` |
| `recallDataset(ds)` | `PUT {request: "hrecall"}` |
| `listUss / readUss / writeUss / createUss / deleteUss` | `/restfiles/fs` |
| `listJobs(owner, prefix)` / `jobStatus()` | `GET /restjobs/jobs` |
| `listSpool()` / `readSpool()` / `jobJcl()` | `GET …/files`, `…/files/{id}/records`, `…/files/JCL/records` |
| `submitJcl(text)` / `submitDataset(dsn)` | `PUT /restjobs/jobs` |
| `cancelJob()` / `purgeJob()` | `PUT {request: "cancel"}` / `DELETE` |
| `tso(cmd)` | start → send → receive until prompt → stop (`/zosmf/tsoApp/tso`) |
| `console(cmd)` | `PUT /restconsoles/consoles/defcn` |

### z/OS URIs

| URI | Meaning |
|---|---|
| `mf://<pid>/zds/<DSN>/<MEMBER>.<ext>` | Partitioned member |
| `mf://<pid>/zdsps/<DSN>.<ext>` | Sequential data set |
| `mf://<pid>/zuss/<path>` | USS file |
| `mfspool://<pid>/zjob/<JOB>/<JOBID>/<id>/<dd>.log` | One spool file (read-only) |
| `mfspool://<pid>/zjoball/<JOB>/<JOBID>.log` | All spool files of a job |

The extension `<ext>` only selects the editor language (`zosExt()` maps the last qualifier: JCL, COBOL, COPY…).

### z/OS tree contexts

`zos-dsRoot`, `zos-dsFilter`, `zos-ds-po`, `zos-ds-ps`, `zos-member`, `zos-ussRoot`, `zos-ussPath`, `zos-ussDir`, `zos-ussFile`, `zos-jobRoot`, `zos-jobFilter`, `zos-job`, `zos-spool`, `zos-favRoot`, `favorite`.

## IBM i: `IbmiClient`

| Method | Implementation |
|---|---|
| `exec(cmd)` / `execScript(interpreter, script)` | SSH exec (script on stdin) |
| `cl(cmd)` | PASE `system`, or Qshell with `liblist` when a library list / current library is set |
| `sql(stmt)` | `db2util -o json`, or Qshell `db2 -f` parsed by `parseDb2Output()` |
| `readMember` / `writeMember` | `CPYTOSTMF` / `CPYFRMSTMF` + SFTP |
| `listLibraries / listObjects / listSourceFiles / listMembers` | QSYS2 SQL services |
| `searchMembers(lib, files, term)` | Qshell `grep -inF` over `/QSYS.LIB/…/*.MBR` |
| `searchIfs(dir, term)` | PASE `grep -rniIF` |
| `listSpool / readSpool / deleteSpool` | `OUTPUT_QUEUE_ENTRIES_BASIC`, `CPYSPLF *TOSTMF`, `DLTSPLF` |
| `listActiveJobs / jobLog / endJob` | `ACTIVE_JOB_INFO`, `JOBLOG_INFO`, `ENDJOB` |
| `listMessages / messageHelp / replyMessage` | `MESSAGE_QUEUE_INFO`, `SNDRPY` |
| `deleteObject / renameObject / printOutput` | `DLTOBJ`, `RNMOBJ`, any command with `OUTPUT(*PRINT)` |

## Adding a z/OS feature, step by step

Example: a "Show member statistics" command.

1. **Client:** add a method to `ZosmfClient`:

    ```ts
    async memberStats(ds: string, member: string) {
      const r = await this.request('GET', `/zosmf/restfiles/ds/${encodeURIComponent(ds)}/member?pattern=${member}`,
        undefined, { 'X-IBM-Attributes': 'base' });
      return this.json(r).items?.[0];
    }
    ```

2. **Command:** register it in `zos/zosCommands.ts`:

    ```ts
    reg('mf.zos.memberStats', async (n: Node) => {
      const s = await guard('Reading statistics', () => sessions.zosClient(n.pid).memberStats(n.data.ds, n.data.member));
      if (s) { await ui.openText(JSON.stringify(s, null, 2), 'json'); }
    });
    ```

3. **Manifest:** in `package.json`, declare the command in `contributes.commands`, show it on members with
   `{"command": "mf.zos.memberStats", "when": "viewItem == zos-member", "group": "5_info@2"}` in `menus.view/item/context`, and hide it from the Command Palette (`"when": "false"` under `menus.commandPalette`) because it needs a tree item.
4. **Test** with F5, then add tests against a mock HTTP server (see below).
5. **Document** it on this site and add a line to `CHANGELOG.md`.

## Testing without a mainframe

- **z/OS:** start a small Node `http` server that answers the z/OSMF URLs you call, and create `ZosmfClient` with `secure: false` and the server's port.
- **IBM i:** use `ssh2`'s `Server` class to answer `exec` requests with canned output (for example Qshell `db2` tables or `grep` lines).
- **Without VS Code:** stub the `vscode` module (only `window.createOutputChannel` is needed for the clients).

## Conventions

- Every host call from a command goes through `guard(title, fn)`, which shows progress, logs errors and shows them to the user.
- Destructive actions ask for confirmation with `ui.confirm()`.
- Never log passwords; `ZosmfClient` logs only method and path, and `IbmiClient` only the command.
- Keep `package.json` menus, `src` registrations and the [Commands](../reference/commands.md) page in sync.
