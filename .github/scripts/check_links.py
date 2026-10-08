import os
import re
import sys
import threading
import requests
from queue import Queue
import argparse

# --- CONFIGURATION ---
MAX_LINK_CHECKER_THREADS = 10

# --- HELPER FUNCTIONS (from our server.py) ---

def check_link(link_info, broken_links_list, lock):
    """
    Checks a single link and appends to the list if broken.
    link_info is a dict: {'link': 'http://...', 'files': ['file1.md'], 'anchors': set(['text'])}
    """
    link = link_info['link']
    try:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }
        response = requests.get(link, timeout=7, allow_redirects=True, headers=headers)
        
        if 400 <= response.status_code < 600:
            with lock:
                link_info['status'] = response.status_code
                broken_links_list.append(link_info)
    except requests.exceptions.Timeout:
        with lock:
            link_info['status'] = 'Timeout'
            broken_links_list.append(link_info)
    except requests.exceptions.ConnectionError:
        with lock:
            link_info['status'] = 'Connection Error'
            broken_links_list.append(link_info)
    except Exception:
        with lock:
            link_info['status'] = 'Invalid URL'
            broken_links_list.append(link_info)

def check_links_threaded(links_to_check):
    """
    links_to_check is a list of link_info dictionaries
    """
    broken_links = []
    link_queue = Queue()
    lock = threading.Lock()
    
    for link_info in links_to_check:
        link_queue.put(link_info)

    def worker():
        while not link_queue.empty():
            link_info = link_queue.get()
            if link_info:
                check_link(link_info, broken_links, lock)
            link_queue.task_done()

    num_threads = min(MAX_LINK_CHECKER_THREADS, len(links_to_check))
    for _ in range(num_threads):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
    
    link_queue.join()
    return broken_links

def find_markdown_files(start_dir):
    """Finds all .md files in the directory, ignoring .git."""
    md_files = []
    for root, dirs, files in os.walk(start_dir, topdown=True):
        # Exclude .git directory
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def parse_files_for_links(md_files):
    """Parses all files and returns a map of unique links to the files they appear in."""
    link_map = {} # { 'http://...': {'link': 'http://...', 'files': set(['file1.md']), 'anchors': set(['text'])} }
    
    link_regex = re.compile(r'\[(.*?)\]\((https?://[^\)]+)\)')
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for text, url in link_regex.findall(content):
                if url not in link_map:
                    link_map[url] = {'link': url, 'files': set(), 'anchors': set()}
                
                link_map[url]['files'].add(file_path)
                link_map[url]['anchors'].add(text or "[No Anchor Text]") # Add anchor text

        except Exception as e:
            print(f"Warning: Could not read file {file_path}. Error: {e}", file=sys.stderr)
            
    return list(link_map.values())

def main(scan_directory):
    print(f"--- Starting Broken Link Check ---")
    print(f"Scanning for .md files in: {scan_directory}\n")
    
    md_files = find_markdown_files(scan_directory)
    if not md_files:
        print("No markdown files found. Exiting.")
        sys.exit(0)
        
    print(f"Found {len(md_files)} markdown files.")
    
    links_to_check = parse_files_for_links(md_files)
    if not links_to_check:
        print("No external links found. Exiting.")
        sys.exit(0)
        
    print(f"Found {len(links_to_check)} unique external links. Checking all...")
    
    broken_links = check_links_threaded(links_to_check)
    
    if not broken_links:
        print("\n--- \U0001F389 All links are healthy! ---")
        sys.exit(0)
    else:
        print(f"\n--- \U0001F6A8 Found {len(broken_links)} Broken Links! ---")
        for b in broken_links:
            print(f"\n[ {b['status']} ] {b['link']}")
            print(f"  Anchors: {', '.join(b['anchors'])}")
            print("  Found in:")
            for file in b['files']:
                print(f"  - {file}")
        
        # This is the most important line:
        # It tells GitHub Actions that this step has failed.
        print("\nBroken links found. Failing the build.")
        sys.exit(1)

if __name__ == "__main__":
    # This allows us to pass the directory from the command line
    parser = argparse.ArgumentParser(description='Check markdown files for broken links.')
    parser.add_argument('--directory', dest='directory', required=True,
                        help='The root directory to scan for .md files')
    args = parser.parse_args()
    
    main(args.directory)
