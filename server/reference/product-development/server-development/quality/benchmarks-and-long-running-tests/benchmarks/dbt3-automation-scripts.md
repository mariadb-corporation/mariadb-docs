# DBT3 Automation Scripts

DBT-3 (OSDL Database Test 3) is a workload tool for the Linux kernel that OSDL\
(Open Source Development Labs, inc) developed based on TPC-H which is provided\
by the Transaction Performance Processing Council (TPC).

DBT-3, like TPC-H, simulates an actual decision-making support system and\
models complex business analysis applications that perform data processing jobs\
for making better business decisions. By running the workload that DBT-3\
simulates, it is possible to verify and measure the performances of the Linux\
kernel in an actual decision-making support system.

DBT-3 uses the "scale factor (SF)" as a stress indicator of the system. By\
varying the SF, it becomes possible to make the size of a database the SF times\
its size.

The tests performed by DBT-3 comprise the three tests listed below. DBT-3\
obtains the execution times of these three tests as well as the system status\
information and database statistics information.

1. Load test

* Enters the data to be used for the Power and Throughput tests into the\
  database. Makes a bulk insert of the huge CSV data corresponding to the\
  scale factor into the database.

1. Power test

* Performs 22 complex queries.

1. Throughput test

* Performs the same 22 queries as in the Power test simultaneously in more\
  than one process.

For the purpose of this task, only the Power test is performed over preliminary\
prepared database with various Scale factors. The time for each query execution\
will be measured and stored into a database. Later the results of one whole\
test with all 22 queries will be rendered into a histogram graphics comparing\
it to different configurations.

## Benchmark environment preparation

### sudo rights

The user that will run the benchmark must have sudo rights on the machine.

For clearing the system caches between query runs, the automation script uses\
the following command:

```
sudo /sbin/sysctl vm.drop_caches=3
```

This command must be run with superuser rights. Even if a user supplies a\
password to sudo, this password expires after some timeout. In order for this\
command to be run without requiring password, the following line should be\
added to the sudoers file (edit it with the `"sudo visudo"` command):

```
'your_username' ALL=NOPASSWD:/sbin/sysctl
```

...where `'your_username'` is the user that will run the benchmark.

### Required software

The automated DBT3 benchmark requires the following software:

