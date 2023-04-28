# Transitioning from the Shared Cluster to Unity

_Last updated: 21 April 2023_

It is our pleasure to welcome you to [Unity](https://unity.rc.umass.edu/), 
a high performance computing cluster located at [MGHPCC](https://www.mghpcc.org/) and managed by 
[UMass Amherst Research Computing](https://www.umass.edu/it/researchcomputing). 
We understand that migrating your work may be stressful and we want to make it as smooth as possible. 
Please see below for important dates and information to guide your transition to Unity.

_For questions about the Unity transition, please attend our 
[onboarding sessions](#onboarding-live-sessions) 
or contact the Unity help desk at [hpc@umass.edu](mailto:hpc@umass.edu)._

_In addition, we have created a new Unity User Community.
Please sign up with your school email
[here](https://join.slack.com/t/unity-user-community/signup).
If you’re unable to register with your school email, please contact 
[hpc@umass.edu](mailto:hpc@umass.edu) 
with your preferred email address and we’ll send you a direct invite._

_Once you’ve signed up, you can access the community 
[here](https://unity-user-community.slack.com)._


[TOC]

## Account Information 

### PI & Faculty Accounts

PIs and faculty can request Unity cluster PI accounts in the 
[Unity Portal](https://unity.rc.umass.edu/). On the left side bar, select “Login / Request Account” and log 
in with your UMass Lowell credentials. Once logged in, under “Account Settings,” 
click the “Request PI Account” button. The Unity team will review your 
request and approve your PI account. 

### Student & Postdoc Accounts

Students request access to PI groups by logging into the 
[Unity Portal](https://unity.rc.umass.edu/), 
navigating to “My PIs,” and clicking the “plus” button to search for your group. 
Students and postdocs can’t access Unity without an associated PI, so please ensure 
the PI account is created and approved before requesting an account.

## Timeline Overview

### Migrating Data to Unity (deadline: May 15, 2023)

All data must be migrated to Unity by May 15, 2023. PIs will temporarily receive 
sufficient storage in the /project directory to move as much data from the shared 
cluster as desired. However, storage quotas will be enforced starting January 2024. 
Users may purchase additional storage at that time. 

### Shared Cluster Shutdown (read-only: May 1, 2023, final shutdown: June 1, 2023)

The Shared Cluster will be turned off permanently on June 1, 2023. However, the cluster 
will become read-only ahead of the shutdown on May 1, 2023. While you will be able to 
continue transferring data, you will no longer be able to run jobs or create new files. 

## Onboarding Live Sessions

To ensure a smooth transition from the Shared Cluster to Unity, we held two online 
workshops on accessing Unity, data transfer and storage, and running jobs. Links to the recordings and slides follow each workshop description.

### Unity Onboarding Workshop Part 1: Access and Data Storage (March 31, 2023)

_Friday, March 31, 2023, 2:00 pm to 3:00 pm (time for questions following)_  
We provided an overview of Unity in comparison to the Shared cluster, explained the account 
request process for PIs/faculty and students/postdocs, and discussed storage on Unity and data 
transfer options.  

[**Recording link**](https://umass-my.sharepoint.com/:v:/g/personal/gstuart_umass_edu/ESGBqTjFg99Bjj5VQ0pG17ABtmvwDozDw1L85Utu2Rmpig)  
[**Slides link**](https://bit.ly/ghpcc-to-unity)

### Unity Onboarding Workshop Part 2: Running Jobs (April 14, 2023)
_Friday, April 14, 2023, 2:00 pm to 3:00 pm (time for questions following)_  
We discussed the differences between the Shared Cluster’s LSF scheduler and Unity’s Slurm 
scheduler, introduced Unity’s partition layout, showed example Slurm jobs, and demonstrated Unity’s 
Open OnDemand portal.   

[**Recording link**](https://umass-my.sharepoint.com/:v:/g/personal/gstuart_umass_edu/ESOfR4VMB0BEiJlqwtRMnxoBmUugUD4YUl5qkBvt0mEilQ)  
[**Slides link**](https://bit.ly/ghpcc-to-unity-2) 

## Technical Information

### Data Transfer

For information about moving data to Unity, see our 
[file transfer documentation](/managing-files/intro.html). 
Please give yourself ample time to move your data ahead of the
May 1, 2023 read-only freeze.

### Job Scheduler

While the Shared Cluster uses LSF to allocate resources, Unity uses the
[Slurm scheduler](/slurm/index.html). See
[this quick reference page](https://scicomp.ethz.ch/wiki/LSF_to_Slurm_quick_reference)
for a comparison between LSF and Slurm options.

A full list of Slurm commands and their equivalents can be found 
[in this PDF](https://slurm.schedmd.com/rosetta.pdf).
