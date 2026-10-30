---
description: >-
  Reference for the JSON user-defined functions bundled with the CONNECT engine: installing them, argument handling, and each Json, Jbin, and Jfile function.
---

# CONNECT JSON UDFs

Although such functions written by other parties do exist,\[1] CONNECT provides its own UDFs that are specifically adapted to the JSON table type and easily available because, being inside the CONNECT library or DLL, they require no additional module to be loaded (see [CONNECT - Compiling JSON UDFs in a Separate Library](../../connect-compiling-json-udfs-in-a-separate-library.md) to make these functions in a separate library module).

Here is the list of the CONNECT functions; more can be added if required.

| Name                     | Type      | Return   | Description                                                                                                                                                                                                                                                                                       |
| ------------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| jbin\_array              | Function  | STRING\* | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       |
| jbin\_array\_add         | Function  | STRING\* | Adds to its first array argument its second arguments.                                                                                                                                                                                                                                            |
| jbin\_array\_add\_values | Function  | STRING\* | Adds to its first array argument all following arguments.                                                                                                                                                                                                                                         |
| jbin\_array\_delete      | Function  | STRING\* | Deletes the nth element of its first array argument.                                                                                                                                                                                                                                              |
| jbin\_file               | Function  | STRING\* | Returns of a (json) file contain.                                                                                                                                                                                                                                                                 |
| jbin\_get\_item          | Function  | STRING\* | Access and returns a json item by a JPATH key.                                                                                                                                                                                                                                                    |
| jbin\_insert\_item       | Function  | STRING   | Insert item values located to paths.                                                                                                                                                                                                                                                              |
| jbin\_item\_merge        | Function  | STRING\* | Merges two arrays or two objects.                                                                                                                                                                                                                                                                 |
| jbin\_object             | Function  | STRING\* | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      |
| jbin\_object\_nonull     | Function  | STRING\* | Make a JSON object containing its not null arguments.                                                                                                                                                                                                                                             |
| jbin\_object\_add        | Function  | STRING\* | Adds to its first object argument its second argument.                                                                                                                                                                                                                                            |
| jbin\_object\_delete     | Function  | STRING\* | Deletes the nth element of its first object argument.                                                                                                                                                                                                                                             |
| jbin\_object\_key        | Function  | STRING\* | Make a JSON object for key/value pairs.                                                                                                                                                                                                                                                           |
| jbin\_object\_list       | Function  | STRING\* | Returns the list of object keys as an array.                                                                                                                                                                                                                                                      |
| jbin\_set\_item          | Function  | STRING   | Set item values located to paths.                                                                                                                                                                                                                                                                 |
| jbin\_update\_item       | Function  | STRING   | Update item values located to paths.                                                                                                                                                                                                                                                              |
| jfile\_bjson             | Function  | STRING   | Convert a pretty=0 file to another BJson file.                                                                                                                                                                                                                                                    |
| jfile\_convert           | Function  | STRING   | Convert a Json file to another pretty=0 file.                                                                                                                                                                                                                                                     |
| jfile\_make              | Function  | STRING   | Make a json file from its json item first argument.                                                                                                                                                                                                                                               |
| json\_array              | Function  | STRING   | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       |
| json\_array\_add         | Function  | STRING   | Adds to its first array argument its second arguments.                                                                                               |
| json\_array\_add\_values | Function  | STRING   | Adds to its first array argument all following arguments.                                                                                                                                                                                                                                         |
| json\_array\_delete      | Function  | STRING   | Deletes the nth element of its first array argument.                                                                                                                                                                                                                                              |
| json\_array\_grp         | Aggregate | STRING   | Makes JSON arrays from coming argument.                                                                                                                                                                                                                                                           |
| json\_file               | Function  | STRING   | Returns the contains of (json) file.                                                                                                                                                                                                                                                              |
| json\_get\_item          | Function  | STRING   | Access and returns a json item by a JPATH key.                                                                                                                                                                                                                                                    |
| json\_insert\_item       | Function  | STRING   | Insert item values located to paths.                                                                                                                                                                                                                                                              |
| json\_item\_merge        | Function  | STRING   | Merges two arrays or two objects.                                                                                                                                                                                                                                                                 |
| json\_locate\_all        | Function  | STRING   | Returns the JPATH’s of all occurrences of an element.                                                                                                                                                                                                                                             |
| json\_make\_array        | Function  | STRING   | Make a JSON array containing its arguments.                                                                                                                                                                                                                                                       |
| json\_make\_object       | Function  | STRING   | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      |
| json\_object             | Function  | STRING   | Make a JSON object containing its arguments.                                                                                                                                                                                                                                                      |
| json\_object\_delete     | Function  | STRING   | Deletes the nth element of its first object argument.                                                                                                                                                                                                                                             |
| json\_object\_grp        | Aggregate | STRING   | Makes JSON objects from coming arguments.                                                                                                                                                                                                                                                         |
| json\_object\_list       | Function  | STRING   | Returns the list of object keys as an array.                                                                                                                                                                                                                                                      |
| json\_object\_nonull     | Function  | STRING   | Make a JSON object containing its not null arguments.                                                                                                                                                                                                                                             |
| json\_serialize          | Function  | STRING   | Serializes the return of a “Jbin” function.                                                                                                                                                                                                                                                       |
| json\_set\_item          | Function  | STRING   | Set item values located to paths.                                                                                                                                                                                                                                                                 |
| json\_update\_item       | Function  | STRING   | Update item values located to paths.                                                                                                                                                                                                                                                              |
| jsonvalue                | Function  | STRING   | Make a JSON value from its unique argument. |
| jsoncontains             | Function  | INTEGER  | Returns 0 or 1 if an element is contained in the document.                                                                                                                                                                                                                                        |
| jsoncontains\_path       | Function  | INTEGER  | Returns 0 or 1 if a JPATH is contained in the document.                                                                                                                                                                                                                                           |
| jsonget\_string          | Function  | STRING   | Access and returns a string element by a JPATH key.                                                                                                                                                                                                                                               |
| jsonget\_int             | Function  | INTEGER  | Access and returns an integer element by a JPATH key.                                                                                                                                                                                                                                             |
| jsonget\_real            | Function  | REAL     | Access and returns a real element by a JPATH key.                                                                                                                                                                                                                                                 |
| jsonlocate               | Function  | STRING   | Returns the JPATH to access one element.                                                                                                                                                                                                                                                          |

