---
hidden: true
---

# System Troubleshooting MariaDB ColumnStore

### MariaDB ColumnStore alias commands

During the installation, these alias commands are defined and placed in the .bashrc file of the install user. 1.1 and later releases, the alias will reside in /etc/profile.d/columnstoreAlias.sh

This example is from a non-root install:

```
alias mcsmysql='/home/mariadb-user/mariadb/columnstore/mysql/bin/mysql --defaults-file=/home/mariadb-user/mariadb/columnstore/mysql/my.cnf -u root'
alias ma=/home/mariadb-user/mariadb/columnstore/bin/mcsadmin
alias mcsadmin=/home/mariadb-user/mariadb/columnstore/bin/mcsadmin
alias cpimport=/home/mariadb-user/mariadb/columnstore/bin/cpimport
alias home='cd /home/mariadb-user/mariadb/columnstore'
alias log='cd /var/log/mariadb/columnstore/'
alias dbrm='cd /home/mariadb-user/mariadb/columnstore/data1/systemFiles/dbrm'
alias module='cat /home/mariadb-user/mariadb/columnstore/local/module'

mcsmysql - Access the MariaDB ColumnStore MySQL Console
ma and mcsadmin - Access the MariaDB ColumnStore Admin Console
cpimport - short-cut to run the Bulk Load Process, cpimport
home - cd to MariaDB ColumnStore home directory
log - cd to MariaDB ColumnStore log directory
dbrm - cd to MariaDB ColumnStore DBRM file directory
module - outputs the MariaDB ColumnStore local mode name, like 'pm1'
```

### MariaDB ColumnStore Support Report tool

This tool can be executed by users, called "columnstoreSupport", that will generated a report that contains the log files and other system data that is used by MariaDB personnel to help diagnose system related issues and errors within the MariaDB ColumnStore Product.

Here is how to run it:

On a single server:

```
/usr/local/mariadb/columnstore/bin/columnstoreSupport -a -bl
```

On a multi-node combo server, run on pm1

```
/usr/local/mariadb/columnstore/bin/columnstoreSupport -a -bl -p 'user-password'
```

On a multi-node separate server, run on um1

```
/usr/local/mariadb/columnstore/bin/columnstoreSupport -a -bl -p 'user-password'
```

NOTE: If ssh-keys are setup, enter the work 'ssh' for user-password. If no ssh-keys, then enter the Unix User password that is used to ssh login to the system.

NOTE: If there is a MariaDB/MySQL root user password setup for the mysql console, you will need to add that password into the ColumnStores my.cnf file.

When password is not set in the my.cnf, this error will be reported:

```
NOTE: MariaDB Columnstore root user password is set
NOTE: No password provide on command line or found uncommented in my.cnf
```

Add this line to the my.cnf file

```
password='root-password'
```

Here is an example of it getting run the report that is generated:

```
/usr/local/mariadb/columnstore/bin/columnstoreSupport -a
Get software report data for pm1
Get config report data for pm1
Get log report data for pm1
Get log config data for pm1
Get hardware report data for pm1
Get resource report data for pm1
Get dbms report data for pm1

Columnstore Support Script Successfully completed, files located in columnstoreSupportReport.tar.gz
```

columnstoreSupportReport.tar.gz is what you would provide to MariaDB personnel or attach to a JIRA.

This is what the report consist of:

1. Compressed log files from each module : pm1\_logReport.tar.gz\
   a. This is the directory /var/log/mariadb/columnstore from pm1 which will contain:

* system logs for ColumnStore, debug, info, err, warning, and critical
* the alarm logs, alarm.log and activealarmLog
* UI command log, uiCommands.log, which are commands entered into\
  mcsadmin

2. Config report from each module: pm1\_configReport.txt. NOTE: on a single server\
   system, pm1 report will contain more configuration data. On a multi-node seperate\
   system um1 report will contain more data

* /etc/tstab
* Server processes - ps command info and top
* System network information
* System configuration information including storage
* System status information at the time the report was run
* System configuration file, Columnstore.xml

3. Hardware report for each module: pm1\_hardwareReport.txt

* OS version
* CPU information
* Memory information
* Storage mount information
* Ip address information, ifconfig

4. Resource report for each module: pm1\_resourceReport.txt

* Shared memory
* Disk usage
* DBRM files
* Active table locks
* BRM extent map

5. Software report for each module: pm1\_softwareReport.txt

* MariaDB ColumnStore software version

6. DBMR report, from the front-end modules: um1\_dbmsReport.txt

* MariaDB version
* System catalog and tables
* MariaDB Columnstore usernames
* MariaDB ColumnStore variables
* MariaDB ColumnStore configuration file, my.cnf
* List of active queries at the time the report was run

