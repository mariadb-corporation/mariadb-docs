# Measuring cpimport Performance Baseline with ioping

The purpose of this guide is to detail the process for establishing a performance baseline for the `cpimport` bulk data loading utility and diagnosing storage subsystem bottlenecks using `ioping`. Storage design choices—such as local disk deployment versus High Availability Network File Systems (NFS HA)—profoundly impact chunk ingestion execution times.

The reference benchmarks documented here were established on a system containing AWS 4vCPUs and 16GB of RAM.

## Baseline Performance Reference Metrics

The following matrix reflects baseline loading rates recorded for a standard testing profile consisting of 10,000 records with 250 columns across varying disk architectures:

| Infrastructure Layout                               | Ingestion Runtime             | Observed Storage Latency (ioping)                                                                                                                                                                                                      |
| --------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No NFS (Local Storage)                              | <p>5 to 6 seconds </p><p></p> | `data1`: 450 µs \| `data2`: 475 µs \| `data3`: 430 µs                                                                                                                                                                                  |
| With NFS HA                                         | 29 to 32 seconds              | `data1`: 3.7 ms \| `data2`: 3.1 ms \| `data3`: 3.1 ms                                                                                                                                                                                  |
| With NFS HA & Low Latency Storage at `bulkrollback` | 14 to 15 seconds              | <p><code>data1</code>: 3.3 ms (<code>bulkRollback</code>: 590 µs)</p><p><br></p><p><code>data2</code>: 3.2 ms (<code>bulkRollback</code>: 560 µs)</p><p><br></p><p><code>data3</code>: 3.8 ms (<code>bulkRollback</code>: 490 µs) </p> |

## Manual Benchmarking Procedure

To run a manual performance check and track read latencies across your column store directories, execute the following steps in sequence:

1.  Create the ColumnStore testing table: Initialize a test table (`cptest`) matching the 250-column layout using the `COLUMNSTORE` storage engine:

    ```sql
    CREATE TABLE cptest (
      group_name CHAR(2),
      number1 DECIMAL(12, 2),
      -- [Truncated for brevity; insert columns up to col250]
      col250 varchar(250)
    ) ENGINE=COLUMNSTORE;
    ```
2.  Generate data and populate the table: Seed the table with 10,000 randomized evaluation rows using the system sequence loop engine:

    ```sql
    INSERT INTO cptest
    SELECT 
      CAST(ROUND(RAND() * 10, 0) AS CHAR),
      ROUND(RAND() * 10000, 2),
      -- [Truncated for brevity; complete selections to match your column layout]
      substring(MD5(RAND()),1,2)
    FROM seq_1_to_10000;
    ```
3.  Export data to a local CSV file: Dump the resulting ColumnStore table fields out to a temporary flat comma-separated file:

    ```sql
    SELECT * FROM cptest INTO OUTFILE '/tmp/cptest.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';
    ```
4.  Benchmark the `cpimport` execution rate: Execute the ingestion tool directly to capture baseline loading speeds:

    ```bash
    cpimport -E '"' -s "," test cptest /tmp/cptest.csv
    ```
5.  Measure disk sub-system latency using `ioping`: Install the latency verification tool and run a sequence of 30 tests directly on your active database storage directories to analyze performance consistency:

    ```bash
    sudo yum install ioping
    cd /var/lib/columnstore/dataX/
    ioping -c 30 .
    ```

### Evaluating `ioping` Output Summary

When the test completes, evaluate the statistical summary metrics:

```
--- . (xfs /dev/xvda1) ioping statistics ---
29 requests completed in 15.1 ms, 116 KiB read, 1.92 k iops, 7.51 MiB/s
generated 30 requests in 29.0 s, 120 KiB, 1 iops, 4.14 KiB/s
min/avg/max/mdev = 407.4 us / 520.4 us / 694.0 us / 64.8 us
```

* Target Guideline: For consistent and dependable storage throughput, target a low AVG execution result under 700 µs, combined with a low standard deviation (`mdev`).

## Automated Scripted Performance Testing

You can automate this benchmarking process by saving the comprehensive verification logic into an administrative script named `cpimportBench.bash`.

### Script Implementation

```bash
#!/bin/bash
##################
# Purpose: Test cpimport using a 250 column test & ioping test
# Example: bash cpimportBench.bash root test
##################

USER=root
DATABASE=test
RECORDS=10000
TABLE=cptest
CSVPATH="/tmp/$TABLE.csv"
ITERATIONS=20

if [ ! -z "$1" ]; then USER=$1; fi
if [ ! -z "$2" ]; then DATABASE=$2; fi
if [ ! -z "$3" ]; then ITERATIONS=$3; fi

echo "Variable Summary"
echo "User: $USER"
echo "Database: $DATABASE"
echo "Table: $TABLE"
echo "CSV Path: $CSVPATH"
echo "Iterations: $ITERATIONS"

# Check daemon requirements
if [ -z $(pidof mariadbd) ]; then
    printf "[X] MariaDB is offline\n\n"
    exit 1
fi
if [ -z $(pidof PrimProc) ]; then
    printf "[X] Columnstore is offline\n\n"
    exit 1
fi

# Ensure dependency is present
if ! command -v ioping >/dev/null ; then
    yum install ioping
    printf "\n\n[X] Rerun the script now that ioping is installed\n\n"
    exit 1
fi

# Create database if not exists
if [ -z $(mariadb -s -e "SHOW DATABASES LIKE '%$DATABASE%'") ]; then
    echo "[+] Creating Database: $DATABASE ..."
    mariadb -e "CREATE DATABASE $DATABASE"
else
    echo "[*] Database Exists"
fi

# [Table Generation, Row Verification, and CSV Export Logic goes here based on Manual Steps 1-3]

printf "[~] Beginning Import Test\n"
i=0
results=()

while [ $i -le $ITERATIONS ]; do
    printf "\n\nStarting Iteration ${i}\n"
    start=`date +%s.%N`
    cpimport -E '"' -s "," $DATABASE $TABLE $CSVPATH
    end=`date +%s.%N`
    results+=($( echo "$end - $start" | bc -l )) 
    ((i++))
done

# Perform automated ioping test
if ! command -v ioping; then
    printf "\n\n[X] Please make sure ioping is installed and executable\n\n"
    exit 1
else
    printf "\n\n Checking Latency of Data1 DBroot \n\n"
    ioping -c 30 /var/lib/columnstore/data1
fi

printf "\n\nCpimport Summary Timings\n"
for t in "${results[@]}"; do
    echo $t
done
```
