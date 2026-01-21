---
description: >-
  The Information Schema SYSTEM_VARIABLES table contains all system variables
  and their current global or session values.
---

# Information Schema SYSTEM\_VARIABLES Table

The [Information Schema](../) `SYSTEM_VARIABLES` table shows current values and various metadata of all [system variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md).

It contains the following columns:

| Column                  | Description                                                                                                                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VARIABLE\_NAME          | System variable name.                                                                                                                                                                                                                          |
| SESSION\_VALUE          | Session value of the variable or NULL if the variable only has a global scope.                                                                                                                                                                 |
| GLOBAL\_VALUE           | Global value of the variable or NULL if the variable only has a session scope.                                                                                                                                                                 |
| GLOBAL\_VALUE\_ORIGIN   | How the global value was set — a compile-time default, auto-configured by the server, configuration file (or a command line), with the SQL statement.                                                                                          |
| DEFAULT\_VALUE          | Compile-time default value of the variable.                                                                                                                                                                                                    |
| VARIABLE\_SCOPE         | Global, session, or session-only.                                                                                                                                                                                                              |
| VARIABLE\_TYPE          | Data type of the variable value.                                                                                                                                                                                                               |
| VARIABLE\_COMMENT       | Help text, usually shown in mariadbd --help --verbose.                                                                                                                                                                                         |
| NUMERIC\_MIN\_VALUE     | For numeric variables — minimal allowed value.                                                                                                                                                                                                 |
| NUMERIC\_MAX\_VALUE     | For numeric variables — maximal allowed value.                                                                                                                                                                                                 |
| NUMERIC\_BLOCK\_SIZE    | For numeric variables — a valid value must be a multiple of the "block size".                                                                                                                                                                  |
| ENUM\_VALUE\_LIST       | For ENUM, SET, and FLAGSET variables — the list of recognized values.                                                                                                                                                                          |
| READ\_ONLY              | Whether a variable can be set with the SQL statement. Note that many "read only" variables can still be set on the command line.                                                                                                               |
| COMMAND\_LINE\_ARGUMENT | Whether an argument is required when setting the variable on the command line. NULL when a variable can not be set on the command line.                                                                                                        |
| GLOBAL\_VALUE\_PATH     | Which config file the variable got its value from. NULL if not set in any config file. Added in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes). |

## Example

```sql
SELECT * FROM information_schema.SYSTEM_VARIABLES 
  WHERE VARIABLE_NAME='JOIN_BUFFER_SIZE'\G
*************************** 1. row *****************************
        VARIABLE_NAME: JOIN_BUFFER_SIZE
        SESSION_VALUE: 131072
         GLOBAL_VALUE: 131072
  GLOBAL_VALUE_ORIGIN: COMPILE-TIME
        DEFAULT_VALUE: 131072
       VARIABLE_SCOPE: SESSION
        VARIABLE_TYPE: BIGINT UNSIGNED
     VARIABLE_COMMENT: The size of the buffer that is used for joins
    NUMERIC_MIN_VALUE: 128
    NUMERIC_MAX_VALUE: 18446744073709551615
   NUMERIC_BLOCK_SIZE: 128
      ENUM_VALUE_LIST: NULL
            READ_ONLY: NO
COMMAND_LINE_ARGUMENT: REQUIRED
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
