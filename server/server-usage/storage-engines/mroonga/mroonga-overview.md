---
description: >-
  Learn about the Mroonga storage engine, which provides fast CJK-ready
  full-text searching using column-based storage and supports Groonga's
  features.
---

# Mroonga Overview

Once Mroonga has been installed (see [About Mroonga](about-mroonga.md)), its basic usage is similar to that of a [regular fulltext index](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).

For example:

```sql
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy)) ENGINE=Mroonga;

INSERT INTO ft_mroonga(copy) VALUES ('Once upon a time'),
    ('There was a wicked witch'), ('Who ate everybody up');

SELECT * FROM ft_mroonga WHERE MATCH(copy) AGAINST('wicked');
+--------------------------+
| copy                     |
+--------------------------+
| There was a wicked witch |
+--------------------------+
```

## Score

Mroonga can also order by weighting. For example, first add another record:

```sql
INSERT INTO ft_mroonga(copy) VALUES ('She met a wicked, wicked witch');
```

Records can be returned by weighting, for example, the newly added record has two occurences of the word 'wicked' and a higher weighting:

```sql
SELECT *, MATCH(copy) AGAINST('wicked') AS score FROM ft_mroonga 
   WHERE MATCH(copy) AGAINST('wicked') ORDER BY score DESC;
+--------------------------------+--------+
| copy                           | score  |
+--------------------------------+--------+
| She met a wicked, wicked witch | 299594 |
| There was a wicked witch       | 149797 |
+--------------------------------+--------+
```

## Parser

Mroonga permits you to set a different parser for searching by specifying the parser in the `CREATE TABLE` statement as a comment or, in older versions, changing the value of the [mroonga\_default\_parser](mroonga-system-variables.md#mroonga_default_parser) system variable.

For example:

```sql
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy) COMMENT 'parser "TokenDelimitNull"') 
  ENGINE=Mroonga;,
```

or

```sql
SET GLOBAL mroonga_default_parser = 'TokenBigramSplitSymbol';
```

The following parser settings are available:

| Setting                                     | Description                                                                                                             |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| off                                         | No tokenizing is performed.                                                                                             |
| TokenBigram                                 | Default value. Continuous alphabetical characters, numbers or symbols are treated as a token.                           |
| TokenBigramIgnoreBlank                      | Same as TokenBigram except that white spaces are ignored.                                                               |
| TokenBigramIgnoreBlankSplitSymbol           | Same as TokenBigramSplitSymbol. except that white spaces are ignore.                                                    |
| TokenBigramIgnoreBlankSplitSymbolAlpha      | Same as TokenBigramSplitSymbolAlpha except that white spaces are ignored.                                               |
| TokenBigramIgnoreBlankSplitSymbolAlphaDigit | Same as TokenBigramSplitSymbolAlphaDigit except that white spaces are ignored.                                          |
| TokenBigramSplitSymbol                      | Same as TokenBigram except that continuous symbols are not treated as a token, but tokenised in bigram.                 |
| TokenBigramSplitSymbolAlpha                 | Same as TokenBigram except that continuous alphabetical characters are not treated as a token, but tokenised in bigram. |
| TokenDelimit                                | Tokenises by splitting on white spaces.                                                                                 |
| TokenDelimitNull                            | Tokenises by splitting on null characters (\0).                                                                         |
| TokenMecab                                  | Tokenise using MeCab. Required Groonga to be buillt with MeCab support.                                                 |
| TokenTrigram                                | Tokenises in trigrams but continuous alphabetical characters, numbers or symbols are treated as a token.                |
| TokenUnigram                                | Tokenises in unigrams but continuous alphabetical characters, numbers or symbols are treated as a token.                |

### Examples

#### TokenBigram vs TokenBigramSplitSymbol

`TokenBigram` failing to match partial symbols which `TokenBigramSplitSymbol` matches, since `TokenBigramSplitSymbol` does not treat continuous symbols as a token.

```sql
DROP TABLE ft_mroonga;
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy) COMMENT 'parser "TokenBigram"') 
  ENGINE=Mroonga;
INSERT INTO ft_mroonga(copy) VALUES ('Once upon a time'),   
  ('There was a wicked witch'), 
  ('Who ate everybody up'), 
  ('She met a wicked, wicked witch'), 
  ('A really wicked, wicked witch!!?!');
SELECT * FROM ft_mroonga WHERE MATCH(copy) AGAINST('!?');
Empty set (0.00 sec)

DROP TABLE ft_mroonga;
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy) COMMENT 'parser "TokenBigramSplitSymbol"') 
  ENGINE=Mroonga;
INSERT INTO ft_mroonga(copy) VALUES ('Once upon a time'),   
  ('There was a wicked witch'), 
  ('Who ate everybody up'), 
  ('She met a wicked, wicked witch'), 
  ('A really wicked, wicked witch!!?!');
SELECT * FROM ft_mroonga WHERE MATCH(copy) AGAINST('!?');
+-----------------------------------+
| copy                              |
+-----------------------------------+
| A really wicked, wicked witch!!?! |
+-----------------------------------+
```

#### TokenBigram vs TokenBigramSplitSymbolAlpha

```sql
DROP TABLE ft_mroonga;
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy) COMMENT 'parser "TokenBigram"') 
  ENGINE=Mroonga;
INSERT INTO ft_mroonga(copy) VALUES ('Once upon a time'),   
  ('There was a wicked witch'), 
  ('Who ate everybody up'), 
  ('She met a wicked, wicked witch'), 
  ('A really wicked, wicked witch!!?!');
SELECT * FROM ft_mroonga WHERE MATCH(copy) AGAINST('ick');
Empty set (0.00 sec)

DROP TABLE ft_mroonga;
CREATE TABLE ft_mroonga(copy TEXT,FULLTEXT(copy) COMMENT 'parser "TokenBigramSplitSymbolAlpha"') 
  ENGINE=Mroonga;
INSERT INTO ft_mroonga(copy) VALUES ('Once upon a time'),   
  ('There was a wicked witch'), 
  ('Who ate everybody up'), 
  ('She met a wicked, wicked witch'), 
  ('A really wicked, wicked witch!!?!');
SELECT * FROM ft_mroonga WHERE MATCH(copy) AGAINST('ick');
+-----------------------------------+
| copy                              |
+-----------------------------------+
| There was a wicked witch          |
| She met a wicked, wicked witch    |
| A really wicked, wicked witch!!?! |
+-----------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
