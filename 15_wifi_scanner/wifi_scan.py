import subprocess
import re
import sys

def get_wifi_networks():
    # Windows command to show networks
    try:
        # standard output encoding might vary, using errors='ignore' for safety
        result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], shell=True, stderr=subprocess.STDOUT)
        result = result.decode('utf-8', errors='ignore')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return []

    networks = []
    # Parsing the output is non-trivial as it's text based and varies by locale
    # Typical block:
    # SSID 1 : MyNetwork
    #     Network type            : Infrastructure
    #     Authentication          : WPA2-Personal
    #     Encryption              : CCMP
    #     BSSID 1                 : aa:bb:cc:dd:ee:ff
    #         Signal             : 90%
    
    # We will split by "SSID"
    parts = result.split("SSID ")
    for part in parts[1:]: # skip preamble
        try:
            lines = part.splitlines()
            # First line is "N : Name"
            name_part = lines[0].split(":", 1)
            if len(name_part) < 2: continue
            ssid = name_part[1].strip()
            
            auth = "Unknown"
            encryption = "Unknown"
            signal = "Unknown"
            
            for line in lines:
                if "Authentication" in line:
                    auth = line.split(":", 1)[1].strip()
                if "Encryption" in line:
                    encryption = line.split(":", 1)[1].strip()
                if "Signal" in line:
                    signal = line.split(":", 1)[1].strip()
            
            networks.append({
                "SSID": ssid,
                "Auth": auth,
                "Encryption": encryption,
                "Signal": signal
            })
        except Exception as e:
            continue
            
    return networks

def main():
    print("Scanning for WiFi Networks (Windows)...")
    networks = get_wifi_networks()
    
    if not networks:
        print("[-] No networks found or interface disabled.")
        return

    print(f"\n[+] Found {len(networks)} networks:\n")
    print(f"{'SSID':<30} {'SIGNAL':<10} {'AUTH':<20} {'ENCRYPTION':<10}")
    print("-" * 75)
    
    for net in networks:
        print(f"{net['SSID']:<30} {net['Signal']:<10} {net['Auth']:<20} {net['Encryption']:<10}")

if __name__ == "__main__":
    main()
