# IP Range Table Performance

## The situation

Your data includes a large set of non-overlapping 'ranges'. These could be IP addresses, datetimes (show times for a single station), zipcodes, etc.

You have pairs of start and end values; one 'item' belongs to each such 'range'. So, instinctively, you create a table with start and end of the range, plus info about the item. Your queries involve a WHERE clause that compares for being between the start and end values.

## The problem

Once you get a large set of items, performance degrades. You play with the indexes, but find nothing that works well. The indexes fail to lead to optimal functioning because the database does not understand that the ranges are non-overlapping.

## The solution

I will present a solution that enforces the fact that items cannot have overlapping ranges. The solution builds a table to take advantage of that, then uses Stored Routines to get around the clumsiness imposed by it.

## Performance

The instinctive solution often leads to scanning half the table to do just about anything, such as finding the item containing an 'address'. In complexity terms, this is Order(N).

The solution here can usually get the desired information by fetching a single row, or a small number of rows. It is Order(1).

In a large table, "counting the disk hits" is the important part of performance. Since InnoDB is used, and the PRIMARY KEY (clustered) is used, most operations hit only 1 block.

Finding the 'block' where a given IP address lives:

* For start of block: One single-row fetch using the PRIMARY KEY
* For end of block: Ditto. The record containing this will be 'adjacent' to the other record.

For allocating or freeing a block:

* 2-7 SQL statements, hitting the clustered PRIMARY KEY for the rows containing and immediately adjacent to the block.
* One SQL statement is a DELETE; if hits as many rows as are needed for the block.
* The other statements hit one row each.

## Design decisions

This is crucial to the design and its performance:

* Having just one address in the row.\
  These were alternative designs; they seemed to be no better, and possibly worse:
* That one address could have been the 'end' address.
* The routine parameters for a 'block' could have be start of this block and start of next block.
* The IPv4 parameters could have been dotted quads; I chose to keep the reference implemetation simpler instead.
* The IPv6 parameters are 32-digit hex because it was the simpler that BINARY(16) or IPv5 for a reference implementation.

The interesting work is in the Ips, not the second table, so I focus on it. The inconvenience of JOINing to the second table is small compared to the performance gains.

## Details

Two, not one, tables will be used. The first table (`Ips` in the reference implementations) is carefully designed to be optimal for all the basic operations needed. The second table contains other infomation about the 'owner' of each 'item'. In the reference implementations `owner` is an id used to JOIN the two tables. This discussion centers around `Ips` and how to efficiently map IP(s) to/from owner(s). The second table has "PRIMARY KEY(owner)".

In addition to the two-table schema, there are a set of Stored Routines to encapsulate the necessary code.

One row of Ips represents one 'item' by specifying the starting IP address and the 'owner'. The next row gives the starting IP address of the next "address block", thereby indirectly providing the ending address for the current block.

This lack of explicitly stating the "end address" leads to some clumsiness. The stored routines hide it from the user.

A special owner (indicated by '0') is reserved for "free" or "not-owned" blocks. Hence, sparse allocation of address blocks is no problem. Also, the 'free' owner is handled no differently than real owners, so there are no extra Stored Routines for such.

Links below give "reference" implementations for IPv4 and IPv6. You will need to make changes for non-IP situations, and may need to make changes even for IP situations.

These are the main stored routines provided:

* IpIncr, IpDecr -- for adding/subtracting 1
* IpStore -- for allocating/freeing a range
* IpOwner, IpRangeOwners, IpFindRanges, Owner2IpStarts, Owner2IpRanges -- for lookups
* IpNext, IpEnd -- IP of start of next block, or end of current block

None of the provided routines JOIN to the other table; you may wish to develop custom queries based on the given reference Stored Procedures.

The Ips table's size is proportional to the number of blocks. A million 'owned' blocks may be 20-50MB. This varies due to

* number of 'free' gaps (between zero and the number of owned blocks)
* datatypes used for `ip` and `owner`
* [InnoDB](../../../server-usage/storage-engines/innodb/) overhead\
  Even 100M blocks is quite manageable in today's hardware. Once things are cached, most operations would take only a few milliseconds. A trillion blocks would work, but most operations would hit the disk a few times -- only a few times.

## Reference implementation of IPv4

