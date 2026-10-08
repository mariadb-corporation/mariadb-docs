# Sysbench Results

Results from various sysbench v0.5 runs, made during MariaDB 5.1 and 5.2 development.

The "perro" and "work" systems were configured as follows:

| System | Configuration |
| ------ | ------------- |
| perro  | Linux openSUSE 11.1 (x86\_64), single socket dual-core Intel 3.2GHz. with 1MB L2 cache, 2GB RAM, data\_dir on 2 disk software RAID 0 |
| work   | Linux openSUSE 11.1 (x86\_64), dual socket quad-core Intel 3.0GHz. with 6MB L2 cache, 8 GB RAM, data\_dir on single disk. |

## Sysbench v0.5 Results

The results were originally published as OpenDocument spreadsheets (`.ods`), which are no longer available. Where a run has its own page, the list links to it:

* [Single Five Minutes Runs on T500 Laptop](sysbench-v0.5-single-five-minute-runs-on-t500-laptop.md)
* [Single Five Minutes Runs on perro](sysbench-v0.5-single-five-minute-runs-on-perro.md)
* [Single Five Minutes Runs on work](sysbench-v0.5-single-five-minute-runs-on-work.md)
* [Three Times Five Minutes Runs on work with 5.1.42](sysbench-v0.5-three-times-five-minutes-runs-on-work-with-5.1.42.md)
* [Three Times Five Minutes Runs on work with 5.2-wl86 key\_cache\_partitions on and off](sysbench-v0.5-3x-five-minute-runs-on-work-with-5.2-wl86.md)
* [Three Times Five Minutes Runs on work with 5.1 vs. 5.2-wl86 key\_cache\_partitions off](sysbench-v0.5-3x-five-minute-runs-on-work-with-5.1-vs.-5.2-wl86.md)
* [Three Times Fifteen Minutes Runs on perro with 5.2-wl86 key\_cache\_partitions off, 8, and 32 and key\_buffer\_size 400](sysbench-v0.5-3x-15-minute-runs-on-perro-with-5.2-wl86-a.md)
* [Three Times Fifteen Minutes Runs on perro with 5.2-wl86 key\_cache\_partitions off, 8, and 32 and key\_buffer\_size 75](sysbench-v0.5-3x-15-minute-runs-on-perro-with-5.2-wl86-b.md)
* [select\_random\_ranges and select\_random\_points](select-random-ranges-and-select-random-point.md)
* `select_100_random_points.lua` result on perro with key\_cache\_partitions off and 32
* `select_random_points.lua --random-points=50` result on perro with key\_cache\_partitions off and 32
* `select_random_points.lua --random-points=10` result on perro with key\_cache\_partitions off and 32
* `select_random_points.lua --random-points=10, 50, and 100` results on perro with key\_cache\_segments off, 32, and 64
* `select_random_points.lua --random-points=10, 50, and 100` results on pitbull with key\_cache\_segments off, 32, and 64

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
