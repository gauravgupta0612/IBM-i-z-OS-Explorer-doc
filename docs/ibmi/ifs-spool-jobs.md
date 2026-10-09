# IFS, spool & jobs

## IFS

Under **IFS**, click **Add IFS Path** and enter a directory, for example `/home/GGUPTA` or `/www`.

| Action | How |
|---|---|
| Browse | Expand folders; folders come first, files show their size |
| Open / edit / save | Click a file, press ++ctrl+s++ |
| New file / folder | Right-click a folder → **Create IFS File** / **Create IFS Directory** |
| Delete | Right-click → **Delete IFS Entry**. You are asked to confirm, and folders are deleted with all their contents. |

IFS files are transferred unchanged over SFTP. Files in EBCDIC CCSIDs will look garbled; convert them to UTF-8 (CCSID 1208) first.

## My Spooled Files

Shows your spooled files, newest first (up to 300), with job, number, status, pages and creation time.

- **Click** a spooled file to open it (read-only text, via `CPYSPLF … TOFILE(*TOSTMF)`).
- **Right-click → Delete Spooled File** deletes it (`DLTSPLF`).
- Click the **refresh** icon on **My Spooled Files** to reload the list.

## My Active Jobs

Shows your active jobs with status, type, subsystem and current function. Jobs in `MSGW` show a warning icon.

- **Click** a job, or use **Show Job Log**, to open its job log: time, message ID, type and text.
- **Right-click → End Job** runs `ENDJOB … OPTION(*IMMED)`. You are asked to confirm first.
