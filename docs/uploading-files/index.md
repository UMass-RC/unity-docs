# Uploading Files to the Unity Filesystem
The only way to add files to the Unity filesystem is through an SSL encrypted connection. It can be done with FileZilla (recommended), in JupyterLab, or in the command line.

!!! note
    Uploading files using American residential internet is typically very slow.
    UMass Amherst has a fibre line going directly to MGHPCC to improve speeds.

## Your Key File ##
When you set up your Unity account, you chose between PuTTY (`.ppk`) and OpenSSH. (`.rsa`)

`scp` and `rsync` use OpenSSH, and FileZilla prefers `.ppk` but can work with `.rsa`.

Depending on which software you use, you can generate one of each. You can also convert between these keys using a program like PuttyGEN.

[Configuring SSH Keys](../connecting/ssh.md)

[Account Settings](https://unity.rc.umass.edu/panel/account.php)

## FileZilla ##
FileZilla can use either an `.rsa` or a `.ppk` private key, but the 'Browse' button will show only `.ppk` files. To use an `.rsa` key, type in the path to the keyfile by hand.

This guide assumes that your key lives at `~/.ssh/KEYFILE`, but you can substitute this path.

You can install FileZilla [here](https://filezilla-project.org/download.php?type=client)

* FileZilla may ask you if you want to install McAfee, you probably don't. If you don't have antivirus already, you probably should.
* The FileZilla installer executable can be sometimes marked as a virus, it isn't.

Select the Site Manager in FileZilla:

![Select the Site Manager in FileZilla](res/select-site-manager.png)

Create a New Site:

![Create a New Site](res/select-new-site.png)

Fill in the Fields:

* Type a name for the site under My Sites on the left
* Protocol: SFTP
* Host: unity.rc.umass.edu
* User: your email but replace the `.` and `@` with `_`
* Key File: /path/to/your/keyfile

![Fill in the Fields](res/site-config.png)

This configuration is saved automatically.
You can use the 'Connect' button in the bottom right to open an explorer on the Unity Filesystem,and you can drag and drop your files across the two panels.

Properly connected, FileZilla should look like this:

![FileZilla](res/done.png)

## JupyterLab ##
Start a session in JupyterLab. Navigate to your home directory, and click the upload button.

![JupyterLab Start Page](res/jupyter-start.png)

## Globus ##
Globus Connect allows for transfers between Globus collections.

This can be useful, for example, when migrating from one HPC cluster to another.

[How can I transfer files to and from my local machine with Globus?](https://docs.globus.org/faq/transfer-sharing/#how_can_i_transfer_files_to_and_from_my_laptop_or_desktop)

### Using Globus Connect in your browser ###

**Know which two Globus collections you want to transfer between.**

One is presumably Unity. The other could be your local machine if you install Globus Connect Personal. (see above)

**Go to [app.globus.org](https://app.globus.org)**

**If prompted, select your university and login with their identity provider.**

![Login to Globus](res/globus-login.png)

**Go to the File Manager and select a collection.**

Either collection involved in your transfer will do. At the time of this writing, there is more than one collection named Unity.
The following string can be pasted into the search box to select our Globus endpoint:
`acda5457-9c06-4564-8375-260ba428f22a`

![Globus select split panels](res/globus-collection-search.png)

Once a collection is selected, there should be two mirrored panels. If not, **select the split panel layout in the top right:**

![Globus select split panels](res/globus-select-split-panels.png)

**Select the other collection involved in your transfer.** This will take you back to the collection search page.

Of the two split panels, each has a Collection, a **Path**, a number of **selected** files, and a **Start** button to copy the selected files to the other side. Below is one panel:

![Configure Globus Transfer](res/globus-configure-transfer.png)

**Configure your transfer and press 'Start'.**


## CLI ##
It's best to try this after you have already successfully connected to Unity with OpenSSH.

As these are CLI procedures, the first thing you need to do is open your terminal and navigate to the directory (folder) where the files you want to upload are located. Alternatively you can use [absolute paths](https://networkencyclopedia.com/absolute-path/) in your command and skip this step.
```
# Windows
cd C:/Users/YOUR_NAME/Desktop
# Linux
cd /home/$USER/Desktop
# Mac
cd /Users/YOUR_NAME/Desktop
```
Assuming, of course, that the files you want to upload are located in your desktop directory.
And in the Windows case, assuming that the drive you want to copy from is the C drive.

!!! note
    If your file name contains spaces, you will have to put it in quotes.

### SCP ###
OpenSSH comes with the `scp` command, which uses the same argument structure as `cp` (copy) but with the added benefit of referencing the OpenSSH config file (`~/.ssh/config`). This is how I can use `unity` as part of a command, because the OpenSSH config file contains the connection information for host `unity`.
```
# single file
scp FILE_NAME unity:~

# entire directory
scp -r DIRECTORY_NAME unity:~
```
This will copy the files in question to your Unity home directory.
You could also upload to elsewhere on the Unity filesystem, wherever you have permissions.
!!! note
    `-r` in many commands is short for 'recursive'.
    It means to recursively open directories to ensure that all contained files are accounted for.

!!! note
    `~` in the terminal represents your home directory.

    This is `C:/Users/YOUR_NAME` in Windows, `/home/YOUR_NAME` in Linux, and `/Users/YOUR_NAME` in [Mac](https://www.cnet.com/tech/computing/how-to-find-your-macs-home-folder-and-add-it-to-finder/).

### RSYNC ###
`rsync` can be installed on Linux and Mac. The syntax is the same as `scp`.
It also references the OpenSSH config file.

It's recommended to use the `-tlp` flags so that timestamps, relative links, and permissions are preserved, respectively.
```
# single file
rsync -tlp FILE_NAME unity:~

# entire directory
rsync -rtlp DIRECTORY_NAME unity:~
```


