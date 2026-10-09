# JCL templates & snippets

## JCL templates

**Generate JCL from Template…** (right-click a member, the editor context menu of a member, or the Command Palette) fills a JCL template for the selected member and opens it in a new editor. You review it, then press ++ctrl+alt+s++ to submit.

### Built-in templates

| Name | Procedure / program |
|---|---|
| COBOL compile + link (IGYWCL) | `IGYWCL` |
| COBOL compile, link & go (IGYWCLG) | `IGYWCLG` |
| Assemble + link (HLASM, ASMACL) | `ASMACL` |
| Run program (EXEC PGM) | `EXEC PGM=<member>` with `STEPLIB` |

### Variables

| Variable | Value |
|---|---|
| `${JOBCARD}` | The job card from `mainframe.zos.jobCard` (variables inside are filled too) |
| `${JOBNAME}` | First 7 characters of your user ID + `C` |
| `${USER}` | Your user ID |
| `${ACCOUNT}` | `mainframe.zos.tsoAccount` |
| `${MEMBER}` | The selected member |
| `${SRCLIB}` | The data set of the selected member |
| `${LOADLIB}` | `mainframe.zos.loadLibrary`, or `<USER>.LOAD` |
| `${COPYLIB}` | `mainframe.zos.copyLibrary`, or `<USER>.COPYLIB` |

JCL's own symbols, such as `&SYSUID` or `&&TEMP`, are left unchanged.

### Job card

Default:

```jcl
//${JOBNAME} JOB (${ACCOUNT}),'${USER}',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
```

To use your site's job card, set it once:

```json
"mainframe.zos.jobCard": "//${JOBNAME} JOB (D123,456),'${USER}',CLASS=T,MSGCLASS=H,REGION=0M,NOTIFY=&SYSUID"
```

### Add your own

`mainframe.zos.jclTemplates` maps a name to JCL text. Use a string with `\n`, or an array of lines. Your templates are listed after the built-in ones; a template with the same name as a built-in one replaces it.

## Snippets

In any editor of the right language, type the prefix and press ++tab++ (or ++ctrl+space++ to see the list).

=== "JCL"

    | Prefix | Inserts |
    |---|---|
    | `jobcard` | JOB statement |
    | `exec` | Program step with STEPLIB, SYSOUT, SYSPRINT |
    | `ddshr` / `ddnew` / `ddin` | DD for an existing data set / a new data set / in-stream data |
    | `iefbr14` | Allocate a PDSE |
    | `delete` | Delete a data set with IEFBR14 |
    | `iebcopy` | Copy PDS members |
    | `iebgener` | Copy a sequential data set |
    | `sort` | DFSORT step |
    | `idcams` / `ksds` | IDCAMS step / define a VSAM KSDS |
    | `ikjeft01` | TSO commands in batch |
    | `if` | IF / THEN / ENDIF |
    | `comment` | Comment box |

=== "COBOL"

    | Prefix | Inserts |
    |---|---|
    | `program` | Program skeleton |
    | `perform` / `varying` | PERFORM UNTIL / PERFORM VARYING |
    | `evaluate` | EVALUATE … WHEN … END-EVALUATE |
    | `if` | IF / ELSE / END-IF |
    | `readloop` | Sequential file read loop |
    | `execsql` | EXEC SQL … END-EXEC |
    | `call` | CALL … USING |

=== "RPGLE"

    | Prefix | Inserts |
    |---|---|
    | `free` | `**FREE` program with ctl-opt |
    | `proc` | `dcl-proc` with `dcl-pi` |
    | `dcl-pr` | Prototype for an external program |
    | `dcl-ds` | Qualified data structure |
    | `for` / `dow` / `select` / `monitor` | Control structures |
    | `execsql` / `cursor` | Embedded SQL select / cursor loop |

=== "CL"

    | Prefix | Inserts |
    |---|---|
    | `pgm` | CL program with error handling |
    | `dcl` | DCL variable |
    | `if` / `dowhile` | Control structures |
    | `monmsg` / `sndpgmmsg` | Messages |
    | `ovrdbf` / `sbmjob` | Override / submit job |
