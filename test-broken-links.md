# Test File for Broken Links

This is a test file to make sure our GitHub Action is working.

This is a good link:
[MariaDB](https://mariadb.com)

Here are some bad links that should fail the build:
- [This link returns a 404](https://httpstat.us/404)
- [This one also returns a 404](https://www.google.com/this-page-does-not-exist-ever)
- [This domain should not exist](httpss://thisshouldnotexist-404.com)
