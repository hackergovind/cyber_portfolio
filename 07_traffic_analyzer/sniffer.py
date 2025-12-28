from scapy.all import sniff, IP, TCP, UDP, ARP
import sys

def packet_callback(packet):
    # Check if packet has IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        protocol_name = "OTHER"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"
            
        print(f"[IP] {ip_src} -> {ip_dst} | Protocol: {protocol_name}")
        
    elif ARP in packet:
        print(f"[ARP] {packet[ARP].psrc} -> {packet[ARP].pdst} | Op: {packet[ARP].op}")

def main():
    print("Starting Network Sniffer...")
    print("Note: This often requires Administrator/Root privileges.")
    print("Press Ctrl+C to stop.")
    print("-" * 50)
    
    # Filter can be added, e.g., filter="tcp port 80"
    try:
        sniff(prn=packet_callback, store=0, count=20) # Capturing 20 packets for demo
        print("-" * 50)
        print("Sniffing finished (20 packets captured for demo).")
    except Exception as e:
        print(f"Error: {e}")
        print("Did you run as Administrator?")

if __name__ == "__main__":
    main()
