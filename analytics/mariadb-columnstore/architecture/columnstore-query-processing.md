# ColumnStore Query Processing

Clients issue a query to the MariaDB Server, which has the ColumnStore storage engine installed. MariaDB Server parses the SQL, identifies the involved ColumnStore tables, and creates an initial logical query execution plan.

\
Using the ColumnStore storage engine interface (`ha_columnstore`), MariaDB Server converts involved table references into ColumnStore internal objects. These are then handed off to the `ExeMgr`, which is responsible for managing and orchestrating query execution across the cluster.

The `ExeMgr` analyzes the query plan and translates it into a distributed ColumnStore execution plan. It determines the necessary query steps and the execution order, including any required parallelization.

The `ExeMgr` then references the extent map to identify which PrimProc instances hold the relevant data segments. It applies extent elimination to exclude any PrimProc nodes whose extents do not match the query’s filter criteria.

The `ExeMgr` dispatches commands to the selected PrimProc instances to perform data block I/O operations.

The PrimProc components perform operations such as

* Predicate filtering
* Join processing
* Initial aggregation
* Data retrieval from local disk or external storage (e.g., S3 or cloud object storage)

They then return intermediate result sets to the ExeMgr.

The `ExeMgr` handles:

* Final-stage aggregation
* Window function evaluation
* Result-set sorting and shaping

The completed result set is returned to the MariaDB Server, which performs any remaining SQL operations like `ORDER BY`, `LIMIT`, or computed expressions in the `SELECT` list.

\
Finally, the MariaDB Server returns the result set to the client.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
