# z/OS developer workflow

This page walks through a complete COBOL **edit → compile → link → run → debug** cycle with the extension. The same pattern works for Assembler and any other language with a compile procedure.

!!! info "Before you start"
    You need a working [z/OS connection](../connections/zos.md). Your system programmer must have z/OSMF set up as described in [z/OSMF setup for system programmers](zosmf-setup.md).

## 1. Create your libraries (one time)

Right-click **Data Sets** → **Create Data Set** and allocate:

| Data set | Preset | Holds |
|---|---|---|
| `YOURID.COBOL` | PDSE – source (FB 80) | COBOL programs |
| `YOURID.COPYLIB` | PDSE – source (FB 80) | Copybooks |
| `YOURID.JCL` | PDSE – source (FB 80) | Your JCL |
| `YOURID.LOAD` | PDS – load library (U) | Link-edited programs |

??? tip "Or allocate all four with one job"
    Create a member in `YOURID.JCL`, type `iefbr14` and press ++tab++ to insert the snippet, then copy the DD statement once per library. Press ++ctrl+alt+s++ to submit.

The JCL templates use `YOURID.LOAD` and `YOURID.COPYLIB` by default. To use other libraries, set `mainframe.zos.loadLibrary` and `mainframe.zos.copyLibrary` (see [Settings](../reference/settings.md)).

## 2. Write the program

Right-click `YOURID.COBOL` → **Create Member** → `HELLO`. The member opens with COBOL highlighting. Type `program` and press ++tab++ for a skeleton, or paste:

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NAME            PIC X(20) VALUE 'z/OS'.
       PROCEDURE DIVISION.
       MAIN-PARA.
           DISPLAY 'HELLO FROM ' WS-NAME
           GOBACK.
```

Press ++ctrl+s++. The member is saved on the mainframe.

!!! warning "Columns matter"
    COBOL is column-sensitive: area A starts in column 8, area B in column 12, and code must end by column 72. VS Code shows the column at the bottom right. Add rulers with `"editor.rulers": [7, 11, 72]` for the `cobol` language.

## 3. Generate the compile JCL

With `HELLO` open, right-click in the editor → **Generate JCL from Template…** (or right-click the member in the tree), and choose a template:

| Template | What it does |
|---|---|
| **COBOL compile + link (IGYWCL)** | Compiles `YOURID.COBOL(HELLO)` and link-edits it into `YOURID.LOAD(HELLO)` |
| **COBOL compile, link & go (IGYWCLG)** | Same, then runs the program in the same job |
| **Assemble + link (HLASM, ASMACL)** | For Assembler sources |
| **Run program (EXEC PGM)** | Runs `HELLO` from `YOURID.LOAD` |

A new, unsaved JCL editor opens with everything filled in:

```jcl
//YOURIDC JOB (ACCT#),'YOURID',CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1),NOTIFY=&SYSUID
//* If the IGYWCL procedure is not found, uncomment and adjust:
//*       JCLLIB ORDER=(IGY.SIGYPROC)
//* Compile YOURID.COBOL(HELLO) and link-edit into YOURID.LOAD(HELLO)
//CL       EXEC IGYWCL,PARM.COBOL='LIB,LIST,MAP,XREF'
//COBOL.SYSIN  DD DISP=SHR,DSN=YOURID.COBOL(HELLO)
//COBOL.SYSLIB DD DISP=SHR,DSN=YOURID.COPYLIB
//LKED.SYSLMOD DD DISP=SHR,DSN=YOURID.LOAD(HELLO)
```

Review it. In particular, check the **job card** (account, class, MSGCLASS) and whether your site needs the `JCLLIB` line. Ask a colleague for a working job card once, then save it in `mainframe.zos.jobCard`.

## 4. Submit and read the output

Press ++ctrl+alt+s++ and choose **Wait & Show Output**. When the job ends you see its return code, and the complete spool opens.

| Return code | Meaning | What to do |
|---|---|---|
| `CC 0000` | Success | Run the program |
| `CC 0004` | Warnings | Check the warnings in the `SYSPRINT` of step `COBOL`; usually fine |
| `CC 0008` | Errors | The program wasn't linked. Search the compile listing for `IGY` messages with severity E. |
| `CC 0012` / `0016` | Severe errors | Same as above, or a missing data set |
| `JCL ERROR` | JCL problem | Look at `JESMSGLG` and `JESYSMSG` (data set names, procedure not found…) |
| `ABEND S806` | Program not found | The load library in `STEPLIB` is wrong, or the link step failed |
| `ABEND S0C7` | Data exception | Non-numeric data in a numeric field |
| `ABEND S0C4` | Protection exception | Bad address, often a subscript out of range |

!!! tip "Find the error fast"
    In the spool document, press ++ctrl+f++ and search for `IGY` (COBOL compiler messages) or `IEW` (binder messages). The line number in an `IGY` message is the line in your member.

## 5. Save the JCL for next time

Save the generated JCL as a member so you can resubmit it with one click:

1. Right-click `YOURID.JCL` → **Create Member** → `CLHELLO`.
2. Paste the JCL into it and press ++ctrl+s++.

From then on you can:

- right-click the member → **Submit as Job**, or
- in **Jobs**, right-click any previous run → **Resubmit Job**, or **View / Edit Job JCL** to change it first.

## 6. Run the program

Generate the **Run program (EXEC PGM)** template for `HELLO`, then submit it. `HELLO FROM z/OS` appears in the `SYSOUT` spool file of step `RUN`.

## 7. Everyday helpers

| Task | How |
|---|---|
| Find where a copybook or field is used | Right-click `YOURID.COBOL` → **Search Text in Data Set…** |
| Search all your libraries | Right-click the data set filter → **Search Text in All PDS of Filter…** |
| Make a backup copy of a member | Right-click → **Copy Member To…** → `YOURID.COBOL(HELLOBK)` |
| Work offline, or put a library in Git | Right-click the PDS → **Download All Members to Folder…** |
| Bring changes back from a local folder | Right-click the PDS → **Upload Folder into Data Set…** |
| Compare with your local copy | Right-click a member → **Compare with Local File…** |
| Keep important members at hand | Right-click → **Add to Favorites** |

## Your own templates

Add templates for your site's procedures (for example DB2 precompile or CICS translation) in `settings.json`:

```json
"mainframe.zos.jclTemplates": {
  "COBOL + DB2 precompile (site proc)": [
    "${JOBCARD}",
    "//PROCLIB  JCLLIB ORDER=(SYS2.PROCLIB)",
    "//COMP     EXEC DB2COBCL,MEM=${MEMBER}",
    "//PC.SYSIN DD DISP=SHR,DSN=${SRCLIB}(${MEMBER})",
    "//LKED.SYSLMOD DD DISP=SHR,DSN=${LOADLIB}(${MEMBER})"
  ]
}
```

See [JCL templates & snippets](jcl-templates.md) for all variables.
