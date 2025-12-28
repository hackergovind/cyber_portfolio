import re
import argparse
import urllib.parse
import ipaddress

def is_ip_address(domain):
    try:
        ipaddress.ip_address(domain)
        return True
    except ValueError:
        return False

def analyze_url(url):
    print(f"[*] Analyzing: {url}")
    score = 0
    alerts = []
    
    # Parse URL
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    path = parsed.path
    
    # 1. IP Address Check
    if is_ip_address(domain):
        score += 3
        alerts.append("Host is an IP address (High Risk)")
        
    # 2. Length Check
    if len(url) > 75:
        score += 1
        alerts.append("URL length is suspicious (>75 chars)")
        
    # 3. '@' Symbol (Obfuscation)
    if '@' in url:
        score += 3
        alerts.append("Contains '@' symbol (Possible credential embedding)")
        
    # 4. Double Slash in Path
    if '//' in path:
        score += 2
        alerts.append("Path contains '//' (Possible redirect/obfuscation)")
        
    # 5. Suspicious Keywords in Path/Domain
    keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'paypal', 'signin', 'ebay', 'amazon']
    for word in keywords:
        if word in domain or word in path:
            # If it's a known legit domain, maybe ignore, but generally phishing sites use these in subdomains
            # For this simple detector, we flag if it's NOT the main domain (heuristic)
            # A simple way: check if the keyword is in the URL to flag it as "Targeting sensitive info"
            alerts.append(f"Contains sensitive keyword: '{word}'")
            score += 0.5 # Just presence isn't immediate phishing, but combined it is bad
            
    # 6. Excessive Subdomains
    subdomains = domain.split('.')
    # remove www
    if subdomains[0] == 'www':
        subdomains.pop(0)
    
    if len(subdomains) > 3:
        score += 1
        alerts.append(f"Excessive subdomains ({len(subdomains)})")
        
    # 7. Suspicious TLD (Bit rough, but common check)
    if domain.endswith(('.xyz', '.top', '.club', '.info')):
        score += 1
        alerts.append("Uses potentially suspicious TLD (.xyz, .top, etc)")

    print(f"[-] Risk Score: {score}")
    if alerts:
        print("[-] Alerts:")
        for alert in alerts:
            print(f"    - {alert}")
    
    if score >= 3:
        print("[!] VERDICT: PHISHING / HIGH RISK")
    elif score >= 1:
        print("[!] VERDICT: SUSPICIOUS")
    else:
        print("[+] VERDICT: SAFE (Low Risk)")
    print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Phishing URL Detector (Heuristic)")
    parser.add_argument("url", help="URL to analyze")
    args = parser.parse_args()
    
    analyze_url(args.url)

if __name__ == "__main__":
    main()
