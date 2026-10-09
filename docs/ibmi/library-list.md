# Library list & current library

Every CL command, compile and member transfer runs in a fresh IBM i job. By default that job gets the **library list of your user profile's job description**. To compile programs that use `/COPY` members, files or service programs from other libraries, add those libraries to the extension's **Library List**.

## The Library List node

Each IBM i connection has a **Library List** node:

```text
Library List
  ├─ DEVLIB      current library
  ├─ APPLIB      #1
  ├─ UTILLIB     #2
  └─ DATALIB     #3
```

| Action | How |
|---|---|
| Add libraries | Click **+** on **Library List** and type names separated by spaces or commas; or right-click a library under **Libraries** → **Add to Library List** |
| Reorder | **↑** / **↓** icons on an entry. #1 is searched first. |
| Remove | **−** icon on an entry |
| Set the current library | Right-click a library (under **Libraries** or **Library List**) → **Set as Current Library**, or right-click **Library List** → **Set as Current Library** and type a name |
| Clear the current library | **×** icon on the current library |

## How it is applied

When the list or the current library is set, commands run through **Qshell**:

```sh
liblist -c DEVLIB                 # current library
liblist -a DATALIB UTILLIB APPLIB # added so that APPLIB ends up first
system 'CRTBNDRPG PGM(DEVLIB/MYPGM) …'
```

`liblist` changes the Qshell job's library list, and the CL command inherits it. This applies to **Run CL Command**, **Compile**, object actions, and member open/save.

SQL is not affected: it uses SQL naming, so qualify tables as `LIB.TABLE`.

!!! tip "Check it"
    Run the CL command `DSPLIBL OUTPUT(*PRINT)`. The output shows the library list the extension uses.
