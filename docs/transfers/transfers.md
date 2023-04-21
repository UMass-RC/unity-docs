# Transferring data from the Shared Cluster (GHPCC) to Unity:


## This guide will allow you to transfer data from the Shared Cluster (GHPCC) to Unity via Globus.

### Step 1: Log in to Globus

* Visit this site: [https://app.globus.org/file-manager](https://app.globus.org/file-manager)
* Use your university credentials to log in

### Step 2: Connect to the Shared Cluster and Unity
* Select the **File Manager** tab from lefthand pane
* In the two "Collection" boxes, select the Shared Cluster and Unity via their Globus identities
    * The Shared Cluster is ghpcc#ghpcc07
    * Unity is Unity
        * *more technical identifier: acda5457-9c06-4564-8375-260ba428f22a*
    * If you start typing either in the "Collection" text box, the drop-down will update and allow you to select the appropriate "Collection" (aka cluster)
* Provide your login credentials for each cluster
    * Once you're finished logging in to each connection, the screen should look something like this: ![](https://camo.githubusercontent.com/8575d9fbfbcef3b14cedc37eb2f1c04d32496b25a7bc662a253078d084df95ab/68747470733a2f2f692e696d6775722e636f6d2f48713771536d6f2e706e67)

### Step 3: Transfer files
* Below, the Connection and Path text boxes, you should see the contents of each directory.
* Navigate to the location of the file/directory you'd like to transfer from and to.
* Select the file/directory you'd like to transfer
* Click on the "Transfer or Sync to..." button. Shown in the middle here: ![ ](https://camo.githubusercontent.com/8ec1422594b1334bbe8a6614d5c4dce42d8224c67cd81e89d7c09708cd1c9f74/68747470733a2f2f692e696d6775722e636f6d2f614974757653732e706e67)
* Voila! The file/directory will be queued up and transferred shortly!

### Step 4: Confirm that transfer was successful
* You'll receive an email once the transfer occurs.
* Open the Destination directory and confirm that the file was transferred as expected.


## This guide will allow you to send data from the Shared Cluster to the Unity server using `scp` for the purposes of transitioning.
#### Notes:
* You will need to have set up an account on the Unity server.
* You will need your password for the Shared Cluster server (unless you are using private/public keys for logging on to this too).

### Step 1.
* Log in to the Shared Cluster (GHPCC).
* While logged into the Shared Cluster, from your home directory, run `ssh-keygen -t rsa`
    * This will generate a private/public key pair which is unique to each user.
    * The generator will ask you to save the keys as a specific name, and you have the option to associate a password to the keys (recommended but not required).
    * Two files will be created: NAME and NAME.pub
    * NAME.pub is the public key that you will need for Step 2.

### Step 2.
* Log in to the Unity cluster portal: https://unity.rc.umass.edu/
* Navigate to "Account Settings"
* You will see the SSH keys that are currently linked to your account
* Click the "+" button to add the Shared Cluster key to your account.
* Copy the entire contents of the public key (NAME.pub) from the Shared Cluster generated in Step 1 into the prompt.
* Click "add key"
* Click "Set Login Shell"
    * This will now link the two servers, allowing them to communicate
![ ](https://camo.githubusercontent.com/8e79c394e0238f3eaa65a53662d2aaa44ce6f0c7da57b63356e2fb8b27c751f5/68747470733a2f2f692e696d6775722e636f6d2f4476465a32496c2e706e67)

### Step 3.
* Log into the Unity cluster
* Create a file to test the connection between servers (e.g. `touch test.txt`)
* Attempt to transfer the file from Unity to the Shared Cluster:
    * `scp test.txt username@ghpcc06.umassrc.org:/home/username/`
* You will be prompted for your password to the Shared Cluster - enter it here.
* If configured properly, this file should transfer immediately to the specified destination path (in this case `/home/username/`)

### Step 4.
* Assuming that Step 3 worked and the file transferred across from Unity to the Shared Cluster, you can use this to pull data across:
`scp username@ghpcc06.umassrc.org:/where/files/are/you/want/* ./destination/`
* Each time you run `scp` in this way, you will be prompted for your password.
* **Note** that currently this only works when **logged in and running commands from Unity, not the Shared Cluster.**


Globus documentation provided by the Molecular Ecology and Conservation Lab, Dept. Environmental Conservation.
