# Message queues

Each IBM i connection has a **Message Queues** node with:

- **QSYSOPR (system operator)**: `QSYS/QSYSOPR`
- **YOURUSER (your messages)**: `QUSRSYS/<your user>`

Expand a queue to see its latest 200 messages, newest first. The icon shows the kind of message:

| Icon | Meaning |
|---|---|
| :material-help-circle-outline: | Inquiry **waiting for a reply** (shows a reply icon) |
| :material-check-circle-outline: | Inquiry already answered |
| :material-close-circle-outline: | Severity 40 or higher |
| :material-alert-outline: | Severity 20–39 |
| :material-information-outline: | Informational |

## Read a message

Click a message. Its full text, help text (second-level text), sender and time open in an editor.

## Reply to an inquiry

Click an inquiry message and choose **Reply…**, or use the **reply** icon next to it. Type the reply, for example `G`, `C`, `I`, `R` or `D` as listed in the help text.

The extension sends `SNDRPY MSGKEY(…) MSGQ(…) RPY('…')`. You need authority to the message queue; replying to QSYSOPR usually requires `*JOBCTL` special authority or operator rights.

!!! note
    The list comes from the SQL service `QSYS2.MESSAGE_QUEUE_INFO` (IBM i 7.2 TR or later). Click **refresh** on a queue to reload it.
