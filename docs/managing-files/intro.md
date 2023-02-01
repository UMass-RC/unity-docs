# Uploading Files to the Unity Filesystem
The only way to add files to the Unity filesystem is through an SSL encrypted connection. It can be done with Unity OnDemand, FileZilla, Globus, or in the command line.

* Unity OnDemand is the most feature complete and intuitive interface, and is recommended.
* FileZilla is good for those who have their SSH keys set up and are familiar with the software already.
* Globus is recommended for those who already have access to other Globus resources.
* `scp` and `rsync` are recommended for those who are comfortable in the command line and want to work quickly.

!!! note
    Uploading files using American residential internet is typically very slow.
    UMass Amherst has a fiber line going directly to MGHPCC to improve speeds.

## Your Key File ##
The FileZilla and Console methods require public/private SSH keys to be set up.

When you set up your Unity account, you chose between PuTTY (`.ppk`) and OpenSSH. (`.rsa`)

`scp` and `rsync` use OpenSSH, and FileZilla prefers `.ppk` but can work with `.rsa`.

Depending on which software you use, you can generate one of each. You can also convert between these keys using a program like PuttyGEN.

[Configuring SSH Keys](../connecting/ssh.md)

[Account Settings](https://unity.rc.umass.edu/panel/account.php)