This specific to IPv4 (32 bit, a la '196.168.1.255'). It can handle anywhere from 'nothing assigned' (1 row) to 'everything assigned' (4B rows) 'equally' well. That is, to ask the question "who owns '11.22.33.44'" is equally efficient regardless of how many blocks of IP addresses exist in the table. (OK, caching, disk hits, etc may make a slight difference.) The one function that can vary is the one that reassigns a range to a new owner. Its speed is a function of how many existing ranges need to be consumed, since those rows will be DELETEd. (It helps that they are, by schema design, 'clustered'.)

Notes on the [Reference implementation for IPv4](https://mysql.rjweb.org/doc.php/ipv4.sql):

* Externally, the user may use the dotted quad notation (11.22.33.44), but needs to convert to INT UNSIGNED for calling the Stored Procs.
* The user is responsible for converting to/from the calling datatype (INT UNSIGNED) when accessing the stored routine; suggest [INET\_ATON](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/inet_aton.md)/[INET\_NTOA](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/inet_ntoa.md).
* The internal datatype for addresses is the same as the calling datatype (INT UNSIGNED).
* Adding and subtracting 1 (simple arithmetic).
* The datatype of an 'owner' (MEDIUMINT UNSIGNED: 0..16M) -- adjust if needed.
* The address "Off the end" (255.255.255.255+1 - represented as NULL).
* The table is initialized to one row: (ip=0, owner=0), meaning "all addresses are free\
  See the comments in the code for more details.

(The reference implementation does not handle CDRs. Such should be easy to add on, by first turning it into an IP range.)

## Reference implementation of IPv6

The code for handling IP address is more complex, but the overall structure is the same as for IPv4. Launch into it only if you need IPv6.

Notes on the [reference implementation for IPv6](https://mysql.rjweb.org/doc.php/ipv6.sql):

* Externally, IPv6 has a complex string, VARCHAR(39) CHARACTER SET ASCII. The Stored Procedure IpStr2Hex() is provided.
* The user is responsible for converting to/from the calling datatype (BINARY(16)) when accessing the stored routine; suggest [INET6\_ATON](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/inet6_aton.md)/[INET6\_NTOA](../../../reference/sql-functions/secondary-functions/miscellaneous-functions/inet6_ntoa.md).
* The internal datatype for addresses is the same as the calling datatype (BINARY(16)).
* Communication with the Stored routines is via 32-char hex strings.
* Inside the Procedures, and in the Ips table, an address is stored as BINARY(16) for efficiency. HEX() and UNHEX() are used at the boundaries.
* Adding/subtracting 1 is rather complex (see the code).
* The datatype of an 'owner' (MEDIUMINT UNSIGNED: 0..16M); 'free' is represented by 0. You may need a bigger datatype.
* The address "Off the end" (ffff.ffff.ffff.ffff.ffff.ffff.ffff.ffff+1 is represented by NULL).
* The table is initialized to one row: (UNHEX('00000000000000000000000000000000'), 0), meaning "all addresses are free.
* You may need to decide on a canonical representation of IPv4 in IPv6.\
  See the comments in the code for more details.

The INET6\* functions were first available in MySQL 5.6.3 and [MariaDB 10.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.3)

Adapting to a different non-IP 'address range' data

* The external datatype for an 'address' should be whatever is convenient for the application.
* The datatype for the 'address' in the table must be ordered, and should be as compact as possible.
* You must write the Stored functions (IpIncr, IpDecr) for incrementing/decrementing an 'address'.
* An 'owner' is an id of your choosing, but smaller is better.
* A special value (such as 0 or '') must be provided for 'free'.
* The table must be initialized to one row: (SmallestAddress, Free)

"Owner" needs a special value to represent "not owned". The reference implementations use "=" and "!=" to compare two 'owners'. Numeric values and strings work nicely with those operators; NULL does not. Hence, please do not use NULL for "not owned".

Since the datatypes are pervasive in the stored routines, adapting a reference implementation to a different concept of 'address' would require multiple minor changes.

The code enforces that consecutive blocks never have the same 'owner', so the table is of 'minimal' size. Your application can assume that such is always the case.

## Postlog

Original writing -- Oct, 2012; Notes on INET6 functions -- May, 2015.

## See also

* [Related blog](https://jorgenloland.blogspot.co.uk/2011/09/tips-and-tricks-killer-response-time.html)
* [Another approach](https://dba.stackexchange.com/questions/83458/mysql-select-with-between-optimization/83471#83471)
* [Free IP tables](https://lite.ip2location.com/)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [ipranges](https://mysql.rjweb.org/doc.php/ipranges)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
