# MaxScale Resource

The MaxScale resource represents a MaxScale instance and it is the core on top\
of which the modules build upon.

### Resource Operations

### Get global information

```
GET /v1/maxscale
```

Retrieve global information about a MaxScale instance. This includes various\
file locations, configuration options and version information.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/"
    },
    "data": {
        "attributes": {
            "parameters": { // Core MaxScale parameters
                "libdir": "/usr/lib64/maxscale",
                "datadir": "/var/lib/maxscale",
                "process_datadir": "/var/lib/maxscale/data16218",
                "cachedir": "/var/cache/maxscale",
                "configdir": "/etc",
                "config_persistdir": "/var/lib/maxscale/maxscale.cnf.d",
                "module_configdir": "/etc/maxscale.modules.d",
                "piddir": "/var/run/maxscale",
                "logdir": "/var/log/maxscale",
                "langdir": "/var/lib/maxscale",
                "execdir": "/usr/bin",
                "connector_plugindir": "/var/lib/plugin",
                "threads": 4,
                "thread_stack_size": 8388608,
                "auth_connect_timeout": 3,
                "auth_read_timeout": 1,
                "auth_write_timeout": 2,
                "skip_permission_checks": false,
                "admin_auth": false,
                "admin_enabled": true,
                "admin_log_auth_failures": true,
                "admin_host": "::",
                "admin_port": 8989,
                "admin_ssl_key": "",
                "admin_ssl_cert": "",
                "admin_ssl_ca_cert": "",
                "query_classifier": "",
                "query_classifier_cache_size": 416215859,
                "retain_last_statements": 2,
                "dump_last_statements": "never",
                "load_persisted_configs": false
            },
            "version": "2.3.6", // The MaxScale version
            "commit": "47158faf12c156775c39388652a77f8a8c542d28", // Commit that MaxScale was built from
            "started_at": "Thu, 04 Apr 2019 21:04:06 GMT", // The time when MaxScale was started
            "activated_at": "Thu, 04 Apr 2019 21:04:06 GMT", // The last time when the `passive` parameter was set to `false`
            "uptime": 337 // How many seconds MaxScale has been running
        },
        "id": "maxscale",
        "type": "maxscale"
    }
}
```

### Update MaxScale parameters

```
PATCH /v1/maxscale
```

Update MaxScale parameters. The request body must define updated values for the`data.attributes.parameters` object. The following parameters can be altered:

* [admin\_auth](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [auth\_connect\_timeout](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [auth\_read\_timeout](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [auth\_write\_timeout](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [admin\_log\_auth\_failures](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)
* [passive](../maxscale-24-getting-started/mariadb-maxscale-24-mariadb-maxscale-configuration-guide.md)

**Response**

Parameters modified:

`Status: 204 No Content`

Invalid JSON body:

`Status: 403 Forbidden`

### Get thread information

```
GET /v1/maxscale/threads/:id
```

Get the information and statistics of a particular thread. The _:id_ in\
the URI must map to a valid thread number between 0 and the configured\
value of `threads`.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/threads/0"
    },
    "data": {
        "id": "0",
        "type": "threads",
        "attributes": {
            "stats": {
                "reads": 2, // Number of EPOLLIN events
                "writes": 0, // number of EPOLLOUT events
                "errors": 0, // Number of EPOLLERR events
                "hangups": 0, // Number of EPOLLHUP or EPOLLRDHUP events
                "accepts": 0, // Number of EPOLLIN events for listeners
                "max_event_queue_length": 1, // Maximum number of events returned by epoll
                "max_exec_time": 0, // Maximum number of internal ticks (100ms per tick) an event took to execute
                "max_queue_time": 0, // Maximum number of internal ticks that an event waited in the queue
                "current_descriptors": 1, // How many file descriptors this thread is handling
                "total_descriptors": 1, // Total number of file descriptors added to this thread
                "load": { // Thread load in percentages i.e. 100 is 100%
                    "last_second": 0, // Load over the past second
                    "last_minute": 0, // Load over the past minute
                    "last_hour": 0 // Load over the past hour
                }
            }
        },
        "links": {
            "self": "http://localhost:8989/v1/threads/0"
        }
    }
}
```

### Get information for all threads

```
GET /v1/maxscale/threads
```

Get the information for all threads. Returns a collection of threads resources.

**Response**

`Status: 200 OK`

