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
