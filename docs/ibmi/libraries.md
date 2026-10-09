# Libraries & members

## Add libraries

Under **Libraries**, click **Add Library Filter** (filter icon):

- A list of **all user libraries** (`*ALLUSR`) with their descriptions opens. Type to filter, tick one or more, and press ++enter++.
- To add a library that isn't listed (for example `QSYS` or `QGPL`), choose **Enter library name(s) manually…** and type names separated by commas.

Remove a library filter with the **×** next to it.

## What a library shows

| Entry | Icon | Action |
|---|---|---|
| **Source file** (e.g. `QRPGLESRC`) | :material-file-tree: | Expand it to list members |
| `*PGM` | :material-function: | — |
| `*SRVPGM` | :material-package-variant: | — |
| `*FILE` (data) | :material-table: | — |
| `*MODULE`, `*DTAARA`, others | | — |

Each member is listed as `NAME.type` with its text as description; hover it to see the last change date.

## Open, edit and save members

Click a member to open it. Press ++ctrl+s++ to save it back to the member.

!!! warning "Sequence numbers"
    Saving goes through `CPYFRMSTMF`, so source **sequence numbers and change dates are reset**.

## Create

| What | How |
|---|---|
| Source file | Right-click a library → **Create Source File** → name (e.g. `QRPGLESRC`) → record length (default `112`) |
| Member | Right-click a source file → **Create Member** → name → source type → text. The member opens straight away. |

Source types offered: `RPGLE`, `SQLRPGLE`, `CLLE`, `CBLLE`, `SQLCBLLE`, `PF`, `LF`, `DSPF`, `PRTF`, `CMD`, `SQL`, `RPGLEINC`, `TXT`.

## Search text in source

Right-click a **source file** (searches its members) or a **library** (searches all its source files) → **Search Text in Source…**.

The search runs on the IBM i with Qshell `grep` (case-insensitive, plain text). Hits are listed as `MEMBER.type:line`; pick one to open the member at that line.

## Object actions

Right-click any object in a library:

| Action | For | Runs | Shows |
|---|---|---|---|
| **Object Description (DSPOBJD)** | all objects | `DSPOBJD … DETAIL(*FULL) OUTPUT(*PRINT)` | Full object description in an editor |
| **Program References (DSPPGMREF)** | `*PGM`, `*SRVPGM`, `*MODULE` | `DSPPGMREF … OUTPUT(*PRINT)` | Files, programs and data areas the object uses |
| **File Fields (DSPFFD)** | `*FILE` | `DSPFFD … OUTPUT(*PRINT)` | Record formats and fields |
| **Query Data (first 1000 rows)** | `*FILE` | `select * from LIB.FILE fetch first 1000 rows only` | The SQL result grid |
| **Rename Object…** | all objects | `RNMOBJ` | |
| **Delete Object…** | all objects | `DLTOBJ` (asks for confirmation first) | |

The menu only shows the actions that apply to the object's type.

## Delete

Right-click a member → **Delete Member** (`RMVM`). You are asked to confirm first.

## Languages

| Source type | Editor language |
|---|---|
| RPGLE, SQLRPGLE, RPG, RPGLEINC | RPGLE (free and fixed format) |
| CLLE, CLP | CL |
| CBLLE, SQLCBLLE | COBOL |
| PF, LF, DSPF, PRTF | DDS (no colouring) |
| SQL | SQL |
