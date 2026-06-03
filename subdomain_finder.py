import requests
import os
import sys
import time

if len(sys.argv) < 2:
    print("[!] Usage: python subdomain_finder.py <domain>")
    print("[!] Example: python subdomain_finder.py tesla.com")
    sys.exit(1)

domain = sys.argv[1]
print(f"[*] Fetching subdomains for {domain}...")

r = requests.get(f"https://crt.sh/?q={domain}&output=json")
data = r.json()

subdomains = set()
for entry in data:
    name = entry.get("name_value", "")
    for sub in name.split("\n"):
        if sub and "*" not in sub:
            subdomains.add(sub.strip())

subdomains = sorted(subdomains)

results = []
for sub in subdomains:
    status = "Dead/Timeout"
    for scheme in ["https://", "http://"]:
        try:
            r = requests.get(f"{scheme}{sub}", timeout=2)
            status = r.status_code
            break
        except:
            continue
    results.append((sub, status))
    print(f"{sub} --> {status}")
    time.sleep(0.1)

filename = f"{domain}_subdomains.csv"
with open(filename, "w") as f:
    f.write("Subdomain,Status\n")
    for sub, status in results:
        f.write(f"{sub},{status}\n")

print(f"[+] Found {len(subdomains)} unique subdomains")
print(f"[+] Saved to {os.getcwd()}/{filename}")