String values are mapped to JSON strings. These strings are automatically escaped to conform to the JSON syntax. The automatic escaping is bypassed when the value has an alias beginning with ‘json\_’. This is automatically the case when a JSON UDF argument is another JSON UDF whose name begins with “json\_” (not case sensitive). This is why all functions that do not return a Json item are not prefixed by “json\_”.

Argument string values, for some functions, can alternatively be json file names. When this is ambiguous, alias them as _jfile\__. Full path should be used because UDF functions has no means to know what the current database is. Apparently, when the file name path is not full, it is based on the MariaDB data directory but I am not sure it is always true.

Numeric values are (big) integers, double floating point values or decimal values. Decimal values are character strings containing a numeric representation and are treated as strings. Floating point values contain a decimal point and/or an exponent. Integers are written without decimal points.

To install these functions execute the following commands:\[2]

**Note**

Json function names are often written on this page with leading upper case letters for clarity. It is possible to do so in SQL queries because function names are case insensitive. However, when creating or dropping them, their names must match the case they are in the library module, which is in lower case.

On Unix systems (from Connect 1.7.02):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_convert RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_bjson RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On Unix systems (from Connect 1.6):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On Unix systems (until Connect 1.5):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect.so';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect.so';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect.so';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect.so';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect.so';
```

On WIndows (from Connect 1.7.02):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_convert RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_bjson RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

On WIndows (from Connect 1.6):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_make_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

On WIndows (until Connect 1.5):

```
CREATE FUNCTION jsonvalue RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonset_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_grp_size RETURNS INTEGER soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_array_grp RETURNS STRING soname 'ha_connect';
CREATE AGGREGATE FUNCTION json_object_grp RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonlocate RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_locate_all RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsoncontains RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsoncontains_path RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION json_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_string RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jsonget_int RETURNS INTEGER soname 'ha_connect';
CREATE FUNCTION jsonget_real RETURNS REAL soname 'ha_connect';
CREATE FUNCTION json_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_file RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jfile_make RETURNS STRING soname 'ha_connect';
CREATE FUNCTION json_serialize RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add_values RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_array_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_nonull RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_key RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_add RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_delete RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_object_list RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_item_merge RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_get_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_set_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_insert_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_update_item RETURNS STRING soname 'ha_connect';
CREATE FUNCTION jbin_file RETURNS STRING soname 'ha_connect';
```

## Jfile\_Bjson

JFile\_Bjson was introduced in MariaDB.

```
Jfile_Bjson(in_file_name, out_file_name, lrecl)
```

Converts the first argument pretty=0 json file to Bjson file. B(inary)json is a pre-parsed json format. It is described below in the Performance chapter (available in next Connect versions).

## Jfile\_Convert

JFile\_Convert was introduced in MariaDB.

```
Jfile_Convert(in_file_name, out_file_name, lrecl)
```

Converts the first argument json file to another _pretty=0_ json file. The third integer argument is the record length to use. This is often required to process huge json files that would be very slow if they were in _pretty=2_ format.

This is done without completely parsing the file, is very fast and requires no big memory.

## Jfile\_Make

Jfile\_Make was added in CONNECT 1.4

```
Jfile_Make(arg1, arg2, [arg3], …)
```

The first argument must be a json item (if it is just a string, Jfile\_Make will try its best to see if it is a json item or an input file name). The following arguments are a string file name and an integer pretty value (defaulting to 2) in any order. This function creates a json file containing the first argument item.

The returned string value is the created file name. If not specified as an argument, the file name can in some cases be retrieved from the first argument; in such cases the file itself is modified.

This function can be used to create or format a json file. For instance, supposing we want to format the file tb.json, this can be done with the query:

```
SELECT Jfile_Make('tb.json' jfile_, 2);
```

The tb.json file are changed to:

```
[
  {
    "_id": 5,
    "type": "food",
    "ratings": [
      5,
      8,
      9
    ]
  },
  {
    "_id": 6,
    "type": "car",
    "ratings": [
      5,
      9
    ]
  }
]
```

## Json\_Array\_Add

```
Json_Array_Add(arg1, arg2, [arg3][, arg4][, ...])
```

Note: The following describes this function for CONNECT version 1.4 only. The first argument must be a JSON array. The second argument is added as member of this array:

```
SELECT Json_Array_Add(Json_Array(56,3.1416,'machin',NULL),
'One more') ARRAY;
```

| Array                                   |
| --------------------------------------- |
| \[56,3.141600,"machin",null,"One more"] |

Note: The first array is not escaped, its (alias) name beginning with ‘json\_’.

Now we can see how adding an author to the JSAMPLE2 table can alternatively be done:

```
UPDATE jsample2 SET 
  json_author = json_array_add(json_author, json_object('Charles' FIRSTNAME, 'Dickens' LASTNAME)) 
  WHERE isbn = '9782840825685';
