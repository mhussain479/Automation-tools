# Automation and security tools
Practical Python and Bash scripts for automation, OSINT, server management, and everyday productivity. Includes handy tools for bug bounty hunters, sysadmins, and anyone looking to automate repetitive tasks.

---

## Tools

### 1. Subdomain Finder (`subdomain_finder.py`)
Queries crt.sh for subdomains of a given domain, checks which are live, and then outputs HTTP status codes to a CSV file.

**Usage:**
```bash
Install required library
pip install requests

Download the file or clone the repo

Run it
python subdomain_finder.py <domain>
```
### Output: domain_subdomains.csv with columns: Subdomain, Status

---

### 2. Server Health Check (`server_cleanup.sh`)
This tool runs disk usage, memory, uptime checks and cleans the /tmp directory if needed.

**Usage:**
```bash
chmod +x server_cleanup.sh
./server_cleanup.sh
```

---

### 3. Gmail Inbox Cleaner (`inbox_cleaner.py`)
This tool bulk deletes emails by their sender. Searches your Gmail, finds all relevant emails via pagination, asks for confirmation then removes to the trash.

**Setup:**
1. Follow the [Gmail API Python Quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python) 
2. Enable the Gmail API
3. Create a Desktop OAuth credential
4. Download as `credentials.json` and place in the same folder as the script

**Usage:**
```bash
python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python inbox_cleaner.py
```

### 4. Invoice Data Extractor (`invoice_extractor.py`)
This tool extracts key fields from PDF invoices (invoice number, date, total, etc.) and outputs a clean CSV. It uses regex for flexible field detection (can be edited to suit different field names) alongside error handling for any corrupted or scanned PDFs.

**Usage:**
1. Install: `pip install pdfplumber`
2. Create an `invoices` folder, drop your PDFs in
3. Run: `python invoice_extractor.py`
4. Get `all_invoices.csv` with all extracted data

### Custom Scripts
Need a custom automation or security tool? DM me on Discord: c4spi4n_98034  or Telegram: mhuss479
