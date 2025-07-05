# ColumnStore Redistribute Data

## Introduction

When new PM nodes are added to a running instance it may be desirable to redistribute the data in current nodes across all of the nodes. This is not strictly required as ongoing data ingestion will prioritize the new empty nodes for data loading to rebalance the system.

An important point is that the operation works at Partition granularity, so a minimal data set is 64M rows in a table for this to run.

## Usage

A command redistributeData is available in the admin console to initiate a data distribution:

```
mcsadmin> redistributeData start
redistributedata   Tue Dec 13 04:42:31 2016
redistributeData START
Source dbroots: 1 2
Destination dbroots: 1 2

WriteEngineServer returned status 1: Cleared.
WriteEngineServer returned status 2: Redistribute is started.
```

The command has 3 possible options:

* Start : start a new redistribution to redistribute data equally amongst the current set of DBRoots in the system.
* Stop : abort a redistribution leaving the system in a usable state.
* Status : return status information on an active redistribution.

The start command can take an option of Remove. The Start Remove option is used to remove all data from the enumerated list of dbroots and redistribute the data to the remaining dbroots. This should be done before taking a dbroot out of service in order to preserve the data on that dbroot. The dbroot list is a space delimited list of integers representing the dbroots to be emptied.

As mentioned above, the operation works at partition granularity, which means that a minimal move is 64 million rows. Any table smaller than that will not be redistributed and there may be as much as one full Partition difference in the resulting balance. The redistribute logic does not currently consolidate individually deleted records.

Redistribute can take a long time. During this time, it is required that all data manipulation including bulk inserts are suspended. SuspendDatabaseWrites must be called before redistributedata and ResumeDatabaseWrites should be called when the redistribution is complete.

If "redistributeData stop" is called, all processing stops where it's at, but in a usable state. "redistributeData status" can be used to see how much has been done. A further "redistributeData start" will start over using the new state of the system. This may lead to a less optimal distribution, so stop-start sequences aren't recommended.

While the system is working, "redistributeData status" can be called to see what's happening. a -r option can be used on the status command line to repeat the call and act as a monitor.

To see how much data resides on any given DBRoot for a table, you can use a query like:

```
select count(*) from <table> where idbdbroot(<any column>)=<dbrootnum>;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
