# mysql\_get\_optionv

## Syntax

```c
int mysql_get_optionv(MYSQL * mysql,
                      enum mysql_option,
                      void * arg,
                      ...);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `mysql_option` - the option you want to retrieve. See description below.
* `arg` - pointer to a variable for storing value of the specified option.
* `...` - variable argument list

## Description

Retrieves the value for a given option which was previously set by [mysql\_optionsv](mysql_optionsv.md).

Returns zero on success, non zero if an error occurred (invalid option).

This function was added in MariaDB Connector/C 3.0.0.

### Options

#### Boolean values (my\_bool)

* MYSQL\_OPT\_COMPRESS
* MYSQL\_OPT\_NAMED\_PIPE
* MYSQL\_OPT\_RECONNECT
* MYSQL\_REPORT\_DATA\_TRUNCATION
* MYSQL\_OPT\_NONBLOCK
* MYSQL\_OPT\_SSL\_VERIFY\_SERVER\_CERT
* MARIADB\_OPT\_CONNECTION\_READ\_ONLY
* MYSQL\_SECURE\_AUTH

    ```c
    uint8_t reconnect;
    
    rc = mysql_get_optionv(mysql, MYSQL_OPT_RECONNECT, &reconnect);
    ```

#### Integer values

* MYSQL\_OPT\_CONNECT\_TIMEOUT
* MYSQL\_OPT\_READ\_TIMEOUT
* MYSQL\_OPT\_WRITE\_TIMEOUT
* MYSQL\_OPT\_LOCAL\_INFILE
* MYSQL\_OPT\_PROTOCOL
  
    ```c
    uint32_t timeout;
    
    rc = mysql_get_optionv(mysql, MYSQL_OPT_CONNECT_TIMEOUT, &timeout);
    ```

#### Character arrays
* MYSQL\_INIT\_COMMAND
 
    ```c
    char **commands;
    int elements;

    rc = mysql_get_optionv(mysql, MYSQL_INIT_COMMAND, &commands, &elements);
    ```

#### Character values

* MYSQL\_READ\_DEFAULT\_FILE
* MYSQL\_READ\_DEFAULT\_GROUP
* MYSQL\_SET\_CHARSET\_NAME
* MYSQL\_PLUGIN\_DIR
* MYSQL\_OPT\_SSL\_KEY
* MYSQL\_OPT\_SSL\_CERT
* MYSQL\_OPT\_SSL\_CA
* MYSQL\_OPT\_SSL\_CAPATH
* MYSQL\_OPT\_SSL\_CRL
* MYSQL\_OPT\_SSL\_CRLPATH
* MYSQL\_OPT\_SSL\_CIPHER
* MARIADB\_OPT\_SSL\_FP
* MARIADB\_OPT\_SSL\_FP_LIST
* MARIADB\_OPT\_SSL\_PASSPHRASE
* MYSQL\_DEFAULT\_AUTH
* MYSQL\_OPT\_BIND
* MARIADB\_OPT\_CONNECTION\_HANDLER

    ```c
    char *plugin_dir;
    
    rc = mysql_get_optionv(mysql, MYSQL_PLUGIN_DIR, &plugin_dir);
    ```

### Misc

* MYSQL\_PROGRESS\_CALLBACK: requires a function pointer \*(const MYSQL \*, uint, uint, double, const char \*, uint))arg)
* MYSQL\_CONNECT\_ATTRS: this option requires 5 parameters:

    ```c
    /* get number of connection attributes */
    int i, elements= 0;
    char **key, **value;

    mysql_get_optionv(mysql, MYSQL_CONNECT_ATTRS, NULL, NULL, (void *)&elements);
    key= (char **)malloc(sizeof(char *) * elements);
    val= (char **)malloc(sizeof(char *) * elements);
    mysql_get_optionv(mysql, MYSQL_OPT_CONNECT_ATTRS, &key, &val, &elements);
    for (i=0; i < elements; i++)
      printf("key: %s value: %s", key[i], val[i]);
    ```

* MARIADB\_OPT\_USERDATA: retrieves userdata for a given key.

    ```c
    const char *ssh_user;
    mysql_get_optionv(mysql, MARIADB_OPT_USERDATA, "ssh_user", (void *)ssh_user);
    ```

## See also

* [mysql\_optionsv()](mysql_optionsv.md)


{% @marketo/form formId="4316" %}
