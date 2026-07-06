---
description: >-
  Optimizing queries that fetch the latest items on a topic, such as news
  feeds.
---

# Optimizing for "Latest News"-style Queries

## The problem space

Let's say you have "news articles" (rows in a table) and want a web page showing the latest ten articles about a particular topic.

Variants on "topic":

* Category
* Tag
* Provider (of news article)
* Manufacturer (of item for sale)
* Ticker (financial stock)

Variants on "news article"

* Item for sale
* Blog comment
* Blog thread

Variants on "latest"

* Publication date (unix\_timestamp)
* Most popular (keep the count)
* Most emailed (keep the count)
* Manual ranking (1..10 -- 'top ten')

Variants on "10" - there is nothing sacred about "10" in this discussion.

## The performance issues

Currently you have a table (or a column) that relates the topic to the article. The SELECT statement to find the latest 10 articles has grown in complexity, and performance is poor. You have focused on what index to add, but nothing seems to work.

* If there are multiple topics for each article, you need a many-to-many table.
* You have a flag "is\_deleted" that needs filtering on.
* You want to "paginate" the list (ten articles per page, for as many pages as necessary).

## The solution

First, let me give you the solution, then I will elaborate on why it works well.

* One new table called, say, Lists.
* Lists has _exactly_ 3 columns: topic, article\_id, sequence
* Lists has _exactly_ 2 indexes: PRIMARY KEY(topic, sequence, article\_id), INDEX(article\_id)
* Only viewable articles are in Lists. (This avoids the filtering on "is\_deleted", etc)
* Lists is [InnoDB](../../../server-usage/storage-engines/innodb/). (This gets "clustering".)
* "sequence" is typically the date of the article, but could be some other ordering.
* "topic" should probably be normalized, but that is not critical to this discussion.
* "article\_id" is a link to the bulky row in another table(s) that provide all the details about the article.

## The queries

Find the latest 10 articles for a topic:

```sql
SELECT  a.*
    FROM  Articles a
    JOIN  Lists s ON s.article_id = a.article_id
    WHERE  s.topic = ?
    ORDER BY  s.sequence DESC
    LIMIT  10;
```

You must _not_ have any WHERE condition touching columns in Articles.

When you mark an article for deletion; you _must_ remove it from Lists:

```sql
DELETE  FROM  Lists
    WHERE  article_id = ?;
```

I emphasize "must" because flags and other filtering is often the root of performance issues.

## Why it works

By now, you may have discovered why it works.

The big goal is to minimize the disk hits. Let's itemize how few disk hits are needed. When finding the latest articles with 'normal' code, you will probably find that it is doing significant scans of the Articles table, failing to quickly home in on the 10 rows you want. With this design, there is only one extra disk hit:

* 1 disk hit: 10 adjacent, narrow, rows in Lists -- probably in a single "block".
* 10 disk hits: The 10 articles. (These hits are unavoidable, but may be cached.)\
  The PRIMARY KEY, and using InnoDB, makes these quite efficient.

OK, you pay for this by removing things that you should avoid.

* 1 disk hit: INDEX(article\_id) - finding a few ids
* A few more disk hits to DELETE rows from Lists.\
  This is a small price to pay -- and you are not paying it while the user is waiting for the page to render.

## See also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [lists](https://mysql.rjweb.org/doc.php/lists)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
