---
description: >-
  Migrate from Oracle to MariaDB Server. This page provides detailed guidance,
  tools, and best practices for a smooth and efficient transition of your
  databases and applications.
---

# Oracle XE 11.2. and MariaDB 10.1 integration on Ubuntu 14.04 and Debian systems

### Part 1: Installing Oracle Database Express Edition (XE)

This section covers the installation of Java and the Oracle XE database on a Debian-based system like Ubuntu.

#### Step 1: Download Oracle Database XE

1. Sign up for an Oracle account (if you don't have one) and log in.
2. Navigate to the download page for legacy versions of the database. A good starting point is the [Oracle Database Express Edition (XE) 11gR2 Archive Downloads Page](https://www.oracle.com/database/technologies/xe-prior-release-downloads.html).
3. Accept the license agreement.
4. Download Oracle Database Express Edition 11g Release 2 for Linux x64. The file will be named similarly to `oracle-xe-11.2.0-1.0.x86_64.rpm.zip`.

#### Step 2: Install and Configure Java 8

Oracle XE 11gR2 requires a Java environment.

A) Add the Java PPA and Install

```bash
sudo add-apt-repository ppa:webupd8team/java
# Press Enter to accept when prompted
sudo apt-get update
sudo apt-get install oracle-java8-installer
```

B) Verify Java Installation

After the installation completes, verify the version.

```bash
java -version
```

The output should be similar to:

```
java version "1.8.0_121"
```

C) Set JAVA\_HOME Environment Variable

Edit the system-wide bash configuration file.

```bash
sudo nano /etc/bash.bashrc
```

Scroll to the bottom of the file and add the following lines:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export PATH=$JAVA_HOME/bin:$PATH
```

Save the file and exit. Then, source the file to apply the changes and verify the variable is set.

```bash
source /etc/bash.bashrc
echo $JAVA_HOME
```

The output should be:

```
/usr/lib/jvm/java-8-oracle
```

#### Step 3: Install Prerequisite Packages

Additional packages are required to convert and install the Oracle RPM.

```bash
sudo apt-get install alien libaio1 unixodbc
```

#### Step 4: Convert the Oracle RPM to a DEB Package

The downloaded file is an RPM, which must be converted to a DEB package for Debian-based systems.

```bash
unzip oracle-xe-11.2.0-1.0.x86_64.rpm.zip
cd Disk1/
sudo alien --scripts -d oracle-xe-11.2.0-1.0.x86_64.rpm
```

{% hint style="info" %}
This conversion step might take some time. You can proceed with the following configuration steps in a separate terminal window while it runs.
{% endhint %}

#### Step 5: Create `chkconfig` and Kernel Configuration

A) Create a `chkconfig` Compatibility Script

The Oracle installer expects the chkconfig utility, which doesn't exist on Debian-based systems. Create a compatibility script.

```bash
sudo nano /sbin/chkconfig
```

Add the following content to the new file:

```bash
#!/bin/bash
# Oracle 11gR2 XE installer chkconfig for Ubuntu
file=/etc/init.d/oracle-xe
if [[ ! `tail -n1 $file | grep INIT` ]]; then
  echo >> $file
  echo '### BEGIN INIT INFO' >> $file
  echo '# Provides: OracleXE' >> $file
  echo '# Required-Start: $remote_fs $syslog' >> $file
  echo '# Required-Stop: $remote_fs $syslog' >> $file
  echo '# Default-Start: 2 3 4 5' >> $file
  echo '# Default-Stop: 0 1 6' >> $file
  echo '# Short-Description: Oracle 11g Express Edition' >> $file
  echo '### END INIT INFO' >> $file