7. MariaDB ColumnStore MySQL log file: um1\_mysqllogReport.tar.gz

### MariaDB ColumnStore logging

MariaDB ColumnStore utilizes the install system logging tool, whether it's syslog, rsyslog, or syslog-ng.\
The logs are located in /var/log/mariadb/columnstore. There are these 5 logs:

* crit.log
* err.log
* warning.log
* info.log
* debug.log

log format:

timestamp hostname process name\[pid] time | session id | txn id | thread id | logging level subsystem\_id message

| log part           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| log part           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| timestamp          | Format mmm dd hh24:mm:ss                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| hostname           | hostname of the logging server                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| processname\[pid]: | The Name of the Process (example: ProcessMonitor) followed by the pid enclosed into \[]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| time               | execution time for this step in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| session id         | Session ID. Thread number in the processlist. If N/A than value is 0.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| txn id             | MariaDB Transaction ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| thread id          | Thread ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| logging level      | D = Debug I = Info W = Warning E = Error C = Critical                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| subsystem id       | 1=ddljoblist 2=ddlpackage 3=dmlpackage 4=execplan 5=joblist 6=resultset 7=mcsadmin 8=oamcpp 9=ServerMonitor 10=traphandler 11=alarmmanager 12=configcpp 13=loggingcpp 14=messageqcpp 15=DDLProc 16=ExeMgr 17=ProcessManager 18=ProcessMonitor 19=writeengine 20=DMLProc 21=dmlpackageproc 22=threadpool 23=ddlpackageproc 24=dbcon 25=DiskManager 26=RouteMsg 27=SQLBuffMgr 28=PrimProc 29=controllernode 30=workernode 31=messagequeue 32=writeengineserver 33=writeenginesplit 34=cpimport.bin 35=IDBFile |
| message            | logging message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

We also utilize the log rotate tool and by default we are configured to keep 7 days of log files. They are stored in /var/log/mariadb/columnstore/archive.

The MariaDB ColumnStore logrotate file is located in

/etc/logrotate.d/columnstore

Also in the /var/log/mariadb/columnstore directory, there are a few other logs that are kept:

* activeAlarms – List of active alarms currently set on the system
* alarm.log – list of all the alarms and associated clear alarms
* mcsadmin.log – list of the mcsadmin commands entered

The MariaDB ColumnStore process corefiles would be stored in /var/log/mariadb/columnstore/corefiles, that is if core file dumping is enabled on the system.

#### MariaDB ColumnStore log files and what goes in them

* Crit, err, and warning used to log problems by a MariaDB ColumnStore Process.
* Info will have logs showing high level actions that are going on in the system. During a stop/startsystem,\
  it will show the high level commands of the process/modules being stopped and started. The bulk-load (cpimport) tool logs is high level actions there also.
* Debug will have the lower level actions from the MariaDB ColumnStore Processes, which will include queries.

The MariaDB Server will be logged here.

MariaDB ColumnStore-MySQL logs are stored here:

```
/usr/local/mariadb/columnstore/mysql/db/’server-name’.err
```

NOTE: Other informational log files will be written to the log directory as well as the Temporary Directory from MariaDB ColumnStore process during certain operations. So you will see a few other logs show up in the log directory besides these.

Temporary Directory for root installs is located in /tmp/columnstore/tmp/filles/\
Temporary Directory for non-root installs is located in $HOME/.tmp

#### MariaDB ColumnStore log files and how to setup

The MariaDB ColumnStore log files setup is done as part of the post-install/postConfigure installation process. If some reason the MariaDB ColumnStore log files aren't being generated or the log-rotation is not working, then there might have been some install/setup error that occurred.

Run the following command to get the logging setup:

Root install:

```
/usr/local/mariadb/columnstore/bin/syslogSetup.sh install
```

Non-root install, run as root user. The below example is assuming 'mysql' as the non-root user.

```
export COLUMNSTORE_INSTALL_DIR=/home/mysql/mariadb/columnstore
export LD_LIBRARY_PATH=:/home/mysql/mariadb/columnstore/lib:/home/mysql/mariadb/columnstore/mysql/lib:/home/mysql/mariadb/columnstore/lib:/home/mysql/mariadb/columnstore/mysql/lib
/home/mysql/mariadb/columnstore/bin/syslogSetup.sh --installdir=/home/mysql/mariadb/columnstore --user=mysql install
```

To test the logs, run the following and check the directory

