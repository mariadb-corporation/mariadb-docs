# Using MaxGUI Tutorial

* [Using MaxGUI Tutorial](mariadb-maxscale-2302-using-maxgui-tutorial.md#using-maxgui-tutorial)
* [Introduction](mariadb-maxscale-2302-using-maxgui-tutorial.md#introduction)
* [Dashboard](mariadb-maxscale-2302-using-maxgui-tutorial.md#dashboard)
  * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation)
  * [Create a new MaxScale object](mariadb-maxscale-2302-using-maxgui-tutorial.md#create-a-new-maxscale-object)
  * [View Replication Status](mariadb-maxscale-2302-using-maxgui-tutorial.md#view-replication-status)
  * [How to kill a session](mariadb-maxscale-2302-using-maxgui-tutorial.md#how-to-kill-a-session)
    * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_1)
* [Detail](mariadb-maxscale-2302-using-maxgui-tutorial.md#detail)
  * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_2)
* [Visualization](mariadb-maxscale-2302-using-maxgui-tutorial.md#visualization)
  * [Configuration](mariadb-maxscale-2302-using-maxgui-tutorial.md#configuration)
    * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_3)
  * [Clusters](mariadb-maxscale-2302-using-maxgui-tutorial.md#clusters)
    * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_4)
* [Settings](mariadb-maxscale-2302-using-maxgui-tutorial.md#settings)
  * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_5)
* [Logs Archive](mariadb-maxscale-2302-using-maxgui-tutorial.md#logs-archive)
  * [Annotation](mariadb-maxscale-2302-using-maxgui-tutorial.md#annotation_6)
* [Workspace](mariadb-maxscale-2302-using-maxgui-tutorial.md#workspace)
  * [Run Queries](mariadb-maxscale-2302-using-maxgui-tutorial.md#run-queries)
    * [Query Editor worksheet](mariadb-maxscale-2302-using-maxgui-tutorial.md#query-editor-worksheet)
      * [Create a new connection](mariadb-maxscale-2302-using-maxgui-tutorial.md#create-a-new-connection)
      * [Schemas objects sidebar](mariadb-maxscale-2302-using-maxgui-tutorial.md#schemas-objects-sidebar)
        * [Set the current database](mariadb-maxscale-2302-using-maxgui-tutorial.md#set-the-current-database)
        * [Preview table data of the top 1000 rows](mariadb-maxscale-2302-using-maxgui-tutorial.md#preview-table-data-of-the-top-1000-rows)
        * [Describe table](mariadb-maxscale-2302-using-maxgui-tutorial.md#describe-table)
        * [Alter/Drop/Truncate table](mariadb-maxscale-2302-using-maxgui-tutorial.md#alterdroptruncate-table)
        * [Quickly insert an object into the editor](mariadb-maxscale-2302-using-maxgui-tutorial.md#quickly-insert-an-object-into-the-editor)
      * [Editor](mariadb-maxscale-2302-using-maxgui-tutorial.md#editor)
      * [Re-execute old queries](mariadb-maxscale-2302-using-maxgui-tutorial.md#re-execute-old-queries)
      * [Create query snippet](mariadb-maxscale-2302-using-maxgui-tutorial.md#create-query-snippet)
  * [Data Migration](mariadb-maxscale-2302-using-maxgui-tutorial.md#data-migration)
    * [Data Migration worksheet](mariadb-maxscale-2302-using-maxgui-tutorial.md#data-migration-worksheet)
      * [Connections](mariadb-maxscale-2302-using-maxgui-tutorial.md#connections)
      * [Objects Selection](mariadb-maxscale-2302-using-maxgui-tutorial.md#objects-selection)
      * [Migration](mariadb-maxscale-2302-using-maxgui-tutorial.md#migration)
      * [Migration report](mariadb-maxscale-2302-using-maxgui-tutorial.md#migration-report)

## Introduction

This tutorial is an overview of what the MaxGUI offers as an alternative\
solution to [MaxCtrl](../mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl.md).

## Dashboard

![](../../../../.gitbook/assets/MaxGUI-dashboard.png.png)

### Annotation

1. [MaxScale object](../mariadb-maxscale-23-02-getting-started/mariadb-maxscale-2302-mariadb-maxscale-configuration-guide.md#objects). i.e.\
   Service, Server, Monitor, Filter, and Listener (Clicking on it will navigate\
   to its detail page)
2. Create a new MaxScale object.
3. Dashboard Tab Navigation.
4. Search Input. This can be used as a quick way to search for a keyword in\
   tables.
5. Dashboard graphs. Refresh interval is 10 seconds.

* SESSIONS graph illustrates the total number of current sessions.
* CONNECTIONS graph shows servers current connections.
* LOAD graph shows the last second load of thread.

1. Logout of the app.
2. Sidebar navigation menu. Access to the following pages: Dashboard,\
   Visualization, Settings, Logs Archive, Query Editor

### Create a new MaxScale object

Clicking on the _Create New_ button (Annotation 2) to open a dialog for creating\
a new object.

### View Replication Status

The replication status of a server monitored by [MariaDB-Monitor](../mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md) can be viewed by mousing over\
the server name. A tooltip will be displayed with the following information:\
replication\_state, seconds\_behind\_master, slave\_io\_running, slave\_sql\_running.

### How to kill a session

A session can be killed easily on the "Current Sessions" list which can be\
found on the [Dashboard](mariadb-maxscale-2302-using-maxgui-tutorial.md#dashboard), Server detail, and Service detail page.

![](../../../../.gitbook/assets/MaxGUI-kill-session.png.png)

#### Annotation

1. Kill session button. This button is shown on the mouse hover.
2. Confirm killing the session dialog.

## Detail

This page shows information on each MaxScale object and allow to edit its\
parameter, relationships and perform other manipulation operations. Most of the\
control buttons will be shown on the mouse hover. Below is a screenshot of a\
Monitor Detail page, other Detail pages also have a similar layout structure so\
this is used for illustration purpose.

![](../../../../.gitbook/assets/MaxGUI-detail.png.png)

### Annotation

1. Settings option. Clicking on the gear icon will show icons allowing to do\
   different operations depending on the type of the Detail page.

* Monitor Detail page, there are icons to Stop, Start, and Destroy monitor.
* Service Detail page, there are icons to Stop, Start, and Destroy service.
* Server Detail page, there are icons to Set maintenance mode, Clear server\
  state, Drain and Delete server.
* Filter and Listener Detail page, there is a delete icon to delete the\
  object.

1. Switchover button. This button is shown on the mouse hover allowing to\
   swap the running primary server with a designated secondary server.
2. Edit parameters button. This button is shown on the mouse hover allowing\
   to edit the MaxScale object's parameter. Clicking on it will enable editable\
   mode on the table. After finishing editing the parameters, simply click the\
   Done Editing button.
3. A Detail page has tables showing "Relationship" between other MaxScale\
   object. This "unlink" icon is shown on the mouse hover allowing to\
   remove the relationship between two objects.
4. This button is used to link other MaxScale objects to the relationship.

## Visualization

This page visualizes MaxScale configuration and clusters.

### Configuration

This page visualizes MaxScale configuration as shown in the figure below.

![](../../../../.gitbook/assets/MaxGUI-config-visualization.png.png)

#### Annotation

1. A MaxScale object (a node graph). The position of the node in the graph can\
   be changed by dragging and dropping it.
2. Anchor link. The detail page of each MaxScale object can be accessed by\
   clicking on the name of the node.
3. Filter visualization button. By default, if the number of filters used by a\
   service is larger than 3, filter nodes aren't visualized as shown in the\
   figure. Clicking this button will visualize them.
4. Hide filter visualization button.
5. Refresh rate dropdown. The frequency with which the data is refreshed.
6. Create a new MaxScale object button.

### Clusters

This page shows all monitor clusters using [mariadbmon](../mariadb-maxscale-23-02-monitors/mariadb-maxscale-2302-mariadb-monitor.md) module in a card-like view.\
Clicking on the card will visualize the cluster into a tree graph as shown in\
the figure below.

![](../../../../.gitbook/assets/MaxGUI-cluster-visualization.png.png)

#### Annotation

1. Drag a secondary server on top of a primary server to promote the secondary\
   server as the new primary server.
2. Server manipulation operations button. Showing a dropdown with the following\
   operations:

* Set maintenance mode: Setting a server to a maintenance mode.
* Clear server state: Clear current server state.
* Drain server: Drain the server of connections.

1. Quick access to query editor button. Opening the `Query Editor` page for\
   this server. If the connection is already created for that server, it'll use\
   it. Otherwise, it creates a blank worksheet and shows a connection dialog to\
   connect to that server.
2. Carousel navigation button. Viewing more information about the server in the\
   next slide.
3. Collapse the carousel.
4. Anchor link of the server. Opening the detail page of the server in a new\
   tab.
5. Collapse its children nodes.
6. Rejoin node. When the `auto_rejoin` parameter is disabled, the node can be\
   manually rejoined by dragging it on top of the primary server.
7. Monitor manipulation operations button. Showing a dropdown with the\
   following operations:

* Stop monitor.
* Start monitor.
* Reset Replication.
* Release Locks.
* Master failover. Manually performing a primary failover. This option is\
  visible only when the `auto_failover` parameter is disabled.

1. Refresh rate dropdown. The frequency with which the data is refreshed.
2. Create a new MaxScale object button.

## Settings

This page shows and allows editing of MaxScale parameters.

![](../../../../.gitbook/assets/MaxGUI-settings.png.png)

### Annotation

1. Edit parameters button. This button is shown on the mouse hover allowing\
   to edit the MaxScale parameter. Clicking on it will enable editable mode on\
   the table..
2. Editable parameters are visible as it's illustrated in the screenshot.
3. After finishing editing the parameters, simply click the Done Editing\
   button.

## Logs Archive

This page show real-time MaxScale logs with filter options.

![](../../../../.gitbook/assets/MaxGUI-logs-archive.png.png)

### Annotation

1. Filter by dropdown. All logs types are selected to be shown by default
2. Uncheck the box to disable showing a particular log type.

## Workspace

On this page, you may add numerous worksheets, each of which can be used for either "Run queries" or "Data migration".

![](../../../../.gitbook/assets/MaxGUI-workspace.png.png)

### Run Queries

Clicking on the "Run Queries" card will pop-up a dialog, providing options\
to establish a connection to different MaxScale object types, including\
"Listener, Server, Service".

The Query Editor worksheet will be rendered in the active worksheet after correctly connecting.

#### Query Editor worksheet

There are various features in the Query Editor worksheet, the most notable ones are listed below.

![](../../../../.gitbook/assets/MaxGUI-workspace-query-editor.png.png)

**Create a new connection**

If the connection of the Query Editor expires, or if you wish to make\
a new connection for the active worksheet, simply clicking on the button\
located on the right side of the query tabs navigation bar which features a\
server icon and an active connection name as a label. This will open the\
connection dialog and allow you to create a new connection.

**Schemas objects sidebar**

**Set the current database**

There are two ways to set the current database:

* Double-click on the name of the database.
* Right-click on the name of the database to show the context menu, then select\
  the `Use database` option.

**Preview table data of the top 1000 rows**

There are two ways to preview data of a table:

* Click on the name of the table.
* Right-click on the name of the table to show the context menu, then select\
  the `Preview Data (top 1000)` option.

**Describe table**

Right-click on the name of the table to show the context menu, then select the`View Details` option.

**Alter/Drop/Truncate table**

Right-click on the name of the table to show the context menu, then select the\
desired option.

**Quickly insert an object into the editor**

There are two ways to quickly insert an object to the editor:

* Drag the object and drop it in the desire position in the editor.
* Right-click on the object to show the context menu, then mouse\
  hover the `Place to Editor` option and select the desired insert option.

**Editor**

The editor is powered by [Monaco editor](https://microsoft.github.io/monaco-editor/), therefore, its features are similar to those of\
Visual Studio Code.

To see the command palette, press F1 while the cursor is active on the editor.

The editor also comes with various options to assist your querying tasks. To see\
available options, right-click on the editor to show the context menu.

**Re-execute old queries**

Every executed query will be saved in the browser's storage (IndexedDB).\
Query history can be seen in the `History/Snippets` tab.\
To re-execute a query, follow the same step to [insert an object into the editor](mariadb-maxscale-2302-using-maxgui-tutorial.md#quickly-insert-an-object-into-the-editor)\
and click the execute query button in the editor.

**Create query snippet**

Press CTRL/CMD + D to save the current SQL in the editor to the snippets storage.\
A snippet is created with a prefix keyword, so when that keyword is typed in\
the editor, it will be suggested in the "code completion" menu.

### Data Migration

Clicking on the "Data Migration" card will pop-up a dialog, providing an option\
to name the task. The Data Migration worksheet will be rendered in the active\
worksheet after clicking the `Create` button in the dialog.

#### Data Migration worksheet

MaxScale uses ODBC for extracting and loading from the data source to a server\
in MaxScale. Before starting a migration, ensure that you have set up the\
necessary configurations on the MaxScale server. Instruction can be found [here](../mariadb-maxscale-23-02-rest-api/mariadb-maxscale-2302-sql-resource.md#prepare-etl-operation)\
and limitations [here](../mariadb-maxscale-23-02-about/mariadb-maxscale-2302-limitations-and-known-issues-within-mariadb-maxscale.md#etl-limitations).

**Connections**

![](../../../../.gitbook/assets/MaxGUI-workspace-data-migration-set-up-connections.png.png)

Source connection shows the most common parameter inputs for creating\
an ODBC connection. For extra parameters, enable the `Advanced` mode\
to manually edit the `Connection String` input.

After successfully connected to both source and destination servers,\
click on the `Select objects to migrate` to navigate to the next stage.

**Objects Selection**

![](../../../../.gitbook/assets/MaxGUI-workspace-data-migration-objects-selection.png.png)

Select the objects you wish to migrate to the MariaDB server.

After selecting the desired objects, click on the `Prepare Migration Script` to\
navigate to the next stage. The migration scripts will be generated\
differently based on the value selected for the `Create mode` input. Hover over\
the question icon for additional information on the modes.

**Migration**

![](../../../../.gitbook/assets/MaxGUI-workspace-data-migration-migration-script.png.png)

As shown in the screenshot, you can quickly modify the script for each object\
by selecting the corresponding object in the table and using the editors on the\
right-hand side to make any necessary changes.

After clicking the `Start Migration` button, the script for each object will be\
executed in parallel.

**Migration report**

![](../../../../.gitbook/assets/MaxGUI-workspace-data-migration-migration-report.png.png)

If errors are reported for certain objects, review the output messages and\
adjust the script accordingly. Then, click the `Manage` button and select `Restart`.

To migrate additional objects, click the `Manage` button and select`Migrate other objects`. Doing so will replace the current migration\
report for the current object with a new one.

To retain the report and terminate open connections after migration, click the`Manage` button, then select `Disconnect`, and finally delete the worksheet.

Deleting the worksheet will not delete the migration task. To clean-up\
everything after migration, click the `Manage` button, then select`Delete`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
