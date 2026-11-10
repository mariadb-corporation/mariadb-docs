---
description: >-
  MariaDB Cloud Intelligent Proxy is the cloud-tuned MariaDB MaxScale;
  reference for Configuration Manager parameters such as causal_reads,
  delayed_retry, and routing behavior.
---

# MariaDB Cloud Intelligent Proxy

MariaDB Cloud Intelligent Proxy represents an optimized iteration of MariaDB MaxScale. The subsequent Configuration Manager parameters are leveraged to tailor the behavior of MariaDB MaxScale:

| Name                                                                                                                                                                                                                                             | Default Value              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| [causal\_reads](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#causal_reads)                                                                                                                  | none                       |
| [causal\_reads\_timeout](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#causal_reads_timeout)                                                                                                 | 10s                        |
| [delayed\_retry](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#delayed_retry)                                                                                                                | true                       |
| [delayed\_retry\_timeout](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#delayed_retry_timeout)                                                                                               | 10s                        |
| [failcount](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/mariadb-monitor#failcount)                                                                                                                                | 7                          |
| [master\_accept\_reads](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#master_accept_reads)                                                                                                   | true                       |
| [master\_reconnection](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#master_reconnection)                                                                                                    | true                       |
| [max\_slave\_connections](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#max_slave_connections)                                                                                               | 255                        |
| [max\_replication\_lag](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#max_replication_lag)                                                                                                   | 0ms                        |
| [monitor\_interval](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-old-versions/mariadb-maxscale-25-01/mariadb-maxscale-2501-maxscale-25-01-monitors/mariadb-maxscale-2501-maxscale-2501-common-monitor-parameters#monitor_interval) | 2000ms                     |
| [slave\_selection\_criteria](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#slave_selection_criteria)                                                                                         | LEAST\_CURRENT\_OPERATIONS |
| [strict\_multi\_stmt](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#strict_multi_stmt)                                                                                                       | false                      |
| [strict\_sp\_calls](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#strict_sp_calls)                                                                                                           | false                      |
| [transaction\_replay](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#transaction_replay)                                                                                                      | true                       |
| [transaction\_replay\_attempts](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#transaction_replay_attempts)                                                                                   | 10                         |
| [transaction\_replay\_max\_size](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#transaction_replay_max_size)                                                                                  | 10Mi                       |
| [transaction\_replay\_retry\_on\_deadlock](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#transaction_replay_retry_on_deadlock)                                                               | true                       |
| [use\_sql\_variables\_in](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit/readwritesplit-settings#use_sql_variables_in)                                                                                                | all                        |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
