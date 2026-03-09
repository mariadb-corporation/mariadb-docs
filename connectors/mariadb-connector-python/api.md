# API Reference

# Contents:

* [The MariaDB Connector/Python module](module.md)
  * [Constructors](module.md#constructors)
    * [connect()](module.md#connect) - Synchronous connection
    * [asyncConnect()](module.md#asyncconnect) - Asynchronous connection *(New in 2.0)*
    * [create_pool()](module.md#create_pool) - Synchronous connection pool *(New in 2.0)*
    * [create_async_pool()](module.md#create_async_pool) - Asynchronous connection pool *(New in 2.0)*
  * [Attributes](module.md#attributes)
  * [Exceptions](module.md#exceptions)
* [The connection class](connection.md)
  * [`Connection`](connection.md#mariadb.connections.Connection)
  * [Connection constructors](connection.md#connection-constructors)
  * [Connection methods](connection.md#connection-methods)
  * [Connection attributes](connection.md#connection-attributes)
* [The cursor class](cursor.md)
  * [`Cursor`](cursor.md#mariadb.cursors.Cursor)
  * [Cursor methods](cursor.md#cursor-methods)
  * [Cursor attributes](cursor.md#cursor-attributes)
* [Async/Await Support](async-usage.md) *(New in 2.0)*
  * [AsyncConnection](async-usage.md#basic-async-connection)
  * [AsyncCursor](async-usage.md#async-cursor-operations)
  * [AsyncConnectionPool](async-usage.md#async-connection-pools)
* [Connection Pooling](pooling.md)
  * [Synchronous Pool](pooling.md#synchronous-connection-pool)
  * [Asynchronous Pool](pooling.md#asynchronous-connection-pool)
* [Constants](constants.md)
  * [CAPABILITY](constants.md#module-mariadb.constants.CAPABILITY)
  * [CLIENT](constants.md#module-mariadb.constants.CLIENT)
  * [CURSOR](constants.md#module-mariadb.constants.CURSOR)
  * [ERR (Error)](constants.md#err-error)
  * [FIELD_FLAG](constants.md#module-mariadb.constants.FIELD_FLAG)
  * [FIELD_TYPE](constants.md#module-mariadb.constants.FIELD_TYPE)
  * [INDICATORS](constants.md#indicators)
  * [INFO](constants.md#info)
  * [TPC_STATE](constants.md#tpc-state)
  * [STATUS](constants.md#status)

{% @marketo/form formId="4316" %}
