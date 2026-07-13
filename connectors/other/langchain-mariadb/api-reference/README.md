---
description: >-
  The langchain-mariadb API reference covers four modules: vector stores,
  chat message history, expression filters, and translator for natural
  language to SQL conversion.
---

# API Reference

{% columns %}
{% column %}
{% content-ref url="vectorstores.md" %}
[vectorstores.md](vectorstores.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`MariaDBStore` provides a LangChain-compatible vector store backed by MariaDB, supporting similarity search, metadata filtering, and maximal marginal relevance retrieval.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="chat_message_histories.md" %}
[chat_message_histories.md](chat_message_histories.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`MariaDBChatMessageHistory` persists LangChain conversation history to a MariaDB database table, providing methods to add, retrieve, and clear messages per session.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="expression_filter.md" %}
[expression_filter.md](expression_filter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Expression filter reference for langchain-mariadb, documenting the operator enum, filter builder classes, and `MariaDBFilterExpressionConverter` for metadata-based vector queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="translator.md" %}
[translator.md](translator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`MariaDBTranslator` converts LangChain internal query language operations and comparisons into valid MariaDB filter dictionaries for use with structured vector store queries.
{% endcolumn %}
{% endcolumns %}
