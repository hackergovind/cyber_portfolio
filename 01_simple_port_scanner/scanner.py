import socket
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def scan_port(ip, port, open_ports):
    """
    Scans a single port on the target IP.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # specific error handling for clearer output if needed, but simple connect is fine
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        pass # connection failed or timeout

def main():
    parser = argparse.ArgumentParser(description="Simple Multithreaded Port Scanner")
    parser.add_argument("target", help="Target IP address to scan")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
    
    args = parser.parse_args()
    
    target_ip = args.target
    start_port = args.start
    end_port = args.end
    threads = args.threads
    
    # Resolve hostname to IP if needed
    try:
        target_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        print("Error: Hostname could not be solved")
        return

    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Scanning Ports: {start_port} to {end_port}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []
    
    # Using ThreadPoolExecutor for managing threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port, open_ports)
            
    print("-" * 50)
    print(f"Scanning completed at: {datetime.now()}")
    if open_ports:
        print(f"Open Ports: {sorted(open_ports)}")
    else:
        print("No open ports found in the specified range.")
    print("-" * 50)

if __name__ == "__main__":
    main()
