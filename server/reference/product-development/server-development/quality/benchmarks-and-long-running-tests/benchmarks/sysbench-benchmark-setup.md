# sysbench Benchmark Setup

For our automated MariaDB/MySQL sysbench benchmark tests, we use sysbench from`lp:sysbench`. This page describes the basic parameters and configuration we\
use.

You can find the automation wrapper scripts we use for running sysbench in [lp:mariadb-tools](mariadb-tools.md)

## Current general parameters

```
table_open_cache = 512
thread_cache = 512
query_cache_size = 0
query_cache_type = 0
```

## Current InnoDB parameters

```
innodb_data_home_dir = /data/mysql/
innodb_data_file_path = ibdata1:128M:autoextend
innodb_log_group_home_dir = /data/mysql/
innodb_buffer_pool_size = 1024M
innodb_additional_mem_pool_size = 32M
innodb_log_file_size = 256M
innodb_log_buffer_size = 16M
innodb_flush_log_at_trx_commit = 1
innodb_lock_wait_timeout = 50
innodb_doublewrite = 0
innodb_flush_method = O_DIRECT
innodb_thread_concurrency = 0
innodb_max_dirty_pages_pct = 80
```

## Compile

Install MariaDB or MySQL to /usr/local and make a symlink to /usr/local/mysql.\
Please use non-debug version! On Mac OS X we currently need automake1.10.

```
./autogen.sh
./configure \
  --without-drizzle \
  --with-mysql-includes=/usr/local/mysql/include/mysql \
  --with-mysql-libs=/usr/local/mysql/lib/mysql
make
optionally: make install
```

## Start and prepare database to use

```
mysqladmin -uroot drop sbtest
mysqladmin -uroot create sbtest
```

### Tests

We use the latest sysbench with Lua scripting support. Therefore the test names\
differ from sysbench <= 0.4. To get reasonable results we use a run time of 5\
minutes.

We run the tests with 1, 4, 8, 16, 32, 64, and 128 threads.

```
NUM_THREADS="1 4 8 16 32 64 128"
SYSBENCH_TESTS="delete.lua \
  insert.lua \
  oltp_complex_ro.lua \
  oltp_complex_rw.lua \
  oltp_simple.lua \
  select.lua \
  update_index.lua \
  update_non_index.lua"

NUM_THREADS=1
TEST_DIR=${HOME}/work/monty_program/sysbench/sysbench/tests/db

./sysbench \
  --test=${TEST_DIR}/oltp_simple.lua \
  --oltp-table-size=2000000 \
  --max-time=300 \
  --max-requests=0 \
  --mysql-table-engine=InnoDB \
  --mysql-user=root \
  --mysql-engine-trx=yes \
  --num-threads=$NUM_THREADS \
  prepare

./sysbench \
  --test=${TEST_DIR}/oltp_simple.lua \
  --oltp-table-size=2000000 \
  --max-time=300 \
  --max-requests=0 \
  --mysql-table-engine=InnoDB \
  --mysql-user=root \
  --mysql-engine-trx=yes \
  --num-threads=$NUM_THREADS \
  run
```

## Custom added tests

We created a couple of custom tests for SysBench:

* select\_random\_ranges.lua
* select\_random\_points.lua

Both of these have been added to the latest SysBench v0.5 repository.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
