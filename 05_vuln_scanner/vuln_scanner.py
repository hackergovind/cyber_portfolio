import socket
import os
import sys

def return_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except Exception as e:
        return None

def check_vulns(banner, filename):
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                vuln = line.strip()
                if vuln in banner:
                    print(f"[!] VULNERABLE BANNER FOUND: '{banner}' match with '{vuln}'")
                    return True
    except FileNotFoundError:
        print(f"Error: Vulnerability database file '{filename}' not found.")
        sys.exit(1)
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python vuln_scanner.py <target_ip>")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    # Common ports to check for banners (FTP, SSH, Telnet, SMTP, HTTP, POP3)
    port_list = [21, 22, 23, 25, 80, 110, 445]
    
    vuln_file = os.path.join(os.path.dirname(__file__), "vulns.txt")
    
    print(f"Scanning target: {target_ip}")
    print(f"Using vulnerability database: {vuln_file}\n")
    
    for port in port_list:
        print(f"[*] Checking port {port}...")
        banner = return_banner(target_ip, port)
        if banner:
            print(f"    [+] Banner: {banner}")
            check_vulns(banner, vuln_file)
        else:
            print("    [-] No banner or connection failed.")

if __name__ == "__main__":
    main()
