# Partition List

#### Core Limits ####
There is currently a 300 CPU core, 64 GPU limit to be shared by the users of each lab.

When you try to go over this limit, you will be denied for `MaxCpuPerAccount`.

### General Use Partitions

These are the only partitions that are open to use by all users of Unity.

{% include-markdown "../../sheets-to-md/output/general-parts.md" %}

#### Preempt ####
Nodes in preempt partitions are buy-in nodes which would normally be inaccessible to general users. Buyers in reserve the right to kill (preempt) any job running on their nodes to make room for their own jobs. When you schedule a job on a preempt partition, your job can be killed after two hours.

If your job is preempted, it will be re-queued and start again on some other hardware. If you don't want your job re-queued (but still killed), you can use the `--no-requeue` Slurm argument. To avoid losing progress, it's a good idea to use software that supports checkpointing. Checkpointing software periodically saves its state to a file. In the event of an interruption, it can read from this file and resume work where it left off.

### Gypsum Cluster Partitions

Gypsum users, depending on the type, have access to these partitions.

{% include-markdown "../../sheets-to-md/output/gypsum-parts.md" %}

### IALS Cluster Partitions

IALS members have access to these partitions.

{% include-markdown "../../sheets-to-md/output/ials-parts.md" %}

### Other Priority Partitions

These partitions represent the specific labs who "bought in" to Unity by providing their own nodes.

{% include-markdown "../../sheets-to-md/output/priority-parts.md" %}