```
# mcsadmin getlogconfig

# ls -ltr /var/log/mariadb/columnstore

// want to see if any of these logs are now showing up

# ls -ltr
total 172
-rwxr-xr-x 1 syslog adm 398 Oct 12 18:27 warning.log
-rwxr-xr-x 1 syslog adm 398 Oct 12 18:27 err.log
-rwxrwxrwx 1 syslog adm 8100 Oct 12 18:27 info.log
-rwxrwxrwx 1 syslog adm 139975 Oct 12 18:27 debug.log
```

If so, then logging is now working...

#### Process STDOUT/STDERR logging

MariaDB ColumnStore Processes have built in STDOUT/STDERR logging that can be enabled. This could be used for additional debugging of issues. This is enabled on a Process by Process Level.\
Here is an example of how to enable and disable. In this example, locate the Process to enable, like DDLProc. Then enter the Process name and Module-type on the 'setprocessconfig' command.

NOTE: run from PM1

```
mcsadmin> getprocessconfig
getprocessconfig   Tue Sep 26 19:21:14 2017

Process Configuration

Process #1 Configuration information
ProcessName = ProcessMonitor
ModuleType = ChildExtOAMModule
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/ProcMon
BootLaunch = 0
LaunchID = 1
RunType = LOADSHARE
LogFile = off

Process #2 Configuration information
ProcessName = ProcessManager
ModuleType = ParentOAMModule
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/ProcMgr
BootLaunch = 1
LaunchID = 2
RunType = ACTIVE_STANDBY
LogFile = off

Process #3 Configuration information
ProcessName = DBRMControllerNode
ModuleType = ParentOAMModule
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/controllernode
ProcessArg1 = /home/mariadb-user/mariadb/columnstore/bin/controllernode
ProcessArg2 = fg
BootLaunch = 2
LaunchID = 4
DepModuleName1 = @
DepProcessName1 = ProcessManager
RunType = SIMPLEX
LogFile = off

Process #4 Configuration information
ProcessName = ServerMonitor
ModuleType = ChildOAMModule
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/ServerMonitor
ProcessArg1 = /home/mariadb-user/mariadb/columnstore/bin/ServerMonitor
BootLaunch = 2
LaunchID = 6
RunType = LOADSHARE
LogFile = off

Process #5 Configuration information
ProcessName = DBRMWorkerNode
ModuleType = ChildExtOAMModule
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/workernode
ProcessArg1 = /home/mariadb-user/mariadb/columnstore/bin/workernode
ProcessArg2 = DBRM_Worker
ProcessArg3 = fg
BootLaunch = 2
LaunchID = 7
RunType = LOADSHARE
LogFile = off

Process #6 Configuration information
ProcessName = DecomSvr
ModuleType = pm
ProcessLocation = //home/mariadb-user/mariadb/columnstore/bin/DecomSvr
BootLaunch = 2
LaunchID = 15
RunType = LOADSHARE
LogFile = off

Process #7 Configuration information
ProcessName = PrimProc
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/PrimProc
BootLaunch = 2
LaunchID = 20
RunType = LOADSHARE
LogFile = off

Process #8 Configuration information
ProcessName = ExeMgr
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/ExeMgr
BootLaunch = 2
LaunchID = 30
DepModuleName1 = pm*
DepProcessName1 = PrimProc
RunType = LOADSHARE
LogFile = off

Process #9 Configuration information
ProcessName = WriteEngineServer
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/WriteEngineServer
BootLaunch = 2
LaunchID = 40
RunType = LOADSHARE
LogFile = off

Process #10 Configuration information
ProcessName = DDLProc
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/DDLProc
BootLaunch = 2
LaunchID = 50
DepModuleName1 = pm*
DepProcessName1 = WriteEngineServer
DepModuleName2 = *
DepProcessName2 = DBRMWorkerNode
DepModuleName3 = *
DepProcessName3 = ExeMgr
RunType = SIMPLEX
LogFile = off

Process #11 Configuration information
ProcessName = DMLProc
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/bin/DMLProc
BootLaunch = 2
LaunchID = 51
DepModuleName1 = pm*
DepProcessName1 = WriteEngineServer
DepModuleName2 = *
DepProcessName2 = DBRMWorkerNode
DepModuleName3 = @
DepProcessName3 = DDLProc
RunType = SIMPLEX
LogFile = off

Process #12 Configuration information
ProcessName = mysqld
ModuleType = pm
ProcessLocation = /home/mariadb-user/mariadb/columnstore/mysql/libexec/mysqld
BootLaunch = 0
LaunchID = 100
RunType = LOADSHARE
LogFile = off

mcsadmin> setprocessconfig DDLProc pm LogFile on
setprocessconfig   Tue Sep 26 19:22:00 2017

   Successfully set LogFile = on

mcsadmin> shutdownsystem y
shutdownsystem   Tue Sep 26 19:23:59 2017

This command stops the processing of applications on all Modules within the MariaDB ColumnStore System

   Checking for active transactions

   Stopping System...
   Successful stop of System 

   Shutting Down System...
   Successful shutdown of System 

mcsadmin> startsystem
startsystem   Tue Sep 26 19:24:36 2017
startSystem command, 'columnstore' service is down, sending command to
start the 'columnstore' service on all modules


   System being started, please wait..................
   Successful start of System 

mcsadmin>
```

