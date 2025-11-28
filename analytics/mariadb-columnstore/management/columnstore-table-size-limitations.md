# ColumnStore Table Size Limitations

MariaDB ColumnStore has a hard limit of 4096 columns per table.

However, it's likely that you run into other limitations before hitting that limit, including:

* Row size limit of tables. This varies, depending on the storage engine you're using. For example, [InnoDB has a row size of 64KB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview#maximum-row-size) which indirectly limits the number of columns.
* Size limit of `.frm` files. Those files hold the column description of tables. Column descriptions vary in length. Once all column descriptions combined reach a length of 64KB, the table's `.frm` file is full, limiting the number of columns you can have in a table.

Given that, the maximum number of columns a ColumnStore table can effectively have is around **2000 columns**.

