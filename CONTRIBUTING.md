# Contributing Documentation

The documentation for MariaDB products is

* written in standard American English,
* using Markdown format,
* stored in Git.

While the documentation is mainly maintained by the documentation team at MariaDB plc, **we are happy to get contributions**. Being stored in Git, it allows anyone to contribute to the documentation. You need [a GitHub account](https://github.com/), [a basic knowledge of Markdown](https://www.writethedocs.org/guide/writing/markdown/), and some expertise in what you’re writing about. You also have to agree to our [contributor agreement](https://mariadb.com/docs/general-resources/community/community/legal-documents/mca).

Contributing is as simple as this:

* Access [this repository](https://github.com/mariadb-corporation/mariadb-docs), log in with your GitHub account.
* Find the page in the documentation that you want to edit, correct, or amend.
* Make a pull request, edit, and submit.

The MariaDB documentation team will review your edits, smooth out any rough edges (language and style), and incorporate your contribution into the documentation. Don’t be afraid to submit imperfect contributions, as long as they’re factually correct.

## Using Cross-Space Link Aliases
To simplify linking between different documentation spaces (e.g., linking from MariaDB Server to MaxScale), this repository uses Link Aliases. You do not need to search for long, complex GitBook IDs; instead, use a simple {alias} placeholder.

When you submit a Pull Request, a GitHub Action automatically scans your changes and replaces the alias with the correct, full URL.

### How to Use Aliases

Instead of using a full internal URL, use the following syntax: [Link Text]({alias}/path/to/page)

Example:

You write: [Securing Communications](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/securing-communications-in-galera-cluster)

The Bot expands it to: [Securing Communications](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/securing-communications-in-galera-cluster)

Available Aliases

Alias	Target Space	Alias	Target Space
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV	MariaDB Server	https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX	MariaDB MaxScale
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7	Galera Cluster	https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14	Analytics
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD	Tools	https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L	Connectors
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb	SkySQL	https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn	Enterprise Platform
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/gmXC0YXB3rRhXvpg5mb1	Home / Landing	https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd	MariaDB Cloud

⚠️ Important: Link Validity

Please note that these expanded URLs (starting with app.gitbook.com/...) are internal GitBook application links.

Don't panic if these links do not work when clicked from within a local text editor (like VS Code), the GitHub web interface, or the GitHub app. They are designed to work perfectly once the documentation is live and when accessed through the GitBook application. This tool is intended to assist with authoring content for the published docs, not for local repository browsing.

## Technical Writing and Formatting Guidelines

Before you start making larger contributions, make yourself familiar with [the basics of technical writing](https://developers.google.com/style/highlights) (a 1-minute read). This is about using proper tone and content, language and grammar, as well as formatting, punctuation, and organization.

The source format of pages is Markdown. How to format text is [on this GitBook page](https://gitbook.com/docs/creating-content/formatting/markdown). A Markdown cheat sheet with a 10-minute tutorial and a Markdown "playground" [can be found here](https://commonmark.org/help/).

Read our [style guide](https://mariadb.com/docs/general-resources/about/readme/documentation-style-guide), too. (It's short!)

Also see the [About Links](https://mariadb.com/docs/general-resources/about/readme/about-links) page. It has useful information for when you are adding links to other pages.
