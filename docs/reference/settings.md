# Settings

Open **File → Preferences → Settings** (++ctrl+comma++) and search for **mainframe**.

| Setting | Type | Default | Description |
|---|---|---|---|
| `mainframe.zos.maxItems` | number | `500` | Maximum number of data sets / jobs returned per list request. |
| `mainframe.zos.encoding` | string | *(empty)* | Optional EBCDIC code page for data set read/write (e.g. IBM-1047, IBM-037). Empty = z/OSMF default. |
| `mainframe.zos.tsoAccount` | string | `ACCT#` | TSO account number used to start a TSO address space. |
| `mainframe.zos.tsoProc` | string | `IKJACCNT` | TSO logon procedure. |
| `mainframe.ibmi.tempDir` | string | `/tmp` | IFS directory used for temporary files when reading/writing source members. |
| `mainframe.ibmi.sourceCcsid` | number | `1208` | Stream file CCSID used when transferring source members (1208 = UTF-8). |
| `mainframe.ibmi.compileCommands` | object | *(see below)* | Compile command per source type. Variables: &LIB, &FILE, &MBR, &OBJLIB. |

## Examples

```json
{
  "mainframe.zos.encoding": "IBM-037",
  "mainframe.zos.tsoAccount": "ACCT123",
  "mainframe.zos.tsoProc": "IKJACCNT",
  "mainframe.zos.maxItems": 1000,
  "mainframe.ibmi.tempDir": "/tmp",
  "mainframe.ibmi.sourceCcsid": 1208
}
```

## Compile commands

`mainframe.ibmi.compileCommands` maps a **source type** to a CL command. See [Compile](../ibmi/compile.md) for the defaults and variables.

## Per-connection settings

These are set through **Edit Connection**, not in settings.json:

| Setting | Platform |
|---|---|
| Host, port, user | both |
| Protocol (HTTPS/HTTP), certificate check | z/OS |
| Password or SSH key file | IBM i |
| Object library for compiles | IBM i |
| Filters (data sets, jobs, USS, libraries, IFS) | both, from the tree |
