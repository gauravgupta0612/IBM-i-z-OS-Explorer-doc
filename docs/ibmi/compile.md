# Compile

## How to compile

- In an open member: press ++ctrl+e++, or click the **⚙ Compile Current Member** button in the editor title bar.
- In the tree: click the **⚙** icon on a member, or right-click → **Compile**.

What happens:

1. Unsaved changes are saved.
2. The compile command for the member's **source type** is shown, already filled in. You can edit it before pressing ++enter++.
3. The command runs, and its messages appear in **Output → IBM i & z/OS**.
4. If the command contains `OPTION(*EVENTF)`, errors and warnings are read from the event file and shown in the **Problems** panel (++ctrl+shift+m++) on the right lines.

| Severity | Shown as |
|---|---|
| 30 and higher | Error |
| 20 | Warning |
| below 20 | Information |

## Default commands

| Type | Command |
|---|---|
| RPGLE | `CRTBNDRPG PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) DBGVIEW(*SOURCE) OPTION(*EVENTF)` |
| SQLRPGLE | `CRTSQLRPGI OBJ(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) OBJTYPE(*PGM) DBGVIEW(*SOURCE) OPTION(*EVENTF)` |
| RPG | `CRTRPGPGM PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR)` |
| CLLE | `CRTBNDCL PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) DBGVIEW(*SOURCE)` |
| CLP | `CRTCLPGM PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR)` |
| CBLLE | `CRTBNDCBL PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) DBGVIEW(*SOURCE)` |
| SQLCBLLE | `CRTSQLCBLI OBJ(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) OBJTYPE(*PGM)` |
| PF / LF | `CRTPF` / `CRTLF FILE(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR)` |
| DSPF / PRTF | `CRTDSPF` / `CRTPRTF FILE(&OBJLIB/&MBR) …` |
| CMD | `CRTCMD CMD(&OBJLIB/&MBR) PGM(&OBJLIB/&MBR) …` |
| SQL | `RUNSQLSTM SRCFILE(&LIB/&FILE) SRCMBR(&MBR) COMMIT(*NONE) NAMING(*SQL)` |

Variables:

| Variable | Replaced by |
|---|---|
| `&LIB` | Library of the source |
| `&FILE` | Source file |
| `&MBR` | Member name |
| `&OBJLIB` | The connection's **object library**, or the source library if none is set |

## Change the commands

**Settings** → search `mainframe.ibmi.compileCommands` → **Edit in settings.json**:

```json
"mainframe.ibmi.compileCommands": {
  "RPGLE": "CRTBNDRPG PGM(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) DBGVIEW(*LIST) OPTION(*EVENTF) TGTRLS(V7R3M0)",
  "MODULE": "CRTRPGMOD MODULE(&OBJLIB/&MBR) SRCFILE(&LIB/&FILE) SRCMBR(&MBR) OPTION(*EVENTF)"
}
```

!!! note
    Setting this object **replaces** all defaults, so include every type you use. Types without a command make you type the command each time.

## Object library

Right-click the connection → **Edit Connection** → press ++enter++ through the prompts → **Object library for compiles**. Leave it empty to compile into the source library.
