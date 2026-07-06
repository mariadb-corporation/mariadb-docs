---
description: >-
  Efficient pagination techniques for splitting long lists across pages.
---

# Pagination Optimization

## The Desire

You have a website with news articles, or a blog, or some other thing with a list of things that might be too long for a single page. So, you decide to break it into chunks of, say, 10 items and provide a \[Next] button to go the next "page".

You spot [OFFSET and LIMIT](../../../reference/sql-statements/data-manipulation/selecting-data/limit.md) in MariaDB and decide that is the obvious way to do it.

```sql
SELECT  *
        FROM  items
        WHERE  messy_filtering
        ORDER BY  date DESC
        OFFSET  $M  LIMIT $N
```

Note that the problem requirement needs a \[Next] link on each page so that the user can 'page' through the data. He does not really need "GoTo Page #". Jump to the \[First] or \[Last] page may be useful.

## The Problem

All is well -- until you have 50,000 items in a list. And someone tries to walk through all 5000 pages. That 'someone' could be a search engine crawler.

Where's the problem? Performance. Your web page is doing "SELECT ... OFFSET 49990 LIMIT 10" (or the equivalent "LIMIT 49990,10"). MariaDB has to find all 50,000 rows, step over the first 49,990, then deliver the 10 for that distant page.

If it is a crawler ('spider') that read all the pages, then it actually touched about 125,000,000 items to read all 5,000 pages.

Reading the entire table, just to get a distant page, can be so much I/O that it can cause timeouts on the web page. Or it can interfere with other activity, causing other things to be slow.

## Other Bugs

In addition to a performance problem, ...

* If an item is inserted or deleted between the time you look at one page and the next, you could miss an item, or see an item duplicated.
* The pages are not easily bookmarked or sent to someone else because the contents shift over time.
* The WHERE clause and the [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) may even make it so that all 50,000 items have to be read, just to find the 10 items for page 1!

## What to Do?

Hardware? No, that's just a bandaid. The data will continue to grow and even the new hardware won't handle it.

Better INDEX? No. You must get away from reading the entire table to get the 5000th page.

Build another table saying where the pages start? Get real! That would be a maintenance nightmare, and expensive.

Bottom line: Don't use OFFSET; instead remember where you "left off".

```sql
# First page (latest 10 items):
    SELECT ... WHERE ... ORDER BY id DESC LIMIT 10
# Next page (second 10):
    SELECT ... WHERE ... AND id < $left_off ORDER BY id DESC LIMIT 10
```

With INDEX(id), this suddenly becomes very efficient.

## Implementation -- Getting Rid of OFFSET

You are probably doing this now: [ORDER BY](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) datetime DESC LIMIT 49990,10 You probably have some unique id on the table. This can probably be used for "left off".

Currently, the \[Next] button probably has a url something like ?topic=xyz\&page=4999\&limit=10 The 'topic' (or 'tag' or 'provider' or 'user' or etc) says which set of items are being displayed. The product of page\*limit gives the OFFSET. (The "limit=10" might be in the url, or might be hard-coded; this choice is not relevant to this discussion.)

The new variant would be ?topic=xyz\&id=12345\&limit=10. (Note: the 12345 is not computable from 4999.) By using INDEX(topic, id) you can efficiently say

```sql
WHERE topic = 'xyz'
      AND id >= 1234
    ORDER BY id
    LIMIT 10
```

That will hit only 10 rows. This is a huge improvement for later pages. Now for more details.

## Implementation -- "Left Off"

What if there are exactly 10 rows left when you display the current page? It would make the UI nice if you grayed out the \[Next] button, wouldn't it. (Or you could suppress the button all together.)

How to do that? Instead of LIMIT 10, use LIMIT 11. That will give you the 10 items needed for the current page, plus an indication of whether there is another page. And the id for that page.

So, take the 11th id for the \[Next] button: \<a href=?topic=xyz\&id=$id11\&limit=10>Next

## Implementation -- Links Beyond \[Next]

Let's extend the 11 trick to also find the next 5 pages and build links for them.

Plan A is to say LIMIT 51. If you are on page 12, that would give you links for pages 13 (using 11th id) through pages 17 (51st).

Plan B is to do two queries, one to get the 10 items for the current page, the other to get the next 41 ids (LIMIT 10, 41) for the next 5 pages.

Which plan to pick? It depends on many things, so benchmark.

## A Reasonable Set of Links

Reaching forward and backward by 5 pages is not too much work. It would take two separate queries to find the ids in both directions. Also, having links that take you to the First and Last pages would be easy to do. No id is needed; they can be something like

