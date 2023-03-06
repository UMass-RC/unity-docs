# HPC Workspace

Unity provides a tool called [HPC Workspace](https://github.com/holgerBerger/hpc-workspace) to allow you to create and manage scratch space in a sustainable fashion.

## Creating a workspace

Creating a workspace is done with the `ws_allocate` command.
To view all options, run `ws_allocate -h`.

### Examples

#### Create simple workspace for single user with defaults

```
username@login2:~$ ws_allocate simple
Info: creating workspace.
/scratch/workspace/username-simple
remaining extensions  : 3
remaining time in days: 1
```

Now we can see the directory that was created.

```
username@login2:~$ ls -ld /scratch/workspace/username-simple
drwx------ 2 username username 4096 Mar  2 17:48
```

#### Send email reminder before workspace expiration

The `-m` option allows you to specify an email address to be notified prior to workspace expiration.
When using this option, you are also required to specify the number of days prior to expiration via the `-r` option.

```
username@login2:~$ ws_allocate -m username@umass.edu -r 1 email 2
Info: creating workspace.
/scratch/workspace/username-email
remaining extensions  : 3
remaining time in days: 2
```

#### List workspaces

The `ws_list` command can be used to list your workspaces.

```
username@login2:~$ ws_list 
id: username-email
     workspace directory  : /scratch/workspace/username-email
     remaining time       : 0 days 23 hours
     creation time        : Fri Mar  3 16:56:51 2023
     expiration date      : Sat Mar  4 16:56:50 2023
     filesystem name      : workspace
     available extensions : 3
id: username-simple
     workspace directory  : /scratch/workspace/username-simple
     remaining time       : 0 days 23 hours
     creation time        : Fri Mar  3 16:56:44 2023
     expiration date      : Sat Mar  4 16:56:44 2023
     filesystem name      : workspace
     available extensions : 3
```

#### Release workspace

Once you are done using a workspace, you can **release** it.
Releasing a workspace means that the ID can be reused and the directory is not accessible.

```
username@login2:~$ ws_release email
username@login2:~$ ws_release simple
username@login2:~$ ws_list
username@login2:~$
```

!!! important 
    Releasing a workspace does not delete the data immediately.
    The deletion of the workspace can take place at any time once it's released.

#### Extend workspace

You are allowed a limited number of opportunities to extend a workspace.
You can see the available number of extensions in the output of `ws_list`.

Create a workspace and extend it for 30 days.

```
username@login2:~$ ws_allocate extend
Info: creating workspace.
/scratch/workspace/username-extend
remaining extensions  : 3
remaining time in days: 1
username@login2:~$ ws_allocate -x extend 30
Info: extending workspace.
/scratch/workspace/username-extend
remaining extensions  : 2
remaining time in days: 30
```

#### Creating a Group workspace

The HPC Workspace utility allows you to create **shared** workspaces which can be useful for collaborating on a project.
In order to create a shared workspace, all members must be members of a common group.
For example, it may be that all members of a particular PI group want to collaborate on a project.

Create a group workspace that can be shared amongst a particular PI group.

```
username@login2:~$ ws_allocate -G pi_pi-username shared
Info: creating workspace.
/scratch/workspace/username-shared
remaining extensions  : 3
remaining time in days: 0
```

Now you can see that the directory was created with group sharing permissions.

```
username@login2:~$ ls -ld /scratch/workspace/username-shared 
drwxrws--- 2 username pi_pi-username 4096 Mar  3 19:08
```
