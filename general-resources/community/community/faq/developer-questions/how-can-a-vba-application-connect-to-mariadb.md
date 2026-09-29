# How can a VBA Application Connect to MariaDB?

A VBA application, such as a Microsoft Access or Excel macro, connects to MariaDB through ODBC. Install [MariaDB Connector/ODBC]({connectors}/mariadb-connector-odbc), then either [create a data source]({connectors}/mariadb-connector-odbc/creating-a-data-source-with-mariadb-connectorodbc) and refer to it by name, or pass a DSN-less connection string that names the driver. In both cases, use an ADO `Connection` object (or DAO, in Access) to open the connection, and run SQL statements through it.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
