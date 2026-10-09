# CL & SQL

## Run a CL command

Right-click an IBM i connection → **Run CL Command**, or use **IBM i: Run CL Command** from the Command Palette.

```text
DSPLIBL
CRTLIB LIB(TESTLIB) TEXT('Test library')
WRKOBJ OBJ(MYLIB/*ALL)
SNDMSG MSG('Hello') TOUSR(QSYSOPR)
```

- The command runs through PASE `system`, and its spooled output and messages appear in **Output → IBM i & z/OS** together with the exit code.
- If the command fails, an error message shows the last CPF message.
- Your last 50 commands are remembered.

!!! note "Interactive commands"
    Commands that need a 5250 screen (e.g. `WRKACTJOB` without `OUTPUT(*PRINT)`) can't display interactively. Use their `OUTPUT(*PRINT)` form or the matching SQL service.

## Run SQL

=== "From a prompt"

    Right-click a connection → **Run SQL**:

    ```sql
    select * from qsys2.library_list_info
    ```

=== "From an editor"

    Open or create any `.sql` file, then:

    - press ++ctrl+r++ (or click **▶ Run SQL Statement**) to run the statement **under the cursor**. Statements are separated by `;`;
    - select text to run only the **selection**.

    Lines starting with `--` are ignored.

## Result grid

`SELECT` results open in a panel next to the editor:

- click a **column header** to sort (numbers sort as numbers);
- type in **Filter rows…** to search all columns;
- **Export CSV** saves the full result to a file;
- `NULL` values are shown in grey italics.

Up to 5,000 rows are displayed (export includes all rows).

Statements that return no rows (`INSERT`, `UPDATE`, `CREATE`…) show a completion message instead.

## Useful SQL services

```sql
-- Jobs using the most CPU
select job_name, cpu_time from table(qsys2.active_job_info()) order by cpu_time desc fetch first 20 rows only;

-- Objects in a library
select objname, objtype, objtext from table(qsys2.object_statistics('MYLIB','*ALL'));

-- Messages in QSYSOPR
select message_timestamp, message_id, message_text from qsys2.message_queue_info
 where message_queue_name = 'QSYSOPR' order by message_timestamp desc fetch first 50 rows only;

-- PTF groups
select * from qsys2.group_ptf_info;
```
