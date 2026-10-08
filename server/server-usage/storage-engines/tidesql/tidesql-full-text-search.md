---
description: >-
  FULLTEXT indexes in TideSQL with natural-language and boolean modes, BM25
  ranking, tokenization, stop words, and blend characters.
---

# TideSQL Full-Text Search

TideSQL supports `FULLTEXT` indexes for natural-language and boolean full-text search with BM25 relevance ranking. Each `FULLTEXT` index is a dedicated column family holding an inverted index, where each entry maps a term-document pair to its term frequency and document length.

```sql
CREATE TABLE articles (
  id INT NOT NULL PRIMARY KEY, title VARCHAR(200), body TEXT,
  FULLTEXT ft_content (title, body)
) ENGINE=TIDESDB;
```

## Natural-Language Mode

The default mode tokenizes the query, scans the inverted index for each term, computes BM25 scores, and returns results ordered by score:

```sql
SELECT id, title, MATCH(title, body) AGAINST('tutorial') AS score
FROM articles WHERE MATCH(title, body) AGAINST('tutorial')
ORDER BY score DESC;
```

Multi-term queries accumulate BM25 scores across terms, so documents matching more terms with higher frequencies rank higher, normalized by document length.

## Boolean Mode

Boolean mode supports required `+`, excluded `-`, prefix wildcard `*`, and exact phrase `"..."`:

```sql
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('+mysql +tutorial' IN BOOLEAN MODE);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('+mysql -tutorial' IN BOOLEAN MODE);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('optim*' IN BOOLEAN MODE);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('"database management system"' IN BOOLEAN MODE);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST('+"management system" -tutorial' IN BOOLEAN MODE);
```

A phrase query uses the inverted index to find candidate documents containing all phrase words, then verifies the exact sequence by re-tokenizing the document, the same approach InnoDB's FTS uses.

## BM25 Ranking

Scores use the Okapi BM25 algorithm:

```
IDF(t) = ln(1 + (N - df + 0.5) / (df + 0.5))
score  = IDF * (tf * (k1+1)) / (tf + k1 * (1 - b + b * |d| / avgdl))
```

`N` is the document count, `df` the document frequency of the term, `tf` its frequency in the document, `|d|` the document length in tokens, and `avgdl` the average document length. The `+1` inside the logarithm keeps every term's IDF non-negative, matching the Lucene variant. `k1` and `b` are set by `tidesdb_fts_bm25_k1` (default 1.2) and `tidesdb_fts_bm25_b` (default 0.75).

## Tokenization

The tokenizer is charset-aware and handles multi-byte scripts including UTF-8, CJK, Cyrillic, and Greek. Text is split on word boundaries using MariaDB's charset classification and lowercased with the charset's case-folding rules. Words shorter than `tidesdb_fts_min_word_len` (default 3) or longer than `tidesdb_fts_max_word_len` (default 84) are excluded from the index and from queries.

## Stop Words

Common words are excluded from the index. By default, TideSQL uses the same default list as InnoDB (`information_schema.INNODB_FT_DEFAULT_STOPWORD`). Stop words are filtered during tokenization, so they are never stored and never match. The list is customizable with `tidesdb_ft_stopword_table`, which names a `db_name/table_name` table that must have a `value` VARCHAR column of one word per row. The stop-word table must itself be a TideSQL table, since the loader resolves it as a TidesDB column family. Pointing the variable at a table on another engine logs a warning and leaves the previous list in place rather than taking effect. Setting it to NULL or empty restores the default:

```sql
CREATE TABLE mydb.my_stopwords (value VARCHAR(50)) ENGINE=TIDESDB;
INSERT INTO mydb.my_stopwords (value) VALUES ('custom'), ('words'), ('here');
SET GLOBAL tidesdb_ft_stopword_table = 'mydb/my_stopwords';
```

After changing the stop-word table, rebuild existing FULLTEXT indexes with `ALTER TABLE ... DROP INDEX ..., ADD FULLTEXT INDEX ...` so they reflect the new list.

## Blend Characters

A blend character is treated as both a separator and a valid word character. When one appears inside a token, the tokenizer emits both the full blended form and the sub-parts, which makes Romance-language elision and apostrophe names searchable by any component or the whole form. With `tidesdb_fts_blend_chars = "'"`:

| Input | Indexed tokens |
|-------|----------------|
| `L'aria` | `l'aria`, `aria` |
| `Dell'aria` | `dell'aria`, `dell`, `aria` |
| `O'Malley` | `o'malley`, `malley` |

```sql
SET GLOBAL tidesdb_fts_blend_chars = "'";
```

The default is empty. The setting is global and applies to subsequent indexing and queries, so rebuild existing indexes after changing it.

The full-text tuning variables above are documented on the [TideSQL System Variables](tidesql-system-variables.md) page.

## Multi-Column Indexes and Maintenance

A single `FULLTEXT` index can span several columns, and the engine concatenates their text into one document for tokenization and scoring:

```sql
CREATE TABLE docs (
  id INT NOT NULL PRIMARY KEY, title VARCHAR(200), summary TEXT, body TEXT,
  FULLTEXT (title, summary, body)
) ENGINE=TIDESDB;
```

Index entries are maintained inside the same transaction as the row change. An insert tokenizes the document and writes one entry per unique term, a delete removes the entries, and an update that changes the indexed columns removes the old entries and writes new ones. The document count and average document length for BM25 are maintained atomically in the data column family.

<sub>_This page is licensed: GPLv2_</sub>
