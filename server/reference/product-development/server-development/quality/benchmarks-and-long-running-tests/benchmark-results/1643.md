# sysbench v0.5 - Single Five Minute Runs on T500 Laptop

MariDB/MySQL sysbench benchmark comparison in %

```
Number of threads
                     1       4       8       16      32      64      128
 sysbench test
  delete             92.42   82.60   88.05   89.85   94.68   98.75   97.77
  insert            100.70   99.90  103.21   89.51   85.16  105.39  108.51
  oltp_complex_ro   101.09  101.83  100.32  103.78  102.10  101.29  102.92
  oltp_complex_rw    95.04   90.22   91.84   88.78  100.98  101.96  101.60
  oltp_simple       100.29   99.90  101.69  102.22  102.61  102.18  101.49
  select            101.57  101.73  100.26  102.15  101.99  102.39  102.09
  update_index       96.01  103.06  105.89  108.35  108.13  104.36  101.61
  update_non_index   99.85  102.05  110.76  119.51  119.69  118.25  122.77

(MariaDB q/s / MySQL q/s * 100)
```

Run on Lenovo ThinkPad T500 with dual core 2.80GHz and 4GB RAM

MariaDB and MySQL were compiled with

```
BUILD/compile-amd64-max
```

MariaDB revision was:

```
revno: 2818 timestamp: Wed 2010-02-17 21:10:02 +0100
```

MySQL revision was:

```
revno: 3360 [merge] timestamp: Wed 2010-02-17 18:48:40 +0100
```

sysbench was run with these parameters:

```
--oltp-table-size=2000000 \
--max-time=300 \
--max-requests=0 \
--mysql-table-engine=InnoDB \
--mysql-user=root \
--mysql-engine-trx=yes
```

and this variable part of parameters

```
--num-threads=$THREADS --test=${TEST_DIR}/${SYSBENCH_TEST}
```

Configuration used for MariDB and MySQL:

```
--no-defaults \
--skip-grant-tables \
--language=./sql/share/english \
--datadir=$DATA_DIR \
--tmpdir=$TEMP_DIR \
--socket=$MY_SOCKET \
--table_open_cache=512 \
--thread_cache=512 \
--query_cache_size=0 \
--query_cache_type=0 \
--innodb_data_home_dir=$DATA_DIR \
--innodb_data_file_path=ibdata1:128M:autoextend \
--innodb_log_group_home_dir=$DATA_DIR \
--innodb_buffer_pool_size=1024M \
--innodb_additional_mem_pool_size=32M \
--innodb_log_file_size=256M \
--innodb_log_buffer_size=16M \
--innodb_flush_log_at_trx_commit=1 \
--innodb_lock_wait_timeout=50 \
--innodb_doublewrite=0 \
--innodb_flush_method=O_DIRECT \
--innodb_thread_concurrency=0 \
--innodb_max_dirty_pages_pct=80"
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
