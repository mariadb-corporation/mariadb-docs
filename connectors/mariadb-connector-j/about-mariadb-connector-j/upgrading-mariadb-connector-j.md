---
description: >-
  Default and behavior changes to check when upgrading MariaDB Connector/J
  from 2.x to 3.x, and from 3.x to 4.x.
---

# Upgrading MariaDB Connector/J

Check these default and behavior changes before you upgrade MariaDB Connector/J to a new release series.

## Upgrading from 2.x to 3.x

Connector/J 3.x is a complete rewrite. While mostly compatible, several internal defaults have changed to favor performance, which can impact server resource usage.

### Critical Default Changes

<table><thead><tr><th width="216.5">Option</th><th width="128">Default in 2.7.x</th><th width="130">Default in 3.x</th><th>Impact</th></tr></thead><tbody><tr><td><strong>useBulkStmtsForInserts</strong></td><td><code>—</code> (n/a)</td><td><code>true</code></td><td>3.x uses the <code>COM_STMT_BULK</code> protocol by default for batch inserts (governed by <code>useBulkStmtsForInserts</code>, which defaults to <code>true</code>; the separate <code>useBulkStmts</code> option remains <code>false</code> by default). This is faster. <code>getGeneratedKeys()</code> still returns <em>all</em> generated ids (one per inserted row) — the same result as without bulk; only the underlying mechanism differs by server version.</td></tr><tr><td><strong>prepStmtCacheSqlLimit</strong></td><td><code>256</code></td><td><em>removed</em></td><td>This option was removed in Connector/J 3.x.</td></tr><tr><td><strong>useServerPrepStmts</strong></td><td><code>false</code></td><td><code>false</code></td><td>While the default remains false, if enabled, 3.x is more aggressive in preparing statements. Combined with the larger cache limit, this can exhaust the server's <code>max_prepared_stmt_count</code>.</td></tr></tbody></table>

### Feature Gaps

* **rewriteBatchedStatements:** Removed in 3.0.0 and re-introduced in 3.5.6. Users requiring the "rewrite" behavior for `INSERT` statements must use version 3.5.6 or higher.

## Upgrading from 3.x to 4.x

Connector/J 4.0 requires Java 17 or later. The 3.5 release series remains maintained for applications on Java 8 or Java 11. The following defaults and behaviors changed:

<table><thead><tr><th width="260">Behavior</th><th width="220">Connector/J 3.5</th><th>Connector/J 4.0</th></tr></thead><tbody><tr><td>Minimum Java version</td><td>Java 8</td><td>Java 17</td></tr><tr><td><strong>sslMode</strong> default</td><td><code>disable</code></td><td><code>verify-full</code>: TLS is enabled by default, with certificate and host name validation. Set <code>sslMode=disable</code> to connect without TLS. The new <code>deferCertificateValidation</code> option controls the zero-configuration TLS fallback.</td></tr><tr><td><strong>enabledSslProtocolSuites</strong> default</td><td>JVM default</td><td><code>TLSv1.3,TLSv1.2</code></td></tr><tr><td><strong>permitNoResults</strong> default</td><td><code>true</code></td><td><code>false</code>: <code>PreparedStatement.executeQuery()</code> throws for a statement that returns no result set, as the JDBC specification requires.</td></tr><tr><td><strong>cacheCodecs</strong> default</td><td><code>false</code></td><td><code>true</code></td></tr><tr><td><code>Connection.setSavepoint()</code> in auto-commit mode</td><td>Succeeds silently</td><td>Throws an <code>SQLException</code></td></tr><tr><td><strong>useReadAheadInput</strong> option</td><td>Available</td><td>Removed</td></tr><tr><td><strong>defaultFetchSize</strong></td><td>Positive values only</td><td><code>Integer.MIN_VALUE</code> enables sequential access, streaming LOB columns from the socket</td></tr><tr><td><code>AWS-IAM</code> credential plugin</td><td>Bundled, needs <code>software.amazon.awssdk:rds</code> on the classpath</td><td>Separate <code>mariadb-java-client-aws</code> artifact, with STS assume-role support and the RDS root certificates</td></tr><tr><td>GSSAPI on Windows</td><td>Waffle native implementation (<code>waffle-jna</code>)</td><td>Operating-system GSS-API with <code>-Dsun.security.jgss.native=true</code>. No third-party dependency</td></tr><tr><td>Unix domain sockets</td><td>Need JNA, Unix only</td><td>JDK implementation, no dependency, also on Windows</td></tr><tr><td>Java module</td><td>Automatic module</td><td>First-class <code>module-info.java</code> declaring the <code>org.mariadb.jdbc</code> module</td></tr></tbody></table>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
