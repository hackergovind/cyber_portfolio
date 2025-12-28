import dns.resolver
import argparse
import sys

def get_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        print(f"--- {record_type} Records ---")
        for rdata in answers:
            print(f" {rdata}")
    except dns.resolver.NoAnswer:
        print(f"--- {record_type} Records ---")
        print(" No records found.")
    except dns.resolver.NXDOMAIN:
        print(f"Error: Domain '{domain}' does not exist.")
        return False
    except Exception as e:
        print(f"Error retrieving {record_type} records: {e}")
    return True

def main():
    parser = argparse.ArgumentParser(description="DNS Lookup Tool")
    parser.add_argument("domain", help="Domain to resolve (e.g., google.com)")
    
    args = parser.parse_args()
    domain = args.domain
    
    print(f"Resolving DNS records for: {domain}\n")
    
    # Common record types to query
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    for r_type in record_types:
        if not get_dns_records(domain, r_type):
            break # Stop if domain doesn't exist
        print("")

if __name__ == "__main__":
    main()
