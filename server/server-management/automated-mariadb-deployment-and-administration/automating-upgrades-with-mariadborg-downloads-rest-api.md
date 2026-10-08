---
description: >-
  A guide on using the MariaDB Downloads REST API to programmatically retrieve
  information about software versions, facilitating automated upgrade scripts.
---

# Automating Upgrades with MariaDB.Org Downloads REST API

The MariaDB Foundation maintains a Downloads REST API. See the [Downloads API documentation](https://mariadb.org/downloads-rest-api/) to find out all the tasks that you can accomplish with this API. Generally speaking, we can say that it provides information about MariaDB products and available versions. This allows to easily automate upgrades for MariaDB and related products.

The Downloads API exposes HTTPS endpoints that return information in JSON format. HTTP and JSON are extremely common standards that can be easily used with any programming language. All the information provided by the API is public, so no authentication is required.

## How to Use the API with a Unix Shell

Linux shells are great for writing simple scripts. They are compatible to each other to some extent, so simple scripts can be run on almost any Unix/Linux system. In the following examples we'll use Bash.

On Linux, some programs you'll generally need to work with any REST API are:

* [curl](https://curl.se/), to call HTTP URLs and get their output.
* [js](https://stedolan.github.io/jq/), to extract or transform information from a JSON document.

### Example: Check When a New Version Becomes GA

A trivial use case is to write a script that checks the list of MariaDB GA major versions and, when something changes, send us an email. So we can test the newest GA version and eventually install it.

The script in this example will be extremely simple. We'll do it this way:

* Retrieve the JSON object describing all MariaDB versions.
* For each element of the array, only show the `release_id` and `release_status` properties, and concatenate them.
* Apply a filter, so we only select the rows containing 'stable' but not 'old' (so we exclude 'Old Stable').
* From the remaining rows, only show the first column (the version number).
* If the results we obtained are different from the previously written file (see last point) send an email.
* Save the results into a file.

This is something that we can easily do with a Unix shell:

```sh
#!/bin/bash

current_ga_versions=$(
    curl https://downloads.mariadb.org/rest-api/mariadb/ | \
    jq -r '.major_releases[] | .release_id + " " + .release_status' | \
    grep -i 'stable' | grep -vi 'old' | \
    cut -d ' ' -f 1
)

# create file if it doesn't exist, then compare version lists
touch ga_versions
previous_ga_versions=$( cat ga_versions )

echo "$current_ga_versions" > ga_versions

if [ "$current_ga_versions" != "$previous_ga_versions" ];
then
    mail -s 'NOTE: New MariaDB GA Versions' devops@example.com <<< 'There seems to be a new MariaDB GA version! Yay!'
fi
```

The only non-standard command here is jq. It is a great way to manipulate JSON documents, so if you don't know it you may want to take a look at [jq documentation](https://stedolan.github.io/jq/manual/).

## How to Use the API with a Python Script

To use the API with Python, we need a module that is able to send HTTP requests and parse a JSON output. The `requests` module has both these features. It can be installed as follows:

```bash
pip install requests
```

The following script prints stable versions to the standard output:

```bash
#!/usr/bin/env python

import requests

response = requests.get('https://downloads.mariadb.org/rest-api/mariadb/').json()

for x in response['major_releases']:
    if x['release_status'] == 'Stable':
        print(x['release_id'])
```

`requests.get()` makes an HTTP call of type GET, and `requests.json()` returns a dictionary representing the previously obtained JSON document.

Content initially contributed by [Vettabase Ltd](https://vettabase.com/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
