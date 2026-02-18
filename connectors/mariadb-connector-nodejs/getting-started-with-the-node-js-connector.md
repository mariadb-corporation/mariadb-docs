---
description: >-
  Complete Node.js connector guide for MariaDB. Complete reference for
  installation, connection pooling, query execution, and error handling for
  production use.
---

# Getting Started With the Node.js Connector

The MariaDB Node.js Connector is available through the Node.js repositories. You can install it using npm:

```bash
npm install mariadb
```

Using ECMAScript, prior to 2017:

```js
const mariadb = require('mariadb');
const pool = mariadb.createPool({
     host: 'mydb.com', 
     user:'myUser', 
     password: 'myPassword',
     connectionLimit: 5
});
pool.getConnection()
    .then(conn => {
    
      conn.query("SELECT 1 as val")
        .then((rows) => {
          console.log(rows); //[ {val: 1}, meta: ... ]
          //Table must have been created before 
          // " CREATE TABLE myTable (id int, val varchar(255)) "
          return conn.query("INSERT INTO myTable value (?, ?)", [1, "mariadb"]);
        })
        .then((res) => {
          console.log(res); // { affectedRows: 1, insertId: 1, warningStatus: 0 }
          conn.end();
          pool.end();
        })
        .catch(err => {
          //handle error
          console.log(err); 
          conn.end();
          pool.end();
        })
        
    }).catch(err => {
      //not connected
      pool.end();
    });
```

Using ECMAScript 2017:

```js
const mariadb = require('mariadb');
const pool = mariadb.createPool({
     host: 'mydb.com', 
     user:'myUser', 
     password: 'myPassword',
     connectionLimit: 5
});
async function asyncFunction() {
  let conn;
  try {
	conn = await pool.getConnection();
	const rows = await conn.query("SELECT 1 as val");
	console.log(rows); //[ {val: 1}, meta: ... ]
	const res = await conn.query("INSERT INTO myTable value (?, ?)", [1, "mariadb"]);
	console.log(res); // { affectedRows: 1, insertId: 1, warningStatus: 0 }

  } catch (err) {
	throw err;
  } finally {
	if (conn) conn.end();
  }
}
asyncFunction().then(() => {
  pool.end();
});
```

The MariaDB Connector can use different APIs on the back-end: [Promise](connector-nodejs-promise-api.md) and [Callback](connector-nodejs-callback-api.md).
API is the same for TypeScript, but please read specific   
The default API is Promise. The callback API is provided for compatibility with the mysql and mysql2 APIs.

{% @marketo/form formId="4316" %}
