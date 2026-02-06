import re

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
    desc_pattern = re.compile(r'^#{2,}\s*description', re.IGNORECASE)
    example_pattern = re.compile(r'^#{2,}\s*examples?', re.IGNORECASE)
    
    for line in range(len(content)):
        if syntax_pattern.match(content[line]):
            syntax_start = line
        elif desc_pattern.match(content[line]):
            desc_start = line
        elif example_pattern.match(content[line]):
            example_start = line

    desc = content[desc_start+2:example_start-1] if desc_start and example_start else []
    syntax = content[syntax_start:desc_start-1] if syntax_start and desc_start else []
    
    syntax_content = extract_code_block(syntax)
    example_content = extract_code_block(content[example_start+1:] if example_start else [])
    
    description = "\n".join(syntax_content) + "\n\n" + "\n".join(desc)
 
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
    return text.replace("'", "''")

def generate_insert(name, description, example, help_topic_id, url, help_category_id):

    sql = (
        f"INSERT INTO help_topic (help_topic_id, help_category_id, name, description, example, url) "
        f"VALUES ({help_topic_id}, {help_category_id}, '{name}', '{description}', '{example}', '{url}');"
    )
    return sql


def main():
    path = 'server/server-usage/stored-routines/stored-procedures/alter-procedure.md'

    help_topic_id = 1000

    try:
        data = open_file(path)
        content, name = find_line_range(data)
        
        if content is None:
            print(f"Failed to parse {path}: No H1 heading found")
            return None
            
        desc, example = extract_sections(content)
        full_content = build_output(name, desc, example, path)

        name_ = escape_sql(full_content["name"])
        description_ = escape_sql(full_content["description"])
        example_ = escape_sql(full_content["example"])
        url_ = escape_sql(full_content["url"])
        category_id = get_category_id(path)
        insert_statement = generate_insert(name_, description_, example_, help_topic_id, url_, category_id)

        # print("insert statement", insert_statement)
        
    except Exception as e:
        print(f"Failed to parse {path}: {e}")
        return None

if __name__ == "__main__":
    main()

       