import argparse
import sys

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine ASCII offset (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            
            # Perform shift
            # (char_code - offset + shift) % 26 + offset
            processed_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += processed_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")
    parser.add_argument("-m", "--mode", choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")
    parser.add_argument("-t", "--text", help="Text to process")
    parser.add_argument("-s", "--shift", type=int, help="Shift value")
    
    args = parser.parse_args()

    # Interactive mode if arguments are missing
    if not args.mode or not args.text or args.shift is None:
        print("--- Caesar Cipher Tool ---")
        if not args.mode:
            args.mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
        if not args.text:
            args.text = input("Enter text: ")
        if args.shift is None:
            try:
                args.shift = int(input("Enter shift value (integer): "))
            except ValueError:
                print("Invalid shift value.")
                sys.exit(1)

    if args.mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
        sys.exit(1)

    result = caesar_cipher(args.text, args.shift, args.mode)
    
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
