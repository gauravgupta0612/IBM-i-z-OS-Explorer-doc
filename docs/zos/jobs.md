# Jobs & JCL

## Submit JCL

=== "From the editor"

    Open any JCL (a member or a local `.jcl` file) and either:

    - press ++ctrl+alt+s++,
    - click **▶ Submit JCL** in the editor title bar, or
    - right-click → **Submit JCL**.

    If text is selected, only the selection is submitted.

=== "From a member"

    Right-click a member or sequential data set → **Submit as Job**. z/OSMF submits it straight from the data set (`//'DSN(MEMBER)'`).

After submitting you get two choices:

- **Wait & Show Output**: polls the job every 2 seconds (for up to 4 minutes, and you can cancel), then shows the return code and opens the full spool.
- **Show Output Now**: opens the spool right away.

!!! note "Which system?"
    For a local `.jcl` file with more than one z/OS connection defined, you are asked which system to submit to.

## Job filters

Under **Jobs**, click **Add Job Filter**: **owner** (`*` for all) and **prefix** (`*` for all, or e.g. `PAY*`).

Each job shows **JOBNAME(JOBID)** with its status and return code:

| Icon | Meaning |
|---|---|
| :material-sync: spinning | Active |
| :material-check-circle:{ style="color: green" } | `CC 0000` or `CC 0004` |
| :material-alert-circle:{ style="color: red" } | ABEND, JCL ERROR, SEC ERROR or CC ≥ 0008 |
| :material-circle-outline: | Other (input, held, CC with no code…) |

## Spool output

- Expand a job to see its spool files (DD name, step, procstep, record count). Click one to open it.
- Click **Open All Spool Output** (output icon on the job) to open all spool files in one document, with a separator between them.
- Spool documents are **read-only**.

## View, edit and resubmit the JCL

Right-click a job:

- **View / Edit Job JCL**: opens the JCL exactly as it was submitted, in a new JCL editor. Change it if needed and press ++ctrl+alt+s++ to submit it again.
- **Resubmit Job**: submits the same JCL again straight away, then offers to wait for it and show the output.

## Cancel / purge

Right-click a job:

- **Cancel Job**: cancels an active or waiting job.
- **Purge Job**: removes the job and its output. You are asked to confirm first.
