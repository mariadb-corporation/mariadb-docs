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
  # One description per known page, written from what the page documents. The
  # doxygen groups carry no brief of their own (every @defgroup is a bare
  # name), so there is nothing better to derive this from. A page the
  # generator adds later gets the generic fallback until it is listed here.
  case "$base" in
    README.md)
      description="Generated reference for the MariaDB plugin API, built from the server headers by doxygen and moxygen."
      ;;
    api.md)
      description="Every generated Plugin API class, macro, typedef, and function on one page, including the plugin services and the audit, authentication, and encryption plugin interfaces."
      ;;
    Instrumentation_interface.md)
      description="The Performance Schema instrumentation interface (PSI) that the server and plugins use to report locks, I/O, statements, and other events, with links to each instrumentation group."
      ;;
    Group_PSI_v1.md)
      description="Version 1 of the Performance Schema instrumentation ABI: the PSI_v1 interface structure, the instrument info structures, and the locker state structures."
      ;;
    File_instrumentation.md)
      description="The MYSQL_FILE structure and the mysql_file_* wrappers for opening, reading, writing, seeking, syncing, renaming, and deleting files with Performance Schema instrumentation."
      ;;
    Idle_instrumentation.md)
      description="The MYSQL_START_IDLE_WAIT and MYSQL_END_IDLE_WAIT macros, which mark the start and end of an idle wait event for the Performance Schema."
      ;;
    Memory_instrumentation.md)
      description="The mysql_memory_register macro, which registers memory instruments with the Performance Schema."
      ;;
    Metadata_instrumentation.md)
      description="The mysql_mdl_create, mysql_mdl_set_status, and mysql_mdl_destroy macros, which instrument metadata locks for the Performance Schema."
      ;;
    Socket_instrumentation.md)
      description="The MYSQL_SOCKET structure and the mysql_socket_* wrappers for creating, connecting, sending, receiving, and closing sockets with Performance Schema instrumentation."
      ;;
    Stage_instrumentation.md)
      description="Macros that register statement execution stages, set the current stage, and report stage progress (work completed and work estimated) to the Performance Schema."
      ;;
    Statement_instrumentation.md)
      description="Macros that register statement instruments and report a statement's start, text, digest, lock time, rows sent and examined, and end to the Performance Schema."
      ;;
    Table_instrumentation.md)
      description="Macros that instrument table handles, table shares, and table lock waits for the Performance Schema, including open, close, unbind, and rebind."
      ;;
    Thread_instrumentation.md)
      description="Instrumented mutex, rwlock, prlock, and condition structures and their wrappers, and the PSI_CALL_* thread macros that register threads and set their attributes."
      ;;
    Transaction_instrumentation.md)
      description="Macros that report a transaction's start, GTID, XID, XA state, savepoints, commit, and rollback to the Performance Schema."
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
