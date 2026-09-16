#!/bin/bash

set -euo pipefail

# Adds GitBook frontmatter to the generated Plugin API pages, which moxygen
# emits without any. Pass a local base directory to run this outside CI, e.g.:
#   ./add_frontmatter_to_server_plugin_api.sh /path/to/mariadb-docs
basedir="${1:-.}"

dest_dir="$basedir/server/reference/plugins/api-plugin"
test -d "$dest_dir"

shopt -s nullglob
for page in "$dest_dir"/*.md; do
  base="$(basename "$page")"
  # Never write a second block: the run is idempotent, and a hand-edited
  # description on a page must survive the next generation.
  if [ "$(head -n 1 "$page")" = "---" ]; then
    echo "frontmatter already present, skipping: $base"
    continue
  fi
  # Title extraction matches the SUMMARY script's, minus moxygen's {#anchor}.
  title="$(grep -m1 '^# ' "$page" | sed 's/^# //; s/[[:space:]]*{#[^}]*}[[:space:]]*$//' || true)"
  if [ -z "$title" ]; then
    title="${base%.md}"
  fi
  case "$base" in
    README.md)
      description="Generated reference for the MariaDB plugin API, built from the server headers by doxygen and moxygen."
      ;;
    api.md)
      description="Complete generated Plugin API reference, built from the MariaDB server headers by doxygen and moxygen."
      ;;
    *)
      description="Plugin API reference: ${title}. Generated from the MariaDB server headers by doxygen and moxygen."
      ;;
  esac
  tmp_page="$(mktemp)"
  {
    printf -- '---\ndescription: >-\n  %s\n---\n\n' "$description"
    cat "$page"
  } > "$tmp_page"
  mv "$tmp_page" "$page"
  echo "added frontmatter: $base"
done
