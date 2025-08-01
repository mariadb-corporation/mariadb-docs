# Stored Procedure Internals

## Implementation Specification for Stored Procedures

### How Parsing and Execution of Queries Work

In order to execute a query, the function `sql_parse.cc:mysql_parse()` is\
called, which in turn calls the parser (`yyparse()`) with an updated Lex\
structure as the result. `mysql_parse()` then calls `mysql_execute_command()`\
which dispatches on the command code (in Lex) to the corresponding code for\
executing that particular query.

There are three structures involved in the execution of a query which are of\
interest to the [stored procedure](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/stored-routines/stored-procedures/README.md) implementation:

* Lex (mentioned above) is the "compiled" query, that is the output from\
  the parser and what is then interpreted to do the actual work.\
  It constains an enum value (sql\_command) which is the query type, and\
  all the data collected by the parser needed for the execution (table\
  names, fields, values, etc).
* THD is the "run-time" state of a connection, containing all that is\
  needed for a particular client connection, and, among other things, the\
  Lex structure currently being executed.
* `Item_*`: During parsing, all data is translated into "items", objects of\
  the subclasses of "Item", such as `Item_int`, `Item_real`, `Item_string`, etc.,\
  for basic datatypes, and also various more specialized Item types for\
  expressions to be evaluated (`Item_func` objects).

### How to Fit Stored Procedures into this Scheme

#### Overview of the Classes and Files for Stored Procedures

(More detailed APIs at the end of this page)

**class sp\_head (sp\_head.{cc,h})**

This contains, among other things, an array of "instructions" and the\
method for executing the procedure.

**class sp\_pcontext (sp\_pcontext.{cc,h}**

This is the parse context for the procedure. It's primarily used during\
parsing to keep track of local parameters, variables and labels, but\
it's also used at [CALL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/stored-routine-statements/call) time to find the parameters mode (IN, OUT or INOUT)\
and type when setting up the runtime context.

**class sp\_instr (sp\_head.{cc,h})**

This is the base class for "instructions", that is, what is generated\
by the parser. It turns out that we only need a minimum of 5 different\
sub classes:

* sp\_instr\_stmt\
  Execute a statement. This is the "call-out" any normal SQL statement,\
  like a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) etc. It contains the Lex structure for the\
  statement in question.
* sp\_instr\_set\
  Set the value of a local variable (or parameter)
* sp\_instr\_jump\
  An unconditional jump.
* sp\_instr\_jump\_if\_not\
  Jump if condition is not true. It turns out that the negative test is\
  most convenient when generating the code for the flow control\
  constructs.
* sp\_instr\_freturn\
  Return a value from a FUNCTION and exit.\
  For condition HANDLERs some special instructions are also needed, see\
  that section below.

**class sp\_rcontext (sp\_rcontext.h)**

This is the runtime context in the THD structure.\
It contains an array of items, the parameters and local variables for\
the currently executing stored procedure.\
This means that variable value lookup is in runtime is constant time,\
a simple index operation.

**class Item\_splocal (Item.{cc,h})**

This is a subclass of Item. Its sole purpose is to hide the fact that\
the real Item is actually in the current frame (runtime context).\
It contains the frame offset and defers all methods to the real Item\
in the frame. This is what the parser generates for local variables.

**Utility Functions (sp.{cc,h})**

This contains functions for creating, dropping and finding a stored\
procedure in the [mysql.proc table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) (or the internal cache).

#### Parsing CREATE PROCEDURE

When parsing a [CREATE PROCEDURE](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/stored-routines/stored-procedures/create-procedure.md) the parser first initializes the`sphead` and `spcont` (runtime context) fields in the Lex.\
The sql\_command code for the result of parsing a is`SQLCOM_CREATE_PROCEDURE`.

The parsing of the parameter list and body is relatively\
straightforward:

* Parameters:\
  name, type and mode (IN/OUT/INOUT) is pushed to `spcont`
* Declared local variables:\
  Same as parameters (mode is then IN)
* Local Variable references:\
  If an identifier is found in `spcont`, an `Item_splocal` is created\
  with the variable's frame index, otherwise an `Item_field` or `Item_ref`\
  is created (as before).
* Statements:\
  The Lex in THD is replaced by a new Lex structure and the statement,\
  is parsed as usual. A `sp_instr_stmt` is created, containing the new\
  Lex, and added to the instructions in `sphead`.\
  Afterwards, the procedure's Lex is restored in THD.
* SET var:\
  Setting a local variable generates a `sp_instr_set` instruction,\
  containing the variable's frame offset, the expression (an Item),\
  and the type.
* Flow control:\
  Flow control constructs such as [IF](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/programmatic-compound-statements/if.md), [WHILE](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/programmatic-compound-statements/while.md), etc, generate a conditional\
  and unconditional jumps in the "obvious" way, but a few notes may\
  be required:
* Forward jumps: When jumping forward, the exact destination is not\
  known at the time of the creation of the jump instruction. The
  1. sphead`therefore contains a list of instruction-label pairs for each forward reference. When the position later is known, the instructions in the list are updated with the correct location.`
* Loop constructs have optional labels. If a loop doesn't have a\
  label, an anonymous label is generated to simplify the parsing.
* There are two types of CASE. The "simple" case is implemented\
  with an anonymous variable bound to the value to be tested.

**A Simple Example**

Parsing the procedure:

```
CREATE PROCEDURE a(s CHAR(16))
      BEGIN
        DECLARE x INT;
        SET x = 3;
        WHILE x > 0 DO
          SET x = x-1;
          INSERT INTO db.tab VALUES (x, s);
        END WHILE;
      END
```

would generate the following structures:

```
______
      thd: |      |     _________
           | lex -+--->|         |                     ___________________
           |______|    | spcont -+------------------->| "s",in,char(16):0 |
                       | sphead -+------              |("x",in,int     :1)|
                       |_________|      |             |___________________|
                                    ____V__________________
                                   | m_name: "a"           |
                                   | m_defstr: "create ..."|
                                   | m_instr: ...          |
                                   |_______________________|
```

Note that the contents of the `spcont` is changing during the parsing,\
at all times reflecting the state of the would-be runtime frame.\
The `m_instr` is an array of instructions:

```
Pos.  Instruction
       0    sp_instr_set(1, '3')
       1    sp_instr_jump_if_not(5, 'x>0')
       2    sp_instr_set(1, 'x-1')
       3    sp_instr_stmt('insert into ...')
       4    sp_instr_jump(1)
       5    <end>
```

Here, '3', 'x>0', etc, represent the Items or Lex for the respective\
expressions or statements.

#### Parsing CREATE FUNCTION

[Creating a function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function) is essentially the same thing as for a PROCEDURE,\
with the addition that a FUNCTION has a return type and a RETURN\
statement, but no OUT or INOUT parameters.

The main difference during parsing is that we store the result type\
in the sp\_head. However, there are big differences when it comes to\
invoking a FUNCTION. (See below.)

#### Storing, Caching, Dropping

As seen above, the entired definition string, including the "CREATE\
PROCEDURE" (or "FUNCTION") is kept. The procedure definition string is\
stored in the table mysql.proc with the name and type as the key, the\
type being one of the enum ("procedure","function").

A PROCEDURE is just stored in the [mysql.proc table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table). A FUNCTION has an\
additional requirement. They will be called in expressions with the same\
syntax as UDFs, so UDFs and stored FUNCTIONs share the namespace. Thus,\
we must make sure that we do not have UDFs and FUNCTIONs with the same\
name (even if they are stored in different places).

This means that we can reparse the procedure as many time as we want.\
The first time, the resulting Lex is used to store the procedure in\
the database (using the function sp.c:sp\_create\_procedure()).

