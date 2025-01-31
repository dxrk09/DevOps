# [Server Performance Stats](https://roadmap.sh/projects/server-stats)


## Project Overview
This project provides a simple Bash script (`server-stats.sh`) to analyze and display essential server performance metrics. The script gathers information about CPU usage, memory usage, disk usage, and lists the top 5 processes by CPU and memory consumption. It also includes optional additional stats such as OS version, uptime, load average, logged-in users, and failed login attempts.

## Features
- **Total CPU Usage**  
- **Total Memory Usage** (free vs used including percentage)  
- **Total Disk Usage** (free vs used including percentage)  
- **Top 5 Processes by CPU Usage**  
- **Top 5 Processes by Memory Usage**  
- **Additional Stats (Optional):**  
  - OS Version  
  - Uptime  
  - Load Average  
  - Number of Logged-in Users  
  - Failed Login Attempts  

## Requirements
- **Linux** (Ubuntu, CentOS, Debian, etc.)
- **Bash Shell**
- **sysstat** (for `mpstat` command)  
  Install with:  
  ```bash
  sudo apt update && sudo apt install sysstat -y

## Installation
- Clone or download the script to your Linux server.
- Make the script executable:

  ```bash
  chmod +x server-stats.sh

## Usage
Run the script with the following command:
  ```bash
  ./server-stats.sh
  ```
The script will output performance stats directly to the terminal.

## Example Output
```
==== CPU Usage ====
13.5% used

==== Memory Usage ====
Used: 2.5G, Free: 1.5G, Usage: 62.50%

==== Disk Usage ====
Used: 120G, Free: 80G, Usage: 60%

==== Top 5 Processes by CPU Usage ====
PID   COMMAND %CPU
1234  nginx   45.2
4567  java    30.1
7890  python  20.3

==== Top 5 Processes by Memory Usage ====
PID   COMMAND %MEM
2345  mysqld  22.7
6789  node    15.6

==== Additional Stats ====
OS Version:
Ubuntu 22.04.3 LTS

Uptime:
up 5 days, 3 hours, 25 minutes

Load Average:
0.42, 0.67, 0.75

Logged-in Users:
3

Failed Login Attempts:
7
```
## Troubleshooting
- If CPU stats do not display, ensure sysstat is installed (sudo apt install sysstat).
- For failed login attempts, ensure the script has root privileges (sudo ./server-stats.sh).
- Some logs may differ in path (e.g., /var/log/auth.log on Debian/Ubuntu or /var/log/secure on CentOS). Adjust the script accordingly.

## License
This project is open-source and available for use and modification under the MIT License.