fi
update-rc.d oracle-xe defaults 80 01
#EOF
```

Save the file, then make it executable:

```bash
sudo chmod 755 /sbin/chkconfig
```

B) Configure Kernel Parameters

Create a configuration file for Oracle-specific kernel parameters.

```bash
sudo nano /etc/sysctl.d/60-oracle.conf
```

Copy and paste the following into the file. The value for `kernel.shmmax` should be approximately half of your system's physical RAM, specified in bytes (e.g., 512MB = 536870912 bytes).

```
# Oracle 11g XE kernel parameters  
fs.file-max=6815744  
net.ipv4.ip_local_port_range=9000 65000  
kernel.sem=250 32000 100 128 
kernel.shmmax=536870912
```

Apply the new kernel parameters and verify the `fs.file-max` setting.

```bash
sudo service procps start
sudo sysctl -q fs.file-max
```

The expected output is `6815744`.

#### Step 6: Final System Adjustments

A) Create Compatibility Links and Directories

```bash
sudo ln -s /usr/bin/awk /bin/awk
sudo mkdir /var/lock/subsys
sudo touch /var/lock/subsys/listener
```

B) Configure Shared Memory (/dev/shm)

To avoid a potential ORA-00845: MEMORY\_TARGET error, re-mount the /dev/shm directory with a sufficient size. Replace 4096m with the amount of RAM on your machine.

```bash
sudo rm -rf /dev/shm
sudo mkdir /dev/shm
sudo mount -t tmpfs shmfs -o size=4096m /dev/shm
```

To make this change persistent across reboots, create a startup script.

```bash
sudo nano /etc/rc2.d/S01shm_load
```

Add the following content, again replacing `4096m` with your machine's RAM size.

```bash
#!/bin/sh
case "$1" in
start)
  mkdir /var/lock/subsys 2>/dev/null
  touch /var/lock/subsys/listener
  rm /dev/shm 2>/dev/null
  mkdir /dev/shm 2>/dev/null
  mount -t tmpfs shmfs -o size=4096m /dev/shm
  ;;
*)
  echo "Usage: $0 start"
  exit 1
  ;;
esac
```

Save the file and make it executable:

```bash
sudo chmod 755 /etc/rc2.d/S01shm_load
```

#### Step 7: Install and Configure Oracle XE

A) Install the Converted Package

By now, the .deb package should have been created. Install it using `\`.

```bash
sudo dpkg --install oracle-xe_11.2.0-2_amd64.deb
```

B) Run the Oracle Configuration Script

Configure the database by running the script and answering the prompts. The default answers are usually acceptable.

```bash
sudo /etc/init.d/oracle-xe configure
```

You will be prompted for:

* HTTP port for Oracle Application Express (default: `8080`)
* Database listener port (default: `1521`)
* A password for the `SYS` and `SYSTEM` accounts.
* Whether to start the database on boot (default: `y`)

C) Set Oracle Environment Variables

Edit `/etc/bash.bashrc` again to add the Oracle-specific variables.

```bash
sudo nano /etc/bash.bashrc
```

Add the following to the end of the file:

```bash
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
export ORACLE_SID=XE
export NLS_LANG=`$ORACLE_HOME/bin/nls_lang.sh`
export ORACLE_BASE=/u01/app/oracle
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$ORACLE_HOME/bin:$PATH
```

Apply and verify the changes:

```bash
source /etc/bash.bashrc
echo $ORACLE_HOME
```

D) Start Oracle

```bash
sudo service oracle-xe start
```

### Part 2: Installing SQL Developer

#### Step 1: Download and Install SQL Developer

1. Go to the Oracle site and download the Linux RPM package for Oracle SQL Developer.
2. Use `alien` to convert the package and `dpkg` to install it.

```bash
sudo alien --scripts -d sqldeveloper-4.1.5.21.78-1.noarch.rpm
sudo dpkg --install sqldeveloper_4.1.5.21.78-2_all.deb
```

3. Create a configuration directory.

```bash
mkdir ~/.sqldeveloper
```

#### Step 2: Run and Connect to Oracle XE

1.  Launch SQL Developer.

    Bash

    ```bash
    sudo /opt/sqldeveloper/sqldeveloper.sh
    ```
2. If it asks for the Java path, provide it: `/usr/lib/jvm/java-8-oracle`.
3. Inside SQL Developer, create a new connection with the following details:
   * Click: `Connections`, then `Add new connection`
   * Connection Name: `XE`
   * Username: `SYSTEM`
   * Password: `<your-password>`
   * Connection Type: `Basic`, Role: `Default`
   * Hostname: `localhost`
   * Port: `1521`
   * SID: `xe`

### Part 3: Installing MariaDB and Connecting to Oracle

#### Step 1: Install MariaDB

Follow the official instructions on the MariaDB website for your specific OS version.

{% hint style="danger" %}
Do NOT copy the commands below. Go to the [MariaDB Repository Configuration Tool](https://www.google.com/search?q=https://mariadb.org/mariadb/repositories/) to generate the correct commands for your system. The following is only an example.
{% endhint %}

```bash
# Example commands for Ubuntu 14.04 Trusty
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://mirror.netinch.com/pub/mariadb/repo/10.1/ubuntu trusty main'
sudo apt-get update
sudo apt-get install mariadb-server
```

#### Step 2: Install MariaDB ODBC Connector

1. Download the "MariaDB Connector/ODBC" for Linux from the MariaDB website.
2. Extract the archive and copy the library file.

```bash
tar xfz mariadb-connector-odbc-2.0.13-ga-linux-x86_64.tar.gz
sudo cp -p mariadb-connector-odbc-2.0.13-ga-linux-x86_64/lib/libmaodbc.so /lib
sudo ldconfig
```

#### Step 3: Install UnixODBC and CONNECT Engine

```bash
sudo apt-get install unixodbc-dev unixodbc-bin unixodbc libodbc1 mariadb-connect-engine-10.1
```

#### Step 4: Configure ODBC Drivers

A) Configure the Oracle Driver

Edit `/etc/odbcinst.ini` and add the following section:

```toml
[Oracle ODBC driver for Oracle 11.2]
Description     = Oracle 11.2 ODBC driver
Driver          = /u01/app/oracle/product/11.2.0/xe/lib/libsqora.so.11.1
```

B) Configure the Oracle DSN

Edit `/etc/odbc.ini` and add a Data Source Name (DSN) for your Oracle XE database.

```toml
[XE]
Driver          = Oracle ODBC driver for Oracle 11.2
ServerName      = //localhost:1521/xe
DSN             = XE
UserName        = SYSTEM
Password        = <your-password>
```

#### Step 5: Test the Oracle ODBC Connection

Use `isql` to test the connection and create a sample table in Oracle.

```sql
isql -v XE SYSTEM <your-password>

