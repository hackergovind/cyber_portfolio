import hashlib
import sys
import itertools
import string
import os

def hash_text(text, algo='md5'):
    if algo == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    return None

def dictionary_attack(target_hash, wordlist_path, algo='md5'):
    print(f"[*] Starting Dictionary Attack using {wordlist_path}...")
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as f:
            for line in f:
                word = line.strip()
                if hash_text(word, algo) == target_hash:
                    return word
    except FileNotFoundError:
        print("Error: Wordlist file not found.")
    return None

def brute_force_attack(target_hash, max_length=4, algo='md5'):
    print(f"[*] Starting Brute Force Attack (Max Length: {max_length})...")
    chars = string.ascii_lowercase + string.digits
    
    for length in range(1, max_length + 1):
        print(f"    Checking length {length}...")
        for guess in itertools.product(chars, repeat=length):
            word = ''.join(guess)
            if hash_text(word, algo) == target_hash:
                return word
    return None

def main():
    print("--- Hash Cracker Tool ---")
    target_hash = input("Enter target hash: ").strip()
    algo = input("Enter algorithm (md5/sha256): ").strip().lower()
    mode = input("Enter mode (dict/brute): ").strip().lower()
    
    if algo not in ['md5', 'sha256']:
        print("Unsupported algorithm.")
        sys.exit(1)
        
    result = None
    
    if mode == 'dict':
        wordlist = input("Enter wordlist path (default: wordlist.txt): ").strip()
        if not wordlist:
            # default relative to script
            wordlist = os.path.join(os.path.dirname(__file__), "wordlist.txt")
            
        result = dictionary_attack(target_hash, wordlist, algo)
        
    elif mode == 'brute':
        try:
            max_len = int(input("Enter max length (recommend < 5 for demo): "))
        except:
            max_len = 3
        result = brute_force_attack(target_hash, max_len, algo)
    
    else:
        print("Invalid mode.")
        sys.exit(1)
        
    if result:
        print(f"\n[SUCCESS] Password found: {result}")
    else:
        print("\n[FAIL] Password not found.")

if __name__ == "__main__":
    main()