```

Note: Calling a column returning JSON a name prefixed by json\_ (like json\_author here) is good practice and removes the need to give it an alias to prevent escaping when used as an argument.

Additional arguments:\
If a third integer argument is given, it specifies the position (zero based) of the added value:

```
SELECT Json_Array_Add('[5,3,8,7,9]' json_, 4, 2) ARRAY;
```

| Array          |
| -------------- |
| \[5,3,4,8,7,9] |

If a string argument is added, it specifies the Json path to the array to be modified. For instance:

```
SELECT Json_Array_Add('{"a":1,"b":2,"c":[3,4]}' json_, 5, 1, 'c');
```

| Json\_Array\_Add('{"a":1,"b":2,"c":\[3, 4]}' json\_, 5, 1, 'c') |
| --------------------------------------------------------------- |
| {"a":1,"b":2,"c":\[3,5,4]}                                      |

## Json\_Array\_Add\_Values

Json\_Array\_Add\_Values added in CONNECT 1.4 replaces the function Json\_Array\_Add of CONNECT version 1.3.

```
Json_Array_Add_Values(arg, arglist)
```

The first argument must be a JSON array string. Then all other arguments are added as members of this array:

```
SELECT Json_Array_Add_Values
  (Json_Array(56, 3.1416, 'machin', NULL), 'One more', 'Two more') ARRAY;
```

| Array                                              |
| -------------------------------------------------- |
| \[56,3.141600,"machin",null,"One more","Two more"] |

## Json\_Array\_Delete

```
Json_Array_Delete(arg1, arg2 [,arg3] [...])
```

The first argument should be a JSON array. The second argument is an integer indicating the rank (0 based conforming to general json usage) of the element to delete:

```
SELECT Json_Array_Delete(Json_Array(56,3.1416,'foo',NULL),1) ARRAY;
```

| Array            |
| ---------------- |
| \[56,"foo",null] |

Now we can see how to delete the second author from the JSAMPLE2 table:

```
UPDATE jsample2 SET json_author = json_array_delete(json_author, 1) 
  WHERE isbn = '9782840825685';
