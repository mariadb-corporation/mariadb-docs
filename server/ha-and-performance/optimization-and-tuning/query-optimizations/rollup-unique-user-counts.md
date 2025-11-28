# Rollup Unique User Counts

## The Problem

The normal way to count "Unique Users" is to take large log files, sort by userid, dedup, and count. This requires a rather large amount of processing. Furthermore, the count derived cannot be rolled up. That is, daily counts cannot be added to get weekly counts -- some users will be counted multiple times.

So, the problem is to store the counts is such a way as to allow rolling up.

## The solution

Let's think about what we can do with a hash of the userid. The hash could map to a bit in a bit string. A BIT\_COUNT of the bit string would give the 1-bits, representing the number of users. But that bit string would have to be huge. What if we could use shorter bit strings? Then different userids would be folded into the same bit. Let's assume we can solve that.

Meanwhile, what about the rollup? The daily bit strings can be OR'd together to get a similar bit string for the week.

We have now figured out how to do the rollup, but have created another problem -- the counts are too low.

## Inflating the BIT\_COUNT

A sufficiently random hash (eg MD5) will fold userids into the same bits with a predictable frequency. We need to figure this out, and work backwards. That is, given that X percent of the bits are set, we need a formula that says approximately how many userids were used to get those bits.

I simulated the problem by generating random hashes and calculated the number of bits that would be set. Then, with the help of Eureqa software, I derived the formula:

Y = 0.5456_X + 0.6543_tan(1.39_X_X\*X)

## How good is it?

The formula is reasonably precise. It is usually within 1% of the correct value; rarely off by 2%.

Of course, if virtually all the bits are set, the forumla can't be very precise. Hence, you need to plan to have the bit strings big enough to handle the expected number of Uniques. In practice, you can use less than 1 bit per Unique. This would be a huge space savings over trying to save all the userids.

Another suggestion... If you are rolling up over a big span of time (eg hourly -> monthly), the bit strings must all be the same length, and the monthly string must be big enough to handle the expected count. This is likely to lead to very sparse hourly bit strings. Hence, it may be prudent to compress the hourly stings.

## Postlog

Invented Nov, 2013; published Apr, 2014

Future: Rick is working on actual code (Sep, 2016)\
It is complicated by bit-wise operations being limited to BIGINT.\
However, with MySQL 8.0 (freshly released), the desired bit-wise\
operations can be applied to BLOB, greatly simplifying my code.\
I hope to publish the pre-8.0 code soon; 8.0 code later.

## See also

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [uniques](https://mysql.rjweb.org/doc.php/uniques)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
