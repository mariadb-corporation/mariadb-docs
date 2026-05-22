# Capturing System-Level Process Dumps (Core Dumps)

When a critical MariaDB ColumnStore process (such as `PrimProc` or `ExeMgr`) terminates unexpectedly due to a segmentation fault (segfault), the operating system can write the contents of its memory state to a core dump file. These files are invaluable for post-mortem debugging and determining the exact root cause of a failure.

By default, many modern Linux distributions limit or disable core dump generation to conserve disk space. This guide outlines how to configure a RHEL/CentOS-based system to capture complete, uncompressed core dumps for ColumnStore processes.

{% stepper %}
{% step %}
### Configure OS Resource Limits (`limits.conf`)

The operating system enforces shell-level resource limits (`ulimits`) that prevent large processes from writing files that exceed set maximum sizes. Because ColumnStore processes utilize substantial memory, resource limits must be explicitly set to `unlimited`.

1.  Open `/etc/security/limits.conf` in a text editor as `root`:

    ```bash
    sudo vi /etc/security/limits.conf
    ```
2.  Append the following lines to ensure the `mysql` user accounts (and root if applicable) have unrestricted core dump size permissions:

    ```
    mysql      soft    core    unlimited
    mysql      hard    core    unlimited
    root       soft    core    unlimited
    root       hard    core    unlimited
    ```
3. Save and close the file.
{% endstep %}

{% step %}
### Configure Systemd Coredump Behavior (`coredump.conf`)

On systemd-enabled operating systems (RHEL/CentOS 7/8/9), core dumps are often intercepted and managed by `systemd-coredump`. You must ensure that systemd does not truncate large core files.

1.  Open `/etc/systemd/coredump.conf`:

    ```bash
    sudo vi /etc/systemd/coredump.conf
    ```
2.  Modify or add parameters under the `[Coredump]` section to adjust max sizes for large analytics engine processes:

    ```ini
    [Coredump]
    Storage=external
    Compress=no
    ProcessSizeMax=unlimited
    ExternalSizeMax=unlimited
    MaxUse=20G
    ```
3.  Reload the systemd daemon to apply changes:

    ```bash
    sudo systemctl daemon-reload
    ```
{% endstep %}

{% step %}
### Configure Core Storage Path (`sysctl.conf`)

To ensure core dumps are saved persistently and with standard naming conventions, the kernel must be directed to write files into a dedicated space using a custom file pattern.

1.  Open `/etc/sysctl.conf` to persistently set kernel behavior:

    ```bash
    sudo vi /etc/sysctl.conf
    ```
2.  Add the following line to route core dumps into a persistent directory layout using variables for process name (`%e`), process ID (`%p`), and epoch timestamp (`%t`):

    ```
    kernel.core_pattern = /var/crash/core-%e-%p-%t
    ```
3.  Force the kernel to read and apply the parameters immediately without a reboot:

    Bash

    ```bash
    sudo sysctl -p
    ```
{% endstep %}

{% step %}
### Create and Secure the Target Directory

For a service process to successfully write a core file, it requires absolute write access to the targeted filesystem partition.

1.  Create the targeted path directory specified in the kernel pattern:

    ```bash
    sudo mkdir -p /var/crash
    ```
2.  Apply full read, write, and execute permissions globally (`777`). This is an explicit requirement to guarantee that the `mysql` runtime context can safely dump its memory segments into the root-owned path directory:

    ```bash
    sudo chmod 777 /var/crash
    ```
{% endstep %}

{% step %}
### Verification

To verify that changes have been applied correctly across the node, start a new interactive session or restart the core process and check that resource limits have refreshed:

```bash
ulimit -c
```

_Expected Output:_

```
unlimited
```

You can also view the limits of a currently running ColumnStore process by checking its runtime environment explicitly via its PID:

```bash
cat /proc/$(pidof PrimProc)/limits | grep "Max core file size"
```
{% endstep %}
{% endstepper %}
