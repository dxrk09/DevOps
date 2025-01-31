# Log Archiver Tool

## Project Overview
This project provides a command-line tool (`log-archive.py`) to compress and archive logs from a specified directory into a `.tar.gz` file. It helps maintain a clean system by compressing old logs and storing them in a separate directory for future reference. Additionally, the tool logs the details of each archive operation to a log file.

## Features
- Accepts a log directory as an argument.
- Compresses logs into a `.tar.gz` file.
- Stores the archive in a specified output directory (default: `./archives`).
- Logs the date and time of each archive operation to a `archive_log.txt` file.
- Simple and user-friendly CLI tool.

## Requirements
- Python 3.x
- Unix-based system (Linux, macOS) or WSL on Windows.

## Installation
1. Clone or download the script to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Make the script executable:
   ```bash
   chmod +x log-archive.py
## Usage
Run the script using the command line:

   ```bash
./log-archive.py <log-directory> --output-directory <output-directory>
   ```

## Arguments:
- `<log-directory>`: The directory containing the logs to be archived.
- `--output-directory`: The directory where the archive will be stored. (Optional, default: `./archives`)

## Example:
1. Archive logs from `/var/log` and store them in the `./archives` directory:
```bash
./log-archive.py <log-directory> --output-directory <output-directory>
   ```
2. Archive logs from `/var/log` and store them in /home/user/archives:
```bash
./log-archive.py /var/log --output-directory /home/user/archives
   ```

## Output:
- Compressed archive: `logs_archive_YYYYMMDD_HHMMSS.tar.gz`
- Log file: `archive_log.txt`
## Example Workflow

1. Command:

```bash
./log-archive.py /var/log
   ```
2. Output:

```bash
Logs archived successfully: ./archives/logs_archive_20240816_100648.tar.gz
Archive details logged in: ./archives/archive_log.txt
   ```
3. Directory Structure:

```bash
./archives/
├── logs_archive_20240816_100648.tar.gz
└── archive_log.txt
   ```

## Advanced Features (Optional)
Enhance the tool with additional features:

1. **Email Notifications**: Send an email to the user after each archive operation using `smtplib`.
2. **Cloud Upload**: Upload the archive to cloud storage (e.g., AWS S3, Google Cloud Storage).
3. **Automatic Scheduling**: Automate the tool using `cron` or `systemd`.
   
## Troubleshooting
- Ensure you have read permissions for the log directory.
- If the tool cannot create the output directory, verify that you have sufficient write permissions.
- For Python errors, ensure Python 3.x is installed and correctly configured.
