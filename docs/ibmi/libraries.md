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
