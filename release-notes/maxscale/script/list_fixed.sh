#!/bin/bash


if [ $# -ne 1 ]
then
    echo "USAGE: $0 VERSION"
    exit 1
fi

# Script location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

version=$1

jql="project = MXS AND status = Closed AND fixVersion = $version"
fields="summary,issuetype,resolution,labels,description,customfield_13205,customfield_13206"

# A release has far fewer issues than what Jira returns in one response.
# If that some day is not the case, process.py reports it as an error.
issues=$(curl --silent --show-error --fail --get "https://jira.mariadb.org/rest/api/2/search" \
              --data-urlencode "jql=$jql" \
              --data "fields=$fields" \
              --data "maxResults=1000")

if [ $? -ne 0 ]
then
    echo "error: Could not fetch the issues of $version from Jira." >&2
    exit 1
fi

printf '%s\n' "$issues" | $DIR/process.py
