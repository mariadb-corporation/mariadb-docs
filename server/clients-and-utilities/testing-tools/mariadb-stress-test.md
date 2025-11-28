# mariadb-stress-test

`mariadb-stress-test` is a symlink to `mysql-stress-test`, the script for assisting with adding users or databases or changing passwords in MariaDB.

{% tabs %}
{% tab title="Current" %}
 `mysql-stress-test` is the symlink, and `mariadb-stress-test` the binary name.
{% endtab %}

{% tab title="< 10.5.2" %}
 `mysql-stress-test` is the binary name.
{% endtab %}
{% endtabs %}

_mariadb-stress-test.pl_ is a Perl script that performs stress-testing of the MariaDB server. It requires a version of Perl that has been built with threads support.

### Syntax

```bash
mariadb-stress-test.pl [options]
```

### Options

| Option                            | Description                                                                                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| --help                            | Display a help message and exit.                                                                                                                                                                                                                                                                                         |
| --abort-on-error=N                | Causes the program to abort if an error with severity less than or equal to N was encountered. Set to 1 to abort on any error.                                                                                                                                                                                           |
| --check-tests-file                | Periodically check the file that lists the tests to be run. If it has been modified, reread the file. This can be useful if you update the list of tests to be run during a stress test.                                                                                                                                 |
| --cleanup                         | Force cleanup of the working directory.                                                                                                                                                                                                                                                                                  |
| --log-error-details               | Log error details in the global error log file.                                                                                                                                                                                                                                                                          |
| --loop-count=N                    | In sequential test mode, the number of loops to execute before exiting.                                                                                                                                                                                                                                                  |
| --mysqltest=path                  | The path name to the mysqltest program.                                                                                                                                                                                                                                                                                  |
| --server-database=db\_name        | The database to use for the tests. The default is test.                                                                                                                                                                                                                                                                  |
| --server-host=host\_name          | he host name of the local host to use for making a TCP/IP connection to the local server. By default, the connection is made to localhost using a Unix socket file.                                                                                                                                                      |
| --server-logs-dir=path            | This option is required. path is the directory where all client session logs is stored. Usually this is the shared directory that is associated with the server used for testing.                                                                                                                                   |
| --server-password=password        | The password to use when connecting to the server.                                                                                                                                                                                                                                                                       |
| --server-port=port\_num           | The TCP/IP port number to use for connecting to the server. The default is 3306.                                                                                                                                                                                                                                         |
| --server-socket=file\_name        | For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. The default is /tmp/mysql.sock.                                                                                                                                                                            |
| --server-user=user\_name          | The MariaDB user name to use when connecting to the server. The default is root.                                                                                                                                                                                                                                         |
| --sleep-time=N                    | The delay in seconds between test executions.                                                                                                                                                                                                                                                                            |
| --stress-basedir=path             | This option is required and specified the path is the working directory for the test run. It is used as the temporary location for result tracking during testing.                                                                                                                                                       |
| --stress-datadir=path             | The directory of data files to be used during testing. The default location is the data directory under the location given by the --stress-suite-basedir option.                                                                                                                                                         |
| --stress-init-file\[=path]        | file\_name is the location of the file that contains the list of tests to be run once to initialize the database for the testing. If missing, the default file is stress\_init.txt in the test suite directory.                                                                                                          |
| --stress-mode=mode                | This option indicates the test order in stress-test mode. The mode value is either random to select tests in random order or seq to run tests in each thread in the order specified in the test list file. The default mode is random.                                                                                   |
| --stress-suite-basedir=path       | This option is required and specifies the directory that has the t and r subdirectories containing the test case and result files. This directory is also the default location of the stress-test.txt file that contains the list of tests. (A different location can be specified with the --stress-tests-file option.) |
| --stress-tests-file\[=file\_name] | Use this option to run the stress tests. file\_name is the location of the file that contains the list of tests. If omitted, the default file is stress-test.txt in the stress suite directory. (See --stress-suite-basedir.)                                                                                            |
| --suite=suite\_name               | Run the named test suite. The default name is main (the regular test suite located in the mysql-test directory).                                                                                                                                                                                                         |
| --test-count=N                    | The number of tests to execute before exiting.                                                                                                                                                                                                                                                                           |
| --test-duration=N                 | The duration of stress testing in seconds.                                                                                                                                                                                                                                                                               |
| --threads=N                       | The number of threads. The default is 1.                                                                                                                                                                                                                                                                                 |
| --verbose                         | Verbose mode. Print more information about what the program does                                                                                                                                                                                                                                                         |

CC BY-SA / Gnu FDL

{% @marketo/form formId="4316" %}
