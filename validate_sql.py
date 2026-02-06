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

    insert_pattern = re.compile(
        r"^INSERT INTO help_topic "
        r"\(help_topic_id, help_category_id, name, description, example, url\) "
        r"VALUES \(\d+, \d+, '.+', '.+', '.*', '.+'\);$"
    )

    seen_ids = set()
    seen_names = set()

    for i, line in enumerate(lines, 1):
        line = line.rstrip('\n')

        # Check: valid INSERT structure
        if not line.startswith("INSERT INTO help_topic"):
            errors.append(f"Line {i}: Not an INSERT statement")
            continue

        # Check: statement ends with );
        if not line.endswith(");"):
            errors.append(f"Line {i}: Statement not terminated with );")

        # Extract help_topic_id
        id_match = re.search(r'VALUES \((\d+),', line)
        if id_match:
            topic_id = int(id_match.group(1))
            if topic_id in seen_ids:
                errors.append(f"Line {i}: Duplicate help_topic_id {topic_id}")
            seen_ids.add(topic_id)

        # Extract name
        name_match = re.search(r"VALUES \(\d+, \d+, '([^']*(?:''[^']*)*)'", line)
        if name_match:
            name = name_match.group(1)
            if not name or name.isspace():
                errors.append(f"Line {i}: Empty name")
            if name in seen_names:
                warnings.append(f"Line {i}: Duplicate name '{name}'")
            seen_names.add(name)

        # Check: unescaped single quotes (odd number of consecutive quotes)
        values_part = line[line.index("VALUES"):]
        in_string = False
        j = 0
        while j < len(values_part):
            if values_part[j] == "'" and (j == 0 or values_part[j-1] != "\\"):
                in_string = not in_string
                # Check for escaped quotes ''
                if j + 1 < len(values_part) and values_part[j+1] == "'":
                    j += 1  # skip the escaped quote
                    in_string = not in_string
            j += 1

    # Check: minimum count
    total = len(lines)
    if total < 500:
        errors.append(f"Only {total} statements generated (expected 1000+)")

    # Print results
    print(f"=== SQL Validation Report ===")
    print(f"Total statements: {total}")
    print(f"Unique topic IDs: {len(seen_ids)}")
    print(f"Unique names: {len(seen_names)}")
    print()

    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:20]:  # Show first 20
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