In the log directory, there will be the following 2 files. So all the STDOUT/STDERR from the process will be logged here

```
pwd
/var/log/mariadb/columnstore

ll DDLProc.*
-rw-r--r-- 1 mariadb-user mariadb-user  0 Sep 26 19:25 DDLProc.err
-rw-r--r-- 1 mariadb-user mariadb-user 34 Sep 26 19:25 DDLProc.out
```

To Disable, just set the LogFile setting back to off and do the shutdown/startsystem

```
setprocessconfig DDLProc pm LogFile off
```

### Crash trace files

MariaDB ColumnStore 1.0.13 / 1.1.3 onwards includes a special crash handler which will log details of a crash from the main UM and PM daemons. These can be found in:

```
/var/log/mariadb/columnstore/trace
```

The filenames will be in the form `<processName>.<processID>.log`. These are similar to the crash traces that can be found in the MariaDB server log files if MariaDB server crashes.

### Enable/Disable Core Files

Since core files are very large (1gb) and can take up a lot of disk space, Core File Generating for MariaDB ColumnStore platform processes is defaulted to disable.

The location of the MariaDB ColumnStore Process corefiles get placed here:

/var/log/mariadb/columnstore/corefiles/

You can redirect the location to another disk with more space by using a soft-link.

* Enable from pm1

```
# ma shutdownsystem
# /usr/local/mariadb/columnstore/bin/setConfig Installation CoreFileFlag y
# ma startsystem
```

* Disable from pm1

```
# ma shutdownsystem
# /usr/local/mariadb/columnstore/bin/setConfig Installation CoreFileFlag n
# ma startsystem
```

### MariaDB ColumnStore database files

The MariaDB ColumnStore has 3 sets of database files. These files are also always backed up and restored together as part of the backup and restore process.

* MariaDB ColumnStore-MySQL schemes - /usr/local/mariadb/columnstore/mysql/db/\*
* MariaDB ColumnStore Database - /usr/local/mariadb/columnstore/dataX/000.dir
* MariaDB ColumnStore DBRM files - /usr/local/mariadb/columnstore/data1/systemFiles/dbrm/\*

MariaDB ColumnStore Database: The X represents the DBroot ID #. DBroot is the file directory containing the meta-data. We generally assign 1 DBroot per Performance Module. This DBroot can be pointing to local disk storage area or mounted to external disk. So for a single-server setup, we would have ‘data1’ as the dbroot. If we had a system will 2 Performance modules, then we would have ‘data1’ on PM1 and ‘data2’ on PM2.

MariaDB ColumnStore DBRM files: This is where the Extent Map and Versioning files are located. These make up the DBRM files. There are 3 copies of the files that are keep, one is the current active set and the other 2 are the backup. The current active copy file name is located in this file:

```
/usr/local/mariadb/columnstore/data1/systemFiles/dbrm/BRM_saves_current
```

The Extent Map is loaded into shared memory on each of the nodes during the start-system process time. The version in shared memory on the PM1 node is the main copy. Changes are applied to that version in memory. Then changes are made to the disk version that only exist on PM1 disk storage and a copy of those changes are sent out to the other nodes and their memory copies are updated.

NOTE: The following utility can be used to dump the internal memory copy of the Extent Map `/usr/local/mariadb/columnstore/bin/editem` : there are a few options with this command, -i dumps a raw copy and -d dumps a formatted copy

### MariaDB ColumnStore utilities

Here are a few of the common utilities that are used to view and troubleshoot issues. All of these commands are located in /usr/local/mariadb/columnstore/bin/

These are utilizes to be used to view or set system variables. They should be run on the Active OAM Parent Module, which generally is the Performance Module #1.

* editem – used to view the Extent Map in internal memory, discussed in previous section
* configxml.sh – used to get and set parameters from the system config file, ColumnStore.xml
  * ./configxml.sh getconfig ExeMgr1 Port
  * ./configxml.sh setconfig ExeMgr1 Port 8601
* dbrmctl – used to display are view or change the DBRM status
  * Example, display the current the dbrm status
    * ./dbrmctl status
  * Example, the dbrm might be in a readonly state, this would unlock
    * ./dbrmctl resume

These are utilizes to be used to view or clear Database Table Locks. They should be run on the Active OAM Parent Module, which generally is the Performance Module #1.

* viewtablelock – will display what tables are locked. There might be times when a DML\
  command might fail and leave a table in a locked state. You can run this command to find\
  which tables are locked, and then use the ‘cleartablelock’ command
* cleartablelock – use to clear a table lock. As explained above, could be used to clear a lock on a table that was left set on a failed command

These are utilities that would be run on all nodes in the system

* clearShm – used to clear the shared internal memory, used at times after a system-shutdown command is do just to make sure the memory is cleared

### Tables locks and clearing

A Table lock might be left set due to come failure on processing a DML/DDL command. Normally this lock can be cleared with the utility mentioned above, cleartablelock. But in the case where it doesn't clear the lock, it can also be cleared by restarting the Active DMLProc on the system. This will cause DMLProc to perform the rollback processing that will clear any table locks. And as a third option when the first to doesn't work, there is a tablelock file that can be removed

**viewtablelock and cleartablelock**

Run viewtablelock to get the list of table locks:

```
# /usr/local/mariadb/columnstore/bin/viewtablelock
```

Run cleartablelock with the table lock ID shown in the viewtablelock

```
# /usr/local/mariadb/columnstore/bin/cleartablelock XX
```

**Restart DMLProc**

1. run command to get the Active DMLProc

```
# mcsadmin getsystemi
```

2. Run the follow command that will restart the DMLProc

```
# mcsadmin restartProcess DMLProc xxx (xxx is probably um1 or pm1, based on the system)
```

When the status of DMLProc goes to ACTIVE from BUSY\_INIT (meaning is performing rollbacks), then check to see if the lock still exist.

**delete the tablelock file**

If the previous 2 commands didn't work, you can delete the tablelock file if it exists

This is done from PM1:

```
# cd /usr/local/mariadb/columnstore/data1/systemFiles/dbrm
# rm -f tablelock    // if it exist
# mcsadmin restartSystem y
```

### Multi-node install problems and how to diagnose

Once you install the packages on the initial server, pm1, run post-install and postConfigure.

If it's failing in the remote server install section, go via the install logs in /tmp to see why the failure occurred. It could be related to these issues:

1. user password or ssh-keys not setup, failing to log in
2. Dependent package isn't installed on a remote server
3. Incompatible OS's between nodes, all have to be the same

If you get to the point where it says Starting system processes, but it seems to hang or not return.\
Here are some things to check:

1. Check the locale setting on all servers and make sure they are all the same
2. on pm1, create the alias if you haven't already
3. . /usr/local/mariadb/columnstore/bin/columnstoreAlias\
   then run following command and check the process status:
4. mcsadmin getsysteminfo\
   check if ProcMon is ACTIVE on all configured servers, if not, check the log files on the asscouiated\
   server to see what error ProcMon is reporting. Also make sure the ProcMgr is ACTIVE on pm1.

logs are located in:

/var/log/mariadb/columnstore

generally when ProcMon/ProcMgr isn't active, it's because one of these issues:

1. if external storage, an pm /etc/fstab isnt setup
2. message issue between the servers that is causing ProcMon's and ProcMgr to fail to communicate. Make sure all server firewalls are disable along with SElinux.

### Add Module install problems and how to diagnose

There are a number of reasons why an addModule command might fail, missing dependent packages, password or ssh key is not setup, etc. Here are some things to investigate when this 'mcsadmin' command does fail.

1. Check the log files on the local node where the command is running. Generally an log in the error, warning, or critical log will be reported when a failure occurs.
2. Depending on how far the addModule command got, another log will be generated in /tmp. Look for a log file with binary\_installer, user/performance\_installer. This will echo back the installer script the commands it runs, so it would flag an issue in there.
3. Also make sure you can log into the new server/instance from the local one. Not being able to log in would cause a failure.
4. Also depending on how far the command got, it might have added an entry in the system configuration file for the new module. So you will need to check that and if you were adding pm2 and it failed, then it shows up in the system configuration via the 'getsystemn'. You would then need to remove that module before trying the addModule command.
5. If your get the error return from the 'addModule' command if File Open error, that means it could locate the MariaDB ColumnStore rpm/deb/binary in the $HOME directory, i.e. /root for root user install. The logic takes the packages from here and pushes them to the new server.

### postConfigure install problems and how to diagnose

The installation script, postConfigure, is run at install and upgrade times. The first part of the script takes information from the user and setup the system configuration, which is updating the Columnstore.xml and the ProcessConfig.xml configuration files.

