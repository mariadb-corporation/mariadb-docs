---
description: >-
  Example of benchmarking the MEMORY table using perl to generate the data and
  SQL for the benchmark
---

# Performance of MEMORY Tables

Between MariaDB 5.5.21 and 5.5.22 some work was done on how the hash index for a [MEMORY](../../../../../../server-usage/storage-engines/memory-storage-engine.md) table is created. This results in better performance when inserting rows into a memory table.

The following benchmark compares MariaDB 5.5.21 and 5.5.25. Compiled with identical settings on the same machine. The operation was loading 50 million rows into a `MEMORY` table with [LOAD DATA INFILE](../../../../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

Two different tables were tested: one with an indexed [INT](../../../../../data-types/numeric-data-types/int.md) column and one with an indexed [CHAR(20)](../../../../../data-types/string-data-types/char.md) column. The data files were pre-generated and located on a SSD. In order to make the effect visible, the cpu speed was set to minimum (core I5 @ 800Mhz)

#### Result:

| Table Type | MariaDB Version | rows per second | Percent |
| ---------- | --------------- | --------------- | ------- |
| INT        | 5.5.21          | 411022          | 100%    |
|            | 5.5.25          | 510016          | 124%    |
| CHAR(20)   | 5.5.21          | 259399          | 100%    |
|            | 5.5.25          | 411535          | 159%    |

This is how the benchmark was run:

```sql
MariaDB [test]> tee 5.5.21.txt
MariaDB [test]> set @instance="5.5.21";
MariaDB [test]> source bench.sql
```

The script used to generate the data files:

```perl
#!/usr/bin/perl -w                                                              
                                                                                
$ROWS=50*1024*1024;                                                             

open F, ">/tmp/hash1.txt" or die;                                               
for ($i=0; $i<$ROWS; $i++) {                                                    
    printf F "%d\n", int(rand($ROWS));                                          
}                                                                               
close F or die;                                                                 
                                                                                
open F, ">/tmp/hash2.txt" or die;                                               
for ($i=0; $i<$ROWS; $i++) {                                                    
    $s="";                                                                      
    for (1..20) { $s .= chr(ord('a')+int(rand(26))); }                          
    print F $s, "\n";                                                           
}                                                                               
close F or die;
```

The benchmark SQL script `bench.sql`:

```sql
use test;                                                                       
                                                                                
-- need big heap tables                                                         
set max_heap_table_size=4*1024*1024*1024;                                       
                                                                                
-- table to hold test results                                                   
create table if not exists results (                                            
  id serial,                                                                    
  operation char(32),                                                           
  opsize bigint unsigned,                                                       
  started datetime,                                                             
  ended datetime,                                                               
  instance char(20)                                                             
);                                                                              
                                                                                
-- dummy run with second data file                                              
drop table if exists t1;                                                        
create table t1 (c1 char(20), index (c1)) engine memory;                        
load data infile "/tmp/hash2.txt" into table t1;                                
drop table t1;                                                                  
                                                                                
-- do total of 5 runs for each table                                            
                                                                                
-- run #1                                                                       
create table t1 (c1 int, index (c1)) engine memory;                             
select @t1:=now();                                                              
load data infile "/tmp/hash1.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into INT table", @rows, @t1, @t2, @instance);                     
drop table t1;                                                                  
                                                                                
create table t1 (c1 char(20), index (c1)) engine memory;                        
select @t1:=now();                                                              
load data infile "/tmp/hash2.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into CHAR(20) table", @rows, @t1, @t2, @instance);                
drop table t1;                                                                  
                                                                                
-- run #2                                                                       
create table t1 (c1 int, index (c1)) engine memory;                             
select @t1:=now();                                                              
load data infile "/tmp/hash1.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into INT table", @rows, @t1, @t2, @instance);                     
drop table t1;                                                                  
                                                                                
create table t1 (c1 char(20), index (c1)) engine memory;                        
select @t1:=now();                                                              
load data infile "/tmp/hash2.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into CHAR(20) table", @rows, @t1, @t2, @instance);                
drop table t1;                                                                  
                                                                                
-- run #3                                                                       
create table t1 (c1 int, index (c1)) engine memory;                             
select @t1:=now();                                                              
load data infile "/tmp/hash1.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into INT table", @rows, @t1, @t2, @instance);                     
drop table t1;                                                                  
                                                                                
create table t1 (c1 char(20), index (c1)) engine memory;                        
select @t1:=now();                                                              
load data infile "/tmp/hash2.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into CHAR(20) table", @rows, @t1, @t2, @instance);                
drop table t1;                                                                  
                                                                                
-- run #4                                                                       
create table t1 (c1 int, index (c1)) engine memory;                             
select @t1:=now();                                                              
load data infile "/tmp/hash1.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into INT table", @rows, @t1, @t2, @instance);                     
drop table t1;                                                                  
                                                                                
create table t1 (c1 char(20), index (c1)) engine memory;                        
select @t1:=now();                                                              
load data infile "/tmp/hash2.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into CHAR(20) table", @rows, @t1, @t2, @instance);                
drop table t1;                                                                  
                                                                                
-- run #5                                                                       
create table t1 (c1 int, index (c1)) engine memory;                             
select @t1:=now();                                                              
load data infile "/tmp/hash1.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into INT table", @rows, @t1, @t2, @instance);                     
show table status like 't1';                                                    
drop table t1;                                                                  
                                                                                
create table t1 (c1 char(20), index (c1)) engine memory;                        
select @t1:=now();                                                              
load data infile "/tmp/hash2.txt" into table t1;                                
select @t2:=now();                                                              
select @rows:=count(*) from t1;                                                 
insert into results (operation, opsize, started, ended, instance)               
values ("load into CHAR(20) table", @rows, @t1, @t2, @instance);                
show table status like 't1';                                                    
drop table t1;                                                                  

-- list all results                                                             
select operation, instance, unix_timestamp(ended)-unix_timestamp(started) as duration,                                                                          
 opsize/(unix_timestamp(ended)-unix_timestamp(started)) as ops_per_sec          
from results order by operation, instance, started;                             
                                                                                
-- list average results                                                         
select operation, instance, avg(opsize/(unix_timestamp(ended)-unix_timestamp(started))) as avg_ops_per_sec                                                      
from results group by operation, instance;                                      
```

{% include "../../../../../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}

{% @marketo/form formId="4316" %}
