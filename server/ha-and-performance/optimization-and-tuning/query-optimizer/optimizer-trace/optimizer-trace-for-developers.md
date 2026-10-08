# Optimizer Trace for Developers

This article describes guidelines for what/how to write to Optimizer Trace when doing server development.

## Basic considerations

The trace is a "structured log" of what was done by the optimizer. Prefer to do tracing as soon as a rewrite/decision is made (instead of having a separate trace\_something() function).

Generally, a function should expect to find the trace in a state where we're writing an array. The rationale is that array elements are ordered, while object members are not (even if they come in a certain order in the JSON text). We're writing a log, so it's natural for different entries to form an array.

Typically you'll want to start an unnamed object, then use member names to show what kind of entry you're about to write:

```
[
  ...,  # Something before us
  {
    "my_new_rewrite": {
       "from": "foo", 
       "to": "bar",
       ...
    }
  }
  ...
```

(TODO other considerations)

## Making sure the trace is valid

`Json_writer_object` and `Json_writer_array` classes use RAII idiom and ensure that JSON objects and arrays are "closed" in the reverse order they were started.

However, they do not ensure these constraints:

* JSON objects must have named members.
* JSON arrays must have unnamed members.

Tracing code has runtime checks for these. Attempt to write invalid JSON will cause assertion failure.

## Test coverage

It is possible to run `mysql-test-run` with this argument

```
--mysqld=--optimizer_trace=enabled=on
```

This will run all tests with tracing on. As mentioned earlier, debug build will perform checks that we are not producing invalid trace.

The BuildBot instance atalso runs tests with this argument, see `mtr_opttrace` pass in kvm-fulltest and kvm-fulltest2.

## Debugging

See [optimizer-debugging-with-gdb/#printing-the-optimizer-trace](../optimizer-debugging-with-gdb.md#printing-the-optimizer-trace) for commands to print the trace for the current statement.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
