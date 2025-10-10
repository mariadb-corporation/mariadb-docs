# MariaDB Connector/Python

<!-- import mariadb
conn_params= {
   "host" : "localhost",
   "database" : "test"
}
with mariadb.connect(**conn_params) as conn:
   with conn.cursor() as cursor:
      cursor.execute("CREATE USER IF NOT EXISTS example_user@localhost identified by 'GHbe_Su3B8'")
      cursor.execute("grant all on test.* to example_user@localhost")
      cursor.execute("DROP TABLE IF EXISTS book") -->

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API
which is compliant with the Python DB API 2.0 ([PEP-249](https://peps.python.org/pep-249)). It is written in C and Python and uses
MariaDB Connector/C client library for client server communication.

### Contents

# Contents:

* [Installation](install.md)
  * [Prerequisites](install.md#prerequisites)
  * [Binary installation](install.md#binary-installation)
  * [Installation from Source](install.md#installation-from-source)
  * [Test suite](install.md#test-suite)
* [Basic usage](usage.md)
  * [Connecting](usage.md#connecting)
  * [Passing parameters to SQL statements](usage.md#passing-parameters-to-sql-statements)
* [Connection pooling](pooling.md)
  * [Configuring and using a connection pool](pooling.md#configuring-and-using-a-connection-pool)
* [API Reference](api.md)
  * [The MariaDB Connector/Python module](module.md)
  * [The connection class](connection.md)
  * [The cursor class](cursor.md)
  * [The ConnectionPool class](pool.md)
  * [Constants](constants.md)
* [License](license.md)
  * [MariaDB Connector/Python](license.md#mariadb-connector-python)
  * [MariaDB Connector/Python documentation](license.md#mariadb-connector-python-documentation)
* [Bug reports](bugs.md)
  * [How to report a bug?](bugs.md#how-to-report-a-bug)
* [MariaDB Connector/Python FAQ](faq.md)
  * [Installation](faq.md#installation)
  * [Connecting](faq.md#connecting)
  * [General](faq.md#general)
  * [Transactions](faq.md#transactions)

{% @marketo/form formId="4316" %}
