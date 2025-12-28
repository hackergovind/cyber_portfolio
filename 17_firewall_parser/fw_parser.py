import re
import argparse
import os
from collections import Counter

def parse_fw_log(log_file):
    if not os.path.exists(log_file):
        print(f"Error: File '{log_file}' not found.")
        return

    print(f"[*] Parsing {log_file}...")
    
    # Regex for UFW logs typically: "... [UFW BLOCK] ... SRC=<ip> ... DPT=<port>"
    # We look for "UFW BLOCK" to confirm it's a block event (or just parse all)
    
    blocked_ips = []
    targeted_ports = []
    
    with open(log_file, 'r') as f:
        for line in f:
            if "UFW BLOCK" in line:
                # Extract IP and Port
                # SRC=192.168.1.1
                src_match = re.search(r"SRC=([\d\.]+)", line)
                dpt_match = re.search(r"DPT=(\d+)", line)
                
                if src_match:
                    blocked_ips.append(src_match.group(1))
                if dpt_match:
                    targeted_ports.append(dpt_match.group(1))

    # Statistics
    print(f"[*] Parsing complete. Found {len(blocked_ips)} blocked connection attempts.")
    
    if blocked_ips:
        print("\n--- Top Attackers (Source IPs) ---")
        ip_counts = Counter(blocked_ips).most_common(5)
        for ip, count in ip_counts:
            print(f"{ip:<20} : {count} attempts")
            
        print("\n--- Top Targeted Ports ---")
        port_counts = Counter(targeted_ports).most_common(5)
        for port, count in port_counts:
            print(f"{port:<20} : {count} attempts")
    else:
        print("[*] No blocks found.")

def main():
    parser = argparse.ArgumentParser(description="Firewall Log Parser (UFW)")
    parser.add_argument("logfile", help="Path to firewall log file")
    
    args = parser.parse_args()
    parse_fw_log(args.logfile)

if __name__ == "__main__":
    main()
