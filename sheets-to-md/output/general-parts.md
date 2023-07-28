| Name               | Relative Wait Time   | Default Job Time   | Time Limit          |   Max CPU's Per Node |
|:-------------------|:---------------------|:-------------------|:--------------------|---------------------:|
| cpu                | medium               | 1 hour             | 1 day               |                   40 |
| cpu-long           | long                 | 2 days             | 14 days             |                   40 |
| cpu-preempt        | short                | 1 hour (see below) | 14 days (see below) |                  256 |
| gpu                | medium               | 1 hour             | 1 day               |                   72 |
| gpu-long           | long                 | 2 days             | 14 days             |                   72 |
| gpu-preempt        | short                | 1 hour (see below) | 14 days (see below) |                   64 |
| power9             | short                | 1 hour             | 30 days             |                  128 |
| power9-gpu         | medium               | 1 hour             | 30 days             |                  128 |
| power9-gpu-preempt | short                | 1 hour             | 14 days             |                  128 |
| arm-preempt        | short                | 1 hour             | 14 days             |                   80 |
