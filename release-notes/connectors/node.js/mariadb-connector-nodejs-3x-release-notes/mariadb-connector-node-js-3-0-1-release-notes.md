# MariaDB Connector/Node.js 3.0.1 Release Notes

{% include "../../../.gitbook/includes/latest-nodejs.md" %}

[Download](https://mariadb.com/downloads/connectors/connectors-data-access/nodejs-connector) | [Release Notes](mariadb-connector-node-js-3-0-1-release-notes.md) | [Changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-nodejs-301-changelog.md) | [Connector/Node.js Overview](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide)

**Release date:** 26 Jul 2022

MariaDB Connector/Node.js 3.0.1 is a [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release.

{% hint style="success" %}
**For an overview of MariaDB Connector/Node.js see the** [**About MariaDB Connector/Node.js**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-nodejs/mariadb-connector-node-js-guide) **page**
{% endhint %}

## Notable Changes

### Error description improvement

* Pool might return a common error ‘retrieve connection from pool timeout after XXXms’ in place of real error.\[[CONJS-200](https://jira.mariadb.org/browse/CONJS-200)]
* Trace option now works when using pool/cluster. It is recommended to activate the trace option in development Since driver is asynchronous, enabling this option to save initial stack when calling any driver methods. This allows having the caller method and line in the error stack, permitting error easy debugging. The problem is this error stack is created using Error.captureStackTrace that is very slow. To give an idea, this slows down by 10% a query like 'select \* from mysql.user LIMIT 1', so not recommended in production. \[[CONJS-209](https://jira.mariadb.org/browse/CONJS-209)]

```js
const pool = mariadb.createPool({
      host: 'mydb.com',
      user: 'myUser',
      connectionLimit: 5,
      trace: true
      });
      await pool.query('wrong query');
      /* will throw an error like :
        SqlError: (conn=15868, no: 1064, SQLState: 42000) You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'wrong query' at line 1
          sql: wrong query - parameters:[]
            at Object.module.exports.createError (errors.js:57:10)
            at ...
          From event:
            at Function._PARAM (\integration\test-pool.js:60:18)
            at …
          text: "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'wrong query' at line 1",
          sql: 'wrong query - parameters:[]',
          fatal: false,
          errno: 1064,
          sqlState: '42000',
          code: 'ER_PARSE_ERROR'
      */
```

* Pool error description is improved indicating pool information, like \[[CONJS-208](https://jira.mariadb.org/browse/CONJS-208)]:

```
SqlError: (conn=-1, no: 45028, SQLState: HY000) retrieve connection from pool timeout after 200ms
      (pool connections: active=1 idle=0 limit=1)
      at Object.module.exports.createError
      …
```

### Other improvement

* node.js 18 supported \[[CONJS-197](https://jira.mariadb.org/browse/CONJS-197)]
* New option `checkNumberRange`. When used in conjunction of `decimalAsNumber`, `insertIdAsNumber` or `bigIntAsNumber`, if conversion to number is not exact, connector will throw an error. This permits easier compatibility with mysql/mysql2 and 2.x version driver version. \[[CONJS-198](https://jira.mariadb.org/browse/CONJS-198)]
* Performance enhancement for multi-rows resultset. Internal benchmarks show improved performance by 10% for a result-set of 1000 rows.\[[CONJS-210](https://jira.mariadb.org/browse/CONJS-210)]

### Issues Fixed

* \[[CONJS-193](https://jira.mariadb.org/browse/CONJS-193)] Wrong error returned "Cannot read properties of undefined… … (reading 'charset')" when error during handshake
* \[[CONJS-194](https://jira.mariadb.org/browse/CONJS-194)] Charset change using parameterized query fails with "Uncaught TypeError: opts.emit is not a function"
* \[[CONJS-195](https://jira.mariadb.org/browse/CONJS-195)] Error "cannot mix BigInt and other types" when parsing negative bigint
* \[[CONJS-196](https://jira.mariadb.org/browse/CONJS-196)] connection.close() is now really an alias or connection.release()
* \[[CONJS-199](https://jira.mariadb.org/browse/CONJS-199)] wrong return type for batch() on typescript
* \[[CONJS-201](https://jira.mariadb.org/browse/CONJS-201)] typecast geometry parsing error
* \[[CONJS-202](https://jira.mariadb.org/browse/CONJS-202)] support pre 4.1 error format for 'too many connection' error
* \[[CONJS-203](https://jira.mariadb.org/browse/CONJS-203)] encoding error for connection attributes when using changeUser with connection attributes
* \[[CONJS-206](https://jira.mariadb.org/browse/CONJS-206)] possible race condition on connection destroy when no other connection can be created
* \[[CONJS-204](https://jira.mariadb.org/browse/CONJS-204)] handle password array when using authentication plugin “pam\_use\_cleartext\_plugin”
* \[[CONJS-205](https://jira.mariadb.org/browse/CONJS-205)] query hanging when using batch with option timeout in place of error thrown

## Changelog

For a complete list of changes made in this release, with links to detailed information\
on each push, see the [changelog](../changelogs/mariadb-connector-nodejs-3x-changelogs/mariadb-connector-nodejs-300-ga-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
