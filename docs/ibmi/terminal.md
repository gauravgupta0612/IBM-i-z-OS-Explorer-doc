# PASE terminal

Right-click an IBM i connection → **Open PASE Shell (SSH Terminal)**.

A full interactive SSH terminal opens in the VS Code terminal panel, signed in as your user. The window size follows the panel.

```bash
uname -a
ls -la /home/$USER
system "DSPLIBL"
db2 "select * from qsys2.library_list_info"   # if the db2 command is available
yum list installed | grep -i node
```

Tips:

- The shell is your user's default SSH shell. To switch to bash for the session, run `/QOpenSys/pkgs/bin/bash` (install it with `yum install bash` if needed).
- Close the terminal with `exit` or the trash icon.
