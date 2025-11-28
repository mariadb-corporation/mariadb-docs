# ColumnStore Decimal Math and Scale

1. [Enable/Disable decimal to double math "Enable/Disable decimal to double math"](columnstore-decimal-math-and-scale.md#enabledisable-decimal-to-double-math)
2. [ColumnStore decimal scale "ColumnStore decimal scale"](columnstore-decimal-math-and-scale.md#columnstore-decimal-scale)
3. [Enable/disable decimal scale "Enable/disable decimal scale"](columnstore-decimal-math-and-scale.md#enabledisable-decimal-scale)
4. [Set decimal scale level "Set decimal scale level"](columnstore-decimal-math-and-scale.md#set-decimal-scale-level)

MariaDB ColumnStore has the ability to change intermediate decimal mathematical results from decimal type to double. The decimal type has approximately 17-18 digits of precision but a smaller maximum range. Whereas the double type has approximately 15-16 digits of precision, but a much larger maximum range.

\
In typical mathematical and scientific applications, the ability to avoid overflow in intermediate results with double math is likely more beneficial than the additional two digits of precision. In banking applications, however, it may be more appropriate to leave in the default decimal setting to ensure accuracy to the least significant digit.

## Enable/Disable decimal to double math

The `columnstore_double_for_decimal_math` variable is used to control the data type for intermediate decimal results. This decimal for double math may be set as a default for the instance, set at the session level, or at the statement level by toggling this variable on and off.

To enable/disable the use of the decimal to double math at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
SET columnstore_double_for_decimal_math
```

where n is:

* off (disabled, default)
* on (enabled)

## ColumnStore Decimal Scale

ColumnStore has the ability to support varied internal precision on decimal calculations. `columnstore_decimal_scale` is used internally by the ColumnStore engine to control how many significant digits to the right of the decimal point are carried through in suboperations on calculated columns. If, while running a query, you receive the message ‘aggregate overflow,’ try reducing `columnstore_decimal_scale` and running the query again. Note that, as you decrease `columnstore_decimal_scale`, you may see reduced accuracy in the least significant digit(s) of a returned calculated column. 

`columnstore_decimal_scale` is used internally by the ColumnStore engine to turn the use of this internal precision on and off. These two system variables may be set as a default for the instance or set at the session level.

### Enable/Disable Decimal Scale

To enable/disable the use of the decimal scale at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
SET columnstore_decimal_scale
```

where _n_ is off (disabled) or on (enabled).

### Set Decimal Scale Level

To set the decimal scale at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
SET columnstore_use_decimal_scale
```

where _n_ is the amount of precision desired for calculations.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
