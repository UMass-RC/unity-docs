| Name               | Relative Wait Time   | Default Job Time    | Time Limit          |   Max CPU's Per Node |
|:-------------------|:---------------------|:--------------------|:--------------------|---------------------:|
| cpu                | medium               | 4 hours             | 1 day               |                   40 |
| cpu-long           | long                 | 7 days              | 14 days             |                   40 |
| cpu-preempt        | short                | 4 hours (see below) | 14 days (see below) |                  256 |
| gpu                | medium               | 4 hours             | 1 day               |                   72 |
| gpu-long           | long                 | 7 days              | 14 days             |                   72 |
| gpu-preempt        | short                | 4 hours (see below) | 14 days (see below) |                   64 |
| power9             | short                | 1 day               | 30 days             |                  128 |
| power9-gpu         | medium               | 1 day               | 30 days             |                  128 |
| power9-gpu-preempt | short                | 4 hours             | 14 days             |                  128 |
| arm-preempt        | short                | 4 hours             | 14 days             |                   80 |
