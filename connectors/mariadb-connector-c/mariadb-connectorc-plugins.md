---
description: >-
  MariaDB Connector/C supports loadable and built-in plugins across four
  categories: connection, pvio, I/O, and authentication, including remote_io
  and multiple auth methods.
---

# MariaDB Connector/C Plugins

MariaDB Connector/C functionality can be extended via loadable (or statically compiled in) plugins. As of the version 3.1.11 Connector/C comes with the following plugins

## connection plugins

### replication

## pvio plugins

These plugins are used by the Connector/C to communicate with the MariaDB server.

### socket

### npipe

### shmem

## io plugins

These are plugins that are used whenever Connector/C needs to read a file.\
For example, for `LOAD DATA LOCAL INFILE` statement, when a server requests the Connector/C to send a specific file.

### remote\_io

This plugin uses `libcurl` to access remote files, it allows the client to execute statements like

`LOAD DATA LOCAL INFILE 'http://mariadb.com/example.csv' INTO t1`

Note that here, like with any `LOAD DATA LOCAL`, it'll be the client that fetches the file, not the server.

This plugin supports the following url schemes: `http://`, `https://`, `ftp://`, `sftp://`, `ldap://`, `smb://`.

## auth plugins

These are authentication plugins. They are loaded automatically by the Connector/C when the server requests a specific authentication method.

### mysql\_native\_password

### dialog

This is a generic dialog plugin that asks the user a question (as instructed by the server) and sends the answer to the server. Everything is sent in plain text, one should enable SSL if secrets are sent via this plugin.\
Graphical clients can customize the plugin to provide graphical dialog form. See

### client\_ed25519

### caching\_sha2\_password

### sha256\_password

### auth\_gssapi\_client

### mysql\_old\_password

### mysql\_clear\_password


{% @marketo/form formId="4316" %}
