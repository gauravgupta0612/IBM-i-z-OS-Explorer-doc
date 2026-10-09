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
| `mainframe.zos.jobCard` | string | *(empty)* | Job card used by JCL templates. Variables: ${JOBNAME} ${USER} ${ACCOUNT}. Empty = //${JOBNAME} JOB (${ACCOUNT}),'${USER}',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID |
| `mainframe.zos.loadLibrary` | string | *(empty)* | Load library used by JCL templates (${LOADLIB}). Empty = <USER>.LOAD |
| `mainframe.zos.copyLibrary` | string | *(empty)* | Copybook library used by JCL templates (${COPYLIB}). Empty = <USER>.COPYLIB |
| `mainframe.zos.jclTemplates` | object | `{}` | Your own JCL templates: name → JCL text (string or array of lines). Variables: ${JOBCARD} ${JOBNAME} ${USER} ${ACCOUNT} ${MEMBER} ${SRCLIB} ${LOADLIB} ${COPYLIB}. Added to the built-in templates. |

## Example

```json
{
  "mainframe.zos.encoding": "IBM-037",
  "mainframe.zos.tsoAccount": "ACCT123",
  "mainframe.zos.jobCard": "//${JOBNAME} JOB (ACCT123),'${USER}',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID",
  "mainframe.zos.loadLibrary": "DEV.TEAM.LOAD",
  "mainframe.zos.copyLibrary": "DEV.TEAM.COPYLIB",
  "mainframe.ibmi.tempDir": "/tmp",
  "mainframe.ibmi.sourceCcsid": 1208
}
```

More on the z/OS template settings: [JCL templates & snippets](../zos/jcl-templates.md). IBM i compile commands: [Compile](../ibmi/compile.md).

## Per-connection settings

These are set in the tree or through **Edit Connection**, not in settings.json:

| Setting | Platform | Where |
|---|---|---|
| Host, port, user | both | Edit Connection |
| Protocol (HTTPS/HTTP), certificate check | z/OS | Edit Connection |
| Password or SSH key file | IBM i | Edit Connection |
| Object library for compiles | IBM i | Edit Connection |
| Library list, current library | IBM i | Library List node |
| Filters (data sets, jobs, USS, libraries, IFS) | both | Tree |
| Favorites | both | Right-click → Add to Favorites |