```
// See `/v1/maxscale/threads/:id` for a descriptions of the fields
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/threads/"
    },
    "data": [
        {
            "id": "0",
            "type": "threads",
            "attributes": {
                "stats": {
                    "reads": 1,
                    "writes": 0,
                    "errors": 0,
                    "hangups": 0,
                    "accepts": 0,
                    "blocking_polls": 116,
                    "event_queue_length": 1,
                    "max_event_queue_length": 1,
                    "max_exec_time": 0,
                    "max_queue_time": 0,
                    "current_descriptors": 1,
                    "total_descriptors": 1,
                    "load": {
                        "last_second": 0,
                        "last_minute": 0,
                        "last_hour": 0
                    }
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/threads/0"
            }
        },
        {
            "id": "1",
            "type": "threads",
            "attributes": {
                "stats": {
                    "reads": 1,
                    "writes": 0,
                    "errors": 0,
                    "hangups": 0,
                    "accepts": 0,
                    "blocking_polls": 116,
                    "event_queue_length": 1,
                    "max_event_queue_length": 1,
                    "max_exec_time": 0,
                    "max_queue_time": 0,
                    "current_descriptors": 1,
                    "total_descriptors": 1,
                    "load": {
                        "last_second": 0,
                        "last_minute": 0,
                        "last_hour": 0
                    }
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/threads/1"
            }
        },
        {
            "id": "2",
            "type": "threads",
            "attributes": {
                "stats": {
                    "reads": 1,
                    "writes": 0,
                    "errors": 0,
                    "hangups": 0,
                    "accepts": 0,
                    "blocking_polls": 116,
                    "event_queue_length": 1,
                    "max_event_queue_length": 1,
                    "max_exec_time": 0,
                    "max_queue_time": 0,
                    "current_descriptors": 1,
                    "total_descriptors": 1,
                    "load": {
                        "last_second": 0,
                        "last_minute": 0,
                        "last_hour": 0
                    }
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/threads/2"
            }
        },
        {
            "id": "3",
            "type": "threads",
            "attributes": {
                "stats": {
                    "reads": 1,
                    "writes": 0,
                    "errors": 0,
                    "hangups": 0,
                    "accepts": 0,
                    "blocking_polls": 116,
                    "event_queue_length": 1,
                    "max_event_queue_length": 1,
                    "max_exec_time": 0,
                    "max_queue_time": 0,
                    "current_descriptors": 1,
                    "total_descriptors": 1,
                    "load": {
                        "last_second": 0,
                        "last_minute": 0,
                        "last_hour": 0
                    }
                }
            },
            "links": {
                "self": "http://localhost:8989/v1/threads/3"
            }
        }
    ]
}
```

### Get logging information

```
GET /v1/maxscale/logs
```

Get information about the current state of logging, enabled log files and the\
location where the log files are stored.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/logs/"
    },
    "data": {
        "attributes": {
            "parameters": { // Logging parameters
                "highprecision": false,
                "maxlog": true,
                "syslog": true,
                "throttling": {
                    "count": 10,
                    "suppress_ms": 10000,
                    "window_ms": 1000
                },
                "log_warning": true,
                "log_notice": true,
                "log_info": true,
                "log_debug": false
            },
            "log_file": "/home/markusjm/build/log/maxscale/maxscale.log", // The file MaxScale is logging into if `maxlog` is enabled
            "log_priorities": [ // Enabled log priorities
                "error",
                "warning",
                "notice",
                "info"
            ]
        },
        "id": "logs",
        "type": "logs"
    }
}
```

### Update logging parameters

```
PATCH /v1/maxscale/logs
```

Update logging parameters. The request body must define updated values for the`data.attributes.parameters` object. All logging parameters can be altered at runtime.

**Response**

Parameters modified:

`Status: 204 No Content`

Invalid JSON body:

`Status: 403 Forbidden`

### Flush and rotate log files

```
POST /v1/maxscale/logs/flush
```

Flushes any pending messages to disk and reopens the log files. The body of the\
message is ignored.

**Response**

`Status: 204 No Content`

### Get task schedule

```
GET /v1/maxscale/tasks
```

Retrieve all pending tasks that are queued for execution.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/tasks/"
    },
    "data": [] // No tasks active
}
```

### Get a loaded module

```
GET /v1/maxscale/modules/:name
```

Retrieve information about a loaded module. The _:name_ must be the name of a\
valid loaded module.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/"
    },
    "data": {
        "id": "dbfwfilter",
        "type": "module",
        "attributes": {
            "module_type": "Filter",
            "version": "V1.2.0",
            "description": "Firewall Filter",
            "api": "filter",
            "status": "GA",
            "commands": [ // List of module commands
                {
                    "id": "rules/reload", // Name of the command
                    "type": "module_command",
                    "links": {
                        "self": "http://localhost:8989/v1/modules/dbfwfilter/rules/reload"
                    },
                    "attributes": {
                        "method": "POST", // Whether POST or GET should be used to call this command
                        "arg_min": 1, // Minimum number of arguments
                        "arg_max": 2, // Maximum number of arguments
                        "parameters": [ // Parameter types for the command
                            {
                                "description": "Filter to reload", // Parameter description
                                "type": "FILTER", // Value type
                                "required": true // Whether the parameter is required
                            },
                            {
                                "description": "Path to rule file",
                                "type": "[STRING]",
                                "required": false
                            }
                        ]
                    }
                }
            ],
            "parameters": [ // Module parameters
                {
                    "name": "rules", // Parameter name
                    "type": "path" // Parameter type
                },
                {
                    "name": "log_match",
                    "type": "bool",
                    "default_value": "false" // Default value of the parameter
                },
                {
                    "name": "log_no_match",
                    "type": "bool",
                    "default_value": "false"
                },
                {
                    "name": "action",
                    "type": "enum",
                    "default_value": "block",
                    "enum_values": [ // Accepted enumeration values
                        "allow",
                        "block",
                        "ignore"
                    ]
                }
            ]
        },
        "links": {
            "self": "http://localhost:8989/v1/modules/dbfwfilter"
        }
    }
}
```

### Get all loaded modules

```
GET /v1/maxscale/modules
```

Retrieve information about all loaded modules.

**Response**

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/"
    },
    "data": [
        {
            "id": "qc_sqlite",
            "type": "module",
            "attributes": {
                "module_type": "QueryClassifier",
                "version": "V1.0.0",
                "description": "Query classifier using sqlite.",
                "api": "query_classifier",
                "status": "Beta",
                "parameters": []
            },
            "links": {
                "self": "http://localhost:8989/v1/modules/qc_sqlite"
            }
        },
        {
            "id": "MySQLAuth",
            "type": "module",
            "attributes": {
                "module_type": "Authenticator",
                "version": "V1.1.0",
                "description": "The MySQL client to MaxScale authenticator implementation",
                "api": "authenticator",
                "status": "GA",
                "parameters": []
            },
            "links": {
                "self": "http://localhost:8989/v1/modules/MySQLAuth"
            }
        },
    ]
}
```

### Call a module command

For read-only commands:

```
GET /v1/maxscale/modules/:module/:command
```

For commands that can modify data:

```
POST /v1/maxscale/modules/:module/:command
```

Modules can expose commands that can be called via the REST API. The module\
resource lists all commands in the `data.attributes.commands` list. Each value\
is a command sub-resource identified by its `id` field and the HTTP method the\
command uses is defined by the `attributes.method` field.

The _:module_ in the URI must be a valid name of a loaded module and _:command_\
must be a valid command identifier that is exposed by that module. All\
parameters to the module commands are passed as HTTP request parameters.

Here is an example POST requests to the dbfwfilter module command _reload_ with\
two parameters, the name of the filter instance and the path to a file:

```
POST /v1/maxscale/modules/dbfwfilter/reload?my-dbfwfilter-instance&/path/to/file.txt
```

**Response**

Command with output:

`Status: 200 OK`

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/modules/dbfwfilter/rules/json"
    },
    "meta": [ // Output of module command (module dependent)
        {
            "name": "test3",
            "type": "COLUMN",
            "times_matched": 0
        }
    ]
}
```

The contents of the `meta` field will contain the output of the module\
command. This output depends on the command that is being executed. It can\
contain any valid JSON value.

Command with no output:

`Status: 204 No Content`

### Classify a statement

```
GET /v1/maxscale/query_classifier/classify?sql=<statement>
```

Classify provided statement and return the result.

**Response**

`Status: 200 OK`

```
GET /v1/maxscale/query_classifier/classify?sql=SELECT+1
```

```
{
    "links": {
        "self": "http://localhost:8989/v1/maxscale/query_classifier/classify"
    },
    "data": {
        "id": "classify",
        "type": "classify",
        "attributes": {
            "parse_result": "QC_QUERY_PARSED",
            "type_mask": "QUERY_TYPE_READ",
            "operation": "QUERY_OP_SELECT",
            "has_where_clause": false,
            "fields": [],
            "functions": []
        }
    }
}
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
