from scapy.all import sniff, ARP
import sys

# Global variable to store Gateway MAC
gateway_mac = None
gateway_ip = None

def get_mac(ip):
    # Helper to get MAC of an IP (uses scapy srp)
    from scapy.all import srp, Ether
    # Create ARP request
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    return None

def process_packet(packet):
    global gateway_mac
    
    if packet.haslayer(ARP) and packet[ARP].op == 2: # 2 is 'is-at' (response)
        try:
            real_source_ip = packet[ARP].psrc
            response_mac = packet[ARP].hwsrc
            
            if real_source_ip == gateway_ip:
                if gateway_mac is None:
                    gateway_mac = response_mac
                    print(f"[*] Gateway ({gateway_ip}) initial MAC: {gateway_mac}")
                elif gateway_mac != response_mac:
                    print(f"[!] ALERT: ARP SPOOFING DETECTED!")
                    print(f"    Gateway IP: {gateway_ip}")
                    print(f"    Expected MAC: {gateway_mac}")
                    print(f"    New/Fake MAC: {response_mac}")
                    # Update to avoid spamming if it persists (or keep spamming for alert)
                    # gateway_mac = response_mac 
        except IndexError:
            pass

def main():
    global gateway_ip, gateway_mac
    
    print("--- ARP Spoofing Detector ---")
    if len(sys.argv) < 2:
        gateway_ip = input("Enter Gateway IP to monitor: ").strip()
    else:
        gateway_ip = sys.argv[1]

    print(f"[*] monitoring Gateway: {gateway_ip}")
    print("[*] Resolving initial MAC address...")
    
    try:
        gateway_mac = get_mac(gateway_ip)
    except Exception as e:
        print(f"Error getting initial MAC: {e}")
        # Proceed with None, waiting for first packet
    
    if gateway_mac:
        print(f"[*] Initial MAC: {gateway_mac}")
    else:
        print("[*] Could not resolve MAC automatically. Waiting for traffic...")
    
    print("[*] Sniffing ARP packets... (Press Ctrl+C to stop)")
    try:
        sniff(filter="arp", prn=process_packet, store=0)
    except KeyboardInterrupt:
        print("\n[*] Stopping.")
    except Exception as e:
        print(f"Error: {e}")
        print("Note: Requires Administrator privileges.")

if __name__ == "__main__":
    main()
