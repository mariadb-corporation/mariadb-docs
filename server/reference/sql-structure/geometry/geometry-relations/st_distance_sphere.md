# ST\_DISTANCE\_SPHERE

**MariaDB starting with** [**10.5.10**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10510-release-notes)

`ST_DISTANCE_SPHERE` was introduced in [MariaDB 10.2.38](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10238-release-notes), [MariaDB 10.3.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-10329-release-notes), [MariaDB 10.4.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-10419-release-notes) and [MariaDB 10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10510-release-notes).

## Syntax

```bnf
ST_DISTANCE_SPHERE(g1,g2,[r])
```

## Description

Returns the spherical distance in meters between two geometries (point or multipoint) on a sphere. The optional radius _r_ is in meters, must be positive, and defaults to the Earth's radius (6370986 meters) if not specified. If either of the two geometries are not valid, NULL is returned.

## Example

```sql
SET @zenica   = ST_GeomFromText('POINT(17.907743 44.203438)');
SET @sarajevo = ST_GeomFromText('POINT(18.413076 43.856258)');
SELECT ST_Distance_Sphere(@zenica, @sarajevo);
+----------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo) |
+----------------------------------------+
|                      55878.59337591705 |
+----------------------------------------+

SELECT ST_Distance_Sphere(@zenica, @sarajevo, 6370986);
+-------------------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo, 6370986) |
+-------------------------------------------------+
|                               55878.59337591705 |
+-------------------------------------------------+

SELECT ST_Distance_Sphere(@zenica, @sarajevo, 200);    
+---------------------------------------------+
| ST_Distance_Sphere(@zenica, @sarajevo, 200) |
+---------------------------------------------+
|                           1.754158410516584 |
+---------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
