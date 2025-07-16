import re
from collections import Counter

# Path to log file
log_file = "auth.log"  # Replace with your own log file path

# Regex pattern for failed logins
pattern = r"Failed password for invalid user (\w+) from ([\d.]+)"

usernames = []
ips = []

with open(log_file, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            usernames.append(match.group(1))
            ips.append(match.group(2))

print("\nTop 5 Usernames Attempted:")
for user, count in Counter(usernames).most_common(5):
    print(f"{user}: {count} times")

print("\nTop 5 IPs Attempted:")
for ip, count in Counter(ips).most_common(5):
    print(f"{ip}: {count} times")














