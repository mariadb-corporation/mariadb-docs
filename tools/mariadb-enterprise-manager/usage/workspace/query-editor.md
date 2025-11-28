# Query Editor

The Query Editor is a powerful, integrated environment for database developers and administrators. It provides a comprehensive set of tools for writing and debugging SQL and analyzing query results, all from a single interface.

This procedure outlines the steps required to access and utilize the Query Editor within the Workspace section of Enterprise Manager UI. 

1.  From the main Workspace screen, click the "Run Queries" card.\


    <figure><img src="../../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>
2.  In the "Connect to..." dialog, select your target server, enter your credentials, and click Connect.\


    <figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
3.  Upon successful connection, the main [Query Editor worksheet](broken-reference) will appear, ready for you to begin.\


    <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Query Editor Worksheet

The Query Editor Workspace is organized around a flexible, multi-tabbed interface designed for parallel work. At the top level, **Worksheet tabs** represent your connections to different database servers. Within each worksheet, you can open multiple **Query Tabs**, allowing you to write and execute several independent SQL statements without losing your context.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### SQL Code Management Features

These features are designed to make writing and managing SQL code efficient and intuitive.

#### **SQL Editor**

Write, run, and debug SQL statements. The editor supports executing queries in parallel across multiple **Query Tabs**, allowing you to work on different tasks or connect to different servers simultaneously within isolated sessions.

#### **SQL Code Completion**

Speed up query authoring and minimize syntax errors with context-sensitive suggestions. As you type, the editor offers relevant SQL keywords, functions, and objects (like tables and columns) from the currently selected database schema.

#### **SQL Code Formatter**

Improve readability and maintain consistent coding standards by automatically formatting your SQL code. Access this feature via the editor's context menu or command palette (`F1`).

#### **SQL Syntax Highlighting**

Enhance code clarity with color syntax highlighting. Different parts of your SQL statements (keywords, strings, comments) are displayed in distinct colors, making queries easier to scan and debug.

#### **SQL Snippets**

Save frequently used SQL code blocks for quick reuse across sessions. Press `CTRL+D` (or `CMD+D` on Mac) to save the current content of the editor as a snippet.

#### **SQL History**

Keep track of every query executed within the Workspace. The **History** tab provides a running log, allowing you to quickly find, review, and re-execute previous commands.

#### **Multiple Connections**

Define and manage connections to various database servers (e.g., development, testing, production). Each connection opens in its own top-level **Worksheet tab**, within which you can open multiple **Query Tabs**.

#### **Open/Edit/Save SQL Files**

Load existing SQL scripts from your local machine into the editor, make changes, and save them back without leaving the workspace.

### Data Management and Analysis Features

These features help you interact with and understand the results of your queries.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### **Export Result Sets**

Easily share or archive query results. You can export data grids directly into common formats like `CSV`, `JSON`, or as `SQL INSERT` statements.

{% stepper %}
{% step %}
### From results tab, click Export Results

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### From Export results window, make the selection.

<figure><img src="../../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

| Setting                  | Description                                                                                                              |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| File name                | The name for the downloaded export file. A default name with the current date is usually suggested.                      |
| Fields to export         | Allows you to select which columns from the query result set to include in the export.                                   |
| File format              | Choose the output format: `CSV`, `SQL`, or `JSON`.                                                                       |
| _CSV Options_            |                                                                                                                          |
|     Fields terminated by | The character used to separate values (e.g., `,` or `\t`).                                                               |
|     Lines terminated by  | The character indicating the end of a row (e.g., `\n`).                                                                  |
|     NULL replaced by     | How `NULL` values should be represented (e.g., `\N`).                                                                    |
|     With Headers         | Checkbox to include column names as the first row.                                                                       |
| _SQL Options_            |                                                                                                                          |
|     Export option        | Choose whether to export `Both structure and data`, `Data only` (INSERT statements), or `Structure only` (CREATE TABLE). |
| _JSON Options_           | None                                                                                                                     |
{% endstep %}

{% step %}
### Click Import

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

#### **Display multiple Result Sets**

When executing a script with multiple `SELECT` statements, view each result set in its own dedicated grid within the Results panel for easy comparison.

#### **Vertical Results Mode**

Improve readability for tables with many columns by displaying results in a vertical, record-by-record format.

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

#### **Result Set Limits**

Control the number of rows returned by `SELECT` statements (default: 10,000). This safety feature keeps queries responsive and can be adjusted per role.

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

#### **Result Visualizations**

Gain quick insights from your data by visualizing query results directly within the Workspace as simple **line, bar, or scatter charts**.

#### **Grid Operations**

Interact directly with the data displayed in the Results grid. Perform actions like **searching** for specific values, **filtering** rows, **grouping** data, and customizing column visibility without writing additional SQL.

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
