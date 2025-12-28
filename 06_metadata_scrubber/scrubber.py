from PIL import Image
import sys
import os

def remove_metadata(image_path, output_path):
    try:
        img = Image.open(image_path)
        
        # We create a new image without the data
        # Converting to RGB drops some metadata, and saving without 'exif' keyword finishes it.
        data = list(img.getdata())
        image_without_exif = Image.new(img.mode, img.size)
        image_without_exif.putdata(data)
        
        # Alternatively, just save the original image and explicitly exclude exif
        # img.save(output_path, "JPEG", exif=b"") 
        # But creating a new image is often cleaner for stripping everything.
        
        image_without_exif.save(output_path)
        print(f"[+] Metadata removed. Saved to: {output_path}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrubber.py <image_path> [output_path]")
        sys.exit(1)
        
    input_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Generate default output name
        filename, ext = os.path.splitext(input_path)
        output_path = f"{filename}_clean{ext}"
        
    print(f"Processing: {input_path}")
    remove_metadata(input_path, output_path)

if __name__ == "__main__":
    main()
