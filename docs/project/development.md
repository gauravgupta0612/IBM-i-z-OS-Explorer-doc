# Development

## Requirements

- **Node.js 18+** (20 LTS recommended)
- **VS Code 1.85+**
- **Git**

## Get the source

```bash
git clone https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer.git
cd IBM-i-z-OS-Explorer
npm install
```

## Run and debug

=== "One click (Windows)"

    Double-click **`start-debug.bat`** and choose:

    | Key | Action |
    |---|---|
    | **1** | Run the extension in a new window |
    | **2** | Open the project in VS Code for debugging with F5 |
    | **3** | Build the `.vsix` |

=== "VS Code"

    1. **File → Open Folder…** → the project folder.
    2. **Run and Debug** (++ctrl+shift+d++) → **Run Extension (F5)** → ++f5++.
    3. A second window **[Extension Development Host]** opens with the extension loaded.
    4. Set breakpoints in any `src/*.ts` file; source maps are generated.
    5. After a change, press ++ctrl+shift+f5++ to restart.

    Pick **Run Extension (watch mode)** to rebuild on every save, then press ++ctrl+r++ in the Development Host window to reload it.

## npm scripts

| Script | What it does |
|---|---|
| `npm run compile` | Type-check (`tsc --noEmit`) and bundle with esbuild into `dist/extension.js` (with source maps) |
| `npm run watch` | Rebuild on every change |
| `npm run check-types` | Type-check only |
| `npm run package` | Production build (minified) and `ibmi-zos-explorer-<version>.vsix` |

## Project layout

```text
src/
  extension.ts        activation: views, file system, status bar
  commands.ts         connections, core z/OS + IBM i commands
  general.ts          favorites, compare with local, export/import connections
  profiles.ts         connection profiles, password storage, connection wizard
  sessions.ts         one live client per connection
  fsProvider.ts       "mf:" file system (open/save remote files) + read-only spool documents
  log.ts              output channel and error handling
  zos/zosmf.ts        z/OSMF REST client: data sets, USS, jobs, TSO, console
  zos/zosCommands.ts  search, copy/rename, download/upload, job JCL, JCL templates
  ibmi/ibmiClient.ts  SSH/SFTP client: CL, SQL, members, IFS, spool, jobs, messages
  ibmi/ibmiCommands.ts search, library list, object actions, message queues
  ui/helpers.ts       shared UI helpers (command registration, pickers, prompts)
  ui/trees.ts         sidebar trees for z/OS and IBM i
  ui/sqlView.ts       SQL result grid (webview)
  ui/terminal.ts      PASE SSH terminal
syntaxes/             TextMate grammars: JCL, CL, RPGLE, COBOL
snippets/             JCL, COBOL, RPGLE, CL snippets
media/                icons
.github/workflows/    build + release on tag
```

## Adding a command

1. Declare it in `package.json` → `contributes.commands` (and `menus` if it belongs in the tree).
2. Register it with `reg('mf.…', handler)` in the matching module (`zos/zosCommands.ts`, `ibmi/ibmiCommands.ts` or `general.ts`).
3. Put any host access in `ZosmfClient` or `IbmiClient`.
4. Document it here (the [Commands](../reference/commands.md) page) and in `CHANGELOG.md`.

See [Architecture](architecture.md) for the internals and a full example.

## This documentation

The documentation lives in [IBM-i-z-OS-Explorer-doc](https://github.com/gauravgupta0612/IBM-i-z-OS-Explorer-doc) and is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

```bash
pip install -r requirements.txt
python scripts/sync_changelog.py   # optional: refresh the changelog page
mkdocs serve                       # http://127.0.0.1:8000
```
