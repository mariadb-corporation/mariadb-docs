import os
import re
import urllib.request

# --- Robust Path Configuration ---
def find_repo_root():
    """Automatically locates the true root of the repository"""
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir): 
        if os.path.exists(os.path.join(current_dir, 'server', 'SUMMARY.md')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return os.getcwd() 

DOCS_ROOT = find_repo_root()
SUMMARY_FILE = os.path.join(DOCS_ROOT, 'server', 'SUMMARY.md')
ERROR_CODES_DIR = os.path.join(DOCS_ROOT, 'server', 'reference', 'error-codes')

# --- Dual-Source Live URLs ---
MARIADB_ERRMSG_URL = 'https://raw.githubusercontent.com/MariaDB/server/main/sql/share/errmsg-utf8.txt'
MYSQL_FALLBACK_URL = 'https://raw.githubusercontent.com/mysql/mysql-server/trunk/share/messages_to_clients.txt'

# --- Regex Patterns ---
ERROR_DEF_RE = re.compile(r'^(ER_|WARN_|OBSOLETE_ER_)([A-Z0-9_]+)\s*([A-Z0-9]+)?\s*([A-Z0-9]+)?')
MSG_TEXT_RE = re.compile(r'(?:eng|text)\s+"(.*)"')
SUMMARY_SECTION_RE = re.compile(r'^\s*\*\s*\[.*(\d{4,5})\s+to\s+(\d{4,5})\].*')

# --- Markdown Template ---
MD_TEMPLATE = """# Error {error_code}: {desc_title}

| Error Code | SQLSTATE | Error                    | Description                                               |
| ---------- | -------- | ------------------------ | --------------------------------------------------------- |
| {error_code:<10} | {sqlstate:<8} | {error_name_escaped:<24} | {description} |

## Possible Causes and Solutions

{custom_content}{{% include "../../../.gitbook/includes/contributing-content.md" %}}

{{% include "../../../.gitbook/includes/license-cc-by-sa-gnu-fdl.md" %}}

{fallback_comment}{{% @marketo/form formId="4316" %}}
"""

def parse_mysql_fallback(url):
    """Maps Error String Tokens (like ER_CANT_SET_VARIABLE...) directly to English descriptions."""
    mysql_dict = {}
    print(f"[INFO] Downloading MySQL fallback descriptions from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8', errors='replace')
            lines = content.splitlines()
    except Exception as e:
        print(f"[WARNING] Could not load MySQL fallback data: {e}")
        return {}

    current_name = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('//'):
            continue
            
        tokens = line.split()
        if tokens and (tokens[0].startswith('ER_') or tokens[0].startswith('WARN_') or tokens[0].startswith('OBSOLETE_ER_')):
            current_name = tokens[0].replace('OBSOLETE_', '')
            eng_match = MSG_TEXT_RE.search(line)
            if eng_match:
                mysql_dict[current_name] = eng_match.group(1)
                current_name = None
            continue
            
        if current_name and ('eng "' in line or 'text "' in line):
            eng_match = MSG_TEXT_RE.search(line)
            if eng_match:
                mysql_dict[current_name] = eng_match.group(1)
                current_name = None
                
    return mysql_dict

def parse_mariadb_file(url):
    """Downloads and parses the foundational MariaDB err text file."""
    errors = {}
    current_number = 0
    current_obj = None

    print(f"[INFO] Downloading MariaDB base file from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8', errors='replace')
            lines = content.splitlines()
    except Exception as e:
        print(f"[ERROR] Failed to fetch MariaDB base file: {e}")
        return {}

    for line in lines:
        line = line.rstrip()
        
        if line.startswith('start-error-number'):
            current_number = int(line.split()[1])
            continue
        if line.startswith('skip-to-error-number'):
            current_number = int(line.split()[1])
            continue

        if line.startswith('ER_') or line.startswith('WARN_'):
            match = ERROR_DEF_RE.match(line)
            if match:
                sqlstate = "HY000" 
                tokens = line.split()
                if len(tokens) > 1 and not tokens[1].startswith('eng'):
                     if len(tokens[1]) == 5:
                         sqlstate = tokens[1]
                
                error_name = tokens[0]

                current_obj = {
                    'code': current_number,
                    'name': error_name,
                    'sqlstate': sqlstate,
                    'description': "" 
                }
                
                eng_match = MSG_TEXT_RE.search(line)
                if eng_match:
                    current_obj['description'] = eng_match.group(1)
                    errors[current_number] = current_obj
                    current_obj = None 
                else:
                    errors[current_number] = current_obj  
                
                current_number += 1
                continue

        if current_obj and 'eng "' in line:
            eng_match = MSG_TEXT_RE.search(line)
            if eng_match:
                current_obj['description'] = eng_match.group(1)
                current_obj = None 

    return errors

def get_folder_name(code):
    return f"mariadb-error-codes-{(code // 100) * 100}-to-{(code // 100) * 100 + 99}"

def preserve_custom_content(file_path):
    if not os.path.exists(file_path):
        return ""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'## Possible Causes and Solutions\s*\n(.*?)(\n{% include|$)', re.DOTALL)
    match = pattern.search(content)
    if match:
        custom_text = match.group(1).strip()
        if custom_text:
            return custom_text + "\n\n"
    return ""

def update_summary_file(new_pages):
    if not os.path.exists(SUMMARY_FILE):
        print("[ERROR] SUMMARY.md not found.")
        return

    print("[INFO] Line-sorting and updating SUMMARY.md...")
    with open(SUMMARY_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_pages_by_range = {}
    for code, path, title in new_pages:
        range_start = (code // 100) * 100
        new_pages_by_range.setdefault(range_start, []).append((code, path, title))

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = SUMMARY_SECTION_RE.match(line)
        
        if match:
            range_start = int(match.group(1))
            new_lines.append(line)
            
            indent_match = re.match(r'^(\s*)\*', line)
            base_indent = indent_match.group(1) if indent_match else "  "
            child_indent = base_indent + "  "
            
            block_entries = {}
            
            if range_start in new_pages_by_range:
                for code, path, title in new_pages_by_range[range_start]:
                    block_entries[code] = f"{child_indent}* [{title}]({path})\n"
            
            j = i + 1
            while j < len(lines):
                child_line = lines[j]
                child_match = re.search(r'/e(\d+)\.md', child_line)
                if child_match:
                    c_code = int(child_match.group(1))
                    if range_start <= c_code <= range_start + 99:
                        if c_code not in block_entries:
                            block_entries[c_code] = child_line
                        j += 1
                        continue
                break
            
            for code in sorted(block_entries.keys()):
                new_lines.append(block_entries[code])
                
            i = j  
            continue
        else:
            new_lines.append(line)
            i += 1

    with open(SUMMARY_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def main():
    print("=" * 70)
    print(" DOCS-5990: MariaDB Error Code Automation (GitHub Actions) ")
    print(f" Detected Repository Root: {DOCS_ROOT}")
    print("=" * 70)
    
    errors = parse_mariadb_file(MARIADB_ERRMSG_URL)
    if not errors:
        return
        
    mysql_fallback = parse_mysql_fallback(MYSQL_FALLBACK_URL)
    
    new_pages_for_summary = []

    for code, data in errors.items():
        folder = get_folder_name(code)
        filename = f"e{code}.md"
        
        abs_folder = os.path.join(ERROR_CODES_DIR, folder)
        abs_filepath = os.path.join(abs_folder, filename)
        
        is_unused = data['name'].startswith("ER_UNUSED_")
        file_exists = os.path.exists(abs_filepath)

        if is_unused and not file_exists:
            continue
        elif is_unused and file_exists:
            print(f"[ACTION] OVERWRITE: Error {code} downgraded to unused.")
        elif file_exists:
            continue
        else:
            print(f"[ACTION] CREATE: Resolving reference documentation for Error {code}.")

        if not os.path.exists(abs_folder):
            os.makedirs(abs_folder, exist_ok=True)

        custom_text = preserve_custom_content(abs_filepath)
        
        # --- HYBRID RECONCILIATION ENGINE ---
        raw_desc = data['description'].replace('"', '').strip()
        err_token = data['name']
        fallback_comment = ""
        
        # Check by String Variable Token key name
        if not raw_desc and err_token in mysql_fallback and mysql_fallback[err_token]:
            raw_desc = mysql_fallback[err_token].replace('"', '').strip()
            # --- FEATURE ADDITION: Inject metadata comment tracker ---
            fallback_comment = "\n\n"
            print(f"  -> Reconciled empty gap description for Error {code} via Token mapping.")

        if not raw_desc:
            if err_token.startswith("ER_MYSQL_"):
                desc_title = f"MySQL Compatibility Placeholder ({err_token})"
                desc_table = "This error code number is reserved for upstream MySQL protocol compatibility."
            else:
                desc_title = err_token.replace('ER_', '').replace('WARN_', '').replace('_', ' ').title()
                desc_table = f"Detailed reference description for {err_token} is currently unmapped."
        else:
            desc_title = raw_desc
            desc_table = raw_desc.replace('|', r'\|')

        name_escaped = err_token.replace('_', r'\_')

        content = MD_TEMPLATE.format(
            error_code=code,
            desc_title=desc_title,
            sqlstate=data['sqlstate'],
            error_name_escaped=name_escaped,
            description=desc_table,
            custom_content=custom_text,
            fallback_comment=fallback_comment
        )

        with open(abs_filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if not file_exists:
            rel_path = f"reference/error-codes/{folder}/{filename}"
            title = f"Error {code}: {desc_title}"
            new_pages_for_summary.append((code, rel_path, title))

    if new_pages_for_summary:
        update_summary_file(new_pages_for_summary)
        print(f"[INFO] Generated {len(new_pages_for_summary)} brand new error pages.")
    else:
        print("[INFO] No new errors found. Documentation is fully up to date.")

if __name__ == "__main__":
    main()