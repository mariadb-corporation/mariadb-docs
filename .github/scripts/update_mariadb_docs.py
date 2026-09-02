import os
import re
import sys
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
PAGE_DATA_ROW_RE = re.compile(r'^\|\s*(\d+)\s*\|([^|]*)\|([^|]*)\|(.*)\|\s*$')
PAGE_H1_RE = re.compile(r'^# Error \d+.*$', re.MULTILINE)
SPEC_CANON_RE = re.compile(r'%[-.#0-9*$]*(?:ll|l|z|h)?[a-zA-Z][QTE]?')

# DOCS-6564: an existing page whose code, symbol, SQLSTATE or message no longer
# matches errmsg-utf8.txt is rewritten in place (reconciled). If more than this
# many pages drift in a single run, the job fails instead of mass-rewriting —
# that scale of drift means a parse regression or an upstream renumbering that
# needs human eyes first. Override with the MAX_RECONCILE env var (0 = report-only).
DEFAULT_MAX_RECONCILE = 25

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

def display_message(raw):
    """Renders an errmsg-utf8.txt format string the way the published pages show it:
    length-limited strings become plain %s, %iE becomes %d, the Q flag becomes
    backtick quoting, and literal \\n becomes a space."""
    s = raw.replace('\\n', ' ')
    s = s.replace('%iE', '%d')
    s = re.sub(r'%[-.#0-9*$]*sQ', '`%s`', s)
    s = re.sub(r'%[-.#0-9*$]*sT?', '%s', s)
    return re.sub(r'  +', ' ', s).strip()

def canon_message(s):
    """Canonical form used ONLY to compare a page against errmsg-utf8.txt.
    Collapses printf-style specifiers, markdown escapes, quoting and terminal
    periods so presentation differences do not register as drift."""
    s = s.replace('\\n', ' ').replace('\\', '')
    s = s.replace('`', '').replace('"', '').replace("'", '')
    s = SPEC_CANON_RE.sub('%', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s.rstrip('.').strip()

def compute_display_fields(code, data, mysql_fallback):
    """Resolves the title/table-cell fields for a code. Shared by the create,
    unused-overwrite and reconcile paths. Returns (desc_title, desc_table,
    name_escaped, fallback_comment, has_mariadb_text)."""
    raw_desc = data['description'].replace('"', '').strip()
    has_mariadb_text = bool(raw_desc)
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
        raw_desc = display_message(raw_desc)
        desc_title = raw_desc
        desc_table = raw_desc.replace('|', r'\|')

    name_escaped = err_token.replace('_', r'\_')
    return desc_title, desc_table, name_escaped, fallback_comment, has_mariadb_text

def parse_page_row(file_path):
    """Extracts (code, sqlstate, symbol, message) from a page's table data row,
    or None if the page has no recognizable row."""
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            m = PAGE_DATA_ROW_RE.match(line)
            if m:
                return (int(m.group(1)),
                        m.group(2).strip(),
                        m.group(3).replace(r'\_', '_').strip(),
                        m.group(4).strip())
    return None

def stale_reason(page_row, code, data, desc_table, has_mariadb_text):
    """Why an existing page no longer matches errmsg-utf8.txt — or None if it does.
    The message is only compared when errmsg-utf8.txt itself carries the text
    (fallback-described pages are left alone if the fallback fetch failed)."""
    page_code, page_ss, page_sym, page_msg = page_row
    if page_code != code:
        return f"code cell says {page_code}"
    if page_sym != data['name']:
        return f"symbol is {page_sym}, source says {data['name']}"
    if not (page_ss == data['sqlstate'] or (data['sqlstate'] == 'HY000' and page_ss == '')):
        return f"SQLSTATE is '{page_ss}', source says '{data['sqlstate']}'"
    if has_mariadb_text and canon_message(page_msg) != canon_message(desc_table):
        return "message text no longer matches source"
    return None

def reconcile_page(file_path, code, sqlstate, desc_title, desc_table, name_escaped):
    """Surgically updates a stale page: rewrites only the H1 and the table data
    row, preserving frontmatter, hand-written content and the license line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = PAGE_H1_RE.sub(lambda m: f"# Error {code}: {desc_title}", content, count=1)

    new_row = f"| {code:<10} | {sqlstate:<8} | {name_escaped:<24} | {desc_table} |\n"
    lines = content.splitlines(keepends=True)
    for idx, line in enumerate(lines):
        if PAGE_DATA_ROW_RE.match(line):
            lines[idx] = new_row
            break

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

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
    reconciled_for_summary = []
    reconcile_queue = []

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
            # DOCS-6564: reconcile existing pages against errmsg-utf8.txt instead
            # of skipping them forever (the flaw behind DOCS-6555 and MDEV-35773).
            page_row = parse_page_row(abs_filepath)
            if page_row is None:
                print(f"[WARN] SKIP: {folder}/{filename} has no parsable data row; leaving it untouched.")
                continue
            desc_title, desc_table, name_escaped, _, has_text = compute_display_fields(code, data, mysql_fallback)
            reason = stale_reason(page_row, code, data, desc_table, has_text)
            if reason:
                reconcile_queue.append((code, abs_filepath, folder, filename,
                                        data['sqlstate'], desc_title, desc_table,
                                        name_escaped, reason))
            continue
        else:
            print(f"[ACTION] CREATE: Resolving reference documentation for Error {code}.")

        if not os.path.exists(abs_folder):
            os.makedirs(abs_folder, exist_ok=True)

        custom_text = preserve_custom_content(abs_filepath)

        desc_title, desc_table, name_escaped, fallback_comment, _ = compute_display_fields(code, data, mysql_fallback)

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

    if reconcile_queue:
        max_reconcile = int(os.environ.get('MAX_RECONCILE', DEFAULT_MAX_RECONCILE))
        if len(reconcile_queue) > max_reconcile:
            print(f"[FATAL] {len(reconcile_queue)} existing pages disagree with errmsg-utf8.txt "
                  f"(safety cap: {max_reconcile}). Refusing a mass rewrite — this usually means "
                  f"a parse regression or an upstream renumbering that needs human review. "
                  f"Re-run with MAX_RECONCILE=<n> once the drift list below is confirmed:")
            for code, _fp, folder, filename, _ss, _t, _d, _n, reason in reconcile_queue:
                print(f"  - {folder}/{filename}: {reason}")
            sys.exit(1)
        for code, fp, folder, filename, ss, desc_title, desc_table, name_escaped, reason in reconcile_queue:
            print(f"[ACTION] RECONCILE: Error {code} — {reason}.")
            reconcile_page(fp, code, ss, desc_title, desc_table, name_escaped)
            rel_path = f"reference/error-codes/{folder}/{filename}"
            reconciled_for_summary.append((code, rel_path, f"Error {code}: {desc_title}"))

    if new_pages_for_summary or reconciled_for_summary:
        update_summary_file(new_pages_for_summary + reconciled_for_summary)
    if new_pages_for_summary:
        print(f"[INFO] Generated {len(new_pages_for_summary)} brand new error pages.")
    if reconciled_for_summary:
        print(f"[INFO] Reconciled {len(reconciled_for_summary)} stale error pages against errmsg-utf8.txt.")
    if not new_pages_for_summary and not reconciled_for_summary:
        print("[INFO] No new or stale errors found. Documentation is fully up to date.")

if __name__ == "__main__":
    main()