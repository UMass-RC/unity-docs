!!! note
    The Unity docs are still a work-in-progress. Some docs may be missing, or incomplete. If you would like to contribute to these docs, please submit PRs to the upstream repository [here](https://github.com/UMass-RC/unity-docs).

# Frequently Asked Questions #

### How do I connect to, and start using the cluster? ###
Refer to connection instructions on connecting [here](https://unity.rc.umass.edu/connecting/ssh.html).
You can connect with Putty, SSH in your terminal, or JupyterLab in your browser.

### When I connect over SSH I get a message saying "permission denied (public key)" ### 
This can be due one of these common reasons:
* You have not provided your private key while connecting. `ssh -i <private_key_location> <user>@unity.rc.umass.edu`
* You are not assigned to at least one PI group. We require at least one PI to endorse your account before you can use the cluster. Request to join a PI on the My PIs page.
* You have not added a public key to your account on Unity yet. You can do this on the Account Settings page.
* Your login shell is invalid. In Account Settings, try "/bin/bash" or "/bin/zsh".
* You are a PI, and you are trying to use your PI group name to log in. Your login username should not start with 'pi_'.

### Where can I find software to use on the cluster? ###
Most of our software is package installed and is available by default. 
Non standard and version specific software are available as modules.
The command `module av` will print all available modules. `module av <name>` will filter the available modules.
Then you can use `module load <name>` to load a module and have access to its binaries (executables).

### I'm looking for xyz software, could you install it? ###
Most software that is requested is free for use. 
If this is the case we will install it for you, just send us an email at hpc@umass.edu titled "software request: \<name\>".
If the software you want is licensed, we may be able to help since the campus often has site-wide licenses for many applications.

### Can I run containers on Unity? ###
Yes! We support singularity containers, which are fully compatible with docker images. Run "module load singularity" to access it.

### How much storage do I get on Unity and is it backed up? ###
Refer to storage information [here](https://unity.rc.umass.edu/technical/storage.html).
We do not provide backup solutions by default.
We take a snapshot of all storage at 1 AM every day for the past 48 hours.
This way, if you accidentally deleted something it wouldn't be difficult to get it back within that time frame.

### I'm a PI and I would like to purchase hardware to buy-in to Unity. ###
Great! Send us an email and we'll be happy to help. We are very flexible when it comes to the needs of research labs.