CREATE TABLE t1 (i INT);
INSERT INTO t1 (i) VALUES (1);
INSERT INTO t1 (i) VALUES (3);
INSERT INTO t1 (i) VALUES (5);
INSERT INTO t1 (i) VALUES (8);
SELECT i FROM t1;
```

You should see the rows `1, 3, 5, 8` returned.

#### Step 6: Configure and Test the MariaDB CONNECT Engine

A) Set Environment Variables for MariaDB

For the CONNECT engine to find the Oracle libraries, you must add the Oracle environment variables to MariaDB's startup script. Edit /etc/init.d/mysql.

```bash
sudo nano /etc/init.d/mysql
```

Immediately after `### END INIT INFO`, add the following block:

```bash
# Oracle Environment for MariaDB CONNECT Engine
export JAVA_HOME=/usr/lib/jvm/java-8-oracle 
export PATH=$JAVA_HOME/bin:$PATH 
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe 
export CLIENT_HOME=$ORACLE_HOME 
export ORACLE_SID=XE 
export NLS_LANG=`$ORACLE_HOME/bin/nls_lang.sh` 
export ORACLE_BASE=/u01/app/oracle 
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH 
export PATH=$ORACLE_HOME/bin:$PATH
```

B) Restart MariaDB and Test the Connection

```bash
sudo /etc/init.d/mysql restart
mysql -uroot -p
```

Once logged into the MariaDB client, run the following SQL commands:

```sql
CREATE DATABASE mdb;
USE mdb;
INSTALL SONAME 'ha_connect';
CREATE TABLE t1 ENGINE=CONNECT TABLE_TYPE=ODBC tabname='T1' CONNECTION='DSN=XE;UID=SYSTEM;PWD=<your-password>';

SELECT I FROM t1;
```

You should see the values `1, 3, 5, 8` retrieved from the Oracle table.

### Part 4: Connecting to MariaDB via JDBC

#### Step 1: Install the MariaDB JDBC Driver

1. Download the "MySQL Connector/J" from the MySQL or MariaDB website.
2. Extract the archive and copy the `.jar` file to a known location.

```bash
tar xvfz mysql-connector-java-5.0.8.tar.gz
cd mysql-connector-java-5.0.8/
sudo mkdir -p /usr/lib/jvm/java-8-oracle/lib/mariadb/
sudo cp -p mysql-connector-java-5.0.8-bin.jar /usr/lib/jvm/java-8-oracle/lib/mariadb/
```

#### Step 2: Configure SQL Developer

1. Launch SQL Developer: `sudo /opt/sqldeveloper/sqldeveloper.sh`
2. Go to Tools -> Preferences.
3. Expand Database and click on Third Party JDBC Drivers.
4. Click Add Entry... and navigate to the `.jar` file you copied: `/usr/lib/jvm/java-8-oracle/lib/mariadb/mysql-connector-java-5.0.8-bin.jar`.
5. Click OK to close the preferences.

#### Step 3: Connect to MariaDB

1. In SQL Developer, create a new connection.
2. Switch to the MySQL tab.
3. Enter the connection details:
   * Connection Name: `MariaDB via MySQL Conn`
   * Username: `root`
   * Password: `<your-root-password>`
   * Hostname: `localhost`
   * Port: `3306`
4. Click Test Connection. It should report `Status: Success`.
5. Save and connect. You can now run queries against your MariaDB server in the worksheet.

***

_This page is licensed: CC BY-SA / Gnu FDL_
