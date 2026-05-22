# Profiling Memory Usage with Heaptrack

Heaptrack is a memory profiler used to track allocation patterns, locate memory leaks, and analyze consumption spikes in MariaDB ColumnStore subprocesses, specifically `PrimProc`. The outputs help generate performance flame graphs for deep-dive engineering diagnostics.

## Installation

1.  Clone the directory:

    ```bash
    git clone https://github.com/KDE/heaptrack.git
    ```
2.  Install the development tools group:

    ```bash
    dnf group install "Development Tools" -y
    ```
3.  Create the build folder layout:

    ```bash
    cd heaptrack
    mkdir build
    cd build
    ```
4.  Install prerequisite library dependencies:

    ```bash
    yum install cmake libunwind libunwind-devel boost boost-devel -y
    ```
5.  Configure the build files for a Release target:

    ```bash
    cmake -DCMAKE_BUILD_TYPE=Release .. # look for messages about missing dependencies!
    ```
6.  Compile the tracking application:

    ```bash
    make -j$(nproc)
    ```
7.  Verify the compiled tracking binary target path:

    ```bash
    ls -la /home/rocky/heaptrack/build/bin/heaptrack
    ```

## Running a Memory Profile

1.  Stop the active process service:

    ```
    systemctl stop mcs-primproc
    ```
2.  Relaunch the process in the foreground under Heaptrack:

    ```
    /home/rocky/heaptrack/build/bin/heaptrack /usr/bin/PrimProc -f
    ```

## Capturing and Sharing Results

1.  Check system logs for process behaviors:

    ```bash
    journalctl -ru mcs-primproc
    ```
2.  Stop the process service wrapper instance:

    ```bash
    systemctl stop mcs-primproc
    ```
3. Halt the tracing session: Press `Ctrl` + `C` in the active heaptrack window.
4.  Share the compressed data profile with engineering: Locate and transfer the resulting archive artifact:

    ```
    /home/rocky/heaptrack/build/heaptrack.PrimProc.37747.zst
    ```

## Historical Engineering References

The following benchmarking and signal commands are preserved from internal engineering logs as testing options and should be adapted carefully based on your specific verification context:

{% code overflow="wrap" %}
```bash
# Simulating database workloads via sysbench:
# time sysbench /mnt/data/perf/s21.lua --mysql-db=tpc_h --mysql-user=root --skip_trx --events=8 --threads=5 --time=3600 run --histogram --report-interval=1

# Triggering a manual process crash context:
# kill -SIGHUP $(pidof PrimProc);
```
{% endcode %}