The second part of the script performs a remote install of all of the other servers in the system, which is for a multi-node install configuration. The installation of the remote nodes are done simultaneously and the remote install logs are placed in /tmp on 'pm1', i.e. "pm1\_installer.log". The actual log file name will be different based on if you are doing an rpm, debian, or binary install.\
So if postConfigure reports that a failure occurred during the remote server install phase, you can look at these logs in /tmp. The main reasons why this might fail:

1. ssh access to the remote node from pm1 failed, password or ssh setup issues
2. A missing dependency package on the remote node

The third part of postConfigure is the starting up of the system, which consist of starting up of the 'columnstore' service script on each node. If a failure happens during this time frame, do the following to help determine the failure:

1. first, you might need to run this script to get the 'mcsadmin' alias command defined

```
# . ./usr/local/mariadb/columnstore/bin/aliasColumnstore
```

2. get the system statuses

```
# mcsadmin getsystemi
```

3. Here are some things that can point to you why the system didn't come up:\
   a. Make sure that all ProcMon processes are active on all nodes. If they aren't, then here are some of the reasons why they might not be:\
   i. Firewall is enabled on the 'pm1' node are the installing node, check that.\
   ii. ProcMon might have run into another issues at startup, like failing to mount to an external disk.\
   So check the log files on the remote server where ProcMon failed to go ACTIVE.\
   b. If it reports a module status of FAILED, then check the log files from that module.
4. Also check the log files from the local 'pm1' module.

### startSystem problems and how to diagnose

So this is assuming that the system has made it successfully though a postConfigure install or upgrade. At some point, you might need to do a stop or shutdownsystem for some maintenance or some other reason. And then do the startsystem. If any failures occur with the startSystem command, you can check the following:

1. get the system statuses

```
# mcsadmin getsystemi
```

2. Here are some things that can point to you why the system didn't come up:\
   a. Make sure that all ProcMon processes are active on all nodes. If they aren't, then here are some of the reasons why they might not be:\
   i. Firewall is enabled on the 'pm1' node are the installing node, check that.\
   ii. ProcMon might have run into another issues at startup, like failing to mount to an external disk.\
   So check the log files on the remote server where ProcMon failed to go ACTIVE.\
   b. If any of the DBRM Processes, Controller or Worker nodes are in a FAILED state, the most likely reason for this the there is an issue with the DBRM files. These files are loaded from disk into shared-memory. This is load fails, it will mark the DBRM Process as FAILED. If this is the case, then please contact MariaDB Customer Support. The DBRM fails contain the Extent Map and other metadata related to the MariaDB Columnstore Database files.\
   c. If it reports a module status of FAILED, then check the log files from that module.
3. Also check the log files from the local 'pm1' module.

### System in DBRM Read-Only Mode

The System can go into DBRM Read-Only Mode due to these conditions, a failure while doing a DDL/DML command, network problem between servers where the DBRM could get distributed to the other servers from Performance Module 1, and some failover scenarios. It will be shown by the follow alarm. This alarm along with all critical alarms will be displayed when user logs into the Columnstore Admin Console 'mcsadmin'.

AlarmID = 31\
Brief Description = DBRM\_READ\_ONLY\
Alarm Severity = CRITICAL\
Time Issued = Wed Sep 13 14:32:37 2017\
Reporting Module = pm1\
Reporting Process = DBRMControllerNode\
Reported Device = System

If the system ever gets into DBRM Read-Only Mode, it is best resolved by do a restart system form the 'pm1' module:

```
# mcsadmin restartsystem y
```

DBRM Read-Only Mode means that changes cannot be made to the MariaDB ColumnStore Database while it is in this state. Queries can still be processed.

### Non-Root System, PrimProc Process fails to startup

For non-root systems, the user file settings is required to be set as shown in the Preparing Guide. So if you have a Non-Root install where it fails to start and the 'mcsadmin getsystemi' shows that the PrimProc Process is in a failed state. Double check the user file settings on each node.

preparing-for-columnstore-installation-10x.md

### Create table error - Error occurred when calling system catalog

If you are having a problem creating a table after an new install is performed and you get the error "Error occurred when calling system catalog", chances are the System Catalog didnt get created by postConfigure. The call to create happens at the very end of postConfigure, so it is possible that postConfigure didn't successfully complete or there was an error when trying to create it.

Run the following command from PM1 to create the System Catalog:

/usr/local/mariadb/columnstore/bin/dbbuilder 7

NOTE: This example is assuming it's a root user install

### Missing MariaDB ColumnStore Function or Engine

After new Install or Upgrade, a MariaDB ColumnStore Function or Engine type might be missing from the MariaDB Database. If this occurs, you can run the following procedure on each of the UMs or PMs with UM front-end modules on the system. This procedure should get all of the Functions and Engines created.

From Performance Module #1

```
mcsadmin shutdownsystem y
```

