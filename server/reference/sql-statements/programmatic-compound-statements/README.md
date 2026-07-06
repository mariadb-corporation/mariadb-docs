---
description: >-
  Explore programmatic compound statements in MariaDB Server. This section
  covers BEGIN...END blocks, loops, and conditional logic for writing complex
  stored routines and event definitions.
---

# Programmatic & Compound Statements

{% columns %}
{% column %}
{% content-ref url="begin-end.md" %}
[begin-end.md](begin-end.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Group multiple SQL statements into a logical block. This construct defines a compound statement, creating a new scope for variables and exception handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="case-statement.md" %}
[case-statement.md](case-statement.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete reference for CASE Statement in MariaDB. Complete syntax guide with all options, clauses, and practical examples with comprehensive examples and.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="declare-condition.md" %}
[declare-condition.md](declare-condition.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define named error conditions. This statement associates a name with a specific SQLSTATE or MariaDB error code for easier handling in stored programs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="declare-handler.md" %}
[declare-handler.md](declare-handler.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Specify actions for error conditions. This statement defines handler routines (CONTINUE or EXIT) to manage exceptions or warnings within a block.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="declare-type.md" %}
[declare-type.md](declare-type.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define data types for Oracle compatibility. This statement allows declaring PL/SQL-style record types and associative arrays, and REF CURSOR types within stored procedures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="declare-variable.md" %}
[declare-variable.md](declare-variable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Initialize local variables within a stored program. This statement defines variables with a specific data type and optional default value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="for.md" %}
[for.md](for.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Loop through a range or cursor result set. This control flow statement repeatedly executes a block of code for each item in a specified range or query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="goto.md" %}
[goto.md](goto.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Jump to a labeled point in the code. This Oracle-compatible statement transfers execution control to a specific label within the stored program.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="if.md" %}
[if.md](if.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute code based on conditions. This control flow statement runs different blocks of SQL statements depending on whether a specified condition is true.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="iterate.md" %}
[iterate.md](iterate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restart the current loop. This statement jumps back to the beginning of a LOOP, REPEAT, or WHILE block, skipping any remaining statements in the current iteration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="labels.md" %}
[labels.md](labels.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Identify blocks and loops for flow control. Labels provide names for BEGIN...END blocks or loops, allowing them to be targeted by LEAVE, ITERATE, or GOTO statements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="leave.md" %}
[leave.md](leave.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Exit a labeled block or loop immediately. This statement terminates the execution of the current loop or compound statement and continues after the block.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="loop.md" %}
[loop.md](loop.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a simple loop construct. This statement repeatedly executes a block of code until explicitly terminated by a LEAVE statement.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repeat-loop.md" %}
[repeat-loop.md](repeat-loop.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute a block until a condition is met. This loop construct runs at least once and continues repeating as long as the UNTIL condition remains false.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="resignal.md" %}
[resignal.md](resignal.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Propagate error conditions. This statement allows a handler to pass an error condition back to the caller or modify the error information before passing it on.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="return.md" %}
[return.md](return.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Exit a stored function and return a value. This statement terminates function execution and sends the specified result back to the caller.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="selectinto.md" %}
[selectinto.md](selectinto.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Assign query results to variables. This statement retrieves column values from a single row and stores them in local variables or user-defined variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="signal.md" %}
[signal.md](signal.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Raise a custom error condition. This statement allows stored programs to generate specific error messages and SQLSTATEs to handle application logic exceptions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="while.md" %}
[while.md](while.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute a block while a condition is true. This loop construct checks a condition before each iteration and repeats the block as long as the condition holds.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-compound-statements-outside-of-stored-programs.md" %}
[using-compound-statements-outside-of-stored-programs.md](using-compound-statements-outside-of-stored-programs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use compound statements such as IF and BEGIN...END outside of stored programs, with the delimiter set appropriately.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="programmatic-compound-statements-cursors/" %}
[programmatic-compound-statements-cursors](programmatic-compound-statements-cursors/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about cursors in MariaDB Server's programmatic compound statements. This section details how to iterate over result sets row-by-row within stored procedures and functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="programmatic-compound-statements-diagnostics/" %}
[programmatic-compound-statements-diagnostics](programmatic-compound-statements-diagnostics/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about diagnostics in programmatic compound statements. This section covers error handling and information retrieval within stored procedures and functions for effective debugging.
{% endcolumn %}
{% endcolumns %}
