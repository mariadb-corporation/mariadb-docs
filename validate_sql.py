import re
import sys


def validate_sql(file_path: str = "fill_help_tables.sql") -> bool:
    """Validate the generated fill_help_tables.sql file."""
    errors = []
    warnings = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"FATAL: {file_path} not found")
        return False

    if not lines:
        print(f"FATAL: {file_path} is empty")
        return False

    # Classify every line
    topic_lines = []
    category_lines = []
    keyword_lines = []
    relation_lines = []
    preamble_lines = []

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip('\n')

        if not line or line.startswith('--'):
            preamble_lines.append((i, line))
        elif line.lower().startswith('set ') or line.lower().startswith('use ') or line.lower().startswith('delete '):
            preamble_lines.append((i, line))
        elif line.startswith('INSERT INTO help_topic'):
            topic_lines.append((i, line))
        elif line.lower().startswith('insert into help_category'):
            category_lines.append((i, line))
        elif line.lower().startswith('insert into help_keyword'):
            keyword_lines.append((i, line))
        elif line.lower().startswith('insert into help_relation'):
            relation_lines.append((i, line))
        else:
            errors.append(f"Line {i}: Unrecognized line: {line[:80]}")

    # --- Validate help_topic entries ---
    seen_topic_ids = set()
    seen_names = set()

    for line_num, line in topic_lines:
        if not line.endswith(");"):
            errors.append(f"Line {line_num}: help_topic not terminated with );")

        id_match = re.search(r'VALUES \((\d+),', line)
        if id_match:
            topic_id = int(id_match.group(1))
            if topic_id in seen_topic_ids:
                errors.append(f"Line {line_num}: Duplicate help_topic_id {topic_id}")
            seen_topic_ids.add(topic_id)

        name_match = re.search(r"VALUES \(\d+, \d+, '([^']*(?:''[^']*)*)'", line)
        if name_match:
            name = name_match.group(1)
            if not name or name.isspace():
                errors.append(f"Line {line_num}: Empty topic name")
            if name in seen_names:
                warnings.append(f"Line {line_num}: Duplicate name '{name}'")
            seen_names.add(name)

    # --- Validate help_keyword entries ---
    seen_keyword_ids = set()
    for line_num, line in keyword_lines:
        if not line.endswith(");"):
            errors.append(f"Line {line_num}: help_keyword not terminated with );")
        id_match = re.search(r'values\s*\((\d+),', line, re.IGNORECASE)
        if id_match:
            kid = int(id_match.group(1))
            if kid in seen_keyword_ids:
                errors.append(f"Line {line_num}: Duplicate help_keyword_id {kid}")
            seen_keyword_ids.add(kid)

    # --- Validate help_relation entries ---
    for line_num, line in relation_lines:
        if not line.endswith(");"):
            errors.append(f"Line {line_num}: help_relation not terminated with );")
        rel_match = re.search(r'values\s*\((\d+),(\d+)\)', line, re.IGNORECASE)
        if rel_match:
            tid = int(rel_match.group(1))
            kid = int(rel_match.group(2))
            if tid not in seen_topic_ids:
                errors.append(f"Line {line_num}: help_relation references unknown topic_id {tid}")
            if kid not in seen_keyword_ids:
                errors.append(f"Line {line_num}: help_relation references unknown keyword_id {kid}")

    # --- Minimum counts ---
    if len(topic_lines) < 500:
        errors.append(f"Only {len(topic_lines)} topics (expected 500+)")
    if len(category_lines) < 10:
        errors.append(f"Only {len(category_lines)} categories (expected 10+)")
    if len(keyword_lines) < 100:
        errors.append(f"Only {len(keyword_lines)} keywords (expected 100+)")

    # --- Print results ---
    print("=== SQL Validation Report ===")
    print(f"  Categories: {len(category_lines)}")
    print(f"  Topics:     {len(topic_lines)}  (unique IDs: {len(seen_topic_ids)}, unique names: {len(seen_names)})")
    print(f"  Keywords:   {len(keyword_lines)}  (unique IDs: {len(seen_keyword_ids)})")
    print(f"  Relations:  {len(relation_lines)}")
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
    raise RuntimeError("DELIBERATE TEST FAILURE — remove this line after testing")


if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else "fill_help_tables.sql"
    success = validate_sql(file_path)
    sys.exit(0 if success else 1)
