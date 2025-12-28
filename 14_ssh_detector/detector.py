import re
import argparse
import sys
import os

def parse_log(log_file, threshold=5):
    if not os.path.exists(log_file):
        print(f"Error: File '{log_file}' not found.")
        return

    print(f"[*] Parsing {log_file}...")
    
    # Regex for "Failed password for [invalid user] <user> from <ip>"
    # Example 1: Failed password for root from 10.10.10.50
    # Example 2: Failed password for invalid user admin from 10.10.10.50
    regex = r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)"
    
    failed_attempts = {}
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                user = match.group(1)
                ip = match.group(2)
                
                if ip not in failed_attempts:
                    failed_attempts[ip] = []
                failed_attempts[ip].append(user)

    print(f"[*] Analysis Complete. Checking for IPs with > {threshold} failures.\n")
    
    found_attacker = False
    for ip, attempts in failed_attempts.items():
        count = len(attempts)
        if count >= threshold:
            found_attacker = True
            print(f"[!] POTENTIAL BRUTE FORCE DETECTED!")
            print(f"    Attacker IP: {ip}")
            print(f"    Failed Attempts: {count}")
            print(f"    Targeted Users: {set(attempts)}") # Unique users targeted
            print("-" * 30)

    if not found_attacker:
        print("[+] No brute force attempts detected above threshold.")

def main():
    parser = argparse.ArgumentParser(description="SSH Brute Force Detector")
    parser.add_argument("logfile", help="Path to auth.log file")
    parser.add_argument("-t", "--threshold", type=int, default=5, help="Failure threshold (default: 5)")
    
    args = parser.parse_args()
    parse_log(args.logfile, args.threshold)

if __name__ == "__main__":
    main()
