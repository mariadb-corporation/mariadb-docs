import re
from pathlib import Path

# Directories to exclude (per Stefan's guidance)
EXCLUDED_DIRS = [
    "system-tables",
    "error-codes",
    "clientserver-protocol",
    "product-development",
]

# Maps directory path segments to help_category_id from mysql.help_category
CATEGORY_MAP = {
    "string-functions": 37,
    "aggregate-functions": 16,
    "numeric-functions": 4,
    "date-time-functions": 31,
    "control-flow-functions": 7,
    "encryption-functions": 12,
    "information-functions": 17,
    "bit-functions": 19,
    "miscellaneous-functions": 14,
    "data-types": 22,
    "plugins": 5,
    "stored-procedures": 33,
    "stored-functions": 33,
    "stored-routines": 33,
    "transactions": 8,
    "data-definition": 39,
    "data-manipulation": 27,
    "account-management": 10,
    "geometry": 34,
    "geometry-constructors": 24,
    "geometry-properties": 36,
    "geometry-relations": 30,
    "sql-language-structure": 29,
    "operators": 38,
    "comparison-operators": 18,
    "logical-operators": 15,
    "user-defined-functions": 21,
    "table-maintenance": 20,
    "administrative": 26,
}

def get_category_id(path: str) -> int:
    """Match directory path to category ID. Returns 35 (Contents) if no match."""
    for key, cat_id in CATEGORY_MAP.items():
        if key in path:
            return cat_id
    return 35  # Default: Contents


def get_files(base_path: str = "server/reference") -> list:
    """Find all .md files in base_path, excluding EXCLUDED_DIRS and README files."""
    files = []
    base = Path(base_path)
    
    for md_file in base.rglob("*.md"):
        path_str = str(md_file)
        
        # Skip excluded directories
        if any(excluded in path_str for excluded in EXCLUDED_DIRS):
            continue
        
        # Skip README files
        if md_file.name == "README.md":
            continue
            
        files.append(path_str)
    
    return sorted(files)


def open_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

    
def find_line_range(data: list):
    start = None
    end = None
    name = None
    data_length = len(data)
    
    for line in range(data_length):
        if data[line].startswith("# "):
            start = line
            name = data[line].lstrip("# ")
            break
    
    if start is None:
        return None, None
    
    see_also_pattern = re.compile(r'^#{2,}\s*see\s+also', re.IGNORECASE)
    
    for line in range(start, data_length):
        if (see_also_pattern.match(data[line]) 
            or data[line].lower().startswith("{% @marketo/form") 
            or data[line].lower().startswith("<sub>")):
            end = line
            break
    
    if end is None:
        end = data_length
    
    content = data[start:end]
    return content, name


def extract_sections(content: list):
    syntax_start = None
    desc_start = None
    example_start = None
    
    syntax_pattern = re.compile(r'^#{2,}\s*syntax', re.IGNORECASE)
    desc_pattern = re.compile(r'^#{2,}\s*(description|overview)', re.IGNORECASE)
    example_pattern = re.compile(r'^#{2,}\s*examples?', re.IGNORECASE)
    
    for line in range(len(content)):
        if syntax_pattern.match(content[line]):
            syntax_start = line
        elif desc_pattern.match(content[line]) and desc_start is None:
            desc_start = line
        elif example_pattern.match(content[line]) and example_start is None:
            example_start = line

    # Standard case: has Syntax and Description/Overview
    if syntax_start is not None and desc_start is not None:
        syntax = content[syntax_start:desc_start]
        syntax_content = extract_code_block(syntax)
        if example_start:
            desc = content[desc_start+1:example_start]
        else:
            desc = content[desc_start+1:]
    # Has Description/Overview but no Syntax
    elif desc_start is not None:
        syntax_content = []
        if example_start:
            desc = content[desc_start+1:example_start]
        else:
            desc = content[desc_start+1:]
    # Fallback: no Syntax, no Description - use prose after title
    else:
        syntax_content = []
        if example_start:
            desc = content[1:example_start]  # Skip title line
        else:
            desc = content[1:]  # Everything after title
    
    # Extract example code block
    example_content = extract_code_block(content[example_start+1:] if example_start else [])
    
    # Build description string
    if syntax_content:
        description = "\n".join(syntax_content) + "\n\n" + "\n".join(desc)
    else:
        description = "\n".join(desc)
 
    return description, example_content


def extract_code_block(lines: list):
    start = None
    stop = None
    
    for i in range(len(lines)):
        if lines[i] == "```sql" and start is None:
            start = i
        elif lines[i] == "```" and start is not None:
            stop = i
            break
    
    if start is not None and stop is not None:
        return lines[start+1:stop]
    
    return []


def build_output(name, desc: str, example: list, path: str):
    example_str = "\n".join(example)
    desc_str = f"Syntax:\n{desc}"
    url_path = path.removesuffix(".md")
    url = f"https://mariadb.com/docs/{url_path}"

    content = {
        "name": name,
        "description": desc_str, 
        "example": example_str, 
        "url": url,
    }

    return content

def escape_sql(text):
    # Escape single quotes and convert newlines to \n literal
    text = text.replace("'", "''")
    text = text.replace("\n", "\\n")
    return text

def generate_insert(name, description, example, help_topic_id, url, help_category_id):

    sql = (
        f"INSERT INTO help_topic (help_topic_id, help_category_id, name, description, example, url) "
        f"VALUES ({help_topic_id}, {help_category_id}, '{name}', '{description}', '{example}', '{url}');"
    )
    return sql


def process_single_file(path: str, help_topic_id: int) -> str:
    """Process a single file and return INSERT statement or None on failure."""
    try:
        data = open_file(path)
        content, name = find_line_range(data)
        
        if content is None:
            return None
            
        desc, example = extract_sections(content)
        full_content = build_output(name, desc, example, path)

        name_ = escape_sql(full_content["name"])
        description_ = escape_sql(full_content["description"])
        example_ = escape_sql(full_content["example"])
        url_ = escape_sql(full_content["url"])
        category_id = get_category_id(path)
        
        return generate_insert(name_, description_, example_, help_topic_id, url_, category_id)
        
    except Exception as e:
        print(f"Failed to parse {path}: {e}")
        return None


def process_batch(file_list: list, start_id: int = 1000) -> list:
    """Process all files and return list of INSERT statements."""
    statements = []
    help_topic_id = start_id
    failed = []
    
    for path in file_list:
        result = process_single_file(path, help_topic_id)
        if result:
            statements.append(result)
            help_topic_id += 1
        else:
            failed.append(path)
    
    print(f"Processed: {len(statements)} files")
    print(f"Failed: {len(failed)} files")
    
    return statements, failed


def write_output(statements: list, output_file: str = "fill_help_tables.sql"):
    """Write all INSERT statements to a SQL file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for stmt in statements:
            f.write(stmt + "\n")
    print(f"Written to {output_file}")


def main():
    # Get all files to process
    files = get_files("server/reference")
    print(f"Found {len(files)} files to process")
    
    # Process all files
    statements, failed = process_batch(files)
    
    # Write output
    write_output(statements)
    
    # Optionally write failed files for review
    if failed:
        with open("failed_files.txt", 'w') as f:
            for path in failed:
                f.write(path + "\n")
        print(f"Failed files written to failed_files.txt")


if __name__ == "__main__":
    main()