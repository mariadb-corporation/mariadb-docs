# How to Collect Large Optimizer Traces

[Optimizer traces](./) can be large for some queries.

In order to collect a large trace, you need to perform the following steps (using 128 MB as an example):

```
set global max_allowed_packet=128*1024*1024;
```

Reconnect specifying `--max-allowed-packet=128000000` for the client as well.

```
set optimizer_trace=1;
set optimizer_trace_max_mem_size=127*1024*1024;
```

Now, one can run the query and save the large trace.

## See Also

* [optimizer\_trace](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace) system variable
* [optimizer\_trace\_max\_mem\_size](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#optimizer_trace_max_mem_size) system variable
* [max\_allowed\_packet](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) system variable

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
