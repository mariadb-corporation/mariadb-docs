# What is Table Elimination?

The basic idea behind table elimination is that sometimes it is possible to resolve a query without even accessing some of the tables that the query refers to. One can invent many kinds of such cases, but in Table Elimination we targeted only a certain class of SQL constructs that one ends up writing when\
they are querying [highly-normalized](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/database-theory/database-normalization) data.

The sample queries were drawn from “Anchor Modeling”, a database modeling technique which takes normalization to the extreme. The [slides](https://www.anchormodeling.com/tiedostot/SU_KTH_Course_Presentation.pdf) at the [anchor modeling website](https://www.anchormodeling.com) have an in-depth explanation of Anchor modeling and its merits, but the part that's important for table elimination can be shown with an example.

Suppose the database stores information about actors, together with their names, birthdays, and ratings, where ratings can change over time:

```mermaid
erDiagram
    accTitle: Actor entity with Name, Date of Birth, and Rating attributes
    accDescr { The Actor entity has three attributes: Name, Date of Birth, and Rating. Name and Date of Birth are single-valued attributes. Rating is drawn as a stack of bubbles because it is historized, meaning several rating values are recorded for the same actor over time. }
    ACTOR {
        string Name
        date DateOfBirth
        int Rating "historized: multiple values over time"
    }
```

_The Actor entity with its Name, Date of Birth, and Rating attributes; Rating is historized, so it can hold multiple values over time._

According to anchor modeling, each attribute should go into its own table:

* the 'anchor' table which only has a synthetic primary key:

```sql
CREATE TABLE  ac_anchor(AC_ID INT PRIMARY KEY);
```

* a table for the 'name' attribute:

```sql
CREATE TABLE ac_name(AC_ID INT, ACNAM_name CHAR(N),
                     PRIMARY KEY(AC_ID));
```

* a table for the 'birthdate' attribute:

```sql
CREATE TABLE ac_dob(AC_ID INT,
                    ACDOB_birthdate DATE,
                    PRIMARY KEY(AC_ID));
```

* a table for the ‘rating’ attribute, which is historized:

```sql
CREATE TABLE ac_rating(AC_ID INT,
                       ACRAT_rating INT,
                       ACRAT_fromdate DATE,
                       PRIMARY KEY(AC_ID, ACRAT_fromdate));
```

With this approach it becomes easy to add/change/remove attributes, but this comes at a cost of added complexity in querying the data: in order to answer the simplest, select-star question of displaying actors and their current ratings one has to write outer joins:

Display actors, with their names and current ratings:

```sql
SELECT
  ac_anchor.AC_ID, ACNAM_Name, ACDOB_birthdate, ACRAT_rating
FROM
  ac_anchor
  LEFT JOIN ac_name ON ac_anchor.AC_ID=ac_name.AC_ID
  LEFT JOIN ac_dob ON ac_anchor.AC_ID=ac_dob.AC_ID
  LEFT JOIN ac_rating ON (ac_anchor.AC_ID=ac_rating.AC_ID AND
                          ac_rating.ACRAT_fromdate = 
                            (SELECT MAX(sub.ACRAT_fromdate)
                             FROM ac_rating sub WHERE sub.AC_ID = ac_rating.AC_ID))
```

We don't want to write the joins every time we need to access an actor's properties, so we’ll create a view:

```sql
CREATE VIEW actors AS
  SELECT  ac_anchor.AC_ID, ACNAM_Name,  ACDOB_birthdate, ACRAT_rating
  FROM <see the SELECT above>
```

This will allow us to access the data as if it was stored in a regular way:

```sql
SELECT ACRAT_rating FROM actors WHERE ACNAM_name='Gary Oldman'
```

And this is where table elimination will be needed.

## See Also

* This page is based on the following blog post about table elimination:[?p=58](https://s.petrunia.net/blog/?p=58)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
