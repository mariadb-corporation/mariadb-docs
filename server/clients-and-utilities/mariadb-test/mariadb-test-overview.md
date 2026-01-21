# mariadb-test Overview

## The Basics

At its core, mariadb-test is very simple. The client program `mariadb-test`\
executes a _test file_ and compares the produced output with the _result_\
&#xNAN;_file_. If the files match, the test is passed; otherwise the test has failed.\
This approach can be used to test any SQL statement, as well as other\
executables (with the `exec` command).

The complete process of testing is governed and monitored by\
the _mariadb-test-run.pl_ driver script, or _mtr_ for short (for convenience,`mtr` is created as a symbolic link to `mariadb-test-run.pl`). The mtr script\
is responsible for preparing the test environment, creating a list of all tests\
to run, running them, and producing the report at the end. It can run many\
tests in parallel, execute tests in an order which minimizes server restarts\
(as they are slow), run tests in a debugger or under valgrind or strace, and so\
on.

Test files are located in _suites_. A _suite_ is a directory which contains\
test files, result files, and optional configuration files. The mtr looks for\
suites in the `mariadb-test/suite` directory, and in the `mariadb-test`\
subdirectories of plugins and storage engine directories. For example, the\
following are all valid suite paths:

```
mariadb-test/suite/rpl
```

```
mariadb-test/suite/handler
```

```
storage/example/mariadb-test/demo
```

```
plugin/auth_pam/mariadb-test/pam
```

In almost all cases, the suite directory name is the suite name. A notable\
historical exception is the _main_ suite, which is located directly in the`mariadb-test` directory.

Test files have a `.test` extension and can be placed directly in the suite\
directory (for example, `mariadb-test/suite/handler/interface.test`) or in the`t` subdirectory (e.g. `mariadb-test/suite/rpl/t/rpl_alter.test` or`mariadb-test/t/grant.test`). Similarly, result files have the `.result`\
extension and can be placed either in the suite directory or in the `r`\
subdirectory.

A test file can include other files (with the `source` command). These\
included files can have any name and may be placed anywhere, but customarily\
they have a `.inc` extension and are located either in the suite directory or\
in the `inc` or `include` subdirectories (for example,`mariadb-test/suite/handler/init.inc` or`mariadb-test/include/start_slave.inc`).

Other files which affect testing, while not being tests themselves, are:

* `disabled.def`
* `suite.opt`
* other `*.opt` files
* `my.cnf`
* other `*.cnf` files
* `combinations`
* other `*.combinations` files
* `suite.pm`
* `*.sh` files
* `*.require` files
* `*.rdiff` files
* `valgrind.supp`

See [Auxiliary files](mariadb-test-auxiliary-files.md) for details on these.

## Overlays

In addition to regular suite directories, mtr supports _overlays_.\
An _overlay_ is a directory with the same name as an existing suite, but\
which is located in a storage engine or plugin directory. For example,`storage/myisam/mariadb-test/rpl` could be a _myisam_ overlay of the _rpl_\
suite in `mariadb-test/suite/rpl`. And`plugin/daemon_example/mariadb-test/demo` could be a _daemon\_example_ overlay\
of the _demo_ suite in `storage/example/mariadb-test/demo`. As a special\
exception, an overlay of the main suite, should be called `main`, as in`storage/pbxt/mariadb-test/main`.

An overlay is like a second transparent layer in a graphics editor. It can\
obscure, extend, or modify the background image. Also, one may notice that an\
overlay is very close to a _UnionFS_, but implemented in perl inside mtr.

An overlay can replace almost any file in the overlaid suite, or add new files.\
For example, if some overlay of the main suite contains a`include/have_innodb.inc` file, then all tests that include it will see and\
use the overlaid version. Or, an overlay can create a `t/create.opt` file\
(even though the main suite does not have such a file), and `create.test`\
is executed with the specified additional options.

But adding an overlay never affects how the original suite is executed. That\
is, mtr always executes the original suite as if no overlay was present. And\
then, additionally, it executes a combined "union" of the overlay and the\
original suite. When doing that, mtr takes care to avoid re-executing tests\
that are not changed in the overlay. For example, creating `t/create.opt` in\
the overlay of the main suite will only cause `create.test` to be executed in\
the overlay. But creating `suite.opt` affects all tests\
— and it will cause all tests to be re-executed with\
the new options.

## Combinations

In certain cases it makes sense to run a specific test or a group of tests\
several times with different server settings. This can be done using\
so-called _combinations_. Combinations are groups of settings that are used\
alternatively. A combinations file defines these alternatives using `my.cnf`\
syntax, for example

```
[row]
binlog-format=row

[stmt]
binlog-format=statement

[mix]
binlog-format=mixed
```

And all tests where this combinations file applies is run three times:\
once for the combination called "row", and `--binlog-format=row` on the\
server command line, once for the "stmt" combination, and once for the "mix"\
combination.

More than one combinations file may be applicable to a given test file. In this\
case, mtr will run the test for all possible combinations of the given\
combinations. A test that uses replication (three combinations as above) and\
innodb (two combinations - innodb and xtradb), is run six times.

## Sample Output

Typical mtr output looks like this

