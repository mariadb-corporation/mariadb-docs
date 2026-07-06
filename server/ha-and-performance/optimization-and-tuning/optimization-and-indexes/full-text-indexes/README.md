---
description: >-
  Implement full-text indexes in MariaDB Server for efficient text search. This
  section guides you through creating and utilizing these indexes to optimize
  queries on large text datasets.
---

# Full-Text Indexes

{% columns %}
{% column %}
{% content-ref url="full-text-index-overview.md" %}
[full-text-index-overview.md](full-text-index-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Definitive full-text index guide: MATCH() AGAINST syntax, FULLTEXT index creation, NATURAL/BOOLEAN/QUERY EXPANSION modes, stopwords, ft_min_word_length.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="full-text-index-stopwords.md" %}
[full-text-index-stopwords.md](full-text-index-stopwords.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains stopwords for full-text indexes, the differing default lists in MyISAM and InnoDB, and how to override them, plus the full default MyISAM stopword list.
{% endcolumn %}
{% endcolumns %}
