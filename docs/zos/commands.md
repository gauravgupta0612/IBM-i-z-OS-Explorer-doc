# TSO & console commands

Right-click a z/OS connection, or use the Command Palette (++ctrl+shift+p++):

## TSO command

**z/OS: Issue TSO Command**, for example:

```text
LISTCAT LEVEL(USER01)
TIME
STATUS
LISTDS 'SYS1.PROCLIB' MEMBERS
```

The extension starts a TSO address space, sends the command, collects the output until the TSO prompt comes back, and then ends the address space. The output appears in **Output → IBM i & z/OS**.

The TSO address space uses these settings:

| Setting | Default |
|---|---|
| `mainframe.zos.tsoAccount` | `ACCT#`: replace it with your account number |
| `mainframe.zos.tsoProc` | `IKJACCNT`: your logon procedure |

## MVS console command

**z/OS: Issue MVS Console Command**, for example:

```text
D IPLINFO
D A,L
D T
D GRS,C
```

The command is sent through the z/OSMF default console (`defcn`), and the response is shown in the output channel.

!!! warning
    Console commands run with your RACF authority on the **operator console**. Only use commands you are allowed to issue.

## History

Both prompts remember your last 50 commands. Start typing to filter them, or pick one from the list.
