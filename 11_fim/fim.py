import hashlib
import os
import time
import sys

BASELINE_FILE = "baseline.txt"

def calculate_file_hash(filepath):
    try:
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None

def get_file_hashes(directory):
    files_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # convert to absolute path for consistency
            filepath = os.path.abspath(filepath)
            
            # Skip the baseline file itself if it's in the same directory
            if BASELINE_FILE in filepath:
                continue
                
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                files_hashes[filepath] = file_hash
    return files_hashes

def create_baseline(directory):
    print(f"[*] Creating baseline for: {directory}")
    hashes = get_file_hashes(directory)
    
    with open(BASELINE_FILE, "w") as f:
        for filepath, file_hash in hashes.items():
            f.write(f"{filepath}|{file_hash}\n")
            
    print(f"[+] Baseline created with {len(hashes)} files.")
    print(f"[+] Saved to {os.path.abspath(BASELINE_FILE)}")

def load_baseline():
    baseline = {}
    if not os.path.exists(BASELINE_FILE):
        return None
    
    with open(BASELINE_FILE, "r") as f:
        for line in f:
            if "|" in line:
                filepath, file_hash = line.strip().split("|")
                baseline[filepath] = file_hash
    return baseline

def monitor(directory):
    print(f"[*] Starting monitoring for: {directory}")
    baseline = load_baseline()
    if baseline is None:
        print("[-] Baseline not found. Please create baseline first.")
        return

    print("[*] Monitoring... (Press Ctrl+C to stop)")
    
    try:
        while True:
            time.sleep(2)
            current_hashes = get_file_hashes(directory)
            
            # Check for new and modified files
            for filepath, current_hash in current_hashes.items():
                if filepath not in baseline:
                    print(f"[+] NEW FILE DETECTED: {filepath}")
                    baseline[filepath] = current_hash # Update in-memory baseline to avoid spamming
                elif current_hash != baseline[filepath]:
                    print(f"[!] FILE MODIFIED: {filepath}")
                    baseline[filepath] = current_hash
            
            # Check for deleted files
            # Create a list of keys to remove to avoid runtime error during iteration
            deleted_files = []
            for filepath in baseline:
                if filepath not in current_hashes:
                    print(f"[-] FILE DELETED: {filepath}")
                    deleted_files.append(filepath)
            
            for f in deleted_files:
                del baseline[f]
                
    except KeyboardInterrupt:
        print("\n[*] Monitoring stopped.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python fim.py <directory>")
        sys.exit(1)
        
    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print("Invalid directory.")
        sys.exit(1)
        
    print("Select Mode:")
    print("1) Create Baseline")
    print("2) Start Monitoring")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        create_baseline(target_dir)
    elif choice == "2":
        monitor(target_dir)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
