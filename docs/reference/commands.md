# Commands & shortcuts

All commands are in the Command Palette (++ctrl+shift+p++), prefixed by **Mainframe:**, **z/OS:** or **IBM i:**, except those that need a tree item. You find those by right-clicking in the tree.

## Keyboard shortcuts

| Shortcut | Command | When |
|---|---|---|
| ++ctrl+alt+s++ | Submit JCL | Editor language is JCL |
| ++ctrl+e++ (macOS ++cmd+e++) | Compile current member | An IBM i member is open |
| ++ctrl+r++ (macOS ++cmd+r++) | Run SQL statement under cursor / selection | Editor language is SQL |
| ++ctrl+s++ | Save to the host | Any remote member, data set or file |

You can change them in **File → Preferences → Keyboard Shortcuts**: search for `mf.`.

## General

| Command | ID | Key | Available from |
|---|---|---|---|
| Add z/OS Connection | `mf.addZosProfile` |  | Command Palette, tree |
| Add IBM i Connection | `mf.addIbmiProfile` |  | Command Palette, tree |
| Edit Connection | `mf.editProfile` |  | Command Palette, tree |
| Remove Connection | `mf.removeProfile` |  | Tree (right-click or inline icon) |
| Reset Stored Password | `mf.resetPassword` |  | Tree (right-click or inline icon) |
| Test Connection | `mf.testConnection` |  | Tree (right-click or inline icon) |
| Disconnect | `mf.disconnect` |  | Tree (right-click or inline icon) |
| Refresh | `mf.refresh` |  | Tree (right-click or inline icon) |
| Refresh All | `mf.refreshAll` |  | Command Palette, tree |
| Remove Filter | `mf.removeFilter` |  | Tree (right-click or inline icon) |

## z/OS

| Command | ID | Key | Available from |
|---|---|---|---|
| Add Data Set Filter | `mf.zos.addDsFilter` |  | Command Palette, tree |
| Add USS Path | `mf.zos.addUssPath` |  | Command Palette, tree |
| Add Job Filter | `mf.zos.addJobFilter` |  | Command Palette, tree |
| Create Data Set | `mf.zos.createDataset` |  | Command Palette, tree |
| Create Member | `mf.zos.createMember` |  | Tree (right-click or inline icon) |
| Create USS File | `mf.zos.createUssFile` |  | Tree (right-click or inline icon) |
| Create USS Directory | `mf.zos.createUssDir` |  | Tree (right-click or inline icon) |
| Delete | `mf.zos.delete` |  | Tree (right-click or inline icon) |
| Submit JCL | `mf.zos.submitJcl` | ++ctrl+alt+s++ | Command Palette, tree |
| Submit as Job | `mf.zos.submitMember` |  | Tree (right-click or inline icon) |
| Cancel Job | `mf.zos.cancelJob` |  | Tree (right-click or inline icon) |
| Purge Job | `mf.zos.purgeJob` |  | Tree (right-click or inline icon) |
| Open All Spool Output | `mf.zos.downloadAllSpool` |  | Tree (right-click or inline icon) |
| Issue TSO Command | `mf.zos.tso` |  | Command Palette, tree |
| Issue MVS Console Command | `mf.zos.console` |  | Command Palette, tree |
| Upload Local File to Member / USS | `mf.zos.uploadFile` |  | Tree (right-click or inline icon) |
| Recall Migrated Data Set | `mf.zos.recall` |  | Tree (right-click or inline icon) |

## IBM i

| Command | ID | Key | Available from |
|---|---|---|---|
| Add Library Filter | `mf.ibmi.addLibrary` |  | Command Palette, tree |
| Add IFS Path | `mf.ibmi.addIfsPath` |  | Command Palette, tree |
| Run CL Command | `mf.ibmi.runCl` |  | Command Palette, tree |
| Run SQL | `mf.ibmi.runSql` |  | Command Palette, tree |
| Run SQL Statement (Editor) | `mf.ibmi.runSqlEditor` | ++ctrl+r++ | Command Palette, tree |
| Compile | `mf.ibmi.compile` |  | Tree (right-click or inline icon) |
| Compile Current Member | `mf.ibmi.compileEditor` | ++ctrl+e++ | Command Palette, tree |
| Create Source File | `mf.ibmi.createSrcFile` |  | Tree (right-click or inline icon) |
| Create Member | `mf.ibmi.createMember` |  | Tree (right-click or inline icon) |
| Delete Member | `mf.ibmi.deleteMember` |  | Tree (right-click or inline icon) |
| Create IFS File | `mf.ibmi.createIfsFile` |  | Tree (right-click or inline icon) |
| Create IFS Directory | `mf.ibmi.createIfsDir` |  | Tree (right-click or inline icon) |
| Delete IFS Entry | `mf.ibmi.deleteIfs` |  | Tree (right-click or inline icon) |
| Delete Spooled File | `mf.ibmi.deleteSpool` |  | Tree (right-click or inline icon) |
| End Job | `mf.ibmi.endJob` |  | Tree (right-click or inline icon) |
| Show Job Log | `mf.ibmi.showJobLog` |  | Tree (right-click or inline icon) |
| Open PASE Shell (SSH Terminal) | `mf.ibmi.terminal` |  | Command Palette, tree |
