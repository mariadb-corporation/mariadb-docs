# About Links

{% hint style="info" %}
This page is for contributors to the MariaDB Documentation and goes into detail on the internals of links. This page is not about MariaDB. If you're interested in contributing to the MariaDB Docs, please also see the [Contributing Documentation](contributing-documentation.md) and [Documentation Style Guide](documentation-style-guide.md) pages.
{% endhint %}

There are three types of links in the MariaDB docs: [external](about-links.md#external-links), [relative](about-links.md#relative-links), and [space](about-links.md#space-links). The general rules for when to use each are:

* If the link is outside of `https://mariadb.com/docs/` → Use an [External Link](about-links.md#external-links)
* If the link is to a page in the same space → Use a [Relative Link](about-links.md#relativ-links)
* If the link is to a page in another space → Use a [Space Link](about-links.md#space-links)

See [About Spaces](about-links.md#about-spaces) for information on what Spaces are.

{% hint style="info" %}
Both relative and space **links require the `.md` extension** when linking to a page.

For instance, to create a link pointing to the [About MariaDB](../about-mariadb.md) page from this page, you write:

```
[About MariaDB](../about/about-mariadb.md)
```
{% endhint %}

## About Spaces

In GitBook (our documentation system), _**Spaces**_ are the main sections of the site you see along the top of every docs page:

<figure><picture><source srcset="../../.gitbook/assets/spaces-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/spaces-light.png" alt=""></picture><figcaption></figcaption></figure>

What space you are in is very important in determining whether you need to use a [Relative](about-links.md#relative-links) or [Space](about-links.md#space-links) link. Gitbook identifies Spaces via a unique space identifier. See the [Space Links](about-links.md#space-links) section for more details. We also have a handy [list of Space prefixes](about-links.md#list-of-space-prefixes) for use when creating space links in Markdown.

In the [documentation source repository](https://github.com/mariadb-corporation/mariadb-docs) on GitHub, the spaces are the top-level folders.

## External Links

External links are the easiest, they are to external pages outside the [https://mariadb.com/docs](https://mariadb.com/docs) site. Some examples in Markdown syntax of external links are:

```markdown
* [Example Website](https://example.com)
* [MariaDB Corp Blog](https://mariadb.com/blog)
* [MariaDB JIRA](https://jira.mariadb.org)
```

Technically, you can use external links for links to docs content, you just put in the full URI to the page you want to link to. However, if you do that we lose the ability to automatically update the link if the page you're linking to is moved or renamed. So for links to docs content we prefer to use [Relative Links](about-links.md#relative-links) or [Space Links](about-links.md#space-links).

## Relative Links

Relative links are links to a page in the same space, relative to the page you are editing. For example a relative link to the [Joining the Community](../../community/joining-the-community.md) page, from this page, looks like this in Markdown:

```
[Joining the Community](../../community/joining-the-community.md)
```

One big limitation of relative links is that they cannot cross [_**Space**_](about-links.md#about-spaces) boundaries.

This page you are currently reading is under the [General Resources](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/WCInJQ9cmGjq1lsTG91E/) space, so we can use internal links to link to other pages under `https://mariadb.com/docs/general-resources/`. If we want to link to a page in another space, we need to use [Space Links](about-links.md#space-links).

## Space Links

To link to pages in other [Spaces](about-links.md#about-spaces) we need to use special _Space Links_ which use an internal identifier so that GitBook knows exactly what page you are pointing to.

A space link begins with `https://app.gitbook.com/s/` , followed by a unique alphanumeric _`space identifier`_ (in this doc we'll call both of these together the _`space prefix`_), and finally the _`path`_ to the page _**without**_ the final `.md` extension that exists in the source code.

The _`path`_ is everything after the space name in a full page URI. For example, take the following full URI for the [Securing MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb) page:

```
https://mariadb.com/docs/server/security/securing-mariadb
```

In this URI, the space name is _`server`_ and the _`path`_, if you were creating a space link, is:

```
/security/securing-mariadb
```

To convert that into a space link we need to get the Server space identifier and combine it with the path. Rather than list out just the identifiers for our spaces, we have a [List of Space Prefixes](about-links.md#list-of-space-prefixes) that you can copy from when creating space links.

### Space Link Aliases

Space link prefixes are hard to memorize. To make it easier for contributors, a GitHub Action is available that runs automatically on commit. That functionality allows to use space _aliases_ instead of _prefixes_. For instance, to place a link to a page in the _server_ space from, say, the _release-notes_ space, you can write this:

{% code overflow="wrap" %}
```
https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/installing-mariadb-server-guide.md
```
{% endcode %}

On commit, this will be expanded to this:

{% code overflow="wrap" %}
```
https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/installing-mariadb-server-guide.md
```
{% endcode %}

These space link aliases are available:

* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb`
* `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/WCInJQ9cmGjq1lsTG91E/about/readme`

{% hint style="info" %}
**Remember to use space link aliases only for links across spaces.**

When linking to a page in the same space, use [relative links](about-links.md#relative-links).
{% endhint %}

### Space Link Prefixes

Instead of using space link aliases, you can use "regular" GitBook link prefixes. That's harder than using link aliases, because they're hard to memorize. Therefore, using link aliases is recommended.

Continuing with our example, a full space link in Markdown for the [Securing MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb) page is: _`space prefix`_ (for the Server space) + _`path`_:

```markdown
[Securing MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb)
```

See the [List of Space Prefixes](about-links.md#list-of-space-prefixes) section for a list of all of our space prefixes.

### List of Space Prefixes

A handy list of all space prefixes for the MariaDB Docs:

#### [MariaDB Platform](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/) space prefix

```
https://app.gitbook.com/s/JqgUabdZsoY5EiaJmqgn
```

#### [Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/) space prefix

```
https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV
```

#### [MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) space prefix

```
https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX
```

#### [Analytics](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) space prefix

```
https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14
```

#### [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) space prefix

```
https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7
```

#### [Connectors](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/) space prefix

```
https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L
```

#### [Tools](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD/) space prefix

```
https://app.gitbook.com/s/kuTXWg0NDbRx6XUeYpGD
```

#### [MariaDB Cloud](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd/) space prefix

```
https://app.gitbook.com/s/vPz15Lz0Iw3P3yKR3Prd
```

#### [Release Notes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/) space prefix

```
https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb
```

#### [General Resources](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/WCInJQ9cmGjq1lsTG91E/) space prefix

```
https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E
```

### Space Link Examples

Here are some examples of Markdown links to various pages using space links:

#### [Options, System & Status Variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables) in the Server space

```markdown
[Options, System & Status Variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables)
```

#### [MariaDB 12.1 Changes & Improvements](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1) in the Release Notes space

```markdown
[MariaDB 12.1 Changes & Improvements](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1)
```

#### [MariaDB Connector/C Guide](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/mariadb-connector-c-guide) in the Connectors space

```markdown
[MariaDB Connector/C Guide](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/mariadb-connector-c-guide)
```

When Space Links are rendered to the public site, GitBook handles translating Space Links into a link to the correct page. And if a page is moved or renamed then the link will be automatically updated on every page it appears on.
