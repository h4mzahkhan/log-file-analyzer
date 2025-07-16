# Log File Analyzer

A simple Python script to analyze Linux `auth.log` files and extract the top 5 most attempted usernames and IP addresses from failed SSH login attempts.

## 🔍 What It Does

- Reads through an `auth.log` file
- Uses regex to identify failed login attempts
- Displays the most common usernames and IPs

## 🛠 How to Use

1. Make sure Python is installed
2. Place your `auth.log` file in the same folder
3. Run the script:

```bash
python log_analyzer.py