import re
import sys

# This script validates the generated fill_help_tables.sql file before it is
# uploaded as a CI artifact or loaded into MariaDB.
#
# It does NOT execute SQL — it validates the file as text using regex and
# line-by-line classification. This keeps it dependency-free (no DB required).
#
# Usage:
#   python validate_sql.py help-tables/fill_help_tables.sql
#
# Exit codes:
#   0 — all checks passed
#   1 — one or more errors found


def split_statements(text: str):
    """Yield (start_line, statement) pairs, respecting SQL string and -- comment state."""
    statements = []
    buf = []
    line_no = 1
    start_line = 1
    in_str = False
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if not in_str and c == "-" and i + 1 < n and text[i + 1] == "-":
            while i < n and text[i] != "\n":
                buf.append(text[i])
                i += 1
            continue
        if c == "'":
            if in_str and i + 1 < n and text[i + 1] == "'":
                buf.append("''")
                i += 2
                continue
            in_str = not in_str
            buf.append(c)
            i += 1
            continue
        if c == "\n":
            line_no += 1
        if c == ";" and not in_str:
            buf.append(c)
            stmt = "".join(buf).strip()
            if stmt:
                statements.append((start_line, stmt))
            buf = []
            i += 1
            while i < n and text[i] in " \t\r\n":
                if text[i] == "\n":
                    line_no += 1
                i += 1
            start_line = line_no
            continue
        buf.append(c)
        i += 1
    return statements


def validate_sql(file_path: str = "fill_help_tables.sql") -> bool:
    """Validate the generated fill_help_tables.sql file."""
    errors = []
    warnings = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"FATAL: {file_path} not found")
        return False

    if not text.strip():
        print(f"FATAL: {file_path} is empty")
        return False

    topic_stmts = []
    category_stmts = []
    keyword_stmts = []
    relation_stmts = []

    for line_num, stmt in split_statements(text):
        head = stmt[:30].lower()
        if head.startswith('--') or head.startswith('set ') or head.startswith('use ') or head.startswith('delete '):
            continue
        if head.startswith('insert into help_topic'):
            topic_stmts.append((line_num, stmt))
        elif head.startswith('insert into help_category'):
            category_stmts.append((line_num, stmt))
        elif head.startswith('insert into help_keyword'):
            keyword_stmts.append((line_num, stmt))
        elif head.startswith('insert into help_relation'):
            relation_stmts.append((line_num, stmt))
        else:
            errors.append(f"Line {line_num}: Unrecognized statement: {stmt[:80]}")

    seen_topic_ids = set()
    seen_names = set()

    for line_num, stmt in topic_stmts:
        size = len(stmt.encode('utf-8'))
        if size > 20000:
            errors.append(f"Line {line_num}: help_topic statement is {size} bytes (>20000 bootstrap limit)")

        id_match = re.match(r'INSERT INTO help_topic[^V]*VALUES\s*\((\d+),', stmt, re.IGNORECASE)
        if id_match:
            topic_id = int(id_match.group(1))
            if topic_id in seen_topic_ids:
                errors.append(f"Line {line_num}: Duplicate help_topic_id {topic_id}")
            seen_topic_ids.add(topic_id)

        name_match = re.match(r"INSERT INTO help_topic[^V]*VALUES\s*\(\d+,\s*\d+,\s*'([^']*(?:''[^']*)*)'", stmt, re.IGNORECASE)
        if name_match:
            name = name_match.group(1)
            if not name or name.isspace():
                errors.append(f"Line {line_num}: Empty topic name")
            if name in seen_names:
                warnings.append(f"Line {line_num}: Duplicate name '{name}'")
            seen_names.add(name)

    seen_keyword_ids = set()
    for line_num, stmt in keyword_stmts:
        id_match = re.search(r'values\s*\((\d+),', stmt, re.IGNORECASE)
        if id_match:
            kid = int(id_match.group(1))
            if kid in seen_keyword_ids:
                errors.append(f"Line {line_num}: Duplicate help_keyword_id {kid}")
            seen_keyword_ids.add(kid)

    for line_num, stmt in relation_stmts:
        rel_match = re.search(r'values\s*\((\d+),\s*(\d+)\)', stmt, re.IGNORECASE)
        if rel_match:
            tid = int(rel_match.group(1))
            kid = int(rel_match.group(2))
            if tid not in seen_topic_ids:
                errors.append(f"Line {line_num}: help_relation references unknown topic_id {tid}")
            if kid not in seen_keyword_ids:
                errors.append(f"Line {line_num}: help_relation references unknown keyword_id {kid}")

    if len(topic_stmts) < 500:
        errors.append(f"Only {len(topic_stmts)} topics (expected 500+)")
    if len(category_stmts) < 10:
        errors.append(f"Only {len(category_stmts)} categories (expected 10+)")
    if len(keyword_stmts) < 100:
        errors.append(f"Only {len(keyword_stmts)} keywords (expected 100+)")

    print("=== SQL Validation Report ===")
    print(f"  Categories: {len(category_stmts)}")
    print(f"  Topics:     {len(topic_stmts)}  (unique IDs: {len(seen_topic_ids)}, unique names: {len(seen_names)})")
    print(f"  Keywords:   {len(keyword_stmts)}  (unique IDs: {len(seen_keyword_ids)})")
    print(f"  Relations:  {len(relation_stmts)}")
    print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:20]:
            print(f"  - {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")
        print()
        print("VALIDATION FAILED")
        return False

    print("ALL CHECKS PASSED")
    return True


if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "fill_help_tables.sql"
    success = validate_sql(file_path)
    sys.exit(0 if success else 1)
