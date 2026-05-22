# Decoding ColumnStore Stack Traces

MariaDB ColumnStore includes a specialized crash handler that automatically captures and logs details of a process crash from critical daemons like `PrimProc`. When an unexpected process termination occurs, the raw memory frames and stack traces are preserved on disk to assist with post-mortem analysis and troubleshooting.

## Locating Crash Trace Files

When a ColumnStore subsystem or daemon (such as `PrimProc`) encounters a critical exception or fault, the crash handler writes a trace log file directly to the system log directory.

These specialized logs can be found in the following directory:

```bash
/var/log/mariadb/columnstore/trace
```

### Trace Naming Convention

The generated trace filenames follow a structured format based on the process identity:

```
<processName>.<processID>.log
```

_Example:_ `PrimProc.5667.log`

These generated logs are structures conceptually similar to the crash traces found in standard MariaDB Server error logs when a server component crashes.

## Prerequisites for Decoding

Raw trace files contain hexadecimal memory addresses and function pointer offsets that represent the state of the call stack at the exact moment of the crash. To resolve these addresses into human-readable source code file names and line numbers, the following items must be available on the system:

1. Matching Binary Versions: The exact version of the ColumnStore binary that generated the crash must be used during decoding to ensure memory addresses line up correctly.
2. Debug Info Packages: The corresponding MariaDB ColumnStore `debuginfo` package (matching your installed package version) must be installed to supply the necessary debugging symbols.

## Resolving Traces Using MariaDB Utilities

Because ColumnStore crash traces share structural similarities with standard MariaDB Server crash dumps, you can utilize administrative utilities bundled within the MariaDB ecosystem to help parse the stack frames.

### Using `resolve_stack_dump`

The `resolve_stack_dump` utility is an administrative tool used to decode raw numeric stack tracks into resolved symbolic formats.

1. Locate the utility on your system (typically bundled within the MariaDB Server binary or administrative tools path).
2.  Pass the raw trace file into the utility while pointing to the active daemon binary or symbol path to resolve the hex frames:

    Bash

    ```bash
    resolve_stack_dump -s /usr/lib/debug/usr/bin/PrimProc.debug /var/log/mariadb/columnstore/trace/PrimProc.5667.log
    ```

### Using System Debugging Tools (`addr2line`)

Alternatively, standard system utilities like `addr2line` can be combined with the raw hex addresses found in the trace file to extract the code origins manually:

```bash
addr2line -e /usr/bin/PrimProc <hex-address-from-trace-file>
```

This maps the specific memory frame instruction pointer directly to its corresponding source repository file name and line number, allowing technical teams to quickly identify the exact function where the failure occurred.
