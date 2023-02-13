import sys
logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        # filter out CRON lines
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
        
print(usernames)

# Filter by regex
import re
pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
result = re.search(pattern, line)
print(result[1])

# dictionary count users
usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)