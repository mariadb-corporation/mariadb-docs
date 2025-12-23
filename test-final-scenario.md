# Final System Check

This file tests the Link Expander Action against all known edge cases.

### 1. Simple Inline Links
- Check the [Server Knowledge Base]({server}/kb/en/library).
- Read about [MaxScale Routers]({maxscale}/routers/readwritesplit).

### 2. The "Table Stress Test"
*Previously, links inside tables failed because of the pipe symbol.*

| Component | Documentation Link | Notes |
| :--- | :--- | :--- |
| **Server** | [Server Parameters]({server}/reference/mariadb-server-parameters) | Should expand correctly. |
| **Galera** | [Cluster Address]({galera}/galera-management/configuration/galera-cluster-address) | **Critical Test:** This link failed previously. |
| **Analytics** | [ColumnStore Arch]({analytics}/architecture) | Standard link. |

### 3. Nested Formatting
> **Note:** Please refer to the [Galera Getting Started Guide]({galera}/getting-started) before proceeding.