The simplest way would be to just leave it at that, and re-read the\
procedure from the database each time it is called. (And in fact, that's\
the way the earliest implementation will work.)\
However, this is not very efficient, and we can do better. The full\
implementation should work like this:

1. Upon creation time, parse and store the procedure. Note that we still\
   need to parse it to catch syntax errors, but we can't check if called\
   procedures exists for instance.
2. Upon first CALL, read from the database, parse it, and cache the\
   resulting Lex in memory. This time we can do more error checking.
3. Upon subsequent CALLs, use the cached Lex.

Note that this implies that the Lex structure with its sphead must be\
reentrant, that is, reusable and shareable between different threads\
and calls. The runtime state for a procedure is kept in the sp\_rcontext\
in THD.

The mechanisms of storing, finding, and dropping procedures are\
encapsulated in the files sp.{cc,h}.

#### CALLing a Procedure

A [CALL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/stored-routine-statements/call) is parsed just like any statement. The resulting Lex has the\
sql\_command SQLCOM\_CALL, the procedure's name and the parameters are\
pushed to the Lex' value\_list.

sql\_parse.cc:mysql\_execute\_command() then uses sp.cc:sp\_find() to\
get the sp\_head for the procedure (which may have been read from the\
database or fetched from the in-memory cache) and calls the sp\_head's\
method execute().\
Note: It's important that substatements called by the procedure do not\
do send\_ok(). Fortunately, there is a flag in THD->net to disable\
this during CALLs. If a substatement fails, it will however send\
an error back to the client, so the CALL mechanism must return\
immediately and without sending an error.

The sp\_head::execute() method works as follows:

1. Keep a pointer to the old runtime context in THD (if any)
2. Create a new runtime context. The information about the required size\
   is in sp\_head's parse time context.
3. Push each parameter (from the CALL's Lex->value\_list) to the new\
   context. If it's an OUT or INOUT parameter, the parameter's offset\
   in the caller's frame is set in the new context as well.
4. For each instruction, call its execute() method.\
   The result is a pointer to the next instruction to execute (or NULL)\
   if an error occurred.
5. On success, set the new values of the OUT and INOUT parameters in\
   the caller's frame.

#### USE database

Before executing the instruction we also keeps the current default\
database (if any). If this was changed during execution (i.e. a [USE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/use-database)\
statement has been executed), we restore the current database to the\
original.

This is the most useful way to handle USE in procedures. If we didn't,\
the caller would find himself in a different database after calling\
a function, which can be confusing.\
Restoring the database also gives full freedom to the procedure writer:

* It's possible to write "general" procedures that are independent of\
  the actual database name.
* It's possible to write procedures that work on a particular database\
  by calling USE, without having to use fully qualified table names\
  everywhere (which doesn't help if you want to call other, "general",\
  procedures anyway).

#### Evaluating Items

There are three occasions where we need to evaluate an expression:

* When SETing a variable
* When CALLing a procedure
* When testing an expression for a branch (in IF, WHILE, etc)

The semantics in stored procedures is "call-by-value", so we have to\
evaluate any "func" Items at the point of the CALL or SET, otherwise\
we would get a kind of "lazy" evaluation with unexpected results with\
respect to OUT parameters for instance.\
For this the support function, `sp_head.cc:eval_func_item()` is needed.

#### Calling a FUNCTION

Functions don't have an explicit call keyword like procedures. Instead,\
they appear in expressions with the conventional syntax "fun(arg, ...)".\
The problem is that we already have [User Defined Functions](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/user-defined-functions/README.md) (UDFs) which\
are called the same way. A UDF is detected by the lexical analyzer (not\
the parser!), in the `find_keyword()` function, and returns a `UDF_*_FUNC`\
or `UDA_*_SUM` token with the `udf_func` object as the yylval.

So, stored functions must be handled in a similar way, and as a\
consequence, UDFs and functions must not have the same name.

#### Detecting and Parsing a FUNCTION Invocation

The existence of UDFs are checked during the lexical analysis (in\
sql\_lex.cc:find\_keyword()). This has the drawback that they must\
exist before they are referred to, which was ok before SPs existed,\
but then it becomes a problem. The first implementation of SP FUNCTIONs\
will work the same way, but this should be fixed a.s.a.p. (This will\
required some reworking of the way UDFs are handled, which is why it's\
not done from the start.)\
For the time being, a FUNCTION is detected the same way, and returns\
the token SP\_FUNC. During the parsing we only check for the _existence_\
of the function, we don't parse it, since wa can't call the parser\
recursively.

When encountering a SP\_FUNC with parameters in the expression parser,\
an instance of the new Item\_func\_sp class is created. Unlike UDFs, we\
don't have different classes for different return types, since we at\
this point don't know the type.

#### Collecting FUNCTIONs to invoke

A FUNCTION differs from a PROCEDURE in one important aspect: Whereas a\
PROCEDURE is CALLed as statement by itself, a FUNCTION is invoked\
"on-the-fly" during the execution of _another_ statement.\
This makes things a lot more complicated compared to CALL:

* We can't read and parse the FUNCTION from the [mysql.proc table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) at the\
  point of invocation; the server requires that all tables used are\
  opened and locked at the beginning of the query execution.\
  One "obvious" solution would be to simply push "mysql.proc" to the list\
  of tables used by the query, but this implies a "join" with this table\
  if the query is a select, so it doesn't work (and we can't exclude this\
  table easily; since a privileged used might in fact want to search\
  the proc table).\
  Another solution would of course be to allow the opening and closing\
  of the [mysql.proc table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) during a query execution, but this it not\
  possible at the present.

So, the solution is to collect the names of the referred FUNCTIONs during\
parsing in the lex.\
Then, before doing anything else in `mysql_execute_command()`, read all\
functions from the database an keep them in the THD, where the function`sp_find_function()` can find them during the execution.\
Note: Even with an in-memory cache, we must still make sure that the\
functions are indeed read and cached at this point.\
The code that read and cache functions from the database must also be\
invoked recursively for each read FUNCTION to make sure we have _all_ the\
functions we need.

#### Parsing DROP PROCEDURE/FUNCTION

The procedure name is pushed to Lex->value\_list.\
The sql\_command code for the result of parsing a is`SQLCOM_DROP_PROCEDURE`/`SQLCOM_DROP_FUNCTION`.

Dropping is done by simply getting the procedure with the sp\_find()\
function and calling `sp_drop()` (both in `sp.{cc,h}`).

[DROP PROCEDURE](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/stored-routines/stored-procedures/drop-procedure.md)/[DROP FUNCTION](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/server-usage/stored-routines/stored-functions/drop-function.md) also supports the non-standard "IF EXISTS", analogous to other [DROP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop) statements in MariaDB.

#### Condition and Handlers

Condition names are lexical entities and are kept in the parser context\
just like variables. But, condition are just "aliases" for SQLSTATE\
strings, or mysqld error codes (which is a non-standard extension in\
MySQL), and are only used during parsing.

Handlers comes in three types, CONTINUE, EXIT and UNDO. The latter is\
like an EXIT handler with an implicit rollback, and is currently not\
implemented.\
The EXIT handler jumps to the end of its BEGIN-END block when finished.\
The CONTINUE handler returns to the statement following that which\
invoked the handler.

The handlers in effect at any point is part of each thread's runtime\
state, so we need to push and pop handlers in the sp\_rcontext during\
execution. We use special instructions for this:

* sp\_instr\_hpush\_jump\
  Push a handler. The instruction contains the necessary information,\
  like which conditions we handle and the location of the handler.\
  The jump takes us to the location after the handler code.
* sp\_instr\_hpop\
  Pop the handlers of the current frame (which we are just leaving).

It might seems strange to jump past the handlers like that, but there's\
no extra cost in doing this, and for technical reasons it's easiest for\
the parser to generate the handler instructions when they occur in the\
source.

When an error occurs, one of the error routines is called and an error\
message is normally sent back to the client immediately.\
Catching a condition must be done in these error routines (there are\
quite a few) to prevent them from doing this. We do this by calling\
a method in the THD's sp\_rcontext (if there is one). If a handler is\
found, this is recorded in the context and the routine returns without\
sending the error message.\
The execution loop (sp\_head::execute()) checks for this after each\
statement and invokes the handler that has been found. If several\
errors or warnings occurs during one statement, only the first is\
caught, the rest are ignored.

Invoking and returning from a handler is trivial in the EXIT case.\
We simply jump to it, and it will have an sp\_instr\_jump as its last\
instruction.

Calling and returning from a CONTINUE handler poses some special\
problems. Since we need to return to the point after its invocation,\
we push the return location on a stack in the sp\_rcontext (this is\
done by the execution loop). The handler then ends with a special\
instruction, sp\_instr\_hreturn, which returns to this location.

CONTINUE handlers have one additional problem: They are parsed at\
the lexical level where they occur, so variable offsets will assume\
that it's actually called at that level. However, a handler might be\
invoked from a sub-block where additional local variables have been\
declared, which will then share the location of any local variables\
in the handler itself. So, when calling a CONTINUE handler, we need\
to save any local variables above the handler's frame offset, and\
restore them upon return. (This is not a problem for EXIT handlers,\
since they will leave the block anyway.)\
This is taken care of by the execution loop and the sp\_instr\_hreturn\
instruction.

**Examples**

EXIT handler:

```
begin
        declare x int default 0;

        begin
          declare exit handler for 'XXXXX' set x = 1;

          (statement1);
          (statement2);
        end;
        (statement3);
      end
```

```
Pos.  Instruction
       0    sp_instr_set(0, '0')
       1    sp_instr_hpush_jump(4, 1)           # location and frame size
       2    sp_instr_set(0, '1')
       3    sp_instr_jump(6)
       4    sp_instr_stmt('statement1')
       5    sp_instr_stmt('statement2')
       6    sp_instr_hpop(1)
       7    sp_instr_stmt('statement3')
```

CONTINUE handler:

```
CREATE PROCEDURE hndlr1(val INT)
      BEGIN
        DECLARE x INT DEFAULT 0;
        DECLARE foo CONDITION FOR 1146;
        DECLARE CONTINUE HANDLER FOR foo SET x = 1;

        INSERT INTO t3 VALUES ("hndlr1", val);     # Non-existing table?
        IF x>0 THEN
          INSERT INTO t1 VALUES ("hndlr1", val);   # This instead then
        END IF;
      END|
```

```
Pos.  Instruction
       0    sp_instr_set(1, '0')
       1    sp_instr_hpush_jump(4, 2)
       2    sp_instr_set(1, '1')
       3    sp_instr_hreturn(2)                 # frame size
       4    sp_instr_stmt('insert ... t3 ...')
       5    sp_instr_jump_if_not(7, 'x>0')
       6    sp_instr_stmt('insert ... t1 ...')
       7    sp_instr_hpop(2)
```

#### Cursors

For stored procedures to be really useful, you want to have cursors.\
MySQL doesn't yet have "real" cursor support (with API and ODBC support,\
allowing updating, arbitrary scrolling, etc), but a simple asensitive,\
non-scrolling, read-only cursor can be implemented in SPs using the\
class Protocol\_cursor.\
This class intecepts the creation and sending of results sets and instead\
stores it in-memory, as MYSQL\_FIELDS and MYSQL\_ROWS (as in the client API).

To support this, we need the usual name binding support in sp\_pcontext\
(similar to variables and conditions) to keep track on declared cursor\
names, and a corresponding run-time mechanism in sp\_rcontext.\
Cursors are lexically scoped like everything with a body or BEGIN/END\
block, so they are pushed and poped as usual (see conditions and variables\
above).\
The basic operations on a cursor are OPEN, FETCH and CLOSE, which will\
each have a corresponding instruction. In addition, we need instructions\
to push a new cursor (this will encapsulate the LEX of the SELECT statement\
of the cursor), and a pop instruction:

* sp\_instr\_cpush\
  Push a cursor to the sp\_rcontext. This instruction contains the LEX\
  for the select statement
* sp\_instr\_cpop\
  Pop a number of cursors from the sp\_rcontext.
* sp\_instr\_copen\
  Open a cursor: This will execute the select and get the result set\
  in a sepeate memroot.
* sp\_instr\_cfetch\
  Fetch the next row from the in-memory result set. The instruction\
  contains a list of the variables (frame offsets) to set.
* sp\_instr\_cclose\
  Free the result set.

A cursor is a separate class, sp\_cursor (defined in sp\_rcontex.h) which\
encapsulates the basic operations used by the above instructions.\
This class contains the LEX, Protocol\_cursor object, and its memroot,\
as well as the cursor's current state.\
Compiling and executing is fairly straight-forward. sp\_instr\_copen is\
a subclass of sp\_instr\_stmt and uses its mechanism to execute a\
substatement.

**Example**

```
begin
        declare x int;
        declare c cursor for select a from t1;

        open c;
        fetch c into x;
        close c;
      end
```

```
Pos.  Instruction
       0    sp_instr_cpush('select a from ...')
       1    sp_instr_copen(0)                   # The 0'th cursor
       2    sp_instr_cfetch(0)                  # Contains the variable list
       3    sp_instr_cclose(0)
       4    sp_instr_cpop(1)
```

#### The SP cache

There are two ways to cache SPs:

1. one global cache, share by all threads/connections,
2. one cache per thread.

There are pros and cons with both methods:

1.

* Pros: Save memory, each SP only read from table once,
* Cons: Needs locking (= serialization at access), requires thread-safe\
  data structures,

1.

* Pros: Fast, no locking required (almost), limited thread-safe\
  requirement,
* Cons: Uses more memory, each SP read from table once per thread.

Unfortunately, we cannot use alternative 1 for the time being, as most\
of the data structures to be cached (lex and items) are not reentrant\
and thread-safe. (Things are modified at execution, we have THD pointers\
stored everywhere, etc.)\
This leaves us with alternative 2, one cache per thread; or actually\
two, since we keep FUNCTIONs and PROCEDUREs in separate caches.\
This is not that terrible; the only case when it will perform\
significantly worse than a global cache is when we have an application\
where new threads are connecting, calling a procedure, and disconnecting,\
over and over again.

The cache implementation itself is simple and straightforward, a hashtable\
wrapped in a class and a C API (see APIs below).

There is however one issue with multiple caches: dropping and altering\
procedures. Normally, this should be a very rare event in a running\
system; it's typically something you do during development and testing,\
so it's not unthinkable that we would simply ignore the issue and let\
any threads running with a cached version of an SP keep doing so until\
its disconnected.\
But assuming we want to keep the caches consistent with respect to drop\
and alter, it can be done:

1. A global counter is needed, initialized to 0 at start.
2. At each DROP or ALTER, increase the counter by one.
3. Each cache has its own copy of the counter, copied at the last read.
4. When looking up a name in the cache, first check if the global counter\
   is larger than the local copy.\
   If so, clear the cache and return "not found", and update the local\
   counter; otherwise, lookup as usual.

This minimizes the cost to a single brief lock for the access of an\
integer when operating normally. Only in the event of an actual drop or\
alter, is the cache cleared. This may seem to be drastic, but since we\
assume that this is a rare event, it's not a problem.\
It would of course be possible to have a much more fine-grained solution,\
keeping track of each SP, but the overhead of doing so is not worth the\
effort.

#### Class and Function APIs

This is an outline of the key types. Some types and other details\
in the actual files have been omitted for readability.

**The parser context: sp\_pcontext.h**

```
typedef enum
      {
        sp_param_in,
        sp_param_out,
        sp_param_inout
      } sp_param_mode_t;

      typedef struct
      {
        LEX_STRING name;
        enum enum_field_types type;
        sp_param_mode_t mode;
        uint offset;                    // Offset in current frame
        my_bool isset;
      } sp_pvar_t;

      typedef struct sp_cond_type
      {
        enum { number, state, warning, notfound, exception } type;
        char sqlstate[6];
        uint mysqlerr;
      } sp_cond_type_t;

      class sp_pcontext
      {
        sp_pcontext();

        // Return the maximum frame size
        uint max_framesize();

        // Return the current frame size
        uint current_framesize();

        // Return the number of parameters
        uint params();

        // Set the number of parameters to the current frame size
        void set_params();

        // Set type of the variable at offset 'i' in the frame
        void set_type(uint i, enum enum_field_types type);

        // Mark the i:th variable to "set" (i.e. having a value) with
        // 'val' true.
        void set_isset(uint i, my_bool val);

        // Push the variable 'name' to the frame.
        void push_var(LEX_STRING *name,
                      enum enum_field_types type, sp_param_mode_t mode);

        // Pop 'num' variables from the frame.
        void pop_var(uint num = 1);

        // Find variable by name
        sp_pvar_t *find_pvar(LEX_STRING *name);

        // Find variable by index
        sp_pvar_t *find_pvar(uint i);

        // Push label 'name' of instruction index 'ip' to the label context
        sp_label_t *push_label(char *name, uint ip);

        // Find label 'name' in the context
        sp_label_t *find_label(char *name);

        // Return the last pushed label
        sp_label_t *last_label();

        // Return and remove the last pushed label.
        sp_label_t *pop_label();

        // Push a condition to the context
        void push_cond(LEX_STRING *name, sp_cond_type_t *val);

        // Pop a 'num' condition from the context
        void pop_cond(uint num);

        // Find a condition in the context
        sp_cond_type_t *find_cond(LEX_STRING *name);

        // Increase the handler count
        void add_handler();

        // Returns the handler count
        uint handlers();

	// Push a cursor
        void push_cursor(LEX_STRING *name);

	// Find a cursor
	my_bool find_cursor(LEX_STRING *name, uint *poff);

	// Pop 'num' cursors
	void pop_cursor(uint num);

	// Return the number of cursors
	uint cursors();
      }
```

**Run-time context (call frame): sp\_rcontext.h:**

```
#define SP_HANDLER_NONE      0
    #define SP_HANDLER_EXIT      1
    #define SP_HANDLER_CONTINUE  2
    #define SP_HANDLER_UNDO      3

    typedef struct
    {
      struct sp_cond_type *cond;
      uint handler;             // Location of handler
      int type;
      uint foffset;             // Frame offset for the handlers declare level
    } sp_handler_t;

    class sp_rcontext
    {
      // 'fsize' is the max size of the context, 'hmax' the number of handlers,
      // 'cmax' the number of cursors
      sp_rcontext(uint fsize, uint hmax, , uint cmax);

      // Push value (parameter) 'i' to the frame
      void push_item(Item *i);

      // Set slot 'idx' to value 'i'
      void set_item(uint idx, Item *i);

      // Return the item in slot 'idx'
      Item *get_item(uint idx);

      // Set the "out" index 'oidx' for slot 'idx. If it's an IN slot,
      // use 'oidx' -1.
      void set_oindex(uint idx, int oidx);

      // Return the "out" index for slot 'idx'
      int get_oindex(uint idx);

      // Set the FUNCTION result
      void set_result(Item *i);

      // Get the FUNCTION result
      Item *get_result();

      // Push handler at location 'h' for condition 'cond'. 'f' is the
      // current variable frame size.
      void push_handler(sp_cond_type_t *cond, uint h, int type, uint f);

      // Pop 'count' handlers
      void pop_handlers(uint count);

      // Find a handler for this error. This sets the state for a found
      // handler in the context. If called repeatedly without clearing,
      // only the first call's state is kept.
      int find_handler(uint sql_errno);

      // Returns 1 if a handler has been found, with '*ip' and '*fp' set
      // to the handler location and frame size respectively.
      int found_handler(uint *ip, uint *fp);

      // Clear the found handler state.
      void clear_handler();

      // Push a return address for a CONTINUE handler
      void push_hstack(uint ip);

      // Pop the CONTINUE handler return stack
      uint pop_hstack();

      // Save variables from frame index 'fp' and up.
      void save_variables(uint fp);

      // Restore saved variables from to frame index 'fp' and up.
      void restore_variables(uint fp);

      // Push a cursor for the statement (lex)
      void push_cursor(LEX *lex);

      // Pop 'count' cursors
      void pop_cursors(uint count);

      // Pop all cursors
      void pop_all_cursors();

      // Get the 'i'th cursor
      sp_cursor *get_cursor(uint i);

    }
```

**The procedure: sp\_head.h:**

```
#define TYPE_ENUM_FUNCTION  1
      #define TYPE_ENUM_PROCEDURE 2

      class sp_head
      {
        int m_type;             // TYPE_ENUM_FUNCTION or TYPE_ENUM_PROCEDURE

        sp_head();

        void init(LEX_STRING *name, LEX *lex, LEX_STRING *comment, char suid);

        // Store this procedure in the database. This is a wrapper around
        // the function sp_create_procedure().
        int create(THD *);

        // Invoke a FUNCTION
        int
        execute_function(THD *thd, Item **args, uint argcount, Item **resp);

        // CALL a PROCEDURE
        int
        execute_procedure(THD *thd, List<Item> *args);

        // Add the instruction to this procedure.
        void add_instr(sp_instr *);

        // Returns the number of instructions.
        uint instructions();

        // Returns the last instruction
        sp_instr *last_instruction();

        // Resets lex in 'thd' and keeps a copy of the old one.
        void reset_lex(THD *);

        // Restores lex in 'thd' from our copy, but keeps some status from the
        // one in 'thd', like ptr, tables, fields, etc.
        void restore_lex(THD *);

        // Put the instruction on the backpatch list, associated with
        // the label.
        void push_backpatch(sp_instr *, struct sp_label *);

        // Update all instruction with this label in the backpatch list to
        // the current position.
        void backpatch(struct sp_label *);

        // Returns the SP name (with optional length in '*lenp').
        char *name(uint *lenp = 0);

        // Returns the result type for a function
        Item_result result();

        // Sets various attributes
        void sp_set_info(char *creator, uint creatorlen,
                         longlong created, longlong modified,
                         bool suid, char *comment, uint commentlen);
      }
```

**Instructions**

**The base class**

```
class sp_instr
        {
          // 'ip' is the index of this instruction
          sp_instr(uint ip);

          // Execute this instrution.
          // '*nextp' will be set to the index of the next instruction
          // to execute. (For most instruction this will be the
          // instruction following this one.)
          // Returns 0 on success, non-zero if some error occurred.
          virtual int execute(THD *, uint *nextp)
        }
<<code>>


===== Statement instruction
<<code>>
        class sp_instr_stmt : public sp_instr
        {
          sp_instr_stmt(uint ip);

          int execute(THD *, uint *nextp);

          // Set the statement's Lex
          void set_lex(LEX *);

          // Return the statement's Lex
          LEX *get_lex();
        }
```

**SET instruction**

```
class sp_instr_set : public sp_instr
        {
          // 'offset' is the variable's frame offset, 'val' the value,
          // and 'type' the variable type.
          sp_instr_set(uint ip,
                       uint offset, Item *val, enum enum_field_types type);

          int execute(THD *, uint *nextp);
        }
```

**Unconditional jump**

```
class sp_instr_jump : public sp_instr
        {
          // No destination, must be set.
          sp_instr_jump(uint ip);

          // 'dest' is the destination instruction index.
          sp_instr_jump(uint ip, uint dest);

          int execute(THD *, uint *nextp);

          // Set the destination instruction 'dest'.
          void set_destination(uint dest);
        }
```

**Conditional jump**

```
class sp_instr_jump_if_not : public sp_instr_jump
        {
          // Jump if 'i' evaluates to false. Destination not set yet.
          sp_instr_jump_if_not(uint ip, Item *i);

          // Jump to 'dest' if 'i' evaluates to false.
          sp_instr_jump_if_not(uint ip, Item *i, uint dest)

          int execute(THD *, uint *nextp);
        }
```

**Return a function value**

```
class sp_instr_freturn : public sp_instr
        {
          // Return the value 'val'
          sp_instr_freturn(uint ip, Item *val, enum enum_field_types type);
          
          int execute(THD *thd, uint *nextp);
        }
```

**Push a handler and jump**

```
class sp_instr_hpush_jump : public sp_instr_jump
        {
          // Push handler of type 'htype', with current frame size 'fp'
          sp_instr_hpush_jump(uint ip, int htype, uint fp);

          int execute(THD *thd, uint *nextp);

          // Add condition for this handler
          void add_condition(struct sp_cond_type *cond);
        }
```

**Pops handlers**

```
class sp_instr_hpop : public sp_instr
        {
          // Pop 'count' handlers
          sp_instr_hpop(uint ip, uint count);

          int execute(THD *thd, uint *nextp);
        }
```

**Return from a CONTINUE handler**

```
class sp_instr_hreturn : public sp_instr
        {
          // Return from handler, and restore variables to 'fp'.
          sp_instr_hreturn(uint ip, uint fp);

          int execute(THD *thd, uint *nextp);
        }
```

**Push a CURSOR**

```
class sp_instr_cpush : public sp_instr_stmt
	{
          // Push a cursor for statement 'lex'
	  sp_instr_cpush(uint ip, LEX *lex)

	  int execute(THD *thd, uint *nextp);
        }
```

**Pop CURSORs**

```
class sp_instr_cpop : public sp_instr_stmt
	{
          // Pop 'count' cursors
	  sp_instr_cpop(uint ip, uint count)

	  int execute(THD *thd, uint *nextp);
        }
```

**Open a CURSOR**

```
class sp_instr_copen : public sp_instr_stmt
	{
          // Open the 'c'th cursor
	  sp_instr_copen(uint ip, uint c);

	  int execute(THD *thd, uint *nextp);
        }
```

**Close a CURSOR**

```
class sp_instr_cclose : public sp_instr
	{
          // Close the 'c'th cursor
	  sp_instr_cclose(uint ip, uint c);

	  int execute(THD *thd, uint *nextp);
        }
```

**Fetch a row with CURSOR**

```
class sp_instr_cfetch : public sp_instr
	{
          // Fetch next with the 'c'th cursor
	  sp_instr_cfetch(uint ip, uint c);

	  int execute(THD *thd, uint *nextp);

	  // Add a target variable for the fetch
	  void add_to_varlist(struct sp_pvar *var);
        }
```

**Utility functions: sp.h**

```
#define SP_OK                 0
      #define SP_KEY_NOT_FOUND     -1
      #define SP_OPEN_TABLE_FAILED -2
      #define SP_WRITE_ROW_FAILED  -3
      #define SP_DELETE_ROW_FAILED -4
      #define SP_GET_FIELD_FAILED  -5
      #define SP_PARSE_ERROR       -6

      // Finds a stored procedure given its name. Returns NULL if not found.
      sp_head *sp_find_procedure(THD *, LEX_STRING *name);

      // Store the procedure 'name' in the database. 'def' is the complete
      // definition string ("create procedure ...").
      int sp_create_procedure(THD *,
                              char *name, uint namelen,
                              char *def, uint deflen,
                              char *comment, uint commentlen, bool suid);

      // Drop the procedure 'name' from the database.
      int sp_drop_procedure(THD *, char *name, uint namelen);

      // Finds a stored function given its name. Returns NULL if not found.
      sp_head *sp_find_function(THD *, LEX_STRING *name);

      // Store the function 'name' in the database. 'def' is the complete
      // definition string ("create function ...").
      int sp_create_function(THD *,
                             char *name, uint namelen,
                             char *def, uint deflen,
                             char *comment, uint commentlen, bool suid);

      // Drop the function 'name' from the database.
      int sp_drop_function(THD *, char *name, uint namelen);
```

**The cache: sp\_cache.h**

```
/* Initialize the SP caching once at startup */
      void sp_cache_init();

      /* Clear the cache *cp and set *cp to NULL */
      void sp_cache_clear(sp_cache **cp);

      /* Insert an SP to cache. If **cp points to NULL, it's set to a
         new cache */
      void sp_cache_insert(sp_cache **cp, sp_head *sp);

      /* Lookup an SP in cache */
      sp_head *sp_cache_lookup(sp_cache **cp, char *name, uint namelen);

      /* Remove an SP from cache */
      void sp_cache_remove(sp_cache **cp, sp_head *sp);
```

### The mysql.proc schema

This is the [mysql.proc table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/mysql-proc-table) used in [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104):

```
CREATE TABLE `proc` (
  `db` char(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `name` char(64) NOT NULL DEFAULT '',
  `type` enum('FUNCTION','PROCEDURE','PACKAGE','PACKAGE BODY') NOT NULL,
  `specific_name` char(64) NOT NULL DEFAULT '',
  `language` enum('SQL') NOT NULL DEFAULT 'SQL',
  `sql_data_access` enum('CONTAINS_SQL','NO_SQL','READS_SQL_DATA','MODIFIES_SQL_DATA') NOT NULL DEFAULT 'CONTAINS_SQL',
  `is_deterministic` enum('YES','NO') NOT NULL DEFAULT 'NO',
  `security_type` enum('INVOKER','DEFINER') NOT NULL DEFAULT 'DEFINER',
  `param_list` blob NOT NULL,
  `returns` longblob NOT NULL,
  `body` longblob NOT NULL,
  `definer` char(141) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `created` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `modified` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `sql_mode` set('REAL_AS_FLOAT','PIPES_AS_CONCAT','ANSI_QUOTES','IGNORE_SPACE','IGNORE_BAD_TABLE_OPTIONS','ONLY_FULL_GROUP_BY','NO_UNSIGNED_SUBTRACTION','NO_DIR_IN_CREATE','POSTGRESQL','ORACLE','MSSQL','DB2','MAXDB','NO_KEY_OPTIONS','NO_TABLE_OPTIONS','NO_FIELD_OPTIONS','MYSQL323','MYSQL40','ANSI','NO_AUTO_VALUE_ON_ZERO','NO_BACKSLASH_ESCAPES','STRICT_TRANS_TABLES','STRICT_ALL_TABLES','NO_ZERO_IN_DATE','NO_ZERO_DATE','INVALID_DATES','ERROR_FOR_DIVISION_BY_ZERO','TRADITIONAL','NO_AUTO_CREATE_USER','HIGH_NOT_PRECEDENCE','NO_ENGINE_SUBSTITUTION','PAD_CHAR_TO_FULL_LENGTH','EMPTY_STRING_IS_NULL','SIMULTANEOUS_ASSIGNMENT') NOT NULL DEFAULT '',
  `comment` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `character_set_client` char(32) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `collation_connection` char(32) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `db_collation` char(32) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `body_utf8` longblob DEFAULT NULL,
  `aggregate` enum('NONE','GROUP') NOT NULL DEFAULT 'NONE',
  PRIMARY KEY (`db`,`name`,`type`)
) ENGINE=Aria DEFAULT CHARSET=utf8 PAGE_CHECKSUM=1 TRANSACTIONAL=1 COMMENT='Stored Procedures'
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
