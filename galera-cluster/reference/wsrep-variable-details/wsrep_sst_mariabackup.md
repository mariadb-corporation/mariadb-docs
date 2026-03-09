# wsrep\_sst\_mariabackup

#### `wsrep_sst_mariabackup` Variables

The `wsrep_sst_mariabackup` script handles the actual data transfer and processing during an SST. The variables it reads from the `[sst]` group control aspects of the backup format, compression, transfer mechanism, and logging.

The `wsrep_sst_mariadbbackup` script parses the following options:

* `streamfmt` (sfmt)
  * Default: `mbstream`
  * Description: Defines the streaming format used by `mariabackup` for the SST. `mbstream` indicates that `mariabackup` will output a continuous stream of data.

***

* `transferfmt` (tfmt)
  * Default: `socat`
  * Description: Specifies the transfer format or utility used to move the data stream from the donor to the joiner node. `socat` is the standard tool used for this purpose.

***

* `sockopt` (socket options)
  * Description: Allows additional socket options to be passed to the underlying network communication. This includes settings for TCP buffers, keep-alives, or other network-related tunables to optimize transfer performance.

***

* `progress`
  * Description: Controls whether progress information about the SST is displayed or logged. Enabling this option provides visual indicators or detailed log entries about the transfer's advancement.

***

* `time` (ttime)
  * Default: `0`
  * Description: When set to 1, logs the time spent on specific operations during the SST process to help with performance analysis. Specifies a space-separated list of extra files or directories to copy from the donor to the joiner node during the SST.

***

* `cpat`
  * Description: Related to a "copy pattern" or specific path handling during the SST. Its function depends on how the `wsrep_sst_mariabackup` script uses this pattern for file or directory management.

***

* `compressor` (scomp)
  * Description: Specifies the compression utility to be used on the data stream before transfer. Common values include `gzip`, `pigz`, `lz4`, or `qpress`, which reduce the data size for faster transmission over the network.

***

* `decompressor` (sdecomp)
  * Description: Specifies the decompression utility to be used on the receiving end (joiner node) to decompress the data stream that was compressed by `scomp`. It should correspond to the `scomp` setting.

***

* `rlimit` (resource limit)
  * Description: Sets a maximum data transfer rate for State Snapshot Transfers (SST) in which the node serves as a donor. The `rlimit` parameter accepts any value supported by the `pv` utility’s `--rate-limit` option. Note that using this option requires `progress` to be specified and the `pv` utility to be installed on the system.

***

* &#x20;`use-extra` (uextra)
  * Default: `0`
  * Description: Controls the SST connection method that `mariabackup` uses to connect to the local MariaDB server.  By default _(_`uextra=0`_),_ mariabackup connects through the standard database por&#x74;_._ When `uextra=1` is enabled, the connection attempts to use either:
    * The unix socket (if available), or&#x20;
    * The extra\_port (if specified in MariaDB server settings).

***

* `sst-special-dirs` (speciald)
  * Default: `1`
  * Description: A boolean flag that controls whether `mariabackup` handles  special directories (e.g., `innodb_log_group_home_dir`, `datadir`) in a specific way during the SST, rather than just copying them as regular files. This is important for maintaining data consistency.

***

* `sst-initial-timeout` (stimeout)
  * Default: `300`
  * Description: Sets an initial timeout in seconds for the SST process. If the SST operation does not establish a connection or make progress within this period, it will be aborted.

***

* `sst-syslog` (ssyslog)
  * Default: `0`
  * Description: A boolean flag (0 or 1) that controls whether SST-related messages should be logged to syslog. This can be useful for centralized logging and monitoring of Galera cluster events.

***

* `sst-log-archive` (sstlogarchive)
  * Default: `1`
  * Description: A boolean flag (0 or 1) that determines whether SST logs should be archived. Archiving logs helps in post-mortem analysis and troubleshooting of SST failures.

***

* `sst-log-archive-dir` (sstlogarchivedir)
  * Description: Specifies the directory where SST logs should be archived if `sstlogarchive` is enabled.

### Example

#### Set in Configuration File

To configure `wsrep_sst_mariabackup` options, add them to the `[sst]` group in your configuration file:

{% code overflow="wrap" %}
```ini
[sst] 
streamfmt=mbstream 
transferfmt=socat 
compressor=lz4 
decompressor=lz4 
sst-initial-timeout=600 
sst-log-archive=1
```
{% endcode %}
