# Partition List

### General Use Partitions

General use partitions are open to use by all users of Unity.

| Name        | Time Limit | Max CPUs Per Node | Comments                                                                                                                                                |
| ----------- | ---------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cpu         | 1 DAY      | 40                | CPU short partition                                                                                                                                     |
| cpu-long    | 14 DAYS    | 40                | CPU long partition                                                                                                                                      |
| cpu-preempt | 14 DAYS    | 256               | Priority jobs can preempt (requeue) your jobs after a 2 hour grace time. It is a good idea to stick to jobs with checkpoint support for this partition. |
| gpu         | 1 DAY      |                   | GPU short partition                                                                                                                                     |
| gpu-long    | 14 DAYS    |                   | GPU long partition                                                                                                                                      |
| gpu-preempt | 14 DAYS    |                   | Priority jobs can preempt (requeue) your jobs after a 2 hour grace time. It is a good idea to stick to jobs with checkpoint support for this partition. |

### Gypsum Cluster Partitions

Gypsum users, depending on the type, have access to these partitions.

| Name                 | Time Limit | Comments               |
| -------------------- | ---------- | ---------------------- |
| gypsum-m40           | 7 DAYS     | M40 GPU partition      |
| gypsum-titanx        | 7 DAYS     | TITAN X GPU partition  |
| gypsum-1080ti        | 7 DAYS     | 1080 Ti GPU partition  |
| gypsum-2080ti        | 7 DAYS     | 2080 Ti GPU partition  |
| gypsum-rtx8000       | 7 DAYS     | RTX 8000 GPU partition |

### IALS Cluster Partitions

If you are an authorized IALS member on Unity, you can use these partitions.

| Name     | Time Limit | Comments               |
| -------- | ---------- | ---------------------- |
| ials-gpu | 14 DAYS    | GPU partition for IALS |

### Other Priority Partitions

These are the remaining priority partitions for smaller installations purchased for specific labs by themselves.

| Name                   | Time Limit | Comments                                   |
| ---------------------- | ---------- | ------------------------------------------ |
| ceewater_cjgleason-cpu | Unlimited  | ceewater CPU partition for cjgleason group |
| ceewater_casey-cpu     | Unlimited  | ceewater CPU partition for casey group     |
| ceewater_kandread-cpu  | Unlimited  | ceewater CPU partition for kandread group  |
| astroth-cpu            | Unlimited  | astroth CPU partition                      |
| zhoulin-cpu            | Unlimited  | zhoulin CPU partition                      |
| toltec-cpu             | Unlimited  | toltec CPU partition                       |
| gaoseismolab-cpu       | Unlimited  | gaoseismolab CPU partition                 |
| uri-cpu                | Unlimited  | URI CPU partition                          |
| ece-gpu                | 5 DAYS     | ece partition for ECE courses only         |
