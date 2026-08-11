# msql2mysql

## Description

Initially, the MySQL C API was developed to be very similar to that of the
mSQL database system.

Because of this, mSQL programs often can be converted relatively easily for use
with MySQL by changing the names of their C API functions.

The `msql2mysql` utility performs the conversion of mSQL C API
function calls to their MySQL equivalents.

{% hint style="warning" %}
**Warning:** `msql2mysql` converts the input file in place, so make a copy of the original before converting it.
{% endhint %}

## Example

```
shell> cp client-prog.c client-prog.c.orig
shell> msql2mysql client-prog.c
client-prog.c converted
```

After conversion, examine `client-prog.c` and make any necessary
post-conversion revisions.

`msql2mysql` uses the [replace](../administrative-tools/replace-utility.md#options) utility to make the function name
substitutions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
