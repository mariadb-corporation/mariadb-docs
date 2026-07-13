---
name: mariadb-numeric-functions
description: "MariaDB numeric and math functions — rounding/truncation (ROUND, the TRUNCATE function vs the TRUNCATE TABLE statement, FLOOR, CEILING, SIGN, ABS), integer-vs-decimal division (the DIV operator vs /, MOD / %), powers and logs (POW/POWER, SQRT, EXP, LN, LOG, LOG2, LOG10), trigonometry (SIN, COS, TAN, ASIN, ACOS, ATAN, ATAN2, COT, PI, DEGREES, RADIANS), randomness (RAND, seeded RAND(N)), base conversion (CONV, OCT, BIN, HEX), checksums (CRC32, CRC32C), and number formatting (FORMAT). Use when writing SQL that does arithmetic, rounding, base conversion, or random sampling in MariaDB — especially where exact-vs-approximate types or division-by-zero behavior matter."
---

# MariaDB Numeric Functions

*Last updated: 2026-06-24*

Catalog of every built-in numeric/math function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at <https://mariadb.com/docs/server/reference/sql-functions/numeric-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `a / b` between two integers returns an integer (e.g. `7/2 = 3`) | `/` **always returns a decimal** — `7/2` is `3.5000` (four fractional digits by default, via `div_precision_increment`). Use `a DIV b` for integer (toward-zero) division |
| `7 DIV 2` returns a float or rounds | `DIV` returns an **integer**, discarding the remainder (`3`); it's `BIGINT`-based. Get the remainder with `MOD` / `%` |
| `x / 0` raises a division-by-zero error | By default it returns **`NULL`**. You get an error only when `ERROR_ON_DIVISION_BY_ZERO` is in `sql_mode` (it's part of the default strict mode). Same for `MOD` by zero |
| `ROUND(2.5)` uses banker's rounding (round-half-to-even) | For **`DECIMAL`/exact** values MariaDB rounds **half away from zero**: `ROUND(2.5)=3`, `ROUND(-2.5)=-3`. For **`FLOAT`/`DOUBLE`** the platform C library decides, so results can differ between operating systems — round a `DECIMAL` if you need determinism |
| Storing money in `FLOAT`/`DOUBLE` and rounding for display | `FLOAT`/`DOUBLE` are **approximate** (`0.1 + 0.2 != 0.3`). Use `DECIMAL(p,s)` for currency and anything needing exactness (up to 38 digits) |
| `TRUNCATE(x, d)` and `TRUNCATE TABLE` are related | They're unrelated despite the name. `TRUNCATE(X, D)` is the **function** that chops to `D` decimal places toward zero; `TRUNCATE TABLE` is the **DDL statement** that empties a table (see `mariadb-drop-table`) |
| `FLOOR(x)` / `CEILING(x)` always return a `BIGINT` | The return type **follows the argument**: integer/string/double args yield `BIGINT`, but a `DECIMAL` argument yields a **`DECIMAL`**. Don't assume the result fits an integer column |
| `RAND()` is fine for security tokens or unbiased sampling | `RAND()` is **not cryptographically secure**; `RAND(N)` with a constant seed is **repeatable** (good for tests, not secrets), and `RAND()` is unsafe for statement-based replication. `ORDER BY RAND()` scans the whole table — avoid on large ones |
| `MOD(n, 0)` errors, or `MOD` of a negative behaves like Python's `%` | `MOD` returns **`NULL`** for a zero divisor (unless `ERROR_ON_DIVISION_BY_ZERO`), and the result **takes the sign of the dividend** (`-7 MOD 3 = -1`), not the divisor. `N % M`, `N MOD M`, `MOD(N,M)` are equivalent |
| `FORMAT(n, 2)` returns a number you can compute with | `FORMAT` returns a **string** with locale-aware thousands separators (`'1,234,567.89'`). Feeding it back into arithmetic re-parses and truncates at the first separator |
| `CONV(n, 10, 62)` works on every version | Bases up to **62** are supported *(since 11.4)*; earlier versions cap at base 36. `CONV` returns a string at 64-bit precision |
| `CRC32('abc')` is unary and `CRC32C` always exists | `CRC32` gained an optional rolling-checksum argument — `CRC32([par,] expr)` — and `CRC32C` (Castagnoli, as used by InnoDB/MyRocks) was added, both *(since 10.8)* |

## Related operators

Arithmetic lives partly as **operators**, not functions, so they aren't in the catalog below:

- **`/`** — division; always returns a decimal. `div_precision_increment` (default 4) sets the fractional digits.
- **`DIV`** — integer division (toward zero).
- **`%` / `MOD`** — modulo; result takes the dividend's sign; `NULL` on zero divisor unless strict mode errors.

`FORMAT()` (locale-aware number-to-string) and `HEX`/`BIN` are catalogued under **`mariadb-string-functions`**, not here.

## Functions

Auto-generated from the canonical `server/reference/sql-functions/numeric-functions/` pages by `agent-skills/extractor/extract_function_category.py`; regenerate when the doc tree changes. Do not hand-edit between the markers.

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/numeric-functions -->
<!-- 36 functions, 0 pages skipped on extraction failure -->

### ABS
`ABS(X)`  
Returns the absolute (non-negative) value of `X`.

### ACOS
`ACOS(X)`  
Returns the arc cosine of `X`, that is, the value whose cosine is `X`.

### ASIN
`ASIN(X)`  
Returns the arc sine of X, that is, the value whose sine is X.

### ATAN
`ATAN(X)`  
Returns the arc tangent of X, that is, the value whose tangent is X.

### ATAN2
`ATAN(Y,X), ATAN2(Y,X)`  
Returns the arc tangent of the two variables X and Y.

### CEIL
`CEIL(X)`  
`CEIL()` is a synonym for CEILING().

### CEILING
`CEILING(X)`  
Returns the smallest integer value not less than X.

### CONV
`CONV(N,from_base,to_base)`  
Converts numbers between different number bases.

### COS
`COS(X)`  
Returns the cosine of X, where X is given in radians.

### COT
`COT(X)`  
Returns the cotangent of X.

### CRC32
`CRC32([par,]expr)`  
Computes a cyclic redundancy check (CRC) value and returns a 32-bit unsigned value.

### CRC32C
`CRC32C([par,]expr)`  
MariaDB has always included a native unary function CRC32() that computes the CRC-32 of a string using the ISO 3309 polynomial that used by zlib and many others.

### DEGREES
`DEGREES(X)`  
Returns the argument _`X`_, converted from radians to degrees.

### DIV
`DIV`  
Integer division.

### EXP
`EXP(X)`  
Returns the value of e (the base of natural logarithms) raised to the power of X.

### FLOOR
`FLOOR(X)`  
Returns the largest integer value not greater than X.

### LN
`LN(X)`  
Returns the natural logarithm of X; that is, the base-e logarithm of X.

### LOG
`LOG(X), LOG(B,X)`  
If called with one parameter, this function returns the natural logarithm of X.

### LOG10
`LOG10(X)`  
Returns the base-10 logarithm of X.

### LOG2
`LOG2(X)`  
Returns the base-2 logarithm of X.

### MOD
`MOD(N,M), N % M, N MOD M`  
Modulo operation.

### OCT
`OCT(N)`  
Returns a string representation of the octal value of N, where N is a longlong (BIGINT) number.

### PI
`PI()`  
Returns the value of π (pi).

### POW
`POW(X,Y)`  
Returns the value of X raised to the power of Y.

### POWER
`POWER(X,Y)`  
This is a synonym for POW(), which returns the value of X raised to the power of Y.

### RADIANS
`RADIANS(X)`  
Returns the argument _`X`_, converted from degrees to radians.

### RAND
`RAND(), RAND(N)`  
Returns a random DOUBLE precision floating point value v in the range 0 <= v < 1.0.

### ROUND
`ROUND(X), ROUND(X,D)`  
Rounds the argument `X` to `D` decimal places.

### SIGN
`SIGN(X)`  
Returns the sign of the argument as -1, 0, or 1, depending on whether X is negative, zero, or positive.

### SIN
`SIN(X)`  
Returns the sine of X, where X is given in radians.

### SQRT
`SQRT(X)`  
Returns the square root of X.

### TAN
`TAN(X)`  
Returns the tangent of X, where X is given in radians.

### TO_NUMBER
`TO_NUMBER(number_or_string_subject)`  
The function returns the `DOUBLE` data type for all signatures and input data types.

### TRUNCATE
`TRUNCATE(X,D)`  
Returns the number X, truncated to D decimal places.

### XXH3
`XXH3(expr)`  
`XXH3` returns a fast, non-cryptographic xxHash of a text value as a 64-bit number (`BIGINT UNSIGNED`). *(since 13.1)*

### XXH32
`XXH32(expr)`  
`XXH32` returns a fast, non-cryptographic xxHash of a text value as a 32-bit number (`INT UNSIGNED`). *(since 13.1)*
<!-- END GENERATED -->

## See Also

- **`mariadb-create-table`** — choosing `DECIMAL` vs `FLOAT`/`DOUBLE` for the columns these functions operate on
- **`mariadb-drop-table`** — the `TRUNCATE TABLE` statement (not the `TRUNCATE()` function above)
- **`mysql-to-mariadb`** (topical) — division-by-zero `sql_mode` behavior and money-in-`DECIMAL` guidance
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/numeric-functions>