```
<a href=?topic=xyz&id=FIRST&limit=10>First</a>
    <a href=?topic=xyz&id=LAST&limit=10>Last</a>
```

The UI would recognize those, then generate a SELECT with something like

```sql
WHERE topic = 'xyz'
    ORDER BY id ASC -- ASC for First; DESC for Last
    LIMIT 10
```

The last items would be delivered in reverse order. Either deal with that in the UI, or make the SELECT more complex:

```sql
( SELECT ...
        WHERE topic = 'xyz'
        ORDER BY id DESC
        LIMIT 10
    ) ORDER BY id ASC
```

Let's say you are on page 12 of lots of pages. It could show these links:

```
[First] ... [7] [8] [9] [10] [11] 12 [13] [14] [15] [16] [17] ... [Last]
```

where the ellipsis is really used. Some end cases:

<pre class="language-sql"><code class="lang-sql"># Page one of three:
    First [2] [3]
<strong># Page one of many:
</strong>    First [2] [3] [4] [5] ... [Last]
# Page two of many:
    [First] 2 [3] [4] [5] ... [Last]
# If you jump to the Last page, you don't know what page number it is.
# So, the best you can do is perhaps:
#    [First] ... [Prev] Last
</code></pre>

## Why it Works

The goal is to touch only the relevant rows, not all the rows leading up to the desired rows. This is nicely achieved, except for building links to the "next 5 pages". That may (or may not) be efficiently resolved by the simple SELECT id, discussed above. The reason that may not be efficient deals with the WHERE clause.

Let's discuss the optimal and suboptimal indexes.

For this discussion, I am assuming

* The datetime field might have duplicates -- this can cause troubles
* The id field is unique
* The id field is close enough to datetime-ordered to be used instead of datetime.

Very efficient -- it does all the work in the index:

```sql
INDEX(topic, id)
    WHERE topic = 'xyz'
      AND id >= 876
    ORDER BY id ASC
    LIMIT 10,41
<</code??
That will hit 51 consecutive index entries, 0 data rows.

Inefficient -- it must reach into the data:
<<code>>
    INDEX(topic, id)
    WHERE topic = 'xyz'
      AND id >= 876
      AND is_deleted = 0
    ORDER BY id ASC
    LIMIT 10,41
```

That will hit at least 51 consecutive index entries, plus at least 51 _randomly_ located data rows.

Efficient -- back to the previous degree of efficiency:

```sql
INDEX(topic, is_deleted, id)
    WHERE topic = 'xyz'
      AND id >= 876
      AND is_deleted = 0
    ORDER BY id ASC
    LIMIT 10,41
```

Note how all the '=' parts of the WHERE come first; then comes both the '>=' and 'ORDER BY', both on id. This means that the INDEX can be used for all the WHERE, plus the ORDER BY.

## "Items 11-20 Out of 12345"

You lose the "out of" except when the count is small. Instead, say something like

```
Items 11-20 out of Many
```

Alternatively... Only a few searches will have too many items to count. Keep another table with the search criteria and a count. This count can be computed daily (or hourly) by some background script. When discovering that the topic is a busy one, look it up in the table to get

```
Items 11-20 out of about 49,000
```

The background script would round the count off.

The quick way to get an _estimated_ number of rows for an InnoDB table is

```sql
SELECT  table_rows
        FROM  information_schema.TABLES
        WHERE  TABLE_SCHEMA = 'database_name'
          AND  TABLE_NAME = 'table_name'
```

However, it does not allow for the WHERE clause that you probably have.

## Complex WHERE, or JOIN

If the search criteria cannot be confined to an INDEX in a single table, this technique is doomed. I have another paper that discusses "Lists", which solves that (which extra development work), and even improves on what is discussed here.

## How Much Faster?

This depends on

* How many rows (total)
* Whether the WHERE clause prevented the efficient use of the ORDER BY
* Whether the data is bigger than the cache.\
  This last one kicks in when building one page requires reading more data from disk can be cached. At that point, the problem goes from being CPU-bound to being I/O-bound. This is likely to suddenly slow down the loading of a pages by a factor of 10.

## What is Lost

* Cannot "jump to Page N", for an arbitrary N. Why do you want to do that?
* Walking backward from the end does not know the page numbers.
* The code is more complex.

## Postlog

Designed about 2007; posted 2012.

## See Also

* [A forum discussion](https://stackoverflow.com/questions/31533414/filtering-large-db-record-grouped-by-a-column)
* [Luke calls it "seek method" or "keyset pagination"](https://use-the-index-luke.com/no-offset)
* [More by Luke](https://use-the-index-luke.com/sql/partial-results/fetch-next-page)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [pagination](https://mysql.rjweb.org/doc.php/pagination)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