* [Perl](https://www.perl.org/)
  * Project home:
* [mariadb-tools](https://launchpad.net/mariadb-tools)
  * Project home: [mariadb-tools](https://launchpad.net/mariadb-tools)
  * The project folder is called "`dbt3_benchmark`" and is under `mariadb-tools`.
* [dbt3-1.9](https://sourceforge.net/projects/osdldbt/files/dbt3/)
  * Download location:
* [Gnuplot 4.4](https://www.gnuplot.info/) — graphics output program.
  * Project home:
* [Config::Auto](https://search.cpan.org/~simon/Config-Auto-0.03/Auto.pm) —\
  a Perl module that reads configuration files. To install it use the following\
  command:

```
sudo cpan Config::Auto
```

* [DBD::mysql](https://search.cpan.org/~capttofu/DBD-mysql-4.020/lib/DBD/mysql.pm) —\
  a Perl module to connect to MariaDB/MySQL and PostgreSQL. To install it use\
  the following command:

```
sudo cpan DBD::mysql
```

**NOTE:** You may receive an error saying that CPAN could not find`mysql_config`. In this case you have to install the mysql client development\
library. In OpenSuse the command is:

```
sudo zypper install libmysqlclient-devel
```

Alternatively this module can be installed manually by following these steps:

1. Download DBD-mysql-4.020.tar.gz from [mysql.pm](https://search.cpan.org/~capttofu/DBD-mysql-4.020/lib/DBD/mysql.pm) and unpack it
2. Run the perl script PerlMake.pl under the unzipped dir:

```
perl Makefile.PL --mysql_config=/path/to/some/mysql_binary_distribution/bin/mysql_config
```

1. Run `make` to compile `DBD::mysql`:

```
make
```

1. Add the necessary paths in order to run `DBD::mysql`:

```
export PERL5LIB="/path/to/unzipped_DBD_mysql/DBD-mysql-4.020/lib"
export LD_LIBRARY_PATH="/path/to/unzipped_DBD_mysql/DBD-mysql-4.020/blib/arch/auto/DBD/mysql/:/path/to/some/mysql_binary_distribution/lib/"
```

### Tested DBMS

* [MySQL 5.5.x](https://dev.mysql.com/downloads/mysql/#downloads)
  * Download location: [#downloads](https://dev.mysql.com/downloads/mysql/#downloads) →\
    Generally Available (GA) Releases → Linux - Generic 2.6 (x86, 64-bit),\
    Compressed TAR Archive - downloads mysql-5.5.x-linux2.6-x86\_64.tar.gz -\
    gzipped tar file for Linux x86
* [MySQL 5.6.x](https://dev.mysql.com/downloads/mysql/#downloads)
  * Download location: [#downloads](https://dev.mysql.com/downloads/mysql/#downloads) →\
    Development Releases → Linux - Generic 2.6 (x86, 64-bit), Compressed TAR\
    Archive - downloads mysql-5.6.x-m5-linux2.6-x86\_64.tar.gz - gzipped tar file\
    for Linux x86
* [MariaDB 5.3.x](https://launchpad.net/maria/5.3)
  * Download location: [5.3](https://launchpad.net/maria/5.3) , downloaded with Bazaar:

```
bzr branch lp:maria/5.3
```

* [MariaDB 5.5.x](https://launchpad.net/maria/5.3)
  * Download location: [5.5](https://launchpad.net/maria/5.5) , downloaded with Bazaar:

```
bzr branch lp:maria/5.5
```

* [PostgreSQL](https://www.postgresql.org/ftp/source/v9.1rc1/)
  * Download location:

**NOTE:** The DBT3 benchmark requires a lot of disk space (for example MySQL\
5.5.x + MyISAM database with scale factor 30 takes about 50 GB). Also some\
queries require the utilization of temp tables under the directory set by the`--tmpdir` startup parameter passed to `mysqld`. In the\
prepared configuration files the temp directory is pointed to the `mysql`\
system directory of the binary distribution, but one should reassure that there\
is enough free space available for the temp directory.

## Installation instructions

**NOTE:** The directory where all the files will be downloaded or installed\
will be referred as `$PROJECT_HOME`. This could be for example `~/benchmark/dbt3`.

### Download [mariadb-tools](https://launchpad.net/mariadb-tools)

1. Go to your project folder

```
cd $PROJECT_HOME
```

1. Get the latest branch from LaunchPad with Bazaar:

```
bzr branch lp:mariadb-tools
```

Now the project for the dbt3 benchmark test will be in the following dir:

```
$PROJECT_HOME/mariadb-tools/dbt3_benchmark/
```

The project `dbt3_benchmark` has the following directories and files:

* config — a folder where the configuration files\
  for MariaDB, MySQL and PostgreSQL are stored. They are divided into\
  subfolders named '`sXX`', where `XX` is the scale factor.
* dbt3\_mysql — a folder with all the necessary\
  files for preparing DBT3 databases and queries for the tests with MySQL and\
  MariaDB
* tests — a folder where the different test\
  configurations are stored. It contains the following directories:
  * db\_conf — here are stored the database\
    configuration files
  * queries\_conf — here are stored the different\
    queries configuration files
  * results\_db\_conf — here is stored the\
    configuration of the results database
  * test\_conf — here are the test configurations
  * launcher.pl — a perl script that automates the\
    test. Details about calling and functionality of this file are listed later\
    on this page.

### Prepare benchmark workload and queries

For the purpose of the benchmark from [DBT3-1.9](https://sourceforge.net/projects/osdldbt/files/dbt3/) we will only\
need **DBGEN** and **QGEN**. DBGEN is a tool that generates a workload for the\
test and QGEN is a tool that generates the queries used for the test.

1. Go to
2. Download the archive for DBT3 1.9 into your project folder $PROJECT\_HOME
3. Unzip the archive into your project folder

```
cd $PROJECT_HOME
tar -zxf dbt3-1.9.tar.gz
```

1. Copy the file tpcd.h into the dbt3 folder. This step includes the necessary labels for MySQL/MariaDB when building queries.

```
cp $PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/tpcd.h $PROJECT_HOME/dbt3-1.9/src/dbgen/
```

1. Copy the file Makefile under `$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/` into the dbt3 folder

* NOTE: This step is executed only if you want to overwrite the default\
  behavior of PostgreSQL settings. After copying this Makefile and building the\
  project, QGEN will be set to generate queries for MariaDB/MySQL. If you skip\
  this step, QGEN will generate queries for PostgreSQL by default.

```
cp $PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/Makefile $PROJECT_HOME/dbt3-1.9/src/dbgen/
```

1. Go to $PROJECT\_HOME/dbt3-1.9/src/dbgen and build the project

```
cd $PROJECT_HOME/dbt3-1.9/src/dbgen
make
```

1. Set the variable DSS\_QUERY to the folder with template queries for MariaDB/MySQL or for PostgreSQL
2. If you want to build the queries that fit MariaDB/MySQL dialect execute the following command:

```
export DSS_QUERY=$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/mysql_queries/
```

1. If you want to use the default PostgreSQL templates, execute the following command:

```
export DSS_QUERY=$PROJECT_HOME/dbt3-1.9/queries/pgsql/
```

1. Create a directory to store the generated queries in

```
mkdir $PROJECT_HOME/gen_query
```

1. Generate the queries

**NOTE:** The examples use scale factor 30. If you want different scale, change\
the value of `-s` parameter

* ```
  ```

cd $PROJECT\_HOME/dbt3-1.9/src/dbgen\
./qgen -s 30 1 > $PROJECT\_HOME/gen\_query/s30-m/1.sql\
./qgen -s 30 2 > $PROJECT\_HOME/gen\_query/s30-m/2.sql\
./qgen -s 30 3 > $PROJECT\_HOME/gen\_query/s30-m/3.sql\
./qgen -s 30 4 > $PROJECT\_HOME/gen\_query/s30-m/4.sql\
./qgen -s 30 5 > $PROJECT\_HOME/gen\_query/s30-m/5.sql\
./qgen -s 30 6 > $PROJECT\_HOME/gen\_query/s30-m/6.sql\
./qgen -s 30 7 > $PROJECT\_HOME/gen\_query/s30-m/7.sql\
./qgen -s 30 8 > $PROJECT\_HOME/gen\_query/s30-m/8.sql\
./qgen -s 30 9 > $PROJECT\_HOME/gen\_query/s30-m/9.sql\
./qgen -s 30 10 > $PROJECT\_HOME/gen\_query/s30-m/10.sql\
./qgen -s 30 11 > $PROJECT\_HOME/gen\_query/s30-m/11.sql\
./qgen -s 30 12 > $PROJECT\_HOME/gen\_query/s30-m/12.sql\
./qgen -s 30 13 > $PROJECT\_HOME/gen\_query/s30-m/13.sql\
./qgen -s 30 14 > $PROJECT\_HOME/gen\_query/s30-m/14.sql\
./qgen -s 30 15 > $PROJECT\_HOME/gen\_query/s30-m/15.sql\
./qgen -s 30 16 > $PROJECT\_HOME/gen\_query/s30-m/16.sql\
./qgen -s 30 17 > $PROJECT\_HOME/gen\_query/s30-m/17.sql\
./qgen -s 30 18 > $PROJECT\_HOME/gen\_query/s30-m/18.sql\
./qgen -s 30 19 > $PROJECT\_HOME/gen\_query/s30-m/19.sql\
./qgen -s 30 20 > $PROJECT\_HOME/gen\_query/s30-m/20.sql\
./qgen -s 30 21 > $PROJECT\_HOME/gen\_query/s30-m/21.sql\
./qgen -s 30 22 > $PROJECT\_HOME/gen\_query/s30-m/22.sql

```


1. Generate the explain queries
```

./qgen -s 30 -x 1 > $PROJECT\_HOME/gen\_query/s30-m/1\_explain.sql\
./qgen -s 30 -x 2 > $PROJECT\_HOME/gen\_query/s30-m/2\_explain.sql\
./qgen -s 30 -x 3 > $PROJECT\_HOME/gen\_query/s30-m/3\_explain.sql\
./qgen -s 30 -x 4 > $PROJECT\_HOME/gen\_query/s30-m/4\_explain.sql\
./qgen -s 30 -x 5 > $PROJECT\_HOME/gen\_query/s30-m/5\_explain.sql\
./qgen -s 30 -x 6 > $PROJECT\_HOME/gen\_query/s30-m/6\_explain.sql\
./qgen -s 30 -x 7 > $PROJECT\_HOME/gen\_query/s30-m/7\_explain.sql\
./qgen -s 30 -x 8 > $PROJECT\_HOME/gen\_query/s30-m/8\_explain.sql\
./qgen -s 30 -x 9 > $PROJECT\_HOME/gen\_query/s30-m/9\_explain.sql\
./qgen -s 30 -x 10 > $PROJECT\_HOME/gen\_query/s30-m/10\_explain.sql\
./qgen -s 30 -x 11 > $PROJECT\_HOME/gen\_query/s30-m/11\_explain.sql\
./qgen -s 30 -x 12 > $PROJECT\_HOME/gen\_query/s30-m/12\_explain.sql\
./qgen -s 30 -x 13 > $PROJECT\_HOME/gen\_query/s30-m/13\_explain.sql\
./qgen -s 30 -x 14 > $PROJECT\_HOME/gen\_query/s30-m/14\_explain.sql\
./qgen -s 30 -x 15 > $PROJECT\_HOME/gen\_query/s30-m/15\_explain.sql\
./qgen -s 30 -x 16 > $PROJECT\_HOME/gen\_query/s30-m/16\_explain.sql\
./qgen -s 30 -x 17 > $PROJECT\_HOME/gen\_query/s30-m/17\_explain.sql\
./qgen -s 30 -x 18 > $PROJECT\_HOME/gen\_query/s30-m/18\_explain.sql\
./qgen -s 30 -x 19 > $PROJECT\_HOME/gen\_query/s30-m/19\_explain.sql\
./qgen -s 30 -x 20 > $PROJECT\_HOME/gen\_query/s30-m/20\_explain.sql\
./qgen -s 30 -x 21 > $PROJECT\_HOME/gen\_query/s30-m/21\_explain.sql\
./qgen -s 30 -x 22 > $PROJECT\_HOME/gen\_query/s30-m/22\_explain.sql

```


Now the generated queries for MariaDB/MySQL test are ready and are stored into
the folder `$PROJECT_HOME/gen_query/s30-m/` (-m is for MariaDB/MySQL).


Additional reorganization of directories is up to the user.


1. Create a directory for the generated workload
```

mkdir $PROJECT\_HOME/gen\_data/s30

```


1. Set the variable DSS_PATH to the folder with the generated table data. The generated workload for the test will be generated there.
```

export DSS\_PATH=$PROJECT\_HOME/gen\_data/s30/

```


1. Generate the table data


* NOTE: The example uses scale factor = `30`. If you want to change it, you should change the parameter `-s`.
```

./dbgen -vfF -s 30

```


* Now the generated data load is stored into the folder set in `$DSS_PATH = $PROJECT_HOME/gen_data/`


For the purpose of this benchmark these steps have been performed for scale
factor 30 and are stored on facebook-maria1 in the following locations:


* `/benchmark/dbt3/gen_data/s30` — the data load for scale factor 30
* `/benchmark/dbt3/gen_query/s30-m` — generated queries for MariaDB/MySQL with scale factor 30
* `/benchmark/dbt3/gen_query/s30-p` — generated queries for PostgreSQL with scale factor 30


See [DBT3 example preparation time](dbt3-example-preparation-time.md) to see how long it would take you to
prepare the databases for the test.


### Download [MySQL 5.5.x](https://dev.mysql.com/downloads/mysql/#downloads)


1. Download the tar.gz file into your project folder `$PROJECT_HOME/bin/` for example


1. Unzip the archive with the following command:
```

gunzip < mysql-5.5.x-linux2.6-x86\_64.tar.gz |tar xf -

```


Now the server could be started with the following command:

```

$PROJECT\_HOME/bin/mysql-5.5.x-linux2.6-x86\_64/bin/mysqld\_safe --datadir=some/data/dir &

```


### Download [MySQL 5.6.x](https://dev.mysql.com/downloads/mysql/#downloads)


1. Download the tar.gz file into your project folder `$PROJECT_HOME/bin/` for example


1. Unzip the archive with the following command:
```

gunzip < mysql-5.6.x-m5-linux2.6-x86\_64.tar.gz |tar xf -

```


Now the server could be started with the following command:


```

$PROJECT\_HOME/bin/mysql-5.6.x-m5-linux2.6-x86\_64/bin/mysqld\_safe --datadir=some/data/dir &

```

### Download and build [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).x / [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).x


**NOTE:** These steps are the same for [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).x with properly replaced
version numbers


1. Download with Bazaar the [mariadb 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) project
```

bzr branch lp:maria/5.3\
mv 5.3/ mariadb-5.3

```


1. Build MariaDB
```

cd mariadb-5.3/\
./BUILD/compile-amd64-max

```


1. Build a binary distribution tar.gz file
```

./scripts/make\_binary\_distribution

```


1. Move the generated tar.gz file and unzip it to $PROJECT_HOME/bin from where
 it will be used by the automation script
```

mv mariadb-5.3.x-beta-linux-x86\_64.tar.gz $PROJECT\_HOME/bin/\
cd $PROJECT\_HOME/bin/\
tar -xf mariadb-5.3.x-beta-linux-x86\_64.tar.gz

```


Now the server could be started with the following command:

```

$PROJECT\_HOME/bin/mariadb-5.3.x-beta-linux-x86\_64/bin/mysqld\_safe --datadir=some/data/dir &

```


### Prepare the databases for the benchmark


**NOTE:** These instructions are the same for MariaDB, MySQL 5.5.x and MySQL
5.6.x with changing only the database home folders, noted here as $DB_HOME (for
example for MySQL 5.5.x $DB_HOME is
`$PROJECT_HOME/bin/mysql-5.5.x-linux2.6-x86_64`). Also you can prepare InnoDB
storage engine test databases. Instructions for preparing PostgreSQL could be
found in the section for downloading, building and preparing PostgreSQL later
on this page.


1. Open the file `$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/make-dbt3-db_innodb.sql` and edit the values for the call of the sql commands that look like this one:
```

LOAD DATA INFILE '/some/path/to/gen\_data/nation.tbl' into table nation fields terminated by '|';

```


* They all look the same but operate with different tables.


* Replace "/some/path/to/gen_data/" with the proper directory where the
 generated data load is stored. At the end the same command could look like
 this:
```

LOAD DATA INFILE '\~/benchmark/dbt3/gen\_data/s30/nation.tbl' into table nation fields terminated by '|';

```


1. Create an empty MySQL database into a folder that will be used for the benchmark
```

cd $DB\_HOME\
./scripts/mysql\_install\_db --defaults-file=$PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/config/s30/load\_mysql\_myisam\_my.cnf --basedir=$DB\_HOME --datadir=$PROJECT\_HOME/db\_data/myisam-s30/

```


* NOTE: For InnoDB change the defaults-file to `load_mysql_innodb_my.cnf`.


1. Start the mysqld process`./bin/mysqld_safe --defaults-file=$PROJECT_HOME/mariadb-tools/dbt3_benchmark/config/s30/load_mysql_myisam_my.cnf --tmpdir=$PROJECT_HOME/temp/ --socket=$PROJECT_HOME/temp/mysql.sock --datadir=$PROJECT_HOME/db_data/myisam-s30/ &`


* NOTE: For InnoDB change the defaults-file to `load_mysql_innodb_my.cnf`.
 Also make sure that you have enough space in the directory set by the
 parameter `--tmpdir`, since loading the database could take a
 lot of temporary space.


1. Load the data into the database by executing the file `make-dbt3-db_pre_create_PK.sql` (for InnoDB) or `make-dbt3-db_post_create_PK.sql` (for MyISAM)`./bin/mysql -u root -S $PROJECT_HOME/temp/mysql.sock < $PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/make-dbt3-db_post_create_PK.sql`


* NOTE: For faster creation, it is recommended to
 use `make-dbt3-db_pre_create_PK.sql` for loading InnoDB
 and `make-dbt3-db_post_create_PK.sql` for loading MyISAM databases.


1. Shutdown the database server:
```

./bin/mysqladmin --user=root --socket=$PROJECT\_HOME/temp/mysql.sock shutdown 0

```


Now you have a database loaded with scale 30. Its datadir is
`$PROJECT_HOME/db_data/myisam-s30/`


The same steps can be reproduced for different scale factors and for different
storage engines.


### Download, build and prepare [PostgreSQL](https://www.postgresql.org/ftp/source/v9.1rc1/)


1. Go to [](https://www.postgresql.org/ftp/source/v9.1rc1/)


1. Download the file under the link postgresql-9.1rc1.tar.gz


1. Unzip the archive to your project folder
```

gunzip < postgresql-9.1rc1.tar.gz |tar xf -

```


1. Execute the following commnads into the shell to install PostgreSQL:
```

mkdir $PROJECT\_HOME/PostgreSQL\_bin\
cd $PROJECT\_HOME/postgresql-9.1rc1\
./configure --prefix=$PROJECT\_HOME/bin/PostgreSQL\_bin\
make\
make install

```


* NOTE: Configure script may not find the following libraries: readline
 and zlib. In that case you can run configure without these libraries by
 adding the following parameters to the command line:
 `--without-readline --without-zlib`


1. Prepare the database to test with:
```

mkdir $PROJECT\_HOME/db\_data/postgre\_s30\
cd $PROJECT\_HOME/bin/PostgreSQL\_bin\
./bin/initdb -D $PROJECT\_HOME/db\_data/postgre\_s30

```


1. Start the server:
```

./bin/postgres -D $PROJECT\_HOME/db\_data/postgre\_s30 -p 54322 &

```


1. Load the dataload into the DB
```

./bin/createdb -O {YOUR\_USERNAME} dbt3 -p 54322\
./bin/psql -p 54322 -d dbt3 -f $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/dbt3\_mysql/make-dbt3-db\_pg.sql

```


* NOTE: Here under `{YOUR_USERNAME}` you should put the
 database owner.


1. Stop the server:


```

./bin/pg\_ctl -D $PROJECT\_HOME/db\_data/postgre\_s30/ -p 54322 stop

```

The steps for preparing the workload for the benchmark on facebook-maria1 are
already made for MariaDB, MySQL and PostgreSQL. Here are the directories for
the different DBMS, storage engines and scale factors that are prepared on
facebook-maria1:


* `~/benchmark/dbt3/db_data/myisam_s30`
— datadir for MariaDB/MySQL + MyISAM with scale
 factor 30


* `~/benchmark/dbt3/db_data/innodb_mariadb_s30`
— datadir for MariaDB + InnoDB with scale factor 30
 (TODO)


* `~/benchmark/dbt3/db_data/innodb_mysql_s30`
— datadir for
 MySQL + InnoDB with scale factor 30 (TODO)


* `~/benchmark/dbt3/db_data/postgre_s30`
— datadir for
 PostgreSQL with scale factor 30 (TODO)


### Prepare the results database


The results of the benchmark will be stored in a separate database that will be
run by [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).x.


**NOTE:** The results database will be a subject to change in future versions
of the DBT3 benchmarking project.


The database is created by the file
`$PROJECT_HOME/mariadb-tools/dbt3_benchmark/dbt3_mysql/make-results-db.sql`.
In that file you can find details about every table and column in the database.


To prepare the database for work follow these steps:


1. Go to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).x installation directory
```

cd $PROJECT\_HOME/bin/mariadb-5.3.x-beta-linux-x86\_64

```


1. Install the system database tables into the datadir for the results (for
example `$PROJECT_HOME/db_data/dbt3_results_db`)
```

./scripts/mysql\_install\_db --datadir=$PROJECT\_HOME/db\_data/dbt3\_results\_db

```


1. Start mysqld for results db
```

./bin/mysqld\_safe --defaults-file=$PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/config/results\_mariadb\_my.cnf --port=12340 --socket=$PROJECT\_HOME/temp/mysql\_results.sock --datadir=$PROJECT\_HOME/db\_data/dbt3\_results\_db/ &

```


1. Install the database
```

./bin/mysql -u root -P 12340 -S $PROJECT\_HOME/temp/mysql\_results.sock < $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/dbt3\_mysql/make-results-db.sql

```


1. Shutdown the results db server:
```

./bin/mysqladmin --user=root --port=12340 --socket=$PROJECT\_HOME/temp/mysql\_results.sock shutdown 0

```


## Automation script


### Configuring and running a benchmark


In order to run a benchmark, one should have:


* 5 configuration files:

  1. DBMS server configuration (see [#dbms-server-configuration](#dbms-server-configuration))
  1. Test configuration (see [#test-configuration](#test-configuration))
  1. Queries configuration (see [#queries-configuration](#queries-configuration))
  1. Results database configuration (see [#results-database-configuration](#results-database-configuration))
  1. Top-level configuration file that combines all of the above (see
 [#top-level-configuration](#top-level-configuration))
* an automation script `launcher.pl` that could be found
 under `mariadb-tools/dbt3_benchmark/`
* startup parameters that should be passed to the automation script (see
 [#script-startup-parameters](#script-startup-parameters)).


Details about each of these is given in the following sections.


Each benchmark is configured by a set of configuration files. One can find
example (default) configuration files under the directory
'mariadb-tools/dbt3_benchmark/tests'. Each configuration file has an 'ini'
configuration syntax and is parsed by the perl automation script with the CPAN
module [Config::Auto](https://search.cpan.org/~simon/Config-Auto-0.03/Auto.pm)


#### Configuration keywords


Every configuration file could contain keywords that will be replaced by the
script with particular values. They are used for convenience when you want to
make your configuration files more common to the environment that you have
prepared for the benchmark. These keywords are:


* `$PROJECT_HOME` — used as the directory where the
 project '`mariadb-tools`' is located or as a base path for the whole project
 (e.g. "`DBMS_HOME = $PROJECT_HOME/bin/mariadb-5.3.x-beta-linux-x86_64`").
 It is replaced by the value set with the startup parameter 'project-home'
 passed to launcher.pl,


* `$DATADIR_HOME` — used as the directory where the
 datadir folders are located for the benchmark (e.g.
 "`$DATADIR_HOME/myisam-s30`"). It is replaced by the value set
 with the startup parameter 'datadir-home' passed to launcher.pl.


* `$QUERIES_HOME` — used as the directory where the
 queries are located (e.g. "`$QUERIES_HOME/s30-m`"
 — queries for MariaDB/MySQL for scale factor 30). It
 is replaced by the value set with the startup parameter 'queries-home'
 passed to launcher.pl.


* `$SCALE_FACTOR` — the scale factor that will be
 used. It is usually a part of the name of the datadir directory (e.g.
 "`$DATADIR_HOME/myisam-s$SCALE_FACTOR`"), the queries directory (e.g.
 "`$QUERIES_HOME/s$SCALE_FACTOR-m`") or the database configuration directory
 (e.g. `$PROJECT_HOME/mariadb-tools/dbt3_benchmark/config/s$SCALE_FACTOR`).
 It is replaced by the value set with the startup parameter 'scale-factor'
 passed to launcher.pl.


Note that if any of the configuration files contains such keyword, the
corresponding startup parameter passed to **launcher.pl** will become required.


#### Top-level configuration


A top-level configuration file provides paths to the **Test, DBMS, Queries**
and **Results database** configurations files


There are default configuration files in the directory
`mariadb-tools/dbt3_benchmark/tests/` and contain the following settings:



| Parameter | Description |
| --- | --- |
| RESULTS_DB_CONFIG | The configuration file for results DB settings |
| TEST_CONFIG | The configuration file for the test settings |
| QUERIES_CONFIG | The configuration file for the queries settings |
| DB_CONFIG | The configuration file for the DBMS server settigns |



This file has the following format:


```

\[common]\
RESULTS\_DB\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/results\_db\_conf/results\_db.conf\
TEST\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/test\_conf/test\_myisam.conf

\[mariadb\_5\_3]\
QUERIES\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/queries\_conf/queries.conf\
DB\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/db\_conf/db\_mariadb\_5\_3\_myisam.conf

\[mysql\_5\_5]\
QUERIES\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/queries\_conf/queries\_mysql.conf\
DB\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/db\_conf/db\_mysql\_5\_5\_myisam.conf\
...

```

**NOTE:** The settings `RESULTS_DB_CONFIG` and `TEST_CONFIG` should be set
under the `[common]` section. They are common for the whole test (although
some settings from `TEST_CONFIG` could be overridden in the
`QUERIES_CONFIG` file). All settings that combine `QUERIES_CONFIG` and
`DB_CONFIG` should be in a separate section (e.g. `[mariadb_5_3]`).


A test configuration is passed as an input parameter to the automation script
with the parameter
`--test=/path/to/some_test_configuration.conf` (see
[#script-startup-parameters](#script-startup-parameters))


#### DBMS server configuration


These configuration files contain settings that describe the benchmarked DBMS.
They are usually contained into the folder
`mariadb-tools/dbt3_benchmark/tests/db_conf`.


Here is the list of parameters that could be set into this configuration file:



| Parameter | Description |
| --- | --- |
| DBMS_HOME | Where the instalation folder of MariaDB / MySQL / PostgreSQL is located.NOTE: The automation script uses "./bin/mysqld_safe" to start the mysqld process. So the versions of MariaDB and MySQL should be a "binary distribution" ones. |
| DBMS_USER | The database user that will be used. |
| CONFIG_FILE | The config file that mysqld or postgres will use when starting |
| SOCKET | The socket that will be used to start the server |
| PORT | The port that the server will be started on |
| HOST | The host where the server is located |
| DATADIR | Where the datadir for mysqld or postgres is located |
| TMPDIR | Where the temp tables will be created while sorting and grouping. |
| DBNAME | The database (schema) name where the benchmark tables are located. |
| KEYWORD | This text will be stored into the results database as a keyword. Also will be used as a name for a subfolder with results and statistics. |
| DBMS | Database Management System that will be used. Possible values: "MySQL", "MariaDB" and "PostgreSQL" |
| STORAGE_ENGINE | The storage engine that was used (MyISAM, InnoDB, etc.) |
| STARTUP_PARAMS | Any startup parameters that will be used while starting the mysqld process or postgres process. Same format as given on the command line. |
| GRAPH_HEADING | The heading of the graphic for that particular test. |
| MYSQL_SYSTEM_DIR | See "MYSQL_SYSTEM_DIR note", below. |
| READ_ONLY | If set to 1, mysqld process will be started with '--read-only' startup parameter |
| PRE_RUN_SQL | SQL commands that are run prior each query run |
| POST_RUN_SQL | SQL commands that are run after each query run |
| PRE_TEST_SQL | SQL commands that are run prior the whole test with that database settings |
| POST_TEST_SQL | SQL commands that are run after the whole test with that database settings |



**`MYSQL_SYSTEM_DIR` note:**
This option is added for convenience when you want to save time and disk space
for generating databases for different DBMS (and different versions) and use a
single data directory for all of them. When running different versions of
MariaDB/MySQL over a single datadir, one should run
[mysql-upgrade](https://dev.mysql.com/doc/refman/5.5/en/mysql-upgrade.html) in
order to fix the system tables. So in one data directory, you could prepare the
following directories for different MariaDB/MySQL system directories:


* `mysql_mysql_5_5` — a copy of the system directory
 '`mysql`' upgraded by MySQL 5.5.x
* `mysql_mariadb_5_3` — a copy of the system
 directory '`mysql`' upgraded by [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3).x
* `mysql_mariadb_5_5` — a copy of the system
 directory '`mysql`' upgraded by [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5).x

If `MYSQL_SYSTEM_DIR` is set to one of these directories, the automation
script will unlink the current system directory 'mysql' and make a new symbolic
link with that name to the one in the setting.
Here is an example command that will be executed:


```

unlink /path/to/datadir/mysql\
ln -s /path/to/value/in/MYSQL\_SYSTEM\_DIR/mysql\_mariadb\_5\_3 /path/to/datadir/mysql

```

**NOTE:** This approach is suitable for MyISAM tests.


The configuration file looks like this:


```

\[db\_settings]\
DBMS\_HOME = $PROJECT\_HOME/bin/mariadb-5.3.2-beta-linux-x86\_64\
DBMS\_USER = root\
...

```

Note that the section `[db_settings]` is required for the file to be properly
parsed by the automation script.


#### Test configuration


These configuration files contain settings describing the test. They are
usually contained into the folder
**mariadb-tools/dbt3_benchmark/tests/test_conf**.


Here is the list of parameters that could be set into this configuration file:



| Parameter | Description |
| --- | --- |
| QUERIES_AT_ONCE | If set to 1, then all the queries are executed sequentially without restarting the server or clearing the caches between queries. |
| CLEAR_CACHES | If set to 1, the disk caches will be cleared before each query test. |
| WARMUP | Perform a warm-up runs before running the query. |
| EXPLAIN | Run an Explain command prior the run of the query. The explain results will be stored in a file under the results output directory. |
| RUN | Perform the actual test |
| ANALYZE_EXPLAIN | A result extraction mechanism where only the best execution plan (results from EXPLAIN select) will be measured. It is designed to be used when benchmarking InnoDB storage engine where execution plan is changing between server restarts (see [#results-extraction-mechanisms](#results-extraction-mechanisms)). |
| MIN_MAX_OUT_OF_N | A result extraction mechanism where the minimal and maximal values out of N (set by the parameter NUM_TESTS) tests are taken as a result. This could be used when InnoDB storage engine is tested (see [#results-extraction-mechanisms](#results-extraction-mechanisms)). |
| SIMPLE_AVERAGE | A result extraction mechanism where the final result is the average time taken for the tests. The number of tests is per query is set by the NUM_TESTS parameter. Note that if even one test has timed out, the result is 'time-out'. This is used when testing MyISAM storage engine since there the execution plan is constant (see [#results-extraction-mechanisms](#results-extraction-mechanisms)). |
| NUM_TESTS | How many tests should be performed for each query. When ANALYZE_EXPLAIN is set, this value could be set to 0, meaning that the tests will continue until enough results are extracted (see setting CLUSTER_SIZE). This parameter is very important when MIN_MAX_OUT_OF_N or SIMPLE_AVERAGE is selected. |
| MAX_SKIPPED_TESTS | When ANALYZE_EXPLAIN is set and an execution plan that is slower is selected, the execution of the query is skipped and the server is restarted in order to change the execution plan. If the server is restarted more than MAX_SKIPPED_TESTS, there are obviously no more different execution plans and the script continues to the next query benchmark. |
| WARMUPS_COUNT | How many warmup runs will be performed prior the actual benchmark run. |
| CLUSTER_SIZE | How big a cluster with results for a query should be in order to extract the final result. It is used when ANALYZE_EXPLAIN is selected as a result extraction method. |
| MAX_QUERY_TIME | The maximum time that one query will be tested. Currently it is applicable only when ANALYZE_EXPLAIN is selected. |
| TIMEOUT | The maximum time that one query could run. Currently timeout is applicable only for MySQL and MariaDB. |
| OS_STATS_INTERVAL | What is the time interval between extraction of OS statistics for CPU, memory, etc. |
| PRE_RUN_OS | OS commands that should be executed prior each query run |
| POST_RUN_OS | OS commands that should be executed after each query run |
| PRE_TEST_OS | OS commands that should be executed prior the whole test |
| POST_TEST_OS | OS commands that should be executed after the whole test is complete |



The configuration file looks like this:


```

QUERIES\_AT\_ONCE = 0\
CLEAR\_CACHES = 1\
WARMUP = 0\
...

```

#### Queries configuration


These configuration files contain the list of all the queries that will be
benchmarked against each database. Some settings
from `DBMS server configuration` and `Test configuration` could be
overridden into the `Queries configuration` files. The folder that contains
such configurations is `mariadb-tools/dbt3_benchmark/tests/queries_conf`.


Here is the list of parameters that could be set into this configuration file:



| Parameter | Description |
| --- | --- |
| QUERIES_HOME | Where the queries are located on disk. This value is concatenated to the QUERY setting and this makes the path to the particular query. NOTE: This setting should be set under the section [queries_settings]. |
| CONFIG_FILE | This overrides the startup setting CONFIG_FILE from DMBS server configuration file and sets the database configuration file that is used. It could be used if some configuration file without any optimizations should be set for this particular queries configuration file.NOTE: This setting should be set under the section [queries_settings]. |
| QUERY | The name of the query located into QUERIES_HOME folder. E.g. "1.sql" |
| EXPLAIN_QUERY | The name of the explain query into QUERIES_HOME folder. E.g. "1_explain.sql" |
| TMPDIR | This overrides the setting TMPDIR from the DMBS server configuration. |
| STARTUP_PARAMS | This overrides the setting STARTUP_PARAMS from the DMBS server configuration. Using this setting one could change the particular startup parameters (like optimizations and buffers) for the DB server. |
| PRE_RUN_SQL | This overrides the setting PRE_RUN_SQL from the DMBS server configuration. |
| POST_RUN_SQL | This overrides the setting POST_RUN_SQL from the DMBS server configuration. |
| RUN | This overrides the setting RUN from the test configuration. |
| EXPLAIN | This overrides the setting EXPLAIN from the test configuration. |
| TIMEOUT | This overrides the setting TIMEOUT from the test configuration. |
| NUM_TESTS | This overrides the setting NUM_TESTS from the test configuration. |
| MAX_SKIPPED_TESTS | This overrides the setting MAX_SKIPPED_TESTS from the test configuration. |
| WARMUP | This overrides the setting WARMUP from the test configuration. |
| WARMUPS_COUNT | This overrides the setting WARMUPS_COUNT from the test configuration. |
| MAX_QUERY_TIME | This overrides the setting MAX_QUERY_TIME from the test configuration. |
| CLUSTER_SIZE | This overrides the setting CLUSTER_SIZE from the test configuration. |
| PRE_RUN_OS | This overrides the setting PRE_RUN_OS from the test configuration. |
| POST_RUN_OS | This overrides the setting POST_RUN_OS from the test configuration. |
| OS_STATS_INTERVAL | This overrides the setting OS_STATS_INTERVAL from the test configuration. |



The queries configuration file could look like this:


```

\[queries\_settings]\
QUERIES\_HOME = /path/to/queries

\[query1]\
QUERY=1.sql\
EXPLAIN\_QUERY=1\_explain.sql\
STARTUP\_PARAMS=

\[query2]\
QUERY=2.sql\
EXPLAIN\_QUERY=2\_explain.sql\
STARTUP\_PARAMS=--optimizer\_switch='mrr=on' --mrr\_buffer\_size=8M --some\_startup\_parmas\
...

```

...where "`QUERIES_HOME = /path/to/queries`" could be replaced with
"`QUERIES_HOME = $QUERIES_HOME/s$SCALE_FACTOR-m`" for example and thus
`$QUERIES_HOME` and $SCALE_FACTOR will be replaced by the script startup
parameters passed to `launcher.pl` (see [#script-startup-parameters](#script-startup-parameters))


**NOTE:** The section `[queries_settings]` is required for the configuration
file to be parsed correctly. Also each query settings should be set under an
uniquely named configuration section (e.g. `[query1]` or `[1.sql]`)


#### Results database configuration


These configuration files contain settings about the database where the results
will be stored. They are usually contained into the folder
`mariadb-tools/dbt3_benchmark/tests/results_db_conf`.


Here is the list of parameters that could be set into this configuration file:



| Parameter | Description |
| --- | --- |
| DBMS_HOME | Where the database directory is located. E.g. "$PROJECT_HOME/mariadb-5.3.x-beta-linux-x86_64". This should be a binary distribution of MariaDB or MySQL. |
| DBMS_USER | The user that will be used by the DBMS |
| DATADIR | Where the data directory is located for the results database |
| CONFIG_FILE | What the configuration file used by the database is. |
| SOCKET | The socket that will be used by the results database. This should be different socket than the one provided for the testing databases. |
| PORT | The port that the results database will use. This should be different port than the one provided for the testing databases. |
| STARTUP_PARAMS | Any startup parameters that should be set to start the server. |
| DBNAME | The database name to use. |
| HOST | The host where the results database is. |



The results database configuration could look like this:


```

DBMS\_HOME = $PROJECT\_HOME/mariadb-5.3.x-beta-linux-x86\_64\
DBMS\_USER = root\
...

```

#### Script startup parameters


`launcher.pl` could accept startup parameters called in the manner
"`--some-param`". Note that these startup parameters are
case-sensitive. The ones that are with upper-case are used when overriding a
setting in some of the configuration files.


Here is a list of the startup parameters:



| Parameter | Description |
| --- | --- |
| test | The top-level benchmark configuration file that will be run. This is a required startup parameter. |
| results-output-dir | Where the results of the benchmark will be stored. A timestamp is automatically attached to the directory name so that it keeps track of time and date of the benchmark. This is a required parameter. |
| dry-run | If set, no benchmark will be performed. Instead only messages will be displayed for the actions that were intended to be done. |
| project-home | Required if any configuration file uses the variable '$PROJECT_HOME'. If all configuration files use absolute paths, not used. |
| datadir-home | The value in this parameter will replace any occurrences of the string '$DATADIR_HOME' into the configuration files. If there are no such occurances, it is not a required parameter. |
| queries-home | The value in this parameter will replace any occurrences of the string '$QUERIES_HOME' into the configuration files. If there are no such occurances, it is not a required parameter. |
| scale-factor | The value in this parameter will replace any occurrences of the string '$SCALE_FACTOR' into the configuration files. If there are no such occurances, it is not a required parameter. |
| CLEAR_CACHES | If set. this overrides the default setting set into the test configuration file. |
| QUERIES_AT_ONCE | If set. this overrides the default setting set into the test configuration file. |
| RUN | If set. this overrides the default setting set into the test configuration file. |
| EXPLAIN | If set. this overrides the default setting set into the test configuration file. |
| TIMEOUT | If set. this overrides the default setting set into the test configuration file. |
| NUM_TESTS | If set. this overrides the default setting set into the test configuration file. |
| MAX_SKIPPED_TESTS | If set. this overrides the default setting set into the test configuration file. |
| WARMUP | If set. this overrides the default setting set into the test configuration file. |
| WARMUPS_COUNT | If set. this overrides the default setting set into the test configuration file. |
| MAX_QUERY_TIME | If set. this overrides the default setting set into the test configuration file. |
| CLUSTER_SIZE | If set. this overrides the default setting set into the test configuration file. |
| PRE_RUN_OS | If set. this overrides the default setting set into the test configuration file. |
| POST_RUN_OS | If set. this overrides the default setting set into the test configuration file. |
| OS_STATS_INTERVAL | If set. this overrides the default setting set into the test configuration file. |



### Results extraction mechanisms


There are three possible result extraction mechanisms. They are set by the
parameters set into the test configuration file:


* `ANALYZE_EXPLAIN`
* `MIN_MAX_OUT_OF_N`
* `SIMPLE_AVERAGE`


Only one of these should be set to true (1).


**`ANALYZE_EXPLAIN`** is used for benchmarking InnoDB storage engine where the
execution plan could change for the same query when the server is restarted. It
is designed to run the query only with the fastest execution plan. This means
that the server is restarted if the current execution plan is proven slower
than the other. As a final result is taken the result for the query plan that
turns out to be fastest and there are at least `CLUSTER_SIZE` tests with it for
that query. By setting the configuration parameter `NUM_TESTS` you can set a
maximum test runs that when reached will get the best cluster's average time
(even if it is less than `CLUSTER_SIZE`). Also when a timeout for that query
(`MAX_QUERY_TIME`) is reached, the scoring mechanism will return the best
available cluster result.


**`MIN_MAX_OUT_OF_N`** is also used for benchmarking InnoDB storage engine.
As a result are stored the values for the fastest and the slowest run. It is
assumed that when the execution plan has changed it has different execution
plan and we are interested only in the min and max time.


**`SIMPLE_AVERAGE`** is used for benchmarking storage engines that do not
change the execution plan between restarts like MyISAM. The final result is the
average execution time from all the test runs for the query.


### Results graphics


After each query test run, the result is stored into a file named
**results.dat** located into `{RESULTS_OUTPUT_DIR}`. This file
is designed to be easy to be read by the plotting program Gnuplot 4.4. It is
divided into blocks, separated by several new lines. Each block starts with a
comment line containing details for the current block of results.


Queries that have timed out have a value of `100000` so that they run out of
the graphics and are cut off. Other queries have their real times (in seconds)
starting from `0`. The graphics is cut off on the y-axis on the longest time
for `completed test + 20%`. For example if the longest time is `100`
seconds, the graphics is cut-off to `120` seconds. Thus the timed out queries
will be truncated by this limitation and will seem as really timed out.


During the test run, a gnuplot script file is generated with the necessary
parameters for the graphics to be generated automatically. After each query
test run is complete, the graphic is regenerated, so that the user can see the
current results before the whole benchmark is complete. This file is called
`gnuplot_script.txt` and is located into `{RESULTS_OUTPUT_DIR}`. The user
can edit it to fine-tune the parameters or headings after the test is complete
so that one could get the look and feel he/she wants for the final result.


### Script output


#### Benchmark output


In the directory set by the parameter {RESULTS_OUTPUT_DIR} (example:
`/benchmark/dbt3/results/myisam_test_2011-12-08_191427/`) there are the
following files/directories:


* A directory for each test, named as the parameter {KEYWORD} from the test
 configuration (example: `mariadb-5-3-2`)
* cpu_info.txt — the output
 of "`/bin/cat /proc/cpuinfo`" OS command
* uname.txt — the output of "`uname -a`" OS
 command
* results.dat — the results of each query
 execution in one file. This file will be used as a datafile for the gnuplot
 script. It also contains the ratio between the current test and the first
 one.
* gnuplot_script.txt — the Gnuplot script that
 renders the graphics.
* graphics.jpeg — the output graphics
* A benchmark configuration file
 (example: `myisam_test_mariadb_5_3_mysql_5_5_mysql_5_6.conf`) copied
 from `mariadb-tools/dbt3_benchmark/tests/`
* A results database configuration file (example: `results_db.conf`)
 copied from `mariadb-tools/dbt3_benchmark/tests/results_db_conf/`
* A test configuration file (example: `test_myisam.conf`) copied
 from `mariadb-tools/dbt3_benchmark/tests/test_conf/`


#### Test output


In the subdirectory for the particular test, set by the parameter {KEYWORD}
(example:
`/benchmark/dbt3/results/myisam_test_2011-12-08_191427/mariadb-5-3-2/`),
there are the following files:


* pre_test_os_resutls.txt - the output of the OS commands (if any) executed
 before the first query run for that test
* pre_test_sql_resutls.txt - the output of the SQL commands (if any)
 executed before the first query run for that test
* post_test_os_resutls.txt - the output of the OS commands (if any)
 executed after the last query run for that test
* post_test_sql_resutls.txt - the output of the SQL commands (if any)
 executed after the last query run for that test
* all_explains.txt - a file containing all the explain queries, their
 startup parameters for the benchmark and the explain result
* The config file (my.cnf) that was passed to mysqld or postgres
 (example: `mariadb_myisam_my.cnf`) copied
 from `mariadb-tools/dbt3_benchmark/config/s$SCALE_FACTOR/`
* The queries configuration file (example: ''queries-mariadb.conf'') copied
 from `mariadb-tools/dbt3_benchmark/tests/queries_conf/`
* The database configuration file (example: ''db_mariadb_5_3_myisam.conf'')
 copied from `mariadb-tools/dbt3_benchmark/tests/db_conf/`


#### Query output


For each query execution there are several files that are outputted by the
automation script. They are all saved under the subdirectory set by the
parameters `{KEYWORD}`:


* Explain result - a file named
 '{query_name}_{number_of_query_run}_results.txt' (example:
 '1_explain.sql_1_results.txt' — first test for 1_explain.sql)
* Pre-run OS commands - OS commands, executed before the actual query run.
 Output is a file named
 'pre_run_os_q_{query_name}_no_{number_of_query_run}_results.txt' (example:
 'pre_run_os_q_1.sql_no_2_results.txt' — second test for query 1.sql)
* Pre-run SQL commands - SQL commands executed before the actual query run.
 Output is a file named
 'pre_run_sql_q_{query_name}_no_{number_of_query_run}_results.txt'.
* Post-run OS commands - OS commands, executed after the actual query run.
 Output is a file named
 'post_run_os_q_{query_name}_no_{number_of_query_run}_results.txt'.
* Post-run SQL commands - SQL commands executed after the actual query run.
 Output is a file named
 'post_run_sql_q_{query_name}_no_{number_of_query_run}_results.txt'.
* CPU utilization statistics:
 '{query_name}_no_{number_of_query_run}_sar_u.txt'
* I/O and transfer rate statistics:
 '{query_name}_no_{number_of_query_run}_sar_b.txt'
* Memory utilization statistics:
 '{query_name}_no_{number_of_query_run}_sar_r.txt'


### Hooks


The automation script provides hooks that allow the user to add both SQL and OS commands prior and after each test. Here is a list of all possible hooks:


* Pre-test SQL hook: it is set with the parameter `PRE_TEST_SQL`. Contains
 SQL commands that are run once for the whole test configuration before the
 first run.
 (Example: "`use dbt3; select version(); show variables; show engines; show table status;`")
* Post-test SQL hook: it is set with the parameter `POST_TEST_SQL`. Contains
 SQL commands that are run once for the whole test configuration after the
 last run.
* Pre-test OS hook: it is set with the parameter `PRE_TEST_OS`. Contains OS
 commands that are run once for the whole test configuration before the first
 run.
* Post-test OS hook: it is set with the parameter `POST_TEST_OS`. Contains OS
 commands that are run once for the whole test configuration after the last
 run.
* Pre-run SQL hook: it is set with the parameter `PRE_RUN_SQL`. Contains SQL
 commands that are run prior each query run.
 (Example: "`flush status; set global userstat=on;`")
* Post-run SQL hook: it is set with the parameter `POST_RUN_SQL`. Contains SQL
 commands that are run after each query run.
 (Example: "`show status; select * from information_schema.TABLE_STATISTICS;`")
* Pre-run OS hook: it is set with the parameter `PRE_RUN_OS`. Contains OS
 commands that are run once prior each query run.
* Post-run OS hook: it is set with the parameter `POST_RUN_OS`. Contains OS
 commands that are run once after each query run.


The results of these commands is stored into the
`{RESULTS_OUTPUT_DIR}/{KEYWORD}` folder (see [#script-output](#script-output))


### Activities


Here are the main activities that this script does:


1. Parse the configuration files and check the input parameters - if any of the
 required parameters is missing, the script will stop resulting an error.
1. Collect hardware information - collecting information about the hardware of
 the machine that the benchmark is run. Currently it collects `cpuinfo`
 and `uname`. Results of these commands are stored into the results output
 directory set as an input parameter
1. Loop through the passed test configurationsFor each passed in test
 configuration the script does the following:

  1. Start the results database server. The results of the test are stored into
 that database.
  1. Clears the caches on the serverClearing the caches is done with the
 following
 command:
```

sudo /sbin/sysctl vm.drop\_caches=3

```


    * NOTE: In order to clear the caches, the user is required to have
 sudo rights and the following line should be added to the `sudoers` file
 (edit it with "`sudo vusudo`"
 command):
```

{your\_username} ALL=NOPASSWD:/sbin/sysctl

```
  1. Start the database server
  1. Perform pre-test SQL commands. The results are stored
 under `results_output_dir/{KEYWORD}` folder and are
 called `pre_test_sql_results.txt`. `{KEYWORD}` is a unique keyword for
 the current database configuration.
  1. Perform pre-test OS commands. The results are stored
 under `results_output_dir/{KEYWORD}` folder and are
 called `pre_test_os_results.txt`.

    * NOTE: If in the test configuration the setting QUERIES_AT_ONCE is
 set to 0, then the server is restarted between each query run. Thus the
 steps 3.2, 3.3, 3.4 and 3.5 are executed only once right before step 3.6.2.
  1. Read all query configurations and execute the following for each of them:

    1. Check the test configuration parameters. If something is wrong with some
 required parameter, the program will exit resulting an error.
    1. Get the server version if that's the first run of the query
    1. Perform pre-run OS commands in shell. The results of these queries are
 stored into a file named `pre_run_os_q_{QUERY}_no_{RUN_NO}_results.txt`
 under `results_output_dir/{KEYWORD}` where `{QUERY}` is the query name
 (ex: `1.sql`), `{RUN_NO}` is the sequential run number
 and `{KEYWORD}` is a unique keyword for the particular test
 configuration.
    1. Perform pre-run SQL queries. The results of these queries are stored into a
 file named `pre_run_sql_q_{QUERY}_no_{RUN_NO}_results.txt`
 under `results_output_dir/{KEYWORD}` where `{QUERY}` is the query name
 (ex: `1.sql`), `{RUN_NO}` is the sequential run number and `{KEYWORD}` is
 a unique keyword for the particular test configuration.
    1. Perform warm-up runs if set into the test configuration file
    1. Perform actual test run and measure time.

      * During this step, a new child process is created in order to measure
 the statistics of the OS. Currently the statistics being collected are:

        * CPU utilization statistics. The command for this is:
```

sar -u 0 2>null

```
        * I/O and transfer rate statistics. The command for this is:
```

sar -b 0 2>null

```
        * Memory utilization statistics. The command for this is:
```

sar -r 0 2>null

```
      * These statistics are measured every N seconds, where `N` is set with
 the `OS_STATS_INTERVAL` test configuration parameter.
      * The test run for MariaDB and MySQL has an implemented mechanism for
 cut-off when timeout exceeds. It is controlled with the `TIMEOUT` test
 parameter. Currently for PostgreSQL there is no such functionality and
 should be implemented in future versions.
    1. Execute the "explain" statement for that query.

      * NOTE: Running `EXPLAIN` queries with MySQL prior version 5.6.3 could
 result in long running queries since MySQL has to execute the whole query
 when there are nested selects in it. For MariaDB and PostgreSQL there is
 no such problem. The long-running explain queries are for queries #7, 8,
 9, 13 and 15. For that reason in MySQL prior version 5.6.3 for these
 queries no `EXPLAIN` selects should be executed.
    1. Perform post-run SQL queries
    1. Perform post-run OS commands in shell
    1. Log the results into the results database
    1. A graphics with the current results is generated using Gnuplot
  1. Shutdown the database server.
  1. Perform post-test SQL commands. The results are stored
 under `results_output_dir/{KEYWORD}` folder and are
 called `post_test_sql_results.txt`.
  1. Perform post-test OS commands. The results are stored
 under `results_output_dir/{KEYWORD}` folder and are
 called `post_test_os_results.txt`.
  1. Stop the results database server


### Script calling examples


* Example call for MyISAM test for scale factor 30 and timeout 10 minutes:
```

perl launcher.pl\
\--project-home=/path/to/project/home/\
\--results-output-dir=/path/to/project/home/results/myisam\_test\
\--datadir=/path/to/project/home/db\_data/\
\--test=/path/to/project/home/mariadb-tools/dbt3\_benchmark/tests/myisam\_test\_mariadb\_5\_3\_mysql\_5\_5\_mysql\_5\_6.conf\
\--queries-home=/path/to/project/home/gen\_query/\
\--scale-factor=30\
\--TIMEOUT=600

```


...where `/path/to/project/home` is where the `mariadb-tools` project is
located. This will replace all occurrences of the string "$PROJECT_HOME" in the
configuration files (example: "`TMPDIR = $PROJECT_HOME/temp/`" will become
"`TMPDIR = /path/to/project/home/temp/`").


`--TIMEOUT` overrides the timeout setting into the test
configuration file to 10 minutes.


* Example for InnoDB test for scale factor 30 with 2 hours timeout per query
 and 3 runs for each query:
```

perl launcher.pl\
\--project-home=/path/to/project/home/\
\--results-output-dir=/path/to/project/home/results/innodb\_test\
\--datadir=/path/to/project/home/db\_data/\
\--test=/path/to/project/home/mariadb-tools/dbt3\_benchmark/tests/innodb\_test\_mariadb\_5\_3\_mysql\_5\_5\_mysql\_5\_6.conf\
\--queries-home=/path/to/project/home/gen\_query/\
\--scale-factor=30\
\--TIMEOUT=7200\
\--NUM\_TESTS=3

```


* If a newer version of [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5) is available:

  * copy or edit the DMBS server configuration
 file `mariadb-tools/dbt3_benchmark/tests/db_conf/db_mariadb_5_5_myisam.conf`
 and change the parameter `DBMS_HOME` to the new binary distribution. You
 can also edit `KEYWORD` and `GRAPH_HEADING`


* If you want to add additional test in the MyISAM benchmark for [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3),
 but with another defaults-file (my.cnf):

  * copy or edit the DMBS server configuration
 file `mariadb-tools/dbt3_benchmark/tests/db_conf/db_mariadb_5_3_myisam.conf`
 and change the parameter CONFIG_FILE to the new my.cnf
  * copy or edit the test configuration
 file `mariadb-tools/dbt3_benchmark/tests/myisam_test_mariadb_5_3_mysql_5_5_mysql_5_6.conf`
 and add the new configuration settings:
```

\[mariadb\_5\_3\_new\_configuration]\
QUERIES\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/queries\_conf/queries-mariadb.conf\
DB\_CONFIG = $PROJECT\_HOME/mariadb-tools/dbt3\_benchmark/tests/db\_conf/db\_mariadb\_5\_3\_myisam\_new\_configuration.conf

```


* If you want to add additional startup parameters for query 6 for MariaDB for
 example:

  * copy or edit the
 file `mariadb-tools/dbt3_benchmark/tests/queries_conf/queries-mariadb.conf`
 and add a parameter
 "`STARTUP_PARAMS=--optimizer_switch='mrr=on' --mrr_buffer_size=96M`"
 for example for the section for query 6.
  * copy or edit the test configuration
 file `mariadb-tools/dbt3_benchmark/tests/myisam_test_mariadb_5_3_mysql_5_5_mysql_5_6.conf`
 to include the new queries configuration file


## Results


### MyISAM test


DBT3 benchmark for the following configuration:


* [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/mariadb-532-release-notes) Beta + MyISAM
* [MariaDB 5.5.18](https://mariadb.com/kb/en/mariadb-5518-release-notes/) + MyISAM
* MySQL 5.5.19 + MyISAM
* MySQL 5.6.4 + MyISAM


Results page: [DBT3 benchmark results MyISAM](dbt3-benchmark-results-myisam.md)


### InnoDB test


DBT3 benchmark for the following configuration:


* [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/mariadb-532-release-notes) Beta + XtraDB
* [MariaDB 5.5.18](/en/mariadb-5518-release-notes/) + XtraDB
* MySQL 5.5.19 + InnoDB
* MySQL 5.6.4 + InnoDB


Results page: [DBT3 benchmark results InnoDB](dbt3-benchmark-results-innodb.md)


### PostgreSQL test


DBT3 benchmark for the following configuration:


* [MariaDB 5.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/mariadb-532-release-notes) Beta + XtraDB
* MySQL 5.6.4 + InnoDB
* PostgreSQL


Results page: (TODO)


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

```
