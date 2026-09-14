# MariaDB Enterprise Audit Plugin

* Q: What is the MariaDB Enterprise Audit Plugin and its primary function?\
  A: The MariaDB Enterprise Audit Plugin is an advanced security feature available exclusively with MariaDB Enterprise Server. Its primary function is to provide detailed, flexible, and configurable logging of nearly all database activity. This includes tracking user connections, the specific SQL queries executed, tables and other objects accessed, and changes made to server variables, creating a comprehensive audit trail.
* Q: Why is database auditing, as provided by this plugin, important for enterprises?\
  A: Database auditing is critically important for enterprises for several reasons:
  * Security: Helps detect and investigate suspicious activities or security breaches.
  * Compliance: Enables organizations to meet regulatory requirements (GDPR, HIPAA, SOX, PCI DSS) by providing verifiable records of data access and modification.
  * Troubleshooting: Audit logs aid in diagnosing application issues or understanding unexpected database behavior.
  * Accountability: Tracks user actions within the database to establish accountability.
* Q: What are the key features and capabilities of the MariaDB Enterprise Audit Plugin?\
  A: Key features of the MariaDB Enterprise Audit Plugin include highly granular filtering capabilities (allowing administrators to audit specific users, commands, databases, or tables), configuration of audit rules using JSON-based definitions stored in system tables for dynamic control, options to log audit data to secure files or to the system's syslog daemon, and robust log rotation mechanisms. It is designed to provide comprehensive and robust auditing for demanding enterprise environments.
* Q: How does the MariaDB Enterprise Audit Plugin differ from the basic audit plugin available in MariaDB Community Server?\
  A: While a basic audit plugin is available in MariaDB Community Server (often referred to as the "MariaDB Audit Plugin" or "server\_audit"), the MariaDB Enterprise Audit Plugin offers significantly more advanced and flexible capabilities. These include more sophisticated filtering options, the ability to define audit rules dynamically via SQL using JSON, more comprehensive event logging, and features specifically designed to meet the stringent auditing and compliance needs of enterprise organizations.
* Q: Is the MariaDB Enterprise Audit Plugin a commercial feature?\
  A: Yes, the MariaDB Enterprise Audit Plugin, with its full suite of advanced functionalities and enterprise-grade capabilities, is a commercial feature and is part of the MariaDB Enterprise Server subscription provided by MariaDB plc.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
