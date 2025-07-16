# Log File Analyzer

A simple Python script to analyze Linux `auth.log` files and extract the top 5 most attempted usernames and IP addresses from failed SSH login attempts.

## What It Does

- Reads through an `auth.log` file
- Uses regex to identify failed login attempts
- Displays the most common usernames and IPs

## How to Use

1. Make sure Python is installed
2. Place your `auth.log` file in the same folder
3. Make sure the entries in the `auth.log` file are formatted like: "Jul 14 10:15:47 localhost sshd[1999]: Failed password for invalid user test from 192.168.1.11 port 2222 ssh2"
4. Run the script:

```bash
python log_analyzer.py