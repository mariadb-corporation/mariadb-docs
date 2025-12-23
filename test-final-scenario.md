# Final System Check

This file tests the Link Expander Action against all known edge cases.

### 1. Simple Inline Links
- Check the [Server Knowledge Base](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/kb/en/library).
- Read about [MaxScale Routers](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/routers/readwritesplit).

### 2. The "Table Stress Test"
*Previously, links inside tables failed because of the pipe symbol.*

| Component | Documentation Link | Notes |
| :--- | :--- | :--- |
| **Server** | [Server Parameters](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-server-parameters) | Should expand correctly. |
| **Galera** | [Cluster Address](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/configuration/galera-cluster-address) | **Critical Test:** This link failed previously. |
| **Analytics** | [ColumnStore Arch](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/architecture) | Standard link. |

### 3. Nested Formatting
> **Note:** Please refer to the [Galera Getting Started Guide](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/getting-started) before proceeding.

