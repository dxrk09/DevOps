#!/usr/bin/env python3

import os
import tarfile
import datetime
import argparse
import logging

# Function to archive logs
def archive_logs(log_dir, archive_dir):
    if not os.path.exists(log_dir):
        print(f"Error: The log directory '{log_dir}' does not exist.")
        return
    
    # Create archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Generate archive filename with timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_dir, archive_name)

    try:
        # Compress logs into tar.gz file
        with tarfile.open(archive_path, "w:gz") as tar:
            tar.add(log_dir, arcname=os.path.basename(log_dir))
        print(f"Logs archived successfully: {archive_path}")
        
        # Log the archive creation details
        log_message = f"[{timestamp}] Archived logs from '{log_dir}' to '{archive_path}'\n"
        log_file = os.path.join(archive_dir, "archive_log.txt")
        with open(log_file, "a") as f:
            f.write(log_message)
        print(f"Archive details logged in: {log_file}")
    except Exception as e:
        print(f"Error while archiving logs: {e}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Log Archiver Tool")
    parser.add_argument(
        "log_directory", help="The directory containing logs to archive."
    )
    parser.add_argument(
        "--output-directory", 
        default="./archives",
        help="The directory where the archive should be stored (default: ./archives)."
    )
    args = parser.parse_args()

    log_dir = args.log_directory
    archive_dir = args.output_directory

    archive_logs(log_dir, archive_dir)

if __name__ == "__main__":
    main()
