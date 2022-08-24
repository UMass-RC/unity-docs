# Partition List

### General Use Partitions

General use partitions are open to use by all users of Unity.

| Name        | Default Job Time   | Relative Wait Time   | Time Limit   | Max CPU's Per Node   |
|:------------|:-------------------|:---------------------|:-------------|:---------------------|
| cpu         | 4 hours            | medium               | 1 day        | 40.0                 |
| cpu-long    |                    | long                 | 14 days      | 40.0                 |
| cpu-preempt |                    | short                | 14 days      | 256.0                |
| gpu         |                    | medium               | 1 day        |                      |
| gpu-long    |                    | long                 | 14 days      |                      |
| gpu-preempt |                    | short                | 14 days      |                      |

#### Preempt ####
Jobs can be killed and re-queued after two hours in the `-preempt` partition.

To avoid losing progress, it's a good idea to use software that supports checkpointing. Checkpointing in a nutshell is periodically saving the job's state to a file (usually called `state`), and having the capability to read this file and resume work from that state.

If you don't want your job re-queued (but still killed), you can specify `--no-requeue` in your job.

### Gypsum Cluster Partitions

Gypsum users, depending on the type, have access to these partitions.

| Name                 | Time Limit   | Comments                         |
|:---------------------|:-------------|:---------------------------------|
| gypsum-m40-phd       | 7 DAYS       | m40 GPU partition for pHd        |
| gypsum-m40-ms        | 7 DAYS       | m40 GPU partition for MS         |
| gypsum-m40-course    | 7 DAYS       | m40 GPU partition for Courses    |
| gypsum-titanx-phd    | 7 DAYS       | titanx GPU partition for pHd     |
| gypsum-titanx-ms     | 7 DAYS       | titanx GPU partition for MS      |
| gypsum-titanx-course | 7 DAYS       | titanx GPU partition for Courses |
| gypsum-1080ti-phd    | 7 DAYS       | 1080ti GPU partition for pHd     |
| gypsum-1080ti-ms     | 7 DAYS       | 1080ti GPU partition for MS      |
| gypsum-1080ti-course | 7 DAYS       | 1080ti GPU partition for Courses |
| gypsum-2080ti-phd    | 7 DAYS       | 2080ti GPU partition for pHd     |
| gypsum-2080ti-ms     | 7 DAYS       | 2080ti GPU partition for MS      |
| gypsum-2080ti-course | 7 DAYS       | 2080ti GPU partition for Courses |

### IALS Cluster Partitions

If you are an authorized IALS member on Unity, you can use these partitions.

| Name     | Time Limit   | Comments               |
|:---------|:-------------|:-----------------------|
| ials-gpu | 14 DAYS      | GPU partition for IALS |

### Other Priority Partitions

These are the remaining priority partitions for smaller installations purchased for specific labs by themselves.

| Name                   | Time Limit   | Comments                                   |
|:-----------------------|:-------------|:-------------------------------------------|
| ceewater_cjgleason-cpu | Unlimited    | ceewater CPU partition for cjgleason group |
| ceewater_casey-cpu     | Unlimited    | ceewater CPU partition for casey group     |
| ceewater_kandread-cpu  | Unlimited    | ceewater CPU partition for kandread group  |
| astroth-cpu            | Unlimited    | astroth CPU partition                      |
| zhoulin-cpu            | Unlimited    | zhoulin CPU partition                      |
| toltec-cpu             | Unlimited    | toltec CPU partition                       |
| gaoseismolab-cpu       | Unlimited    | gaoseismolab CPU partition                 |
| uri-cpu                | Unlimited    | URI CPU partition                          |
| ece-gpu                | 5 DAYS       | ece partition for ECE courses only         |
