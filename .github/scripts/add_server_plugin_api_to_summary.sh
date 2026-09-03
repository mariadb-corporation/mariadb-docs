#!/bin/bash

set -euo pipefail

# pass a local base directory to run this script locally, e.g.:
#   ./add_server_plugin_api_to_summary.sh /Users/gkodinov/dev/gkodinov/mdbf-1241
basedir="${1:-.}"

# Generated pages live next to SUMMARY.md under server/.
dest_dir="$basedir/server/reference/plugins/api-plugin"
summary="$basedir/server/SUMMARY.md"
# SUMMARY.md paths are relative to the server/ book root.
summary_dir="reference/plugins/api-plugin"
parent_title="Plugin API Documentation"
parent_page="page-index.md"
parent_link="${summary_dir}/${parent_page}"
parent_line="    * [${parent_title}](${parent_link})"
test -f "$summary"
test -d "$dest_dir"
if [[ "$basedir" == "." ]]; then
  bullets_file="$(mktemp)"
#  trap 'rm -f "$bullets_file"' EXIT
else
  bullets_file="$basedir/server/reference/plugins/api-plugin/bullets.tmp"
  rm -f "$bullets_file"
fi
# Recreate child bullets from every generated .md page.
# Title extraction matches: grep '^# ' | sed 's/^# \(.*\)$/\1/g'
find "$dest_dir" -maxdepth 1 -type f -name '*.md' -print | sort | while read -r page; do
  base="$(basename "$page")"
  if [[ "$base" == "$parent_page" ]]; then
    continue
  fi
  title="$(grep '^# ' "$page" | sed 's/^# \(.*\)$/\1/g' | head -n 1 || true)"
  if [ -z "$title" ]; then
    title="${base%.md}"
  fi
  printf '      * [%s](%s/%s)\n' "$title" "$summary_dir" "$base" >> "$bullets_file"
done
test -s "$bullets_file"
if [[ "$basedir" == "." ]]; then
  tmp_summary="$(mktemp)"
#  trap 'rm -f "$bullets_file" "$tmp_summary"' EXIT
else
  tmp_summary="$basedir/server/reference/plugins/api-plugin/tmp_summary.tmp"
  rm -f "$tmp_summary"
fi
awk -v parent_line="$parent_line" -v bullets_file="$bullets_file" '
  function is_child(line) {
    return line ~ /^      \* /
  }
  BEGIN {
    while ((getline b < bullets_file) > 0) {
      bullets = bullets b "\n"
    }
    close(bullets_file)
  }
  {
    if (!found && inserted && $0 ~ /\[Plugin API Documentation\]/) {
      found = 1
      skipping = 1
      next
    }
    if (skipping) {
      if (is_child($0)) {
        next
      }
      skipping = 0
    }
    if (!found && $0 ~ /\* \[Plugin Overview\]\(reference\/plugins\/plugin-overview.md\)/) {
      print
      print parent_line
      printf "%s", bullets
      inserted = 1
      next
    }
    print
  }
  END {
    if (!inserted) {
      print "Could not find the parent for plugins section in SUMMARY.md" > "/dev/stderr"
      exit 1
    }
  }
' "$summary" > "$tmp_summary"
mv "$tmp_summary" "$summary"
echo "Updated $summary Plugin API Documentation section:"
 git diff $summary