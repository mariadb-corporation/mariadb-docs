# sysbench v0.5 - Single Five Minute Runs on work

MariDB/MySQL sysbench benchmark comparison in %

Each test was run for 5 minutes.

```
Number of threads
                     1       4       8       16      32      64      128
 sysbench test
  delete            121.52  144.77  117.70  115.15  100.48   75.39   66.56
  insert            114.89  181.50  118.06  136.00  125.53  141.83  113.88
  oltp_complex_ro   103.13  100.99   94.65  104.14   97.87   90.18   79.93
  oltp_complex_rw   131.65  149.90  120.88  128.58  116.71   89.92   80.63
  oltp_simple       102.32  102.57   97.33   96.34   93.99   78.81   59.71
  select            102.12  102.05   96.64   97.28   93.55   81.53   59.83
  update_index      114.08  103.98  115.59  124.90  123.51  104.38   99.11
  update_non_index  134.04  147.94  150.91  150.04  152.12  108.34   89.24

insert/4 is a glitch

(MariaDB q/s / MySQL q/s * 100)
```

Benchmark was run on\
work: Linux openSUSE 11.1 (x86\_64), daul socket quad-core Intel 3.0GHz. with 6MB L2 cache, 8 GB RAM, data\_dir on single disk.

MariaDB and MySQL were compiled with

```
BUILD/compile-amd64-max
```

MariaDB revision was:

```
revno: 2821
committer: Sergei Golubchik <sergii@pisem.net>
branch nick: maria-5.1
timestamp: Tue 2010-02-23 13:04:58 +0100
message:
fix for a possible DoS in the my_net_skip_rest()
```

MySQL revision was:

```
revno: 2929
committer: Alexander Nozdrin <alik@sun.com>
branch nick: mysql-trunk
timestamp: Sat 2010-02-20 12:26:22 +0300
message:
Fix default.conf.
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

Configuration used for MariaDB and MySQL:

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
