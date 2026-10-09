# Productivity features

## Favorites

Right-click a member, sequential data set, USS file, IBM i member or IFS file → **Add to Favorites**.

A **Favorites** node appears at the top of that connection; click an entry to open it. Remove an entry with the **★** icon. Favorites are stored per connection and included in [connection exports](#export-and-import-connections).

## Compare with a local file

Right-click a remote member or file in the tree, or the tab of an open remote editor, → **Compare with Local File…**. Pick the local file; VS Code opens a side-by-side diff with the local file on the left and the host version on the right.

You can edit the right side and press ++ctrl+s++ to save the changes on the host.

## Export and import connections

The `…` menu of the **z/OS** or **IBM i** view has:

- **Export Connections…**: pick the connections and save them as a JSON file. It includes host, port, user, filters, library list, object library and favorites. **Passwords are never exported.**
- **Import Connections…**: read such a file. Connections that already exist (same name, host and user) are skipped, and each colleague enters their own password on first connect.

```json
{
  "format": "ibmi-zos-explorer-connections",
  "version": 1,
  "connections": [
    { "type": "ibmi", "name": "DEV400", "host": "dev400.company.com", "port": 22, "user": "GGUPTA",
      "libraries": ["DEVLIB"], "libraryList": ["APPLIB"], "currentLibrary": "DEVLIB" }
  ]
}
```

!!! tip "Team setup"
    Put a connections file (with user names replaced) on a shared drive or in your team's wiki, so new team members can import it and be ready in a minute.

## Snippets

Type a prefix such as `jobcard`, `iebcopy`, `program` or `dcl-proc` and press ++tab++. The full list is on the [JCL templates & snippets](../zos/jcl-templates.md#snippets) page.
