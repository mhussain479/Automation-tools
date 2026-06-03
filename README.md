# Automation and security tools
Practical Python and Bash scripts for automation, OSINT, and server management. Includes handy tools for bug bounty hunters and sysadmins.

---

## Tools

### 1. Subdomain Finder (`subdomain_finder.py`)
Queries crt.sh for subdomains of a given domain, checks which are live, and then outputs HTTP status codes to a CSV file.

**Usage:**
```bash
1. Install required library
pip install requests

2.Download the file or clone the repo

3. Run it
python subdomain_finder.py <domain>
```
### Output: domain_subdomains.csv with columns: Subdomain, Status

---

### 2. Server Health Check (server_cleanup.sh)
This tool runs disk usage, memory, uptime checks and cleans the /tmp directory if needed.

**Usage:**
```bash
chmod +x server_cleanup.sh
./server_cleanup.sh
```

---

### Custom Scripts
Need a custom automation or security tool? DM me on reddit: u/Opposite-Blood-3808 or Telegram: mhuss479