On all User Modules or Performance Modules with mysqld installed. This example assumes a root install in /usr/local/, run the following scripts

```
/usr/local/mariadb/columnstore/bin/post-mysqld-install
/usr/local/mariadb/columnstore/bin/post-mysql-install
```

From Performance Module #1

```
mcsadmin startsystem y
```

### Truncate Table Failure with error of Columnstore engine ID different

This issue has been reported after a system was upgraded from 1.1.x to 1.2.x versions of MariaDB ColumnStore. If the truncate error occurs with the Columnstore engine ID being different, then the existing table would need to be dropped and recreated as a fix.

### MariaDB ColumnStore Process Restarting due to Allocating to much memory

In the 1.2.2 and earlier releases, MariaDB ColumnStore Process like PrimProc, ExeMgr, or WriteEngineService can automatically restart due to over allocation of memory. PrimProc and WriteEngineService run on the Performance Module. ExeMgr runs on the User Module.

This can be caused by a few situations like these:

* Doing very large aggregates
* Spike memory usage when dealing with large result sets to buffer the rowgroups

This is a log that is reported for this issue. This example shows PrimProc using 95% of memory.\
The next Log is reporting that it is restarting.

Feb 29 16:22:34 ip-192-168-1-112 ServerMonitor\[1951]: 39.784588 |0|0|0| I 09 CAL0000: Memory Usage for Process: PrimProc : Memory Used 12296930 : % Used 95\
Feb 29 16:23:00 ip-192-168-1-112 ProcessMonitor\[1578]: 05.478658 |0|0|0| C 18 CAL0000: \*\*\*\*\*MariaDB ColumnStore Process Restarting: PrimProc, old PID = 5667

When this issue is occurring on a system running 1.2.2 or earlier, this is a work-around that can be applied.

IMPORTANT: it is recommenced that you check with MariaDB ColumnStore support first on if this change should be made so it can be confirmed that this is the best work-around.

Work-around Process:

```
On pm1

# mcsadmin shutdownsystem y

So this will need to be done on all nodes, both User Modules and Performance Modules

1. install jemalloc package

Install jemalloc package(libjemalloc1 for Ubuntu 18, Centos 7 provides the jemalloc package via EPEL repository). After you install the package, find jemalloc shared object file path(LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.1 in Ubuntu 18)

2. Edit mariadb/columnstore/bin/run.sh

Then edit $install_dir/bin/run.sh using the patch. Please note that libjemalloc.so path must be changed according with your distribution.

--- /run.sh 2019-01-31 05:07:19.473718632 +0000
+++ /usr/local/mariadb/columnstore/bin/run.sh 2019-01-31 05:07:34.057051852 +0000
@@ -49,7 +49,7 @@
fi

while [ $keep_going -ne 0 ]; do
- $exename $args
+ LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.1 $exename $args
if [ -e ${lopt}/StopColumnstore ]; then
exit 0
fi

On pm1
<<code>>
# mcsadmin startsystem y
```

### Error in forking cpimport.bin (errno-12); Cannot allocate memory

This Error is an indication that ExeMgr on the User Module doesnt have enough local memory to run the Bulk Load Process cpimport.bin. So check for Process Memory allocation by other processes on the User Module when this error gets reported.

Here is one example of when this problem has been seen. The setting of innodb\_buffer\_pool\_size in my.cnf is set too high. In general, it shouldn't be set any higher than 50GB or 25% of the total memory.

### How to Switch Primary Master User Module

The commands below will show how to make a different User Module the Master MySQL replication module.\
There are some cases where User Module #2 make have become the Master during a failover scenario or some other case and you want to make User Module #1 the Master once again. These are the commands to do this.

First, check the System Status with the following command to see whether User Module #1 is disabled or not:

On pm1

```
# mcsadmin getsysteminfo
```

If User Module #1 is disabled, run to enable it:

```
# mcsadmin altersystem-enablemodule um1 y
```

Now run the commands to get User Module #1 as the Master. This is assuming User Module #2 is the current the Master:

```
# mcsadmin altersystem-disablemodule um2 y
# mcsadmin altersystem-enablemodule um2 y
```

### How to Recover when system when DBROOT is incorrectly assigned or other Configuration problem

There are times when the system gets into a state where it will not successfully Start due to a configuration problem. And since it will not start, the user can't get it to the point to where it can be fixed via 'mcsadmin'. So when that happen's, they the user will need to run 'postConfigure' to correct the issue.

Here is a couple of examples of a configuration issue that could cause this situation.

1. DBROOT 1 get reassigned to a different PM than PM1 when the system only has local storage, meaning DBOOT 1 is only on PM1.
2. UM or PM is disabled and the user wants to get it enabled.

Here is the process on how to recover. Run from PM1

```
# mcsadmin shutdownsystem y
```

Run 'postConfigure' based on the type of install it is, root or non root. Command line arguments will be different between the two. This example shows for a root install.

```
# /usr/local/mariadb/columnstore/bin/postConfigure

// if ask to use old configuration, answer n
// If you get to the Module that is disabled and you want enabled, answer 'y' to the enable module prompt
// on each of the PM DBROOT prompts, enter the DBOOT number that goes to the PM
// When it completes the configuration part and ask for ssh password, enter 'exit' to exit postConfigure

# mcsadmin startsystem
```

### Query failure MessageQueueClient :: setup (): unknown name or service

Due to a known issue in MariaDB Columnstore 1.2.5 and earlier, if a User Module or a Performance Module on a combined server is removed, the ColumnStore.xml entry for the ExeMgr setting gets set to "unassigned".\
This setting will cause queries to fail especially when running multiple queries in parallel.

The work-around fix is to delete the ExeMgr entry from the Columnstore.xml file.

```
<ExeMgr8>
		<IPAddr>unassigned</IPAddr>
		<Port>8601</Port>
		<Module>unassigned</Module>
	</ExeMgr8>
```

### Replication Data out-of-sync causing mysqld to not start and the System to not startup.

In the case where the system fails to startup or the MariaDB ColumnStore server (mysqld) fails to startup and it isreporting an replication error on Drop, Rename, Move Table or View, this could mean that the Binary Logs on the Module, usually a Slave User Module are out of sync with the Database. An example would be when mysqld startups on User Module #2, a slave module, it will go through the Replication bin-logs and run commands to capture up with the Master DB. If it tried to Drop a Table or View that doesn't exist in the Slave Database, it will reported an error and shutdown. This is an indication that the Replication and maybe the Data itself is out-of-sync between the Master and the slave Modules, usually UM1 and UM2. It resolve the issue to where the UM2 slave mysqld will run, the following procedure needs to be execute to get the UMs back in-sync.

UM1: log into mcsmysql and purge the bin-logs providing todays date

```
mcsmysql
sql > PURGE BINARY LOGS BEFORE '2013-04-21';
```

UM2: move the bin-log and relay-logs to a backup directory. Can delete, but best ti move instead

```
cd ../mariadb/columnstore/mysql/db

# mv mysql-bin.* /tmp/.
# mv relay-bin.* /tmp/.
```

Compare the InnoDB file (ibdata1) on UM1 to UM2 to make sure that file is insync. If it is different between the 2 UMs, then scp the one from UM1 to UM2.\
XXX.XXX.XXX.XXX is UM1 IP Address.

ON UM2:

```
mv ibdata1 /tmp/.

# scp XXX.XXX.XXX.XXX:/usr/local/mariadb/columnstore/mysqld/db/ibdata1 .
```

At this point, lets try to restart the system

FROM PM1:

```
# mcsadmin
> shutdownSystem y
> startsystem
```

### enableMySQLReplication failure

The Front-end Replication can be disabled and enabled via the 'mcsadmin' console. If the Replication stopped working between the User Modules, the user can run the enableMySQLReplication to get it setup and working.

```
# mcsadmin
> enableMySQLReplication
Enter the 'User' Password or 'ssh' if configured with ssh-keys
Please enter: ssh
```

But in the case when this command fails, here is what to do to debug why it failed

```
# mcsadmin
> enableMySQLReplication
Enter the 'User' Password or 'ssh' if configured with ssh-keys
Please enter: ssh

**** enableRep Failed : API Failure return in enableMySQLRep API
```

On User Module #1:

1. Check the Columnstore log files to see which step failed
2. There are also additional log files that scripts will update providing additional information. They are located on UM1 in /tmp/columnstore\_tmp\_files for root install and .tmp in the non-root user home directory.

### Problem Dropping table or Creating table an existing table

Sometimes if the Table information between the front-end and the back-end get out-of-sync, the following errors will be reported not allowing the customer to drop or create the table

```
DROP TABLE TABLE1;
Error Code: 1815. Internal error: CAL0009: Drop table failed due to  IDB-2006: 'TABLE1' does not exist in Columnstore.
```

```
CREATE TABLE `TABLE1` (   `cover_key` int(10) unsigned DEFAULT NULL,   `count_num` bigint(20) unsigned DEFAULT NULL ) ENGINE=Columnstore DEFAULT CHARSET=latin1;
Error Code: 1050. Table 'TABLE1' already exists
```

This problem can be cleaned up by Dropping the table with RESTRICT option.

```
DROP TABLE TABLE1 RESTRICT;
```

Then the customer should be able to create the table at this point.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
