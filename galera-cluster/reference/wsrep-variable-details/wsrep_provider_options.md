# wsrep\_provider\_options

The following options can be set as part of the Galera [wsrep\_provider\_options](../galera-cluster-system-variables.md#wsrep_provider_options) variable. Dynamic options can be changed while the server is running.

Options need to be provided as a semicolon (;) separated list on a single line. Options that are not explicitly set are set to their default value.

Note that before Galera 3, the `repl` tag was named `replicator`.

#### `base_dir`

* Description: Specifies the data directory

#### `base_host`

* Description: For internal use. Should not be manually set.
* Default: `127.0.0.1` (detected network address)

#### `base_port`

* Description: For internal use. Should not be manually set.
* Default: `4567`

#### `cert.log_conflicts`

* Description: Certification failure log details.
* Dynamic: Yes
* Default: `no`

#### `cert.optimistic_pa`

* Description: Controls parallel application of actions on the replica. If set, the full range of parallelization as determined by the certification algorithm is permitted. If not set, the parallel applying window will not exceed that seen on the primary, and applying will start no sooner than after all actions it has seen on the master are committed.
* Dynamic: Yes
* Default: `yes`

#### `debug`

* Description: Enable debugging.
* Dynamic: Yes
* Default: `no`

#### `evs.auto_evict`

* Description: Number of entries the node permits for a given delayed node before triggering the Auto Eviction protocol. An entry is added to a delayed list for each delayed response from a node. If set to `0`, the default, the Auto Eviction protocol is disabled for this node. See [Auto Eviction](https://galeracluster.com/library/documentation/auto-eviction.html) for more.
* Dynamic: No
* Default: `0`

#### `evs.causal_keepalive_period`

* Description: Used by the developers only, and not manually serviceable.
* Dynamic: No
* Default: The [evs.keepalive\_period](wsrep_provider_options.md#evskeepalive_period).

#### `evs.debug_log_mask`

* Description: Controls EVS debug logging. Only effective when [wsrep\_debug](../galera-cluster-system-variables.md#wsrep_debug) is on.
* Dynamic: Yes
* Default: `0x1`

#### `evs.delay_margin`

* Description: Time that response times can be delayed before this node adds an entry to the delayed list. See [evs.auto\_evict](wsrep_provider_options.md#evsauto_evict). Must be set to a higher value than the round-trip delay time between nodes.
* Dynamic: No
* Default: `PT1S`

#### `evs.delayed_keep_period`

* Description: Time that this node requires a previously delayed node to remain responsive before being removed from the delayed list. See [evs.auto\_evict](wsrep_provider_options.md#evsauto_evict).
* Dynamic: No
* Default: `PT30S`

#### `evs.evict`

* Description: When set to the gcomm UUID of a node, that node is evicted from the cluster. When set to an empty string, the eviction list is cleared on the node where it is set. See [evs.auto\_evict](wsrep_provider_options.md#evsauto_evict).
* Dynamic: No
* Default: Empty string

#### `evs.inactive_check_period`

* Description: Frequency of checks for peer inactivity (looking for nodes with delayed responses), after which nodes may be added to the delayed list, and later evicted.
* Dynamic: No
* Default: `PT0.5S`

#### `evs.inactive_timeout`

* Description: Time limit that a node can be inactive before being pronounced as dead.
* Dynamic: No
* Default: `PT15S`

#### `evs.info_log_mask`

* Description: Controls extra EVS info logging. Bits:
  * 0x1 – extra view change information
  * 0x2 – extra state change information
  * 0x4 – statistics
  * 0x8 – profiling (only available in builds with profiling enabled)
* Dynamic: No
* Default: `0`

#### `evs.install_timeout`

* Description: Timeout on waits for install message acknowledgments. Replaces evs.consensus\_timeout.
* Dynamic: Yes
* Default: `PT7.5S`

#### `evs.join_retrans_period`

* Description: Time period for how often retransmission of EVS join messages when forming cluster membership should occur.
* Dynamic: Yes
* Default: `PT1S`

#### `evs.keepalive_period`

* Description: How often keepalive signals should be transmitted when there's no other traffic.
* Dynamic: Yes
* Default: `PT1S`

#### `evs.max_install_timeouts`

* Description: Number of membership install rounds to attempt before timing out. The total rounds will be this value plus two.
* Dynamic: No
* Default: `3`

#### `evs.send_window`

* Description: Maximum number of packets that can be replicated at a time, Must be more than [evs.user\_send\_window](wsrep_provider_options.md#evsuser_send_window), which applies to data packets only (double is recommended). In WAN environments can be set much higher than the default, for example `512`.
* Dynamic: Yes
* Default: `4`

#### `evs.stats_report_period`

* Description: Reporting period for EVS statistics.
* Dynamic: No
* Default: `PT1M`

#### `evs.suspect_timeout`

* Description: A node will be suspected to be dead after this period of inactivity. If all nodes agree, the node is dropped from the cluster before [evs.inactive\_timeout](wsrep_provider_options.md#evsinactive_timeout) is reached.
* Dynamic: No
* Default: `PT5S`

#### `evs.use_aggregate`

* Description: If set to `true` (the default), small packets will be aggregated into one where possible.
* Dynamic: No
* Default: `true`

#### `evs.user_send_window`

* Description: Maximum number of data packets that can be replicated at a time. Must be smaller than [evs.send\_window](wsrep_provider_options.md#evssend_window) (half is recommended). In WAN environments can be set much higher than the default, for example `512`.
* Dynamic: Yes
* Default: `2`

#### `evs.version`

* Description: EVS protocol version. Defaults to `0` for backward compatibility. Certain EVS features (e.g. auto eviction) require more recent versions.
* Dynamic: No
* Default: `0`

#### `evs.view_forget_timeout`

* Description: Time after which past views will be dropped from the view history.
* Dynamic: No
* Default: `P1D`

#### `gcache.dir`

* Description: Directory where GCache files are placed.
* Dynamic: No
* Default: The working directory

#### `gcache.keep_pages_size`

* Description: Total size of the page storage pages for caching. One page is always present if only page storage is enabled.
* Dynamic: No
* Default: `0`

#### `gcache.mem_size`

* Description: Maximum size of size of the malloc() store for setups that have spare RAM.
* Dynamic: No
* Default: `0`

#### `gcache.name`

* Description: Gcache ring buffer storage file name. By default placed in the working directory, changing to another location or partition can reduce disk IO.
* Dynamic: No
* Default: `./galera.cache`

***

#### `gcache.page_size`

* Description: Size of the page storage page files. These are prefixed by `gcache.page`. Can be set to as large as the disk can handle.
* Dynamic: No
* Default: `128M`

#### `gcache.recover`

* Description: Whether or not gcache recovery takes place when the node starts up. If it is possible to recover gcache, the node can then provide IST to other joining nodes, which assists when the whole cluster is restarted.
* Dynamic: No
* Default: `no`
* Introduced: [MariaDB 10.1.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10120-release-notes), [MariaDB Galera 10.0.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10029-release-notes), [MariaDB Galera 5.5.54](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-cluster-5554-release-notes)

#### `gcache.size`

* Description: Gcache ring buffer storage size (the space the node uses for caching write sets), preallocated on startup.
* Dynamic: No
* Default: `128M`

#### `gcomm.thread_prio`

{% hint style="info" %}
`fifo` or `rr` real-time scheduling policies requires  `mariadb` service permissions at the OS level.
{% endhint %}

* Description: Gcomm thread policy and priority (in the format `policy:priority`. Priority is an integer, while policy can be one of:
  * `fifo`: First-in, first-out scheduling. Always preempt other, batch or idle threads and can only be preempted by other `fifo` threads of a higher priority or blocked by an I/O request.
  * `rr`: Round-robin scheduling. Always preempt other, batch or idle threads. Runs for a fixed period of time after which the thread is stopped and moved to the end of the list, being replaced by another round-robin thread with the same priority. Otherwise runs until preempted by other `rr` threads of a higher priority or blocked by an I/O request.
  * `other`: Default scheduling on Linux. Threads run until preempted by a thread of a higher priority or a superior scheduling designation, or blocked by an I/O request.
*   Permissions: Using the `fifo` or `rr` real-time scheduling policies requires granting the `mariadb` service the necessary permissions at the OS level. On systemd-based distributions, this is done by adjusting the resource limits for the service.

    The recommended method is to create a systemd override file:

    1.  Open the MariaDB service unit for editing:

        ```bash
        sudo systemctl edit mariadb
        ```
    2.  Add the following content to the file. This grants the service the ability to set real-time priorities:

        ```toml
        [Service]
        LimitRTPRIO=infinity
        ```
    3. Save the file and exit the editor.
    4.  Reload the systemd daemon and restart the MariaDB service to apply the changes:

        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart mariadb
        ```
* Dynamic: No
* Default: Empty string

#### `gcs.fc_debug`

* Description: If set to a value greater than zero (the default), debug statistics about SST flow control will be posted each timegcs.fc\_master\_slave after the specified number of writesets.
* Dynamic: No
* Default: `0`

#### `gcs.fc_factor`

* Description:Fraction below [gcs.fc\_limit](wsrep_provider_options.md#gcsfc_limit) which if the recv queue drops below, replication resumes.
* Dynamic: Yes
* Default: `1.0`

#### `gcs.fc_limit`

* Description: If the recv queue exceeds this many writesets, replication is paused. Can increase greatly in master-slave setups. Replication will resume again according to the [gcs.fc\_factor](wsrep_provider_options.md#gcsfc_factor) setting.
* Dynamic: Yes
* Default: `16`

#### `gcs.fc_master_slave`

* Description: Whether to assume that the cluster only contains one master. Deprecated since Galera 4.10 ([MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/mariadb-1081-release-notes), [MariaDB 10.7.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1072-release-notes), [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.6), [MariaDB 10.5.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10514-release-notes), [MariaDB 10.4.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10422-release-notes)) - see [gcs.fc\_single\_primary](wsrep_provider_options.md#gcsfc_single_primary)
* Dynamic: No
* Default: `no`

#### `gcs.fc_single_primary`

* Description: Defines whether there is more than one source of replication.\
  As the number of nodes in the cluster grows, the larger the calculated gcs.fc\_limit gets. At the same time, the number of writes from the nodes increases.\
  When this parameter value is set to NO (multi-primary), the gcs.fc\_limit parameter is dynamically modified to give more margin for each node to be a bit further behind applying writes.\
  The gcs.fc\_limit parameter is modified by the square root of the cluster size, that is, in a four-node cluster it is two times higher than the base value. This is done to compensate for the increasing replication rate noise.
* Dynamic: No
* Default: `no`

#### `gcs.max_packet_size`

* Description: Maximum packet size, after which writesets become fragmented.
* Dynamic: No
* Default: `64500`

#### `gcs.max_throttle`

* Description: How much we can throttle replication rate during state transfer (to avoid running out of memory). Set it to 0.0 if stopping replication is acceptable for the sake of completing state transfer.
* Dynamic: No
* Default: `0.25`

#### `gcs.recv_q_hard_limit`

* Description: Maximum size of the recv queue. If exceeded, the server aborts. Half of available RAM plus swap is a recommended size.
* Dynamic: No
* Default: LLONG\_MAX

#### `gcs.recv_q_soft_limit`

* Description: Fraction of [gcs.recv\_q\_hard\_limit](wsrep_provider_options.md#gcsrecv_q_hard_limit) after which replication rate is throttled. The rate of throttling increases linearly from zero (the regular, varying rate of replication) at and below `csrecv_q_soft_limit` to one (full throttling) at [gcs.recv\_q\_hard\_limit](wsrep_provider_options.md#gcsrecv_q_hard_limit)
* Dynamic: No
* Default: `0.25`

#### `gcs.sync_donor`

* Description: Whether or not the rest of the cluster should stay in sync with the donor. If set to `YES` (`NO` is default), if the donor is blocked by state transfer, the whole cluster is also blocked.
* Dynamic: No
* Default: `no`

#### `gmcast.listen_addr`

* Description: Address Galera listens for connections from other nodes. Can be used to override the default port to listen, which is obtained from the connection address.
  * Specifying a hostname isn't supported. Use an IP number instead.
  *   You can specify the setting using either TCP or SSL, like this:

      `gmcast.listen_addr=tcp://192.168.8.111:4567`

      `gmcast.listen_addr=ssl://192.168.8.111:4567`&#x20;
  * If your system supports IPv6, you can also specify it like this:\
    `gmcast.listen_addr=tcp://[::]:4567`
* Dynamic: No
* Default: `tcp://0.0.0.0:4567`

#### `gmcast.mcast_addr`

* Description: Not set by default, but if set, UDP multicast will be used for replication. Must be identical on all nodes.For example, `gmcast.mcast_addr=239.192.0.11`
* Dynamic: No
* Default: None

#### `gmcast.mcast_ttl`

* Description: Multicast packet TTL (time to live) value.
* Dynamic: No
* Default: `1`

#### `gmcast.peer_timeout`

* Description: Connection timeout for initiating message relaying.
* Dynamic: No
* Default: `PT3S`

#### `gmcast.segment`

* Description: Defines the segment to which the node belongs. By default, all nodes are placed in the same segment (`0`). Usually, you would place all nodes in the same datacenter in the same segment. Galera protocol traffic is only redirected to one node in each segment, and then relayed to other nodes in that same segment, which saves cross-datacenter network traffic at the expense of some extra latency. State transfers are also, preferably but not exclusively, taken from the same segment. If there are no nodes available in the same segment, state transfer will be taken from a node in another segment.
* Dynamic: No
* Default: `0`
* Range: `0` to `255`

#### `gmcast.time_wait`

* Description: Waiting time before allowing a peer that was declared outside of the stable view to reconnect.
* Dynamic: No
* Default: `PT5S`

#### `gmcast.version`

* Description: Deprecated option. Gmcast version.
* Dynamic: No
* Default: `0`

#### `ist.recv_addr`

* Description: Address for listening for Incremental State Transfer.
* Dynamic: No
* Default::\<port+1> from [wsrep\_node\_address](../galera-cluster-system-variables.md#wsrep_node_address)

#### `ist.recv_bind`

* Description:
* Dynamic: No
* Default: Empty string
  * Introduced: [MariaDB 10.1.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10117-release-notes), [MariaDB Galera 10.0.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10027-release-notes), [MariaDB Galera 5.5.51](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-cluster-5551-release-notes)

#### `pc.announce_timeout`

* Description: Period of time for which cluster joining announcements are sent every 1/2 second.
* Dynamic: No
* Default: `PT3S`

#### `pc.checksum`

* Description: For debug purposes, by default `false` (`true` in earlier releases), indicates whether to checksum replicated messages on PC level. Safe to turn off.
* Dynamic: No
* Default: `false`

#### `pc.ignore_quorum`

* Description: Whether to ignore quorum calculations, for example when a master splits from several slaves, it will remain in operation if set to `true` (`false is default`). Use with care however, as in master-slave setups, slaves will not automatically reconnect to the master if set.
* Dynamic: Yes
* Default: `false`

#### `pc.ignore_sb`

* Description: Whether to permit updates to be processed even in the case of split brain (when a node is disconnected from its remaining peers). Safe in master-slave setups, but could lead to data inconsistency in a multi-master setup.
* Dynamic: Yes
* Default: `false`

#### `pc.linger`

* Description: Time that the PC protocol waits for EVS termination.
* Dynamic: No
* Default: `PT20S`

#### `pc.npvo`

* Description: If set to `true` (`false` is default), when there are primary component conficts, the most recent component will override the older.
* Dynamic: No
* Default: `false`

#### `pc.recovery`

* Description: If set to `true` (the default), the Primary Component state is stored on disk and in the case of a full cluster crash (e.g power outages), automatic recovery is then possible. Subsequent graceful full cluster restarts will require explicit bootstrapping for a new Primary Component.
* Dynamic: No
* Default: `true`

#### `pc.version`

* Description: Deprecated option. PC protocol version.
* Dynamic: No
* Default: `0`

#### `pc.wait_prim`

* Description: When set to `true`, the default, the node will wait for a primary component for the period of time specified by [pc.wait\_prim\_timeout](wsrep_provider_options.md#pc.wait_prim_timeout). Used to bring up non-primary components and make them primary using [pc.bootstrap](wsrep_provider_options.md#pcbootstrap.).
* Dynamic: No
* Default: `true`

#### `pc.wait_prim_timeout`

* Description: Ttime to wait for a primary component. See [pc.wait\_prim](wsrep_provider_options.md#pcwait_prim).
* Dynamic: No
* Default: `PT30S`

#### `pc.weight`

* Description: Node weight, used for quorum calculation. See the Codership article [Weighted Quorum](https://galeracluster.com/library/documentation/weighted-quorum.html#weighted-quorum).
* Dynamic: Yes
* Default: `1`

#### `protonet.backend`

* Description: Deprecated option. Transport backend to use. Only ASIO is supported currently.
* Dynamic: No
* Default: `asio`

#### `protonet.version`

* Description: Deprecated option. Protonet version.
* Dynamic: No
* Default: `0`

#### `repl.causal_read_timeout`

* Description: Timeout period for causal reads.
* Dynamic: Yes
* Default: `PT30S`

#### `repl.commit_order`

* Description: Whether or not out-of-order committing is permitted, and under what conditions. By default it is not permitted, but setting this can improve parallel performance.
  * `0` BYPASS: No commit order monitoring is done (useful for measuring the performance penalty).
  * `1` OOOC: Out-of-order committing is permitted for all transactions.
  * `2` LOCAL\_OOOC: Out-of-order committing is permitted for local transactions only.
  * `3` NO\_OOOC: Out-of-order committing is not permitted at all.
* Dynamic: No
* Default: `3`

#### `repl.key_format`

* Description: Format for key replication. Can be one of:
  * `FLAT8` - shorter key with a higher probability of false positives when matching
  * `FLAT16` - longer key with a lower probability of false positives when matching
  * `FLAT8A` - shorter key with a higher probability of false positives when matching, includes annotations for debug purposes
  * `FLAT16A` - longer key with a lower probability of false positives when matching, includes annotations for debug purposes
* Dynamic: Yes
* Default: `FLAT8`

#### `repl.max_ws_size`

* Description:
* Dynamic:
* Default: `2147483647`

#### `repl.proto_max`

* Description:
* Dynamic:
* Default: `9`

#### `socket.checksum`

* Description: Method used for generating checksum. Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB with Galera 25.3.x must be started with `wsrep_provider_options='socket.checksum=1'` in order to make it backward compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x are not supported.
* Dynamic: No
* Default: `2`

#### `socket.dynamic`

* Description: Allow both encrypted and unencrypted connections between nodes. Typically this should be set to `false` (the default), when set to `true` encrypted connections will still be preferred, but will fall back to unencrypted connections when encryption is not possible, e.g. not enabled on all nodes yet. Needs to be `true` on all nodes when wanting to enable or disable encryption via a rolling restart. As this can't be changed at runtime a rolling restart to enable or disable encryption may need three restarts per node in total: one to enable `socket.dynamic` on each node, one to change the actual encryption settings on each node, and a final round to change `socket.dynamic` back to `false`.
* Dynamic: No
* Default: `false`
* Introduced: [MariaDB 10.4.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10419-release-notes), [MariaDB 10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-10510-release-notes), [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)

#### `socket.recv_buf_size`

* Description: Size in bytes of the receive buffer used on the network sockets between nodes, passed on to the kernel via the SO\_RCVBUF socket option.
* Dynamic: No
* Default:
  * > \= [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.2.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10232-release-notes), [MariaDB 10.1.45](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes): Auto
  * < [MariaDB 10.3.22](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10322-release-notes): [MariaDB 10.2.31](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10231-release-notes), [MariaDB 10.1.44](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10144-release-notes): `212992`

#### `socket.send_buf_size`

* Description: Size in bytes of the send buffer used on the network sockets between nodes, passed on to the kernel via the SO\_SNDBUF socket option.
* Dynamic: No
* Default:: Auto
* Introduced: [MariaDB 10.3.23](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10323-release-notes), [MariaDB 10.2.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10232-release-notes), [MariaDB 10.1.45](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10145-release-notes)

#### `socket.ssl`

* Description: Explicitly enables TLS usage by the wsrep Provider.
* Dynamic: No
* Default: `NO`

#### `socket.ssl_ca`

* Description: Path to Certificate Authority (CA) file. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option.
* Dynamic: No

#### `socket.ssl_cert`

* Description: Path to TLS certificate. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option.
* Dynamic: No

#### `socket.ssl_cipher`

* Description: TLS cipher to use. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option. Since [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes) defaults to the value of the [ssl\_cipher](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/ssltls-system-variables#ssl_cipher) system variable.
* Dynamic: No
* Default: system default, before [MariaDB 10.2.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10218-release-notes) defaults to `AES128-SHA`.

#### `socket.ssl_compression`

* Description: Compression to use on TLS connections. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option.
* Dynamic: No

#### `socket.ssl_key`

* Description: Path to TLS key file. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option.
* Dynamic: No

#### `socket.ssl_password_file`

* Description: Path to password file to use in TLS connections. Implicitly enables the [socket.ssl](wsrep_provider_options.md#socket.ssl) option.
* Dynamic: No

## See Also

* [Galera parameters documentation from Codership](https://galeracluster.com/library/documentation/galera-parameters.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