```
==============================================================================
TEST                                  WORKER RESULT   TIME (ms) or COMMENT
--------------------------------------------------------------------------
rpl.rpl_row_find_row_debug                [ skipped ]  Requires debug build
main-pbxt.connect                         [ skipped ]  No PBXT engine
main-pbxt.mysqlbinlog_row                 [ disabled ]  test expects a non-transactional engine
rpl.rpl_savepoint 'mix,xtradb'            w2 [ pass ]    238
rpl.rpl_stm_innodb 'innodb_plugin,row'    w1 [ skipped ]  Neither MIXED nor STATEMENT binlog format
binlog.binlog_sf 'stmt'                   w2 [ pass ]      7
unit.dbug                                 w2 [ pass ]      1
maria.small_blocksize                     w1 [ pass ]     23
sys_vars.autocommit_func3 'innodb_plugin' w1 [ pass ]      5
sys_vars.autocommit_func3 'xtradb'        w1 [ pass ]      6
main.ipv6                                 w1 [ pass ]    131
...
```

Every test is printed as "suitename.testname", and a suite name may include an\
overlay name (like in `main-pbxt`). After the test name, mtr prints\
combinations that were applied to this test, if any.

A similar syntax can be used on the mtr command line to specify what tests to\
run:

| $ ./mtr innodb                  | $ ./mtr main.innodb                                                                                           | $ ./mtr main-pbxt.innodb | $ ./mtr main-.innodb | $ ./mtr main.innodb,xtradb | $ ./mtr --suite=rpl | $ ./mtr --suite=mroonga/storage |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------ | -------------------- | -------------------------- | ------------------- | ------------------------------- |
| $ ./mtr innodb                  | search for innodb test in every suite from the default list, and run all that was found.                      |                          |                      |                            |                     |                                 |
| $ ./mtr main.innodb             | run the innodb test from the main suite                                                                       |                          |                      |                            |                     |                                 |
| $ ./mtr main-pbxt.innodb        | run the innodb test from the pbxt overlay of the main suite                                                   |                          |                      |                            |                     |                                 |
| $ ./mtr main-.innodb            | run the innodb test from the main suite and all its overlays.                                                 |                          |                      |                            |                     |                                 |
| $ ./mtr main.innodb,xtradb      | run the innodb test from the main suite, only in the xtradb combination                                       |                          |                      |                            |                     |                                 |
| $ ./mtr --suite=rpl             | Run all test in the rpl suite (found in the suite/rpl directory)                                              |                          |                      |                            |                     |                                 |
| $ ./mtr --suite=mroonga/storage | Run all test in the mroonga/wrapper suite (found in the storage/mroonga/mysql-test/mroonga/storage directory) |                          |                      |                            |                     |                                 |

## Plugin Support

The mtr driver has special support for MariaDB plugins.

First, on startup it copies or symlinks all dynamically-built plugins into`var/plugins`. This allows one to have many plugins loaded at the same time.\
For example, one can load Federated and InnoDB engines together. Also, mtr\
creates environment variables for every plugin with the corresponding plugin\
name. For example, if the InnoDB engine was built, `$HA_INNODB_SO` is\
set to `ha_innodb.so` (or `ha_innodb.dll` on Windows). And the test can\
safely use the corresponding environment variable on all platforms to refer to\
a plugin file; it will always have the correct platform-dependent extension.

Second, when combining server command line options (which may come from many\
different sources) into one long list before starting `mariadbd`, mtr treats`--plugin-load` specially. Normal server semantics is to use the latest value\
of any particular option on the command line. If one starts the server with,\
for example, `--port=2000 --port=3000`, the server will use the last value\
for the port, that is 3000. To allow different `.opt` files to require\
different plugins, mtr goes through the assembled server command line, and\
joins all `--plugin-load` options into one. Additionally it removes all empty`--plugin-load` options. For example, suppose a test is affected by three`.opt` files which contain, respectively:

```
--plugin-load=$HA_INNODB_SO
```

```
--plugin-load=$AUTH_PAM_SO
```

```
--plugin-load=$HA_EXAMPLE_SO
```

...and, let's assume the Example engine was not built (`$HA_EXAMPLE_SO` is\
empty). Then the server will get:

```
--plugin-load=ha_innodb.so:auth_pam.so
```

instead of

```
--plugin-load=ha_innodb.so --plugin-load=auth_pam.so --plugin-load=
```

Third, to allow plugin sources to be simply copied into the `plugin/` or`storage/` directories, and still not affect existing tests (even if new\
plugins are statically linked into the server), mtr automatically disables all\
optional plugins on server startup. A plugin is optional if it can be disabled\
with the corresponding `--skip-XXX` server command line option. Mandatory\
plugins, like MyISAM or MEMORY, do not have `--skip-XXX` options (e.g. there\
is no `--skip-myisam` option). This mtr behavior means that no plugin,\
statically or dynamically built, has any effect on the server unless it was\
explicitly enabled. A convenient way to enable a given plugin _XXX_ for\
specific tests is to create a `have_XXX.opt` file which contains the\
necessary command line options, and a `have_XXX.inc` file which checks\
whether a plugin was loaded. Then any test that needs this plugin can source\
the `have_XXX.inc` file and have the plugin loaded automatically.

## mtr communication procedure

`mtr` is first creating the server socket (`master`).

After that, `workers` are created using `fork()`.

For each worker `run_worker()` function is called, which is executing the following:

* creates a new socket to connect to `server_port` obtained from the `master`
* initiate communication with the `master` using `START` command
* `master` sends first test from list of tests supplied by the user and immediately sends command `TESTCASE` to the `worker`
* `worker` gets command `TESTCASE` and processes test case, by calling `run_testcase()` function which starts(/restarts if needed) the server and sends `TESTRESULT` (in case of restart `WARNINGS` command is issued to the `master` in case some warnings/error logs are found)
* `master` accepts `TESTRESULT` command and run `mtr_report_test()` function which check does the test fail and also generates the new command `TESTCASE` if some new test case exist
* If there is no other test case `master` sends `BYE` command which gets accepted by the `worker` which is properly closing the connection.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
