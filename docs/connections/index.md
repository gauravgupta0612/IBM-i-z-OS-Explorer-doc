# Connections

A **connection** is one IBM i or one z/OS system. You can define as many as you like. Each one appears as its own node in the **IBM i** or **z/OS** section.

## What is stored, and where

| Data | Stored in | Shared? |
|---|---|---|
| Name, host, port, user, filters, object library | VS Code global storage on your PC | No, it stays on your PC |
| Password | OS keychain (Windows Credential Manager, macOS Keychain, libsecret on Linux), through VS Code SecretStorage | No |
| SSH key | Only its **file path** is stored; the key stays where it is | No |

Nothing is written into your project or workspace, so you can't commit a password to Git by accident.

## Manage a connection

Right-click a connection:

| Action | What it does |
|---|---|
| **Test Connection** (plug icon) | Connects and shows the system version |
| **Edit Connection** | Re-runs the wizard with the current values prefilled. For IBM i it also asks for the **object library** used by compiles. |
| **Reset Stored Password** | Removes the stored password and asks for a new one |
| **Disconnect** (IBM i) | Closes the SSH session. It reconnects automatically the next time it's needed. |
| **Remove Connection** | Deletes the connection and its stored password |

## Filters

Filters decide what you see under a connection. Add them with the inline buttons and remove them with the **×** next to each filter.

| Platform | Filter types |
|---|---|
| z/OS | Data set filters (`USER.**`, `SYS1.PROCLIB`, `HLQ.*.COBOL`), USS paths, job filters (owner + prefix) |
| IBM i | Library filters, IFS paths |

Continue with [IBM i connections](ibmi.md) or [z/OS connections](zos.md).
