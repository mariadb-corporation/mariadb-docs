# The ConnectionPool class

### *class* ConnectionPool(\*args, \*\*kwargs)

Class defining a pool of database connections

MariaDB Connector/Python supports simple connection pooling.
A connection pool holds a number of open connections and handles thread safety when providing connections to threads.

The size of a connection pool is configurable at creation time, but cannot be changed afterward. The maximum size of a connection pool is limited to 64 connections.

Keyword Arguments:

- **\`pool_name\`** (`str`) - Name of connection pool
- **\`pool_size\`** (`int`) - Size of pool. The Maximum allowed number is 64. Default to 5
- **\`pool_reset_connection\`** (`bool`) - Will reset the connection before returning it to the pool. Default to True.
- **\`pool_validation_interval\`** (`int`) - Specifies the validation interval in milliseconds after which the status of a connection requested from the pool is checked. A value of 0 means that the status will always be checked. Default to 500 (Added in version 1.1.6)
- **\*\*kwargs** - Optional additional connection arguments, as described in mariadb.connect() method.

## ConnectionPool methods

#### ConnectionPool.add_connection(connection=None)

Adds a connection object to the connection pool.

In case that the pool doesn’t have a free slot or is not configured,
a PoolError exception will be raised.

#### ConnectionPool.close()

Closes connection pool and all connections.

#### ConnectionPool.get_connection()

Returns a connection from the connection pool or raises a PoolError
exception if a connection is not available.

#### ConnectionPool.set_config(\*\*kwargs)

Sets the connection configuration for the connection pool.
For valid connection arguments, check the mariadb.connect() method.

Note: This method doesn’t create connections in the pool.
To fill the pool, one has to use add_connection() ḿethod.

## ConnectionPool attributes

#### ConnectionPool.connection_count

Returns the number of connections in connection pool.

*Since version 1.1.0*

#### ConnectionPool.max_size

Returns the maximum size for connection pools.

#### ConnectionPool.pool_size

Returns the size of the connection pool.

#### ConnectionPool.pool_name

Returns the name of the connection pool.

{% @marketo/form formId="4316" %}
