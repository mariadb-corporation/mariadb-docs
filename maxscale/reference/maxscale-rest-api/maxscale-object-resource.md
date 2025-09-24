# MaxScale Object Resource

The objects resource collection contains all of the objects that are in
MaxScale: listeners, services, filters, servers and monitors. This is a "view"
on top of the other resource collection endpoints.

## Resource Operations

The _:name_ in all of the URIs must be the name of an object in MaxScale.

### Get an object

```
GET /v1/objects/:name
```

Get a single object.

#### Response

`Status: 200 OK`

```javascript
{
    "data": {
        "attributes": {
            "connections": 0,
            "listeners": [
                {
                    "attributes": {
                        "module": "MariaDBProtocol",
                        "parameters": {
                            "MariaDBProtocol": {
                                "allow_replication": true,
                                "compression": "zlib,zstd",
                                "compression_threshold": 50
                            },
                            "address": "::",
                            "authenticator": null,
                            "authenticator_options": null,
                            "connection_init_sql_file": null,
                            "connection_metadata": [
                                "character_set_client=auto",
                                "character_set_connection=auto",
                                "character_set_results=auto",
                                "max_allowed_packet=auto",
                                "system_time_zone=auto",
                                "time_zone=auto",
                                "tx_isolation=auto",
                                "maxscale=auto"
                            ],
                            "port": 4008,
                            "protocol": "MariaDBProtocol",
                            "proxy_protocol_networks": null,
                            "redirect_url": null,
                            "service": "Read-Connection-Router",
                            "socket": null,
                            "sql_mode": "default",
                            "ssl": false,
                            "ssl_ca": null,
                            "ssl_cert": null,
                            "ssl_cert_verify_depth": 9,
                            "ssl_cipher": null,
                            "ssl_crl": null,
                            "ssl_key": null,
                            "ssl_passphrase": "",
                            "ssl_verify_peer_certificate": false,
                            "ssl_verify_peer_host": false,
                            "ssl_version": "MAX",
                            "type": "listener",
                            "user_mapping_file": null
                        },
                        "source": {
                            "file": "/etc/maxscale.cnf",
                            "type": "static"
                        },
                        "state": "Running"
                    },
                    "id": "Read-Connection-Listener",
                    "relationships": {
                        "services": {
                            "data": [
                                {
                                    "id": "Read-Connection-Router",
                                    "type": "services"
                                }
                            ],
                            "links": {
                                "related": "http://localhost:8989/v1/services/",
                                "self": "http://localhost:8989/v1/listeners/Read-Connection-Listener/relationships/services/"
                            }
                        }
                    },
                    "type": "listeners"
                }
            ],
            "module": "readconnroute",
            "parameters": {
                "auth_all_servers": false,
                "connection_keepalive": "300000ms",
                "disable_sescmd_history": false,
                "enable_root_user": false,
                "force_connection_keepalive": false,
                "idle_session_pool_time": "-1ms",
                "localhost_match_wildcard_host": true,
                "log_auth_warnings": true,
                "log_debug": false,
                "log_info": false,
                "log_notice": false,
                "log_warning": false,
                "master_accept_reads": true,
                "max_connections": 0,
                "max_replication_lag": "0ms",
                "max_sescmd_history": 50,
                "multiplex_timeout": "60000ms",
                "net_write_timeout": "0ms",
                "password": "*****",
                "prune_sescmd_history": true,
                "rank": "primary",
                "retain_last_statements": -1,
                "role": null,
                "router": "readconnroute",
                "router_options": "master",
                "strip_db_esc": true,
                "type": "service",
                "user": "maxuser",
                "user_accounts_file": null,
                "user_accounts_file_usage": "add_when_load_ok",
                "version_string": null,
                "wait_timeout": "28800000ms"
            },
            "router": "readconnroute",
            "source": {
                "file": "/etc/maxscale.cnf",
                "type": "static"
            },
            "started": "Fri, 25 Jul 2025 15:43:46 GMT",
            "state": "Started",
            "statistics": {
                "active_operations": 0,
                "avg_sescmd_history_length": 0.0,
                "avg_session_active_pct": 0.0,
                "avg_session_lifetime": 0.0,
                "avg_session_queries": 0.0,
                "connections": 0,
                "failed_auths": 0,
                "max_connections": 0,
                "max_sescmd_history_length": 0,
                "max_session_active_pct": 0.0,
                "max_session_lifetime": 0.0,
                "max_session_queries": 0,
                "routed_packets": 0,
                "routed_reads": 0,
                "routed_writes": 0,
                "total_connections": 0
            },
            "total_connections": 0,
            "users": [
                {
                    "default_role": "",
                    "global_priv": false,
                    "host": "127.0.0.1",
                    "plugins": [
                        {
                            "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": false,
                    "user": "healthcheck"
                },
                {
                    "default_role": "",
                    "global_priv": false,
                    "host": "::1",
                    "plugins": [
                        {
                            "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": false,
                    "user": "healthcheck"
                },
                {
                    "default_role": "",
                    "global_priv": false,
                    "host": "localhost",
                    "plugins": [
                        {
                            "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": false,
                    "user": "healthcheck"
                },
                {
                    "default_role": "",
                    "global_priv": false,
                    "host": "localhost",
                    "plugins": [
                        {
                            "auth_string": "",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": false,
                    "user": "mariadb.sys"
                },
                {
                    "default_role": "",
                    "global_priv": true,
                    "host": "127.0.0.1",
                    "plugins": [
                        {
                            "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": true,
                    "user": "maxuser"
                },
                {
                    "default_role": "",
                    "global_priv": true,
                    "host": "%",
                    "plugins": [
                        {
                            "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": true,
                    "user": "maxuser"
                },
                {
                    "default_role": "",
                    "global_priv": true,
                    "host": "localhost",
                    "plugins": [
                        {
                            "auth_string": "",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": true,
                    "user": "root"
                },
                {
                    "default_role": "",
                    "global_priv": true,
                    "host": "%",
                    "plugins": [
                        {
                            "auth_string": "",
                            "plugin": "mysql_native_password"
                        }
                    ],
                    "proxy_priv": false,
                    "ssl": false,
                    "super_priv": true,
                    "user": "root"
                }
            ],
            "users_last_update": "Fri, 25 Jul 2025 15:43:49 GMT"
        },
        "id": "Read-Connection-Router",
        "links": {
            "self": "http://localhost:8989/v1/services/Read-Connection-Router/"
        },
        "relationships": {
            "filters": {
                "data": [
                    {
                        "id": "QLA",
                        "type": "filters"
                    },
                    {
                        "id": "Hint",
                        "type": "filters"
                    }
                ],
                "links": {
                    "related": "http://localhost:8989/v1/filters/",
                    "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/filters/"
                }
            },
            "listeners": {
                "data": [
                    {
                        "id": "Read-Connection-Listener",
                        "type": "listeners"
                    }
                ],
                "links": {
                    "related": "http://localhost:8989/v1/listeners/",
                    "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/listeners/"
                }
            },
            "servers": {
                "data": [
                    {
                        "id": "server1",
                        "type": "servers"
                    },
                    {
                        "id": "server2",
                        "type": "servers"
                    }
                ],
                "links": {
                    "related": "http://localhost:8989/v1/servers/",
                    "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/servers/"
                }
            }
        },
        "type": "services"
    },
    "links": {
        "self": "http://localhost:8989/v1/services/Read-Connection-Router/"
    }
}
```

### Get all objects

```
GET /v1/objects
```

Get all services.

#### Response

`Status: 200 OK`

```javascript
{
    "data": [
        {
            "attributes": {
                "connections": 1,
                "listeners": [
                    {
                        "attributes": {
                            "module": "MariaDBProtocol",
                            "parameters": {
                                "MariaDBProtocol": {
                                    "allow_replication": true,
                                    "compression": "zlib,zstd",
                                    "compression_threshold": 50
                                },
                                "address": "::",
                                "authenticator": null,
                                "authenticator_options": null,
                                "connection_init_sql_file": null,
                                "connection_metadata": [
                                    "character_set_client=auto",
                                    "character_set_connection=auto",
                                    "character_set_results=auto",
                                    "max_allowed_packet=auto",
                                    "system_time_zone=auto",
                                    "time_zone=auto",
                                    "tx_isolation=auto",
                                    "maxscale=auto"
                                ],
                                "port": 4006,
                                "protocol": "MariaDBProtocol",
                                "proxy_protocol_networks": null,
                                "redirect_url": null,
                                "service": "RW-Split-Router",
                                "socket": null,
                                "sql_mode": "default",
                                "ssl": false,
                                "ssl_ca": null,
                                "ssl_cert": null,
                                "ssl_cert_verify_depth": 9,
                                "ssl_cipher": null,
                                "ssl_crl": null,
                                "ssl_key": null,
                                "ssl_passphrase": "",
                                "ssl_verify_peer_certificate": false,
                                "ssl_verify_peer_host": false,
                                "ssl_version": "MAX",
                                "type": "listener",
                                "user_mapping_file": null
                            },
                            "source": {
                                "file": "/etc/maxscale.cnf",
                                "type": "static"
                            },
                            "state": "Running"
                        },
                        "id": "RW-Split-Listener",
                        "relationships": {
                            "services": {
                                "data": [
                                    {
                                        "id": "RW-Split-Router",
                                        "type": "services"
                                    }
                                ],
                                "links": {
                                    "related": "http://localhost:8989/v1/services/",
                                    "self": "http://localhost:8989/v1/listeners/RW-Split-Listener/relationships/services/"
                                }
                            }
                        },
                        "type": "listeners"
                    }
                ],
                "module": "readwritesplit",
                "parameters": {
                    "auth_all_servers": false,
                    "causal_reads": "none",
                    "causal_reads_timeout": "10000ms",
                    "connection_keepalive": "300000ms",
                    "delayed_retry": false,
                    "delayed_retry_timeout": "10000ms",
                    "disable_sescmd_history": false,
                    "enable_root_user": false,
                    "force_connection_keepalive": false,
                    "idle_session_pool_time": "-1ms",
                    "lazy_connect": false,
                    "localhost_match_wildcard_host": true,
                    "log_auth_warnings": true,
                    "log_debug": false,
                    "log_info": false,
                    "log_notice": false,
                    "log_warning": false,
                    "master_accept_reads": false,
                    "master_failure_mode": "fail_on_write",
                    "master_reconnection": true,
                    "max_connections": 0,
                    "max_replication_lag": "0ms",
                    "max_sescmd_history": 50,
                    "max_slave_connections": 255,
                    "multiplex_timeout": "60000ms",
                    "net_write_timeout": "0ms",
                    "password": "*****",
                    "prune_sescmd_history": true,
                    "rank": "primary",
                    "retain_last_statements": -1,
                    "retry_failed_reads": true,
                    "role": null,
                    "router": "readwritesplit",
                    "slave_connections": 255,
                    "slave_selection_criteria": "least_current_operations",
                    "strict_multi_stmt": false,
                    "strict_sp_calls": false,
                    "strict_tmp_tables": true,
                    "strip_db_esc": true,
                    "sync_transaction": "none",
                    "sync_transaction_count": 1,
                    "sync_transaction_max_lag": "0ms",
                    "sync_transaction_timeout": "10000ms",
                    "transaction_replay": false,
                    "transaction_replay_attempts": 5,
                    "transaction_replay_checksum": "full",
                    "transaction_replay_max_size": 1048576,
                    "transaction_replay_retry_on_deadlock": false,
                    "transaction_replay_retry_on_mismatch": false,
                    "transaction_replay_safe_commit": true,
                    "transaction_replay_timeout": "30000ms",
                    "type": "service",
                    "use_sql_variables_in": "all",
                    "user": "maxuser",
                    "user_accounts_file": null,
                    "user_accounts_file_usage": "add_when_load_ok",
                    "version_string": null,
                    "wait_timeout": "28800000ms"
                },
                "router": "readwritesplit",
                "router_diagnostics": {
                    "queries": 4,
                    "replayed_transactions": 0,
                    "ro_transactions": 0,
                    "route_all": 1,
                    "route_master": 3,
                    "route_slave": 0,
                    "rw_transactions": 1,
                    "sync_transaction_in_progress": 0,
                    "sync_transaction_lag": 0.0,
                    "sync_transaction_ok": 0,
                    "sync_transaction_timeout": 0,
                    "trx_max_size_exceeded": 0
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "started": "Fri, 25 Jul 2025 15:43:46 GMT",
                "state": "Started",
                "statistics": {
                    "active_operations": 0,
                    "avg_sescmd_history_length": 0.0,
                    "avg_session_active_pct": 0.0,
                    "avg_session_lifetime": 0.0,
                    "avg_session_queries": 0.0,
                    "connections": 1,
                    "failed_auths": 0,
                    "max_connections": 1,
                    "max_sescmd_history_length": 0,
                    "max_session_active_pct": 0.0,
                    "max_session_lifetime": 0.0,
                    "max_session_queries": 0,
                    "routed_packets": 4,
                    "routed_reads": 0,
                    "routed_writes": 4,
                    "total_connections": 1
                },
                "total_connections": 1,
                "users": [
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "127.0.0.1",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "::1",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "mariadb.sys"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "127.0.0.1",
                        "plugins": [
                            {
                                "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "maxuser"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "%",
                        "plugins": [
                            {
                                "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "maxuser"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "root"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "%",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "root"
                    }
                ],
                "users_last_update": "Fri, 25 Jul 2025 15:43:49 GMT"
            },
            "id": "RW-Split-Router",
            "links": {
                "self": "http://localhost:8989/v1/services/RW-Split-Router/"
            },
            "relationships": {
                "listeners": {
                    "data": [
                        {
                            "id": "RW-Split-Listener",
                            "type": "listeners"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/listeners/",
                        "self": "http://localhost:8989/v1/services/RW-Split-Router/relationships/listeners/"
                    }
                },
                "monitors": {
                    "data": [
                        {
                            "id": "MariaDB-Monitor",
                            "type": "monitors"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/monitors/",
                        "self": "http://localhost:8989/v1/services/RW-Split-Router/relationships/monitors/"
                    }
                }
            },
            "type": "services"
        },
        {
            "attributes": {
                "connections": 0,
                "listeners": [
                    {
                        "attributes": {
                            "module": "MariaDBProtocol",
                            "parameters": {
                                "MariaDBProtocol": {
                                    "allow_replication": true,
                                    "compression": "zlib,zstd",
                                    "compression_threshold": 50
                                },
                                "address": "::",
                                "authenticator": null,
                                "authenticator_options": null,
                                "connection_init_sql_file": null,
                                "connection_metadata": [
                                    "character_set_client=auto",
                                    "character_set_connection=auto",
                                    "character_set_results=auto",
                                    "max_allowed_packet=auto",
                                    "system_time_zone=auto",
                                    "time_zone=auto",
                                    "tx_isolation=auto",
                                    "maxscale=auto"
                                ],
                                "port": 4008,
                                "protocol": "MariaDBProtocol",
                                "proxy_protocol_networks": null,
                                "redirect_url": null,
                                "service": "Read-Connection-Router",
                                "socket": null,
                                "sql_mode": "default",
                                "ssl": false,
                                "ssl_ca": null,
                                "ssl_cert": null,
                                "ssl_cert_verify_depth": 9,
                                "ssl_cipher": null,
                                "ssl_crl": null,
                                "ssl_key": null,
                                "ssl_passphrase": "",
                                "ssl_verify_peer_certificate": false,
                                "ssl_verify_peer_host": false,
                                "ssl_version": "MAX",
                                "type": "listener",
                                "user_mapping_file": null
                            },
                            "source": {
                                "file": "/etc/maxscale.cnf",
                                "type": "static"
                            },
                            "state": "Running"
                        },
                        "id": "Read-Connection-Listener",
                        "relationships": {
                            "services": {
                                "data": [
                                    {
                                        "id": "Read-Connection-Router",
                                        "type": "services"
                                    }
                                ],
                                "links": {
                                    "related": "http://localhost:8989/v1/services/",
                                    "self": "http://localhost:8989/v1/listeners/Read-Connection-Listener/relationships/services/"
                                }
                            }
                        },
                        "type": "listeners"
                    }
                ],
                "module": "readconnroute",
                "parameters": {
                    "auth_all_servers": false,
                    "connection_keepalive": "300000ms",
                    "disable_sescmd_history": false,
                    "enable_root_user": false,
                    "force_connection_keepalive": false,
                    "idle_session_pool_time": "-1ms",
                    "localhost_match_wildcard_host": true,
                    "log_auth_warnings": true,
                    "log_debug": false,
                    "log_info": false,
                    "log_notice": false,
                    "log_warning": false,
                    "master_accept_reads": true,
                    "max_connections": 0,
                    "max_replication_lag": "0ms",
                    "max_sescmd_history": 50,
                    "multiplex_timeout": "60000ms",
                    "net_write_timeout": "0ms",
                    "password": "*****",
                    "prune_sescmd_history": true,
                    "rank": "primary",
                    "retain_last_statements": -1,
                    "role": null,
                    "router": "readconnroute",
                    "router_options": "master",
                    "strip_db_esc": true,
                    "type": "service",
                    "user": "maxuser",
                    "user_accounts_file": null,
                    "user_accounts_file_usage": "add_when_load_ok",
                    "version_string": null,
                    "wait_timeout": "28800000ms"
                },
                "router": "readconnroute",
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "started": "Fri, 25 Jul 2025 15:43:46 GMT",
                "state": "Started",
                "statistics": {
                    "active_operations": 0,
                    "avg_sescmd_history_length": 0.0,
                    "avg_session_active_pct": 0.0,
                    "avg_session_lifetime": 0.0,
                    "avg_session_queries": 0.0,
                    "connections": 0,
                    "failed_auths": 0,
                    "max_connections": 0,
                    "max_sescmd_history_length": 0,
                    "max_session_active_pct": 0.0,
                    "max_session_lifetime": 0.0,
                    "max_session_queries": 0,
                    "routed_packets": 0,
                    "routed_reads": 0,
                    "routed_writes": 0,
                    "total_connections": 0
                },
                "total_connections": 0,
                "users": [
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "127.0.0.1",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "::1",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "976B96FB3F7898CCFFCABC014300C311FB7607FD",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "healthcheck"
                    },
                    {
                        "default_role": "",
                        "global_priv": false,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": false,
                        "user": "mariadb.sys"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "127.0.0.1",
                        "plugins": [
                            {
                                "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "maxuser"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "%",
                        "plugins": [
                            {
                                "auth_string": "5EDBD32E469DAE0CE10E6999C3899DEFCB9F12E0",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "maxuser"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "localhost",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "root"
                    },
                    {
                        "default_role": "",
                        "global_priv": true,
                        "host": "%",
                        "plugins": [
                            {
                                "auth_string": "",
                                "plugin": "mysql_native_password"
                            }
                        ],
                        "proxy_priv": false,
                        "ssl": false,
                        "super_priv": true,
                        "user": "root"
                    }
                ],
                "users_last_update": "Fri, 25 Jul 2025 15:43:49 GMT"
            },
            "id": "Read-Connection-Router",
            "links": {
                "self": "http://localhost:8989/v1/services/Read-Connection-Router/"
            },
            "relationships": {
                "filters": {
                    "data": [
                        {
                            "id": "QLA",
                            "type": "filters"
                        },
                        {
                            "id": "Hint",
                            "type": "filters"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/filters/",
                        "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/filters/"
                    }
                },
                "listeners": {
                    "data": [
                        {
                            "id": "Read-Connection-Listener",
                            "type": "listeners"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/listeners/",
                        "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/listeners/"
                    }
                },
                "servers": {
                    "data": [
                        {
                            "id": "server1",
                            "type": "servers"
                        },
                        {
                            "id": "server2",
                            "type": "servers"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/servers/",
                        "self": "http://localhost:8989/v1/services/Read-Connection-Router/relationships/servers/"
                    }
                }
            },
            "type": "services"
        },
        {
            "attributes": {
                "gtid_binlog_pos": "0-3000-5",
                "gtid_current_pos": "0-3000-5",
                "last_event": "master_up",
                "lock_held": null,
                "master_group": null,
                "master_id": -1,
                "name": "server1",
                "node_id": 3000,
                "parameters": {
                    "address": "127.0.0.1",
                    "disk_space_threshold": "",
                    "extra_port": 0,
                    "initial_status": "down",
                    "max_routing_connections": 0,
                    "monitorpw": null,
                    "monitoruser": null,
                    "persistmaxtime": "0ms",
                    "persistpoolmax": 0,
                    "port": 3000,
                    "priority": 0,
                    "private_address": null,
                    "proxy_protocol": false,
                    "rank": "primary",
                    "replication_custom_options": null,
                    "socket": null,
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_key": null,
                    "ssl_passphrase": "",
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "use_service_credentials": true
                },
                "read_only": false,
                "replication_lag": 0,
                "server_id": 3000,
                "slave_connections": [],
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Master, Running",
                "statistics": {
                    "active_operations": 0,
                    "adaptive_avg_select_time": "0ns",
                    "connection_pool_empty": 0,
                    "connections": 1,
                    "failed_auths": 0,
                    "max_connections": 1,
                    "max_pool_size": 0,
                    "persistent_connections": 0,
                    "response_time_distribution": {
                        "read": {
                            "distribution": [
                                {
                                    "count": 0,
                                    "time": "0.000001",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000010",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000100",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.001000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.010000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.100000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100000.000000",
                                    "total": 0.0
                                }
                            ],
                            "operation": "read",
                            "range_base": 10
                        },
                        "write": {
                            "distribution": [
                                {
                                    "count": 0,
                                    "time": "0.000001",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000010",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000100",
                                    "total": 0.0
                                },
                                {
                                    "count": 4,
                                    "time": "0.001000",
                                    "total": 0.001319181
                                },
                                {
                                    "count": 0,
                                    "time": "0.010000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.100000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100000.000000",
                                    "total": 0.0
                                }
                            ],
                            "operation": "write",
                            "range_base": 10
                        }
                    },
                    "reused_connections": 0,
                    "routed_packets": 4,
                    "routed_reads": 0,
                    "routed_writes": 4,
                    "total_connections": 1
                },
                "status": {
                    "extra": "",
                    "mode": "Normal",
                    "reason": [
                        "Primary"
                    ],
                    "state": "Write"
                },
                "triggered_at": "Fri, 25 Jul 2025 15:43:48 GMT",
                "uptime": 10,
                "version_string": "10.11.9-MariaDB-ubu2204-log"
            },
            "id": "server1",
            "links": {
                "self": "http://localhost:8989/v1/servers/server1/"
            },
            "relationships": {
                "monitors": {
                    "data": [
                        {
                            "id": "MariaDB-Monitor",
                            "type": "monitors"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/monitors/",
                        "self": "http://localhost:8989/v1/servers/server1/relationships/monitors/"
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        },
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/servers/server1/relationships/services/"
                    }
                }
            },
            "type": "servers"
        },
        {
            "attributes": {
                "gtid_binlog_pos": "0-3000-5",
                "gtid_current_pos": "0-3000-5",
                "last_event": "slave_up",
                "lock_held": null,
                "master_group": null,
                "master_id": 3000,
                "name": "server2",
                "node_id": 3001,
                "parameters": {
                    "address": "127.0.0.1",
                    "disk_space_threshold": "",
                    "extra_port": 0,
                    "initial_status": "down",
                    "max_routing_connections": 0,
                    "monitorpw": null,
                    "monitoruser": null,
                    "persistmaxtime": "0ms",
                    "persistpoolmax": 0,
                    "port": 3001,
                    "priority": 0,
                    "private_address": null,
                    "proxy_protocol": false,
                    "rank": "primary",
                    "replication_custom_options": null,
                    "socket": null,
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_key": null,
                    "ssl_passphrase": "",
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "use_service_credentials": true
                },
                "read_only": false,
                "replication_lag": 0,
                "server_id": 3001,
                "slave_connections": [
                    {
                        "connection_name": "",
                        "gtid_io_pos": "",
                        "last_io_error": "",
                        "last_sql_error": "",
                        "master_host": "127.0.0.1",
                        "master_port": 3000,
                        "master_server_id": 3000,
                        "master_server_name": "server1",
                        "seconds_behind_master": 0,
                        "slave_io_running": "Yes",
                        "slave_sql_running": "Yes",
                        "using_gtid": "No"
                    }
                ],
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Slave, Running",
                "statistics": {
                    "active_operations": 0,
                    "adaptive_avg_select_time": "0ns",
                    "connection_pool_empty": 0,
                    "connections": 1,
                    "failed_auths": 0,
                    "max_connections": 1,
                    "max_pool_size": 0,
                    "persistent_connections": 0,
                    "response_time_distribution": {
                        "read": {
                            "distribution": [
                                {
                                    "count": 0,
                                    "time": "0.000001",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000010",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000100",
                                    "total": 0.0
                                },
                                {
                                    "count": 1,
                                    "time": "0.001000",
                                    "total": 0.00066959099999999998
                                },
                                {
                                    "count": 0,
                                    "time": "0.010000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.100000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100000.000000",
                                    "total": 0.0
                                }
                            ],
                            "operation": "read",
                            "range_base": 10
                        },
                        "write": {
                            "distribution": [
                                {
                                    "count": 0,
                                    "time": "0.000001",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000010",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.000100",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.001000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.010000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "0.100000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "1000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "10000.000000",
                                    "total": 0.0
                                },
                                {
                                    "count": 0,
                                    "time": "100000.000000",
                                    "total": 0.0
                                }
                            ],
                            "operation": "write",
                            "range_base": 10
                        }
                    },
                    "reused_connections": 0,
                    "routed_packets": 1,
                    "routed_reads": 1,
                    "routed_writes": 0,
                    "total_connections": 1
                },
                "status": {
                    "extra": "",
                    "mode": "Normal",
                    "reason": [
                        "Replica"
                    ],
                    "state": "Read"
                },
                "triggered_at": "Fri, 25 Jul 2025 15:43:48 GMT",
                "uptime": 9,
                "version_string": "10.11.9-MariaDB-ubu2204-log"
            },
            "id": "server2",
            "links": {
                "self": "http://localhost:8989/v1/servers/server2/"
            },
            "relationships": {
                "monitors": {
                    "data": [
                        {
                            "id": "MariaDB-Monitor",
                            "type": "monitors"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/monitors/",
                        "self": "http://localhost:8989/v1/servers/server2/relationships/monitors/"
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        },
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/servers/server2/relationships/services/"
                    }
                }
            },
            "type": "servers"
        },
        {
            "attributes": {
                "module": "mariadbmon",
                "monitor_diagnostics": {
                    "failback_master": null,
                    "master": "server1",
                    "master_gtid_domain_id": 0,
                    "primary": null,
                    "server_info": [
                        {
                            "gtid_binlog_pos": "0-3000-5",
                            "gtid_current_pos": "0-3000-5",
                            "lock_held": null,
                            "master_group": null,
                            "name": "server1",
                            "read_only": false,
                            "server_id": 3000,
                            "slave_connections": []
                        },
                        {
                            "gtid_binlog_pos": "0-3000-5",
                            "gtid_current_pos": "0-3000-5",
                            "lock_held": null,
                            "master_group": null,
                            "name": "server2",
                            "read_only": false,
                            "server_id": 3001,
                            "slave_connections": [
                                {
                                    "connection_name": "",
                                    "gtid_io_pos": "",
                                    "last_io_error": "",
                                    "last_sql_error": "",
                                    "master_host": "127.0.0.1",
                                    "master_port": 3000,
                                    "master_server_id": 3000,
                                    "master_server_name": "server1",
                                    "seconds_behind_master": 0,
                                    "slave_io_running": "Yes",
                                    "slave_sql_running": "Yes",
                                    "using_gtid": "No"
                                }
                            ]
                        }
                    ],
                    "state": "Idle"
                },
                "parameters": {
                    "assume_unique_hostnames": true,
                    "auto_failback_switchover": false,
                    "auto_failover": "false",
                    "auto_rejoin": false,
                    "backend_connect_attempts": 1,
                    "backend_timeout": "3000ms",
                    "backup_storage_address": null,
                    "backup_storage_path": null,
                    "cooperative_monitoring_locks": "none",
                    "cs_admin_api_key": null,
                    "cs_admin_base_path": "/cmapi/0.4.0",
                    "cs_admin_port": 8640,
                    "demotion_sql_file": null,
                    "disk_space_check_interval": "0ms",
                    "disk_space_threshold": null,
                    "enforce_read_only_servers": false,
                    "enforce_read_only_slaves": false,
                    "enforce_simple_topology": false,
                    "enforce_writable_master": false,
                    "events": "all,master_down,master_up,slave_down,slave_up,server_down,server_up,synced_down,synced_up,donor_down,donor_up,lost_master,lost_slave,lost_synced,lost_donor,new_master,new_slave,new_synced,new_donor",
                    "failcount": 5,
                    "failover_timeout": "90000ms",
                    "handle_events": true,
                    "journal_max_age": "28800000ms",
                    "maintenance_on_low_disk_space": true,
                    "mariabackup_parallel": 1,
                    "mariabackup_use_memory": "1G",
                    "master_conditions": "primary_monitor_master,disk_space_ok",
                    "master_failure_timeout": "10000ms",
                    "module": "mariadbmon",
                    "monitor_interval": "1000ms",
                    "password": "*****",
                    "primary_state_sql": null,
                    "promotion_sql_file": null,
                    "rebuild_port": 4444,
                    "replica_state_sql": null,
                    "replication_custom_options": null,
                    "replication_master_ssl": false,
                    "replication_password": "*****",
                    "replication_user": "maxuser",
                    "role": null,
                    "script": null,
                    "script_max_replication_lag": -1,
                    "script_timeout": "90000ms",
                    "servers_no_cooperative_monitoring_locks": null,
                    "servers_no_promotion": null,
                    "slave_conditions": "",
                    "ssh_check_host_key": true,
                    "ssh_keyfile": null,
                    "ssh_port": 22,
                    "ssh_timeout": "10000ms",
                    "ssh_user": null,
                    "switchover_on_low_disk_space": false,
                    "switchover_timeout": "90000ms",
                    "type": "monitor",
                    "user": "maxuser",
                    "verify_master_failure": true,
                    "write_test_fail_action": "log",
                    "write_test_interval": "0ms",
                    "write_test_table": "mxs.maxscale_write_test"
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Running",
                "ticks": 12
            },
            "id": "MariaDB-Monitor",
            "links": {
                "self": "http://localhost:8989/v1/monitors/MariaDB-Monitor/"
            },
            "relationships": {
                "servers": {
                    "data": [
                        {
                            "id": "server1",
                            "type": "servers"
                        },
                        {
                            "id": "server2",
                            "type": "servers"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/servers/",
                        "self": "http://localhost:8989/v1/monitors/MariaDB-Monitor/relationships/servers/"
                    }
                },
                "services": {
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/monitors/MariaDB-Monitor/relationships/services/"
                    }
                }
            },
            "type": "monitors"
        },
        {
            "attributes": {
                "module": "qlafilter",
                "parameters": {
                    "append": false,
                    "duration_unit": "ms",
                    "exclude": null,
                    "filebase": "/tmp/qla.log",
                    "flush": true,
                    "log_data": "date,user,query",
                    "log_type": "unified",
                    "match": null,
                    "module": "qlafilter",
                    "newline_replacement": " ",
                    "options": "",
                    "separator": ",",
                    "source": null,
                    "source_exclude": null,
                    "source_match": null,
                    "use_canonical_form": false,
                    "user": null,
                    "user_exclude": null,
                    "user_match": null
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                }
            },
            "id": "QLA",
            "links": {
                "self": "http://localhost:8989/v1/filters/QLA/"
            },
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/filters/QLA/relationships/services/"
                    }
                }
            },
            "type": "filters"
        },
        {
            "attributes": {
                "module": "hintfilter",
                "parameters": {
                    "module": "hintfilter"
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                }
            },
            "id": "Hint",
            "links": {
                "self": "http://localhost:8989/v1/filters/Hint/"
            },
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/filters/Hint/relationships/services/"
                    }
                }
            },
            "type": "filters"
        },
        {
            "attributes": {
                "module": "MariaDBProtocol",
                "parameters": {
                    "MariaDBProtocol": {
                        "allow_replication": true,
                        "compression": "zlib,zstd",
                        "compression_threshold": 50
                    },
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": null,
                    "connection_init_sql_file": null,
                    "connection_metadata": [
                        "character_set_client=auto",
                        "character_set_connection=auto",
                        "character_set_results=auto",
                        "max_allowed_packet=auto",
                        "system_time_zone=auto",
                        "time_zone=auto",
                        "tx_isolation=auto",
                        "maxscale=auto"
                    ],
                    "port": 4006,
                    "protocol": "MariaDBProtocol",
                    "proxy_protocol_networks": null,
                    "redirect_url": null,
                    "service": "RW-Split-Router",
                    "socket": null,
                    "sql_mode": "default",
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_passphrase": "",
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "type": "listener",
                    "user_mapping_file": null
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Running"
            },
            "id": "RW-Split-Listener",
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "RW-Split-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/listeners/RW-Split-Listener/relationships/services/"
                    }
                }
            },
            "type": "listeners"
        },
        {
            "attributes": {
                "module": "MariaDBProtocol",
                "parameters": {
                    "MariaDBProtocol": {
                        "allow_replication": true,
                        "compression": "zlib,zstd",
                        "compression_threshold": 50
                    },
                    "address": "::",
                    "authenticator": null,
                    "authenticator_options": null,
                    "connection_init_sql_file": null,
                    "connection_metadata": [
                        "character_set_client=auto",
                        "character_set_connection=auto",
                        "character_set_results=auto",
                        "max_allowed_packet=auto",
                        "system_time_zone=auto",
                        "time_zone=auto",
                        "tx_isolation=auto",
                        "maxscale=auto"
                    ],
                    "port": 4008,
                    "protocol": "MariaDBProtocol",
                    "proxy_protocol_networks": null,
                    "redirect_url": null,
                    "service": "Read-Connection-Router",
                    "socket": null,
                    "sql_mode": "default",
                    "ssl": false,
                    "ssl_ca": null,
                    "ssl_cert": null,
                    "ssl_cert_verify_depth": 9,
                    "ssl_cipher": null,
                    "ssl_crl": null,
                    "ssl_key": null,
                    "ssl_passphrase": "",
                    "ssl_verify_peer_certificate": false,
                    "ssl_verify_peer_host": false,
                    "ssl_version": "MAX",
                    "type": "listener",
                    "user_mapping_file": null
                },
                "source": {
                    "file": "/etc/maxscale.cnf",
                    "type": "static"
                },
                "state": "Running"
            },
            "id": "Read-Connection-Listener",
            "relationships": {
                "services": {
                    "data": [
                        {
                            "id": "Read-Connection-Router",
                            "type": "services"
                        }
                    ],
                    "links": {
                        "related": "http://localhost:8989/v1/services/",
                        "self": "http://localhost:8989/v1/listeners/Read-Connection-Listener/relationships/services/"
                    }
                }
            },
            "type": "listeners"
        }
    ],
    "links": {
        "self": "http://localhost:8989/v1/objects/"
    }
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
