# MariaDB 5.3/MySQL 5.5 Windows performance patches

I just backported Windows performance patches I've done for 5.5 back to [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3). There will be a bit more in Maria that in MySQL 5.5, but more on this later.

First, I feel Windows performance improvements in 5.5 were never adequately described, so here is the redux.\
For those familiar with Windows systems programming, MySQL code used to offer of low-hanging performance fruits. I picked some of them those back in my days in MySQL/Sun. The result benchmark curve became really nice:\
look at [Calvin's blog entry](https://blogs.innodb.com/wp/2010/09/mysql-5-5-innodb-performance-improvements-on-windows/).

If graphs in this blog looks familiar to you, it is because it was often used by Oracle marketing as proof of big-O's positive influence on MySQL code :)

There were 3 Windows performance related patches. I comment on the bugs history a little bit, too.

* [Bug#24509](https://bugs.mysql.com/bug.php?id=24509). The fix removed the limit of 2048 open MyISAM files, and as a nice side-effect allowed for much bigger table cache. When mysqld starts, it checks the maximum open files value, and corrects the value of table cache, if max\_open\_files is low or max\_connection is high. This is what also happened during benchmarks. If you look at the read-only benchmark graph in the Calvin's blog above, you'll notice a drop around 64 concurrent users. No wonder, mysql server recalculated table cache size, setting it to the absolute minimum, that is to 64.

The fix was to create an own sort-of C runtime library on top of pure Win32, which is capable of handling more than 2048 open files (16K default). Some other things are also done nicer than in Microsofts C runtime, e.g there are no locks, and there is an acceptable pread()/pwrite() implementation. The main advantage as I said is being able to have a large table cache - for this, rewriting C runtime is likely an overkill, but I did not come up with anything better.

* [Bug#52102](https://bugs.mysql.com/bug.php?id=52102). This bug was fixing a lot of questionable places in InnoDB that were written probably back in the NT3.1 days .

First it is importantto understand how innodb "mutex" structure is acquired. Details on it are hairy, mutex is a composite structure which has a real os mutex( known under Windows as CRITICAL\_SECTION) plus innodb event (known under Windows as event). There are a couple of variations on the implementation - mutex can be an interlocked (aka atomic for my Unix friends) variable, under Unix event is represented as condition variable.

Acquisition is done in 2 steps - first, trylock on os mutex is performed , possibly several times with in a loop, if unsuccessfull, event is reserved in a global table of events known as "sync array", event is entering a waiting state. mutex unlock would wakeup the waiters if there are any. Do not ask me why the implementation is so complicated, it is so :) Maybe, this design helps to find deadlocks.

Variation of this implementation - instead of trylock on mutex, there might be a compare\_exchange instruction on interlocked(atomic) variable.

Back to Windows, the implementation of the above exposed a couple of interesting self-compensating bugs.

1. First, I fixed os\_mutex\_trylock() to be what it really means . The implementation was EnterCriticalSection, which is "try very hard", and actually acquire the lock. A more conscious trylock would be TryEnterCriticalSection. When I fixed that, contrary to my expectation, this made mysqld really slow. When trylock() failed, innodb started to enter code paths it has never seen before. for example, reserving space in the mentioned "sync array". Access to sync array is protected by so-called "slow lock" and this showed up very often in the profiler. The next step was fixing the "slow lock"
2. "slow Innodb mutex" was implemented as kernel object aka Windows mutex (for my Unix friends this is sort of SysV semaphore). It can be used to synchronize processes but is an absolute overkill for synchronization of threads inside the same process. It was a "really slow mutex". Changing this to CRITICAL\_SECTION made it faster however...
3. When all of the above was fixed, found out that Windows events (mentioned events) did not really scale well in many-threads scenarios. On newer Windows (Vista+), there is a CONDITION\_VARIABLE that is documented to scale better, and measuring also showed that it scaled really well. So I used condition variables when possible, which is ironic, because InnoDB events were really modeled after Windows events.
4. Reenabled implementation of fast mutexes as atomic variables. Prior to the patch, precompiler flags to enable atomics were commented out with "Windows atomics do not work well" in CMakeLists.txt. Great comment, given that unlike software developers, atomic instructions have no preferences for the OSes they are being used on :)

So, the story about "atomics did not work well on Windows" was a cumulative effect of different things.

Prior to that patch . Once atomics were enabled, implementation of fast mutexes did not use CRITICAL\_SECTION, but compare\_exchange instruction. Ingenious "trylock\_veryhard" as we have seen at the step 1. above is not used anymore, instead it is a quite correct "try" lock . Once try\_lock() began to fail with many concurrent threads, overhead of sync array guard implemented as Windows kernel object that we have seen in 2. became apparent, and less-then inefficient Windows events mentioned in 3. finished that picture.

* [Bug#56585](https://bugs.mysql.com/bug.php?id=56585)

This patch was merely to compensate for negative effects of the 5.5 metadata lock on MyISAM bechmarks, and fix was using native Vista performance primitives. The patch per se is not interesting, and repeats a lot of what was done for Innodb. What was great, was a discussion prior to the patch between myself, Davi, Dmitry on different implementations of reader writer locks, including 2 homebacked ones, and one by [Vance Morrison](https://blogs.msdn.com/b/vancem/archive/2006/03/28/563180.aspx).

Without doubt, the discussions around that was a highlight in my very short stint at Oracle. Also, if you want to get a MySQL-classic-style code review with 17 things to fix, of which at least 10 would be marked with "Coding Style" (yes, both words capitalized) , try to get Dmitry Lenev as a reviewer, he's great - this is the proof [118295](https://lists.mysql.org/commits/118295) Anyway, the patch improves MyISAM throughput by 10-20% , which I think is quite ok. Somehow those percents were subsequently eaten by MDL though :)

## Notes

Taken from a note on Facebook: [note.php?note\_id=238505812835782](https://www.facebook.com/note.php?note_id=238505812835782) by Vladislav Vaintroub.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
