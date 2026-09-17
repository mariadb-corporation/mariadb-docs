# Error 3048: Out of range error

| Error Code | SQLSTATE | Error                          | Description                                 |
| ---------- | -------- | ------------------------------ | ------------------------------------------- |
| 3048       |          | ER\_STD\_OUT\_OF\_RANGE\_ERROR | Out of range error: %-.256s in function %s. |

## Possible Causes and Solutions

### Function Arguments Outside the Expected Bounds

Functions arguments have an expected range, and this error is returned if this range is exceeded. Follow the documentation for the specific function indicated in the error message. For example, the [ST\_GeoHash](../../sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash.md) function expects the longitude and latitude parameters to be between -180 and 180. In this case, the longitude argument is invalid:

```
SELECT ST_GeoHash(181,30,15);                    
ERROR 3048 (HY000): Out of range error: Longitude should be [-180,180] in function ST_GeoHash.
```

By providing a longitude argument within the expected range, the error is no longer returned:

```
SELECT ST_GeoHash(180,30,15);
+-----------------------+
| ST_GeoHash(180,30,15) |
+-----------------------+
| xvrfxvrfxvrfxvr       |
+-----------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