```

A Json path can be specified as a third string argument

## Json\_Array\_Grp

```
Json_Array_Grp(arg)
```

This is an aggregate function that makes an array filled from values coming from the rows retrieved by a query. Let us suppose we have the pet table:

| name    | race   | number |
| ------- | ------ | ------ |
| John    | dog    | 2      |
| Bill    | cat    | 1      |
| Mary    | dog    | 1      |
| Mary    | cat    | 1      |
| Lisbeth | rabbit | 2      |
| Kevin   | cat    | 2      |
| Kevin   | bird   | 6      |
| Donald  | dog    | 1      |
| Donald  | fish   | 3      |

The query:

```
SELECT name, json_array_grp(race) FROM pet GROUP BY name;
```

will return:

| name    |
| ------- |
| Bill    |
| Donald  |
| John    |
| Kevin   |
| Lisbeth |
| Mary    |

One problem with the JSON aggregate functions is that they construct their result in memory and cannot know the needed amount of storage, not knowing the number of rows of the used table.

Therefore, the number of values for each group is limited. This limit is the value of JsonGrpSize whose default value is 10 but can be set using the JsonSet\_Grp\_Size function. Nevertheless, working on a larger table is possible, but only after setting JsonGrpSize to the ceiling of the number of rows per group for the table. Try not to set it to a very large value to avoid memory exhaustion.

## JsonContains

```
JsonContains(json_doc, item [, int])<
```

This function can be used to check whether an item is contained in a document. Its arguments are the same than the ones of the JsonLocate function; only the return value changes. The integer returned value is 1 is the item is contained in the document or 0 otherwise.

## JsonContains\_Path

```
JsonContains_Path(json_doc, path)
```

This function can be used to check whether a Json path is contained in the document. The integer returned value is 1 is the path is contained in the document or 0 otherwise.

## Json\_File

```
Json_File(arg1, [arg2, [arg3]], …)
```

The first argument must be a file name. This function returns the text of the file that is supposed to be a json file. If only one argument is specified, the file text is returned without being parsed. Up to two additional arguments can be specified:

A string argument is the path to the sub-item to be returned. An integer argument specifies the pretty format value of the file.

This function is chiefly used to get the json item argument of other json functions from a json file. For instance, supposing the file tb.json is:

```
{ "_id" : 5, "type" : "food", "ratings" : [ 5, 8, 9 ] }
{ "_id" : 6, "type" : "car", "ratings" : [ 5, 9 ] }
```

Extracting a value from it can be done with a query such as:

```
SELECT JsonGet_String(Json_File('tb.json', 0), '$[1].type') "Type";
```

This query returns:

| Type |
| ---- |
| car  |

However, we’ll see that, most of the time, it is better to use Jbin\_File or to directly specify the file name in queries. In particular this function should not be used for queries that must modify the json item because, even if the modified json is returned, the file itself would be unchanged.

## Json\_Get\_Item

Json\_Get\_Item was added in CONNECT 1.4.

```
Json_Get_Item(arg1, arg2, …)
```

This function returns a subset of the json document passed as first argument. The second argument is the json path of the item to be returned and should be one returning a json item (terminated by a ‘\*’). If not, the function will try to make it right but this is not foolproof. For instance:

```
SELECT Json_Get_Item(Json_Object('foo' AS "first", Json_Array('a', 33) 
  AS "json_second"), 'second') AS "item";
```

The correct path should have been ‘second.\*’), but in this simple case the function was able to make it right. The returned item:

| item      |
| --------- |
| \["a",33] |

Note: The array is aliased “json\_second” to indicate it is a json item and avoid escaping it. However, the “json\_” prefix is skipped when making the object and must not be added to the path.

## JsonGet\_Grp\_Size

```
JsonGet_Grp_Size(val)
```

This function returns the JsonGrpSize value.

## JsonGet\_String / JsonGet\_Int / JsonGet\_Real

JsonGet\_String, JsonGet\_Int and JsonGet\_Real were added in CONNECT 1.4.

```
JsonGet_String(arg1, arg2, [arg3] …)
JsonGet_Int(arg1, arg2, [arg3] …)
JsonGet_Real(arg1, arg2, [arg3] …)
```

The first argument should be a JSON item. If it is a string with no alias, it are converted as a json item. The second argument is the path of the item to be located in the first argument and returned, eventually converted according to the used function:

```
SELECT 
JsonGet_String('{"qty":7,"price":29.50,"garanty":null}','price') "String",
JsonGet_Int('{"qty":7,"price":29.50,"garanty":null}','price') "Int",
JsonGet_Real('{"qty":7,"price":29.50,"garanty":null}','price') "Real";
```

This query returns:

| String | Int | Real               |
| ------ | --- | ------------------ |
| 29.50  | 29  | 29.500000000000000 |

The function _JsonGet\_Real_ can be given a third argument to specify the number of decimal digits of the returned value. For instance:

```
SELECT 
JsonGet_Real('{"qty":7,"price":29.50,"garanty":null}','price',4) "Real";
```

This query returns:

| String |
| ------ |
| 29.50  |

The given path can specify all operators for arrays except the “expand” \[\*] operator). For instance:

```
SELECT 
JsonGet_Int(Json_Array(45,28,36,45,89), '[4]') "Rank",
JsonGet_Int(Json_Array(45,28,36,45,89), '[#]') "Number",
JsonGet_String(Json_Array(45,28,36,45,89), '[","]') "Concat",
JsonGet_Int(Json_Array(45,28,36,45,89), '[+]') "Sum",
JsonGet_Real(Json_Array(45,28,36,45,89), '[!]', 2) "Avg";
```

The result:

| Rank | Number | Concat         | Sum | Avg   |
| ---- | ------ | -------------- | --- | ----- |
| 89   | 5      | 45,28,36,45,89 | 243 | 48.60 |

## Json\_Item\_Merge

```
Json_Item_Merge(arg1, arg2, …)
```

This function merges two arrays or two objects. For arrays, this is done by adding to the first array all the values of the second array. For instance:

```
SELECT Json_Item_Merge(Json_Array('a','b','c'), Json_Array('d','e','f')) AS "Result";
```

The function returns:

| Result                     |
| -------------------------- |
| \["a","b","c","d","e","f"] |

For objects, the pairs of the second object are added to the first object if the key does not yet exist in it; otherwise the pair of the first object is set with the value of the matching pair of the second object. For instance:

```
SELECT Json_Item_Merge(Json_Object(1 "a", 2 "b", 3 "c"), Json_Object(4 "d",5 "b",6 "f")) 
  AS "Result";
```

The function returns:

| Result                          |
| ------------------------------- |
| {"a":1,"b":5,"c":3,"d":4,"f":6} |

## JsonLocate

```
JsonLocate(arg1, arg2, [arg3], …):
```

The first argument must be a JSON tree. The second argument is the item to be located. The item to be located can be a constant or a json item. Constant values must be equal in type and value to be found. This is "shallow equality" – strings, integers and doubles won't match.

This function returns the json path to the located item or null if it is not found:

```
SELECT JsonLocate('{"AUTHORS":[{"FN":"Jules", "LN":"Verne"}, 
  {"FN":"Jack", "LN":"London"}]}' json_, 'Jack') PATH;
```

This query returns:

| Path             |
| ---------------- |
| $.AUTHORS\[1].FN |

The path syntax is the same used in JSON CONNECT tables.

By default, the path of the first occurrence of the item is returned. The third parameter can be used to specify the occurrence whose path is to be returned. For instance:

```
SELECT 
JsonLocate('[45,28,[36,45],89]',45) FIRST,
JsonLocate('[45,28,[36,45],89]',45,2) SECOND,
JsonLocate('[45,28,[36,45],89]',45.0) `wrong type`,
JsonLocate('[45,28,[36,45],89]','[36,45]' json_) JSON;
```

| first | second    | wrong type | json  |
| ----- | --------- | ---------- | ----- |
| $\[0] | $\[2]\[1] |            | $\[2] |

For string items, the comparison is case sensitive by default. However, it is possible to specify a string to be compared case insensitively by giving it an alias beginning by “ci”:

```
SELECT JsonLocate('{"AUTHORS":[{"FN":"Jules", "LN":"Verne"}, 
  {"FN":"Jack", "LN":"London"}]}' json_, 'VERNE' ci) PATH;
```

| Path             |
| ---------------- |
| $.AUTHORS\[0].LN |

## Json\_Locate\_All

```
Json_Locate_All(arg1, arg2, [arg3], …):
```

The first argument must be a JSON item. The second argument is the item to be located. This function returns the paths to all locations of the item as an array of strings:

```
SELECT Json_Locate_All('[[45,28],[[36,45],89]]',45);
```

This query returns:

| All paths                      |
| ------------------------------ |
| \["$\[0]\[0]","$\[1]\[0]\[1]"] |

The returned array can be applied other functions. For instance, to get the number of occurrences of an item in a json tree, you can do:

```
SELECT JsonGet_Int(Json_Locate_All('[[45,28],[[36,45],89]]',45), '$[#]') "Nb of occurs";
```

The displayed result:

| Nb of occurs |
| ------------ |
| 2            |

If specified, the third integer argument set the depth to search in the document. This means the maximum items in the paths. This value defaults to 10 but can be increased for complex documents or reduced to set the maximum wanted depth of the returned paths.

## Json\_Make\_Array

```
Json_Make_Array(val1, …, valn)
```

Json\_Make\_Array returns a string denoting a JSON array with all its arguments as members:

```
SELECT Json_Make_Array(56, 3.1416, 'My name is "Foo"', NULL);
```

| Json\_Make\_Array(56, 3.1416, 'My name is "Foo"',N ULL) |
| ------------------------------------------------------- |
| \[56,3.141600,"My name is "Foo"",null]                  |

Note: The argument list can be void. If so, a void array is returned.

## Json\_Make\_Object

```
Json_Make_Object(arg1, …, argn)
```

Json\_Make\_Object returns a string denoting a JSON object. For instance:

```
SELECT Json_Make_Object(56, 3.1416, 'machin', NULL);
```

The object is filled with pairs corresponding to the given arguments. The key of each pair is made from the argument (default or specified) alias.

| Json\_Make\_Object(56, 3.1416, 'machin', NULL)            |
| --------------------------------------------------------- |
| {"56":56,"3.1416":3.141600,"machin":"machin","NULL":null} |

When needed, it is possible to specify the keys by giving an alias to the arguments:

```
SELECT Json_Make_Object(56 qty, 3.1416 price, 'machin' truc, NULL garanty);
```

| Json\_Make\_Object(56 qty,3.1416 price,'machin' truc, NULL garanty) |
| ------------------------------------------------------------------- |
| {"qty":56,"price":3.141600,"truc":"machin","garanty":null}          |

If the alias is prefixed by ‘json\_’ (to prevent escaping) the key name is stripped from that prefix.

This function is chiefly useful when entering values retrieved from a table, the key being by default the column name:

```
SELECT Json_Make_Object(matricule, nom, titre, salaire) FROM connect.employe WHERE nom = 'PANTIER';
```

| Json\_Make\_Object(matricule, nom, titre, salaire)                             |
| ------------------------------------------------------------------------------ |
| {"matricule":40567,"nom":"PANTIER","titre":"DIRECTEUR","salaire":14000.000000} |

## Json\_Object\_Add

```
Json_Object_Add(arg1, arg2, [arg3] …)
```

The first argument must be a JSON object. The second argument is added as a pair to this object:

```
SELECT Json_Object_Add
  ('{"item":"T-shirt","qty":27,"price":24.99}' json_old,'blue' color) newobj;
```

| newobj                                                       |
| ------------------------------------------------------------ |
| {"item":"T-shirt","qty":27,"price":24.990000,"color":"blue"} |

Note: If the specified key already exists in the object, its value is replaced by the new one.

The third string argument is a Json path to the target object.

## Json\_Object\_Delete

```
Json_Object_Delete(arg1, arg2, [arg3] …):
```

The first argument must be a JSON object. The second argument is the key of the pair to delete:

```
SELECT Json_Object_Delete('{"item":"T-shirt","qty":27,"price":24.99}' json_old, 'qty') newobj;
```

| newobj                           |
| -------------------------------- |
| {"item":"T-shirt","price":24.99} |

The third string argument is a Json path to the object to be the target of deletion.

## Json\_Object\_Grp

```
Json_Object_Grp(arg1,arg2)
```

This function works like Json\_Array\_Grp. It makes a JSON object filled with value pairs whose keys are passed from its first argument and values are passed from its second argument.

This can be seen with the query:

```
SELECT name, json_object_grp(NUMBER,race) FROM pet GROUP BY name;
```

This query returns:

| name    | json\_object\_grp(number,race) |
| ------- | ------------------------------ |
| Bill    | {"cat":1}                      |
| Donald  | {"dog":1,"fish":3}             |
| John    | {"dog":2}                      |
| Kevin   | {"cat":2,"bird":6}             |
| Lisbeth | {"rabbit":2}                   |
| Mary    | {"dog":1,"cat":1}              |

## Json\_Object\_Key

```
Json_Object_Key([key1, val1 [, …, keyn, valn]])
```

Return a string denoting a JSON object. For instance:

```
SELECT Json_Object_Key('qty', 56, 'price', 3.1416, 'truc', 'machin', 'garanty', NULL);
```

The object is filled with pairs made from each key/value arguments.

| Json\_Object\_Key('qty', 56, 'price', 3.1416, 'truc', 'machin', 'garanty', NULL) |
| -------------------------------------------------------------------------------- |
| {"qty":56,"price":3.141600,"truc":"machin","garanty":null}                       |

## Json\_Object\_List

```
Json_Object_List(arg1, …):
```

The first argument must be a JSON object. This function returns an array containing the list of all keys existing in the object:

```
SELECT Json_Object_List(Json_Object(56 qty,3.1416 price,'machin' truc, NULL garanty))
  "Key List";
```

| Key List                          |
| --------------------------------- |
| \["qty","price","truc","garanty"] |

## Json\_Object\_Nonull

```
Json_Object_Nonull(arg1, …, argn)
```

This function works like [Json\_Make\_Object](#json_make_object) but “null” arguments are ignored and not inserted in the object.\
Arguments are regarded as “null” if they are JSON null values, void arrays or objects, or arrays or objects containing only null members.

It is mainly used to avoid constructing useless null items when converting tables (see later).

## Json\_Object\_Values

```
Json_Object_Values(json_object)
```

The first argument must be a JSON object. This function returns an array containing the list of all values existing in the object:

```
SELECT Json_Object_Values('{"One":1,"Two":2,"Three":3}') "Value List";
```

| Value List |
| ---------- |
| \[1,2,3]   |

## JsonSet\_Grp\_Size

```
JsonSet_Grp_Size(val)
```

This function is used to set the JsonGrpSize value. This value is used by the following aggregate functions as a ceiling value of the number of items in each group. It returns the JsonGrpSize value that can be its default value when passed 0 as argument.

## Json\_Set\_Item / Json\_Insert\_Item / Json\_Update\_Item

```
Json_{Set | Insert | Update}_Item(json_doc, [item, path [, val, path …]])
```

These functions insert or update data in a JSON document and return the result. The value/path pairs are evaluated left to right. The document produced by evaluating one pair becomes the new value against which the next pair is evaluated.

* Json\_Set\_Item replaces existing values and adds non-existing values.
* Json\_Insert\_Item inserts values without replacing existing values.
* Json\_Update\_Item replaces only existing values.

Example:

```
SET @j = Json_Array(1, 2, 3, Json_Object_Key('quatre', 4));
SELECT Json_Set_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Set",
Json_Insert_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Insert",
Json_Update_Item(@j, 'foo', '$[1]', 5, '$[3].cinq') AS "Update";
```

This query returns:

| Set                                | Insert                         | Update                    |
| ---------------------------------- | ------------------------------ | ------------------------- |
| \[1,"foo",3,{"quatre":4,"cinq":5}] | \[1,2,3,{"quatre":4,"cinq":5}] | \[1,"foo",3,{"quatre":4}] |

## JsonValue

```
JsonValue (val)
```

Returns a JSON value as a string, for instance:

```
SELECT JsonValue(3.1416);
```

| JsonValue(3.1416) |
| ----------------- |
| 3.141600          |

## Notes

1. See for instance: [json-functions](../../../../../reference/sql-functions/special-functions/json-functions/), [lib\_mysqludf\_json#readme](https://github.com/mysqludf/lib_mysqludf_json#readme) and [json\_udf\_functions\_version\_04](https://blogs.oracle.com/svetasmirnova/entry/json_udf_functions_version_04)
2. This will not work when CONNECT is compiled embedded

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
