#!/bin/bash

# Total CPU Usage
echo "=== CPU Usage ==="
top -bn1 | grep "Cpu(s)" | \
sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \
awk '{print 100 - $1 "% used"}'

# Total Memory Usage
echo -e "\n=== Memory Usage ==="
free -h | awk 'NR==2{printf "Used: %s / %s (%.2f%%)\n", $3, $2, $3/$2*100 }'

# Total Disk Usage
echo -e "\n=== Disk Usage ==="
df -h | awk '$NF=="/"{printf "Used: %s / %s (%s)\n", $3, $2, $5}'

# Top 5 Processes by CPU Usage
echo -e "\n=== Top 5 Processes by CPU Usage ==="
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -6

# Top 5 Processes by Memory Usage
echo -e "\n=== Top 5 Processes by Memory Usage ==="
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -6

# Stretch Goal - Additional Stats
echo -e "\n=== Additional System Information ==="
echo "OS Version: $(lsb_release -d | cut -f2)"
echo "Uptime: $(uptime -p)"
echo "Load Average: $(uptime | awk -F 'load average:' '{print $2}')"
echo "Logged in Users: $(who | wc -l)"
echo "Failed Login Attempts: $(grep 'Failed password' /var/log/auth.log | wc -l)"
