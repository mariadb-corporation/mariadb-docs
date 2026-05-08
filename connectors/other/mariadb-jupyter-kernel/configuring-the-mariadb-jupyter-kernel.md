---
description: >-
  The MariaDB Jupyter Kernel reads connection settings from a JSON config
  file, supporting options for host, port, credentials, server binary paths,
  and auto-start behavior.
---

# Configuring the MariaDB Jupyter Kernel

## Config File Location

The kernel can be configured via a `JSON` file called `mariadb_config.json`.

The kernel will look for this config file in one of these two locations:

1. If the [JUPYTER\_CONFIG\_DIR](https://jupyter.readthedocs.io/en/latest/use/jupyter-directories.html#envvar-JUPYTER_CONFIG_DIR) environment variable is defined (non-empty),[mariadb\_kernel](https://github.com/MariaDB/mariadb_kernel) will try to read `$JUPYTER_CONFIG_DIR/mariadb_config.json`
2. If the environment variable is empty, the kernel will try to read `$HOME/.jupyter/mariadb_config.json`

## Config Example

Here’s an example file containing some of the available options that you can pass to the kernel:

```json
cat ~/.jupyter/mariadb_config.json
{
    "user": "root",
    "host": "localhost",
    "port": "3306",
    "password": "securepassword",
    "start_server": "True",
    "client_bin": "/usr/bin/mariadb",
    "server_bin": "/usr/bin/mariadbd"
}
```

By default the kernel starts a MariaDB server running at `localhost`, on port `3306` and connects to this instance using the user `root` with `no password`. The kernel also assumes that MariaDB Server is installed and its binaries are in `PATH`.\
You can change any of these options to fit your use-case. This also means you can run a notebook locally with a [MariaDB kernel](https://github.com/MariaDB/mariadb_kernel), and make the kernel connect to a server running in the cloud for instance.

The kernel, using the default configuration, looks for the `mysql` and `mysqld` binaries in your `PATH`. You can point (for example if you have a local MariaDB built from sources) the kernel to an exact location for these two binaries using the `client_bin` and `server_bin` options.

The `start_server` option tells the kernel to start a MariaDB Server instance for you, when the kernel is loaded, if it detects no running server given the configurations passed.

## The Full List of JSON Options

If you suspect the documentation might not be up to date, you can check the complete list of available options at this [link](https://github.com/MariaDB/mariadb_kernel/blob/master/mariadb_kernel/client_config.py#L14).

| Option                  | Default                                       | Explanation                                                                                                                                                                                                                                                                                                            |
| ----------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user                    | “root”                                        | Kernel passes `--user=root` to the MariaDB client                                                                                                                                                                                                                                                                      |
| host                    | “localhost”                                   | Kernel passes `--host=localhost` to the MariaDB client                                                                                                                                                                                                                                                                 |
| socket                  | "/tmp/mariadb\_kernel/mysqld.sock"            | If socket authentication is enabled in MariaDB, you can configure this option to tell the kernel that it can use socket authentication for connecting to the server. `--socket` is passed to the MariaDB client and if the server is started by the kernel, the kernel passes the option to the MariaDB server as well |
| port                    | “3306”                                        | Kernel passes `--port=3306` to the MariaDB client                                                                                                                                                                                                                                                                      |
| password                | “”                                            | Kernel passes `--password=”your_pass”` to the MariaDB client                                                                                                                                                                                                                                                           |
| server\_datadir         | "/tmp/mariadb\_kernel/datadir"                | Valid only if `start_server=True`. Tells the kernel the location of the datadir for the started server                                                                                                                                                                                                                 |
| server\_pid             | "/tmp/mariadb\_kernel/mysqld.pid"             | Valid only if `start_server=True`. Tells the kernel the location of the PID file for the started server                                                                                                                                                                                                                |
| start\_server           | “True”                                        | Start a server if no server running is detected for this config                                                                                                                                                                                                                                                        |
| client\_bin             | “mysql”                                       | The name or path for the MariaDB client binary                                                                                                                                                                                                                                                                         |
| server\_bin             | “mysqld”                                      | The name or path for the MariaDB server binary                                                                                                                                                                                                                                                                         |
| db\_init\_bin           | “mysql\_install\_db”                          | Valid only if `start_server=True`. The name or path for the `mysql_install_db` binary. The kernel uses this tool to set up the MariaDB Server instance that it starts for you                                                                                                                                          |
| extra\_server\_config   | \["--no-defaults", "--skip\_log\_error"]      | Valid only if `start_server=True`. Extra arguments to pass to the MariaDB Server instance that the kernel starts for you                                                                                                                                                                                               |
| extra\_db\_init\_config | \["--auth-root-authentication-method=normal"] | Valid only if `start_server=True`. Extra arguments to pass the `mysql_install_db` script when the kernel sets up the server                                                                                                                                                                                            |
| debug                   | "False"                                       | Enables debug logging which provides lots of internals information                                                                                                                                                                                                                                                     |
| code\_completion        | "True"                                        | Enables SQL autocompletion and code introspection                                                                                                                                                                                                                                                                      |


{% @marketo/form formId="4316" %}
