# Big Link Test File

This file tests various types of links to see how the checker handles them.

## Good Links ✅
These should all pass:
1. [Google](https://www.google.com)
2. [GitHub](https://github.com)
3. [MariaDB](https://mariadb.com)
4. [Wikipedia](https://www.wikipedia.org)
5. [BBC News](https://www.bbc.com/news)
6. [Python](https://www.python.org)
7. [Stack Overflow](https://stackoverflow.com)

## Broken Links ❌
These should cause the action to fail:
8. [Missing GitHub Page](https://github.com/mariadb-corporation/this-repo-does-not-exist) (404 Not Found)
9. [Non-existent Domain](https://www.this-domain-definitely-does-not-exist-12345.com) (DNS Error)
10. [Fake Page on Real Site](https://www.google.com/search?q=nothing&this_parameter_breaks_things=true_404) (404 Not Found)
