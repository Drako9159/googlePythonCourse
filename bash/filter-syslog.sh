#!/bin/bash
#cut -d" " -f5- /var/log/syslog | grep -i "cron" | grep -v "sudo" | wc -l
# iterate over all log files in /var/log and print the top 5 
#lines for each file that repeat the most
for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d" " -f5- $logfile | sort | uniq -c | sort -nr | head -5
done