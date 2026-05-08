---
description: >-
  Magic commands reference for the MariaDB Jupyter Kernel, covering lsmagic,
  line/bar/pie plot commands, df export, load, and the delimiter cell magic.
---

# MariaDB Jupyter Kernel Magic Commands

Below you'll find a table with all the available magic commands supported by the kernel.\
For more help information regarding the usage and parameters of each magic command, please run the `%lsmagic` command.

<table><thead><tr><th width="126">Magic</th><th width="98">Type</th><th>Description</th></tr></thead><tbody><tr><td>lsmagic</td><td>line</td><td>lists all available magic and help text for each</td></tr><tr><td>line</td><td>line</td><td>line-plots the result of the last query</td></tr><tr><td>df</td><td>line</td><td>write the result of the last query in a CSV file</td></tr><tr><td>bar</td><td>line</td><td>bar-plots the result of the last query</td></tr><tr><td>pie</td><td>line</td><td>pie-plots the result of the last query</td></tr><tr><td>load</td><td>line</td><td>loads the data from a CSV file into an existing table</td></tr><tr><td>delimiter</td><td>cell</td><td>run a SQL statement using a custom delimiter</td></tr></tbody></table>

{% @marketo/form formId="4316" %}
