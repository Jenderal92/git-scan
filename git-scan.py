import requests
import threading
from Queue import Queue

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def print_banner():
    print(Colors.YELLOW + """
        Mass .git/HEAD Scanner Multithreading | Shin Code
    """ + Colors.RESET)

def load_previous_results(output_file):
    try:
        with open(output_file, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    except IOError:
        return set()

def scan_url(url, headers, timeout, results, lock, output_file):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    git_head_url = url.rstrip("/") + "/.git/HEAD"
    
    try:
        response = requests.get(git_head_url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            content = response.text.strip()
            if "ref: refs/heads/master" in content:
                print(Colors.GREEN + "[+] FOUND: " + git_head_url + Colors.RESET)
                print("[+] Content: " + content)
                with lock:
                    if git_head_url not in results:
                        results.add(git_head_url)
                        with open(output_file, 'a') as f:
                            f.write(git_head_url + "\n")
            else:
                print(Colors.YELLOW + "[!] SKIPPED (Not master branch): " + git_head_url + Colors.RESET)
        elif response.status_code == 403:
            print(Colors.YELLOW + "[!] FORBIDDEN: " + git_head_url + Colors.RESET)
        elif response.status_code == 404:
            print(Colors.RED + "[-] NOT FOUND: " + git_head_url + Colors.RESET)
        else:
            print(Colors.RED + "[-] ERROR: " + git_head_url + " (Status: " + str(response.status_code) + ")" + Colors.RESET)
    except requests.exceptions.ConnectionError:
        print(Colors.RED + "[-] ERROR: " + git_head_url + " (Connection error)" + Colors.RESET)
    except requests.exceptions.ReadTimeout:
        print(Colors.RED + "[-] ERROR: " + git_head_url + " (Read timeout)" + Colors.RESET)
    except requests.exceptions.RequestException:
        print(Colors.RED + "[-] ERROR: " + git_head_url + " (Request failed)" + Colors.RESET)

def worker(queue, headers, timeout, results, lock, output_file):
    while not queue.empty():
        url = queue.get()
        scan_url(url, headers, timeout, results, lock, output_file)
        queue.task_done()

def mass_scan(file_path, output_file, thread_count=10):
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except IOError:
        print(Colors.RED + "[-] Error: Could not read file " + file_path + Colors.RESET)
        return
    previous_results = load_previous_results(output_file)
    print(Colors.GREEN + "[*] Loaded {} existing results from {}".format(len(previous_results), output_file) + Colors.RESET)

    queue = Queue()
    for url in urls:
        queue.put(url)

    print(Colors.GREEN + "[*] Starting scan with " + str(thread_count) + " threads..." + Colors.RESET)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }
    timeout = 5
    results = previous_results.copy()
    lock = threading.Lock()
    threads = []

    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(queue, headers, timeout, results, lock, output_file))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(Colors.GREEN + "[*] Scan complete! Total results: {}".format(len(results)) + Colors.RESET)

if __name__ == "__main__":
    print_banner()
    file_path = raw_input("Put ur list  (e.g., urls.txt): ")
    output_file = "results.txt"
    try:
        thread_count = int(raw_input("Enter the number of threads (default 5): ") or 5)
    except ValueError:
        print(Colors.RED + "[-] Invalid thread count, using default (5)." + Colors.RESET)
        thread_count = 5
    mass_scan(file_path, output_file, thread_count)
