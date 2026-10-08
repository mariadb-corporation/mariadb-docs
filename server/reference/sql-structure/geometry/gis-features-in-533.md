---
description: >-
  An overview of GIS support in MariaDB, based on the OpenGIS Simple Feature
  Access standard.
---

# GIS Features

GIS stands for [Geographic Information System](https://en.wikipedia.org/wiki/Geographic_information_system).

MySQL operates on spatial data based on the OpenGIS standards, particularly the [OpenGIS SFS](https://www.opengeospatial.org/standards/sfs) (Simple feature access, SQL option).

Initial support was based on version 05-134 of the standard. MariaDB implements a subset of the 'SQL with Geometry Types' environment proposed by the OGC. And the SQL environment was extended with a set of geometry types.

MariaDB supports spatial extensions to operate on spatial features. These features are available for [Aria](../../../server-usage/storage-engines/aria/), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/), [InnoDB](../../../server-usage/storage-engines/innodb/), NDB, and [ARCHIVE](../../../server-usage/storage-engines/archive.md) tables.

For spatial columns, Aria and MyISAM supports both [SPATIAL](spatial-index.md) and non-SPATIAL indexes. Other storage engines support non-SPATIAL indexes.

We aim at meeting the OpenGIS requirements. One thing missed in previous MariaDB versions is that the functions which check spatial relations didn't consider the actual shape of an object, instead they operate only on their bounding rectangles. These legacy functions have been left as they are and new, properly-working functions are named with an '`ST_`' prefix, in accordance with the latest OpenGIS requirements. Also, operations over geometry features were added.

## Spatial Operators

Spatial operators produce new geometries.

| Name                                                                                                            | Description                                                                    |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [ST\_UNION(A, B)](../../sql-statements/geometry-constructors/geometry-constructors/st_union.md)                 | union of A and B                                                               |
| [ST\_INTERSECTION(A, B)](../../sql-statements/geometry-constructors/geometry-constructors/st_intersection.md)   | intersection of A and B                                                        |
| [ST\_SYMDIFFERENCE(A, B)](../../sql-statements/geometry-constructors/geometry-constructors/st_symdifference.md) | symdifference, notintersecting parts of A and B                                |
| [ST\_BUFFER(A, radius)](../../sql-statements/geometry-constructors/geometry-constructors/st_buffer.md)          | returns the shape of the area that lies in 'radius' distance from the shape A. |

## Predicates

Predicates return a boolean result of the relationship.

| Name                                                                                                   | Description                     |
| ------------------------------------------------------------------------------------------------------ | ------------------------------- |
| [ST\_INTERSECTS(A, B)](../../sql-statements/geometry-constructors/geometry-relations/st-intersects.md) | if A and B have an intersection |
| [ST\_CROSSES(A, B)](../../sql-statements/geometry-constructors/geometry-relations/st-crosses.md)       | if A and B cross                |
| [ST\_EQUALS(A, B)](../../sql-statements/geometry-constructors/geometry-relations/st-equals.md)         | if A and B are equal            |
| [ST\_WITHIN(A, B)](../../sql-statements/geometry-constructors/geometry-relations/st-within.md)         | if A lies within B              |
| [ST\_CONTAINS(A,B)](../../sql-statements/geometry-constructors/geometry-relations/st-contains.md)      | if B lies within A              |
| [ST\_DISJOINT(A,B)](../../sql-statements/geometry-constructors/geometry-relations/st_disjoint.md)      | if A and B have no intersection |
| [ST\_TOUCHES(A,B)](../../sql-statements/geometry-constructors/geometry-relations/st-touches.md)        | if A touches B                  |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
