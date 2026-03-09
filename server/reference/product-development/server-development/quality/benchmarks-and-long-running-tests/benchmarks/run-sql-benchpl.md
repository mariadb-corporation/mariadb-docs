# run-sql-bench.pl

`run-sql-bench.pl` is a perl script for automating runs of sql-bench\
(You can find sql-bench in the [MariaDB source code](../../../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).)

`run-sql-bench.pl` can be found in the [mariadb-tools](mariadb-tools.md) project on Launchpad. Once you have a copy of mariadb-tools,\
you'll find the script, and its configuration directories, in the `sql-bench` directory. For the purposes of this\
article, wherever you located your local branch of `mariadb-tools` will be called `${BASE_DIR}`.

The `run-sql-bench.pl` script is located at\
'`${BASE_DIR}/sql-bench/run-sql-bench.pl`'.

Example configuration scripts used for different runs can be found in the various subdirectories of `${BASE_DIR}/sql-bench/`.

To run the `run-sql-bench.pl` script, do the following:

1. [Branch a MariaDB or MySQL tree](../../../../../../clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md)
2. Optionally do some code changes in that tree and commit your changes
3. Edit `run-sql-bench.pl` to set internal options, especially the "`my $path`" variable.
4. Create a `${BASE_DIR}/sql-bench/conf/host.cnf` file for your system. An\
   easy way to do this is by duplicating one of the example `host.cnf` files:

```
cp -avi ${BASE_DIR}/sql-bench/conf/pitbull.cnf ${BASE_DIR}/sql-bench/conf/${HOSTNAME}.cnf
```

Edit the file to customize it for your system.

1. Create `${HOSTNAME}.cnf` files under the `${BASE_DIR}/sql-bench/basic`, `${BASE_DIR}/sql-bench/debug`, `${BASE_DIR}/sql-bench/debug-full`,\
   and `${BASE_DIR}/sql-bench/O2` directories, depending on which automated\
   tests you want to run. Use the example files as a base and customize them for\
   your system.
2. Run the `run-sql-bench.pl` script:

```
cd ${BASE_DIR}/sql-bench/; ./run-sql-bench.pl --repository=[/path/to/bzr/repository] --sql-bench-options=[additional sql-bench-options] --debug=[yes|no]
```

* `--repository` is the MariaDB tree to use and compile, the script will also look here for sql-bench.
* `--sql-bench-options` is mostly used in testing and debugging cases where\
  we want to have short run times. For instance, using `--small-test`\
  or `--small-table`.
* You can separate several sql-bench options with spaces like so:

```
--sql-bench-options="--small-test --small-table"
```

## The results

Results are stored at the location specified by the `$sql_bench_results` variable in the `${BASE_DIR}/sql-bench/conf/hostname.cnf` file for your host.\
Results are organized in sub directories with the following schema:

```
sql-bench-results-dir/${HOSTNAME}/YYYY-MM-DD
```

## Future plans

* Crash and error detection and reporting.
* One should be able to specify a test name for each file (`run-all-tests` `--suffix='_xxxx'`)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
