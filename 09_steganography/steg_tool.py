from stegano import lsb
import argparse
import sys
import os

def hide_message(image_path, message, output_path):
    try:
        secret = lsb.hide(image_path, message)
        secret.save(output_path)
        print(f"[+] Message hidden successfully.")
        print(f"[+] Output saved to: {output_path}")
    except Exception as e:
        print(f"Error hiding message: {e}")

def reveal_message(image_path):
    try:
        clear_message = lsb.reveal(image_path)
        if clear_message:
            print(f"[+] Revealed Message: {clear_message}")
        else:
            print("[-] No message found.")
    except Exception as e:
        print(f"Error revealing message: {e}")

def main():
    parser = argparse.ArgumentParser(description="Steganography Tool (LSB)")
    parser.add_argument("action", choices=['hide', 'reveal'], help="Action to perform")
    parser.add_argument("image", help="Path to image file")
    parser.add_argument("-m", "--message", help="Message to hide (required for 'hide')")
    parser.add_argument("-o", "--output", help="Output path (optional for 'hide')")

    args = parser.parse_args()

    if args.action == 'hide':
        if not args.message:
            print("Error: Message is required for 'hide' action.")
            sys.exit(1)
        
        output = args.output
        if not output:
            filename, ext = os.path.splitext(args.image)
            output = f"{filename}_secret{ext}"
            
        hide_message(args.image, args.message, output)
        
    elif args.action == 'reveal':
        reveal_message(args.image)

if __name__ == "__main__":
    main()
