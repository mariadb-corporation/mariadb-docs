---
description: >-
  Review known limitations and constraints of MariaDB MaxScale. Understand
  supported features, configuration boundaries, and protocol specifics to plan
  your deployment effectively.
---

# MariaDB MaxScale Limitations Guide

### Quickstart Guide: MariaDB MaxScale Limitations

While MariaDB MaxScale is a powerful tool for managing MariaDB deployments, it's essential to be aware of its limitations to ensure proper configuration and avoid unexpected behavior. This guide highlights key considerations when deploying and using MaxScale.

#### 1. Configuration File Line Length

* **Limitation:** Older versions of MaxScale (2.1.2 and earlier) had a strict line length limit of 1024 characters in the configuration file (`maxscale.cnf`).
* **Consideration:** Ensure your MaxScale configuration lines do not exceed this limit for older versions. Modern versions (e.g., 2.3.0 and later) have significantly increased this limit (to 16,777,216 characters), making it less of a concern for current deployments. Always check the documentation for your specific MaxScale version.

#### 2. Assumptions about MariaDB Server Configuration

* **Limitation:** MaxScale operates under the assumption that certain MariaDB Server configuration parameters are set to their default values. A critical example is the assumption that `autocommit` is enabled for new connections.
* **Consideration:** If your backend MariaDB servers deviate from default `autocommit` settings or other assumed defaults, it could lead to unexpected behavior in how MaxScale manages connections and routes queries, particularly with transaction handling. Always verify that your MariaDB server configurations align with MaxScale's expectations as outlined in its documentation.

#### 3. Transaction Boundary Detection and XA Transactions

* **Limitation:** MaxScale uses a custom SQL parser to deduce transaction boundaries. This parser may not fully comprehend or correctly classify highly complex SQL statements or certain edge cases. This can lead to a mismatch between MaxScale's understanding of a connection's transaction state and the actual state on the backend database.
* **Specific Issue with XA Transactions:** If a `START TRANSACTION` command fails internally on the backend due to an already open XA transaction (e.g., using `XA START`), MaxScale's parser might not correctly detect this failure. It could mistakenly assume a new transaction has started, leading to discrepancies in transaction state awareness, especially with the `readwritesplit` router.
* **Consideration:** Be cautious with overly complex SQL or when using XA transactions in conjunction with MaxScale's transaction-aware routers. Thoroughly test your application's transaction logic through MaxScale to identify and mitigate any potential inconsistencies.

#### 4. ETL Feature Dependency

* **Limitation:** The ETL (Extract, Transform, Load) feature within MaxScale relies on the MariaDB Connector/ODBC driver for its functionality.
* **Consideration:** To ensure stability and avoid potential crashes or memory leaks when using MaxScale's ETL capabilities, it is highly recommended to use MariaDB Connector/ODBC driver version 3.1.18 or later. Always ensure all components are compatible.

#### Important General Considerations:

* **Query Classification:** MaxScale's ability to route queries correctly relies on its query classification. If queries are ambiguous or use non-standard SQL, they might be misrouted.
* **Prepared Statements:** While supported, complex interactions with prepared statements can sometimes expose nuances in parsing or routing.
* **Protocol Specifics:** MaxScale aims for broad compatibility, but subtle differences in client or server protocol implementations might arise.
* **Monitoring and Filters:** Be aware that specific monitor or filter modules might have their own inherent limitations or performance impacts.

Understanding these limitations helps in designing a robust MaxScale deployment and troubleshooting potential issues effectively.

#### Further Resources:

* [MariaDB MaxScale Limitations Documentation](../maxscale-management/mariadb-maxscale-limitations-guide.md)
* [MariaDB MaxScale Documentation (General)](../maxscale-use-cases/maxscale-overview.md)
