SkySQL Intelligent Proxy represents an optimized iteration of MariaDB MaxScale. The subsequent Configuration Manager parameters are leveraged to tailor the behavior of MariaDB MaxScale:"

| Name | Default Value |
|------|---------------|
| [causal_reads](https://mariadb.com/docs/xpand/ref/mxs/module-parameters/causal_reads/) | none |
| [causal_reads_timeout](https://mariadb.com/docs/xpand/ref/mxs/module-parameters/causal_reads_timeout/) | 10s |
| [delayed_retry](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/delayed_retry/) | true |
| [delayed_retry_timeout](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/delayed_retry_timeout/) | 10s |
| [failcount](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/failcount/) | 7 |
| [master_accept_reads](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/master_accept_reads,Router.readwritesplit/) | true |
| [master_reconnection](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/master_reconnection/) | true |
| [max_slave_connections](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/max_slave_connections/) | 255 |
| [max_slave_replication_lag](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/max_slave_replication_lag/) | 0ms |
| [monitor_interval](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/monitor_interval,Monitor.mariadbmon/) | 2000ms |
| [slave_selection_criteria](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/slave_selection_criteria/) | LEAST_CURRENT_OPERATIONS |
| [strict_multi_stmt](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/strict_multi_stmt/) | false |
| [strict_sp_calls](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/strict_sp_calls/) | false |
| [transaction_replay](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/transaction_replay/) | true |
| [transaction_replay_attempts](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/transaction_replay_attempts/) | 10 |
| [transaction_replay_max_size](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/transaction_replay_max_size/) | 10Mi |
| [transaction_replay_retry_on_deadlock](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/transaction_replay_retry_on_deadlock/) | true |
| [use_sql_variables_in](https://mariadb.com/docs/skysql/ref/mxs/module-parameters/use_sql_variables_in/) | all |
