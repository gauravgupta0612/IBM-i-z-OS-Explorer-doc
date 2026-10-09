# Data sets & members

## Filters

Under **Data Sets**, click the **filter** icon (**Add Data Set Filter**) and type a pattern:

| Pattern | Shows |
|---|---|
| `USER01.*` | Data sets with exactly one qualifier after `USER01` |
| `USER01.**` | Every data set under `USER01` |
| `SYS1.PROCLIB` | Exactly that data set |
| `PROD.*.COBOL` | `PROD.<anything>.COBOL` |

Remove a filter with the **×** next to it. The list is limited by `mainframe.zos.maxItems` (default 500).

Each data set shows its **DSORG RECFM LRECL VOLSER**. The icons show:

| Icon | Meaning |
|---|---|
| :material-library: | Partitioned (PDS/PDSE): expand it for members |
| :material-file: | Sequential: click to open |
| :material-cloud: | Migrated: click to **recall** |

## Open, edit and save

- Click a **member** or a **sequential data set** to open it in the editor.
- Edit, then press ++ctrl+s++: the content is written back to the mainframe.
- **Conflict protection:** if someone else changed the member after you opened it, z/OSMF refuses the save (HTTP 412). You can then cancel or **Overwrite**.
- Syntax highlighting follows the last qualifier:

| Last qualifier | Language |
|---|---|
| `JCL`, `CNTL`, `PROCLIB`, `PROC`, `JCLLIB` | JCL |
| `COBOL`, `CBL`, `COB` | COBOL |
| `COPY`, `COPYLIB`, `CPY` | COBOL copybook |
| `REXX`, `EXEC`, `CLIST` | REXX |
| `ASM`, `MACLIB` | Assembler |
| `SQL`, `DDL` | SQL |

## Create

**Allocate a data set:** right-click **Data Sets** or a filter → **Create Data Set** → name → preset:

| Preset | DSORG | RECFM / LRECL | Space |
|---|---|---|---|
| PDSE – source | PO (LIBRARY) | FB 80 | 5 CYL + 5, 10 dir blocks |
| PDS – source | PO | FB 80 | 5 CYL + 5, 20 dir blocks |
| PDS – load library | PO | U, BLKSIZE 32760 | 5 CYL + 5 |
| Sequential | PS | FB 80 | 1 CYL + 1 |
| Sequential | PS | VB 255 | 1 CYL + 1 |
| Sequential – print | PS | FBA 133 | 1 CYL + 1 |

**Create a member:** right-click a PDS → **Create Member**. The new, empty member opens in the editor.

**Upload:** right-click a PDS → **Upload Local File to Member / USS**. Pick one or more files. Each member name is the file name without its extension, cut to 8 characters.

## Delete

Right-click a member or data set → **Delete**. You are asked to confirm; this can't be undone.

## Submit

Right-click a JCL member or sequential data set → **Submit as Job**. See [Jobs & JCL](jobs.md).
