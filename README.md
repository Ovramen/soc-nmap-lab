# Python Nmap Port Scanner (SOC Lab Project)

This project contains two simple Python-based port scanners designed for SOC Analyst practice.  
Both scanners use Nmap through Python’s `subprocess` module and read their targets from a `targets.txt` file.

The project includes:

- **scanner_full ports.py** - scans **all ports** (`-p-`)
- **scanner_common.py** - scans **most commonly used ports** (faster)

---

## Requirements

### 1. Install Python packages
No external packages are required unless you install optional helpers.  
Python’s built-in `subprocess` module is used.

### 2. Install Nmap  
You must install **Nmap 7.92** (stable version without OpenSSL issues):

Linux/Windows/macOS downloads:  
https://nmap.org/dist/

Check installation:

nmap --version


---

## Project Structure

.
├── scanner_full.py
├── scanner_common.py
├── targets.txt
└── README.md


---

## targets.txt Format

Place each target on a new line:

scanme.nmap.org
1.1.1.1
8.8.8.8
example.com


No comments, no quotes, no commas.

---

## Running the Scanners

### Full Port Scan (slower)

python scanner_full.py


### Common Ports Scan (faster)

python scanner_common.py


---

## scanner_full.py (Description)

- Reads targets from `targets.txt`
- Runs:

nmap -p- <target>

- Extracts and prints all discovered open ports.

---

## scanner_common.py (Description)

- Reads targets from `targets.txt`
- Scans a predefined list of common ports (80, 443, 22, 53, etc.)
- Runs:

nmap -p<comma-separated-port-list> <target>

- Much faster than a full scan.

---

## Purpose

These scripts simulate a typical SOC task:

- Identifying open ports on production servers  
- Automating Nmap scans  
- Parsing output  
- Producing clean, readable results  

They can be extended with threading, logging, JSON export, SIEM ingestion, etc.

---

## License

This project is for educational and SOC training purposes.