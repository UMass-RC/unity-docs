# Partition List

### General Use Partitions

These are the only partitions that are open to use by all users of Unity.

{% include-markdown "../../sheets-to-md/output/general-parts.md" %}

#### Preempt ####
Jobs can be killed and re-queued after two hours in the `-preempt` partition.

To avoid losing progress, it's a good idea to use software that supports checkpointing. Checkpointing in a nutshell is periodically saving the job's state to a file, and having the capability to read this file and resume work from said state.

If you don't want your job re-queued (but still killed), you can specify `--no-requeue` in your job.

### Gypsum Cluster Partitions

Gypsum users, depending on the type, have access to these partitions.

{% include-markdown "../../sheets-to-md/output/gypsum-parts.md" %}

### IALS Cluster Partitions

If you are an authorized IALS member on Unity, you can use these partitions.

{% include-markdown "../../sheets-to-md/output/ials-parts.md" %}

### Other Priority Partitions

These are the remaining priority partitions for smaller installations purchased for specific labs by themselves.

{% include-markdown "../../sheets-to-md/output/priority-parts.md" %}
