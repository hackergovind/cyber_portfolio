import base64
import codecs
import sys

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(text):
    try:
        return base64.b64decode(text).decode()
    except Exception as e:
        return f"Error: {e}"

def encode_hex(text):
    return text.encode().hex()

def decode_hex(text):
    try:
        return bytes.fromhex(text).decode()
    except Exception as e:
        return f"Error: {e}"

def rot13(text):
    return codecs.encode(text, 'rot_13')

def main():
    print("--- Encoder / Decoder Tool ---")
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Hex Encode")
    print("4. Hex Decode")
    print("5. Rot13 (Toggle)")
    
    choice = input("Enter choice (1-5): ").strip()
    text = input("Enter text: ")
    
    if choice == '1':
        print(f"Result: {encode_base64(text)}")
    elif choice == '2':
        print(f"Result: {decode_base64(text)}")
    elif choice == '3':
        print(f"Result: {encode_hex(text)}")
    elif choice == '4':
        print(f"Result: {decode_hex(text)}")
    elif choice == '5':
        print(f"Result: {rot13(text)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
