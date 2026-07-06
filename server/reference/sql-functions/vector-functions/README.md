---
description: >-
  Explore vector functions. This section details SQL functions for manipulating
  and querying vector data types, enabling efficient similarity search and AI/ML
  applications within your  database.
---

# Vector Functions

{% columns %}
{% column %}
{% content-ref url="vector-functions-vec_distance.md" %}
[vector-functions-vec_distance.md](vector-functions-vec_distance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate distance between vectors. This function computes the distance between two vectors using either Euclidean or Cosine metric, depending on the index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vec_distance_cosine.md" %}
[vec_distance_cosine.md](vec_distance_cosine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate Cosine distance. This function computes the Cosine distance between two vectors, measuring the cosine of the angle between them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vec_distance_euclidean.md" %}
[vec_distance_euclidean.md](vec_distance_euclidean.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate Euclidean distance. This function computes the Euclidean (L2) distance between two vectors, representing the straight-line distance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vec_fromtext.md" %}
[vec_fromtext.md](vec_fromtext.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert text to vector. This function parses a JSON array string representation of a vector and converts it into the binary VECTOR data type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vec_totext.md" %}
[vec_totext.md](vec_totext.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert vector to text. This function takes a binary VECTOR data type and returns its JSON array string representation.
{% endcolumn %}
{% endcolumns %}
