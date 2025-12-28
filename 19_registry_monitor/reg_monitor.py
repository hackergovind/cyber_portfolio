import winreg
import time
import sys

# Keys to monitor for persistence
MONITORED_KEYS = [
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
]

def get_registry_values(hive, subkey):
    values = {}
    try:
        key = winreg.OpenKey(hive, subkey, 0, winreg.KEY_READ)
        i = 0
        while True:
            try:
                name, data, _ = winreg.EnumValue(key, i)
                values[name] = data
                i += 1
            except OSError:
                break
        winreg.CloseKey(key)
    except PermissionError:
        # Might fail for HKLM if not admin
        pass
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error reading {subkey}: {e}")
    return values

def get_snapshot():
    snapshot = {}
    for hive, subkey in MONITORED_KEYS:
        hive_name = "HKCU" if hive == winreg.HKEY_CURRENT_USER else "HKLM"
        full_path = f"{hive_name}\\{subkey}"
        snapshot[full_path] = get_registry_values(hive, subkey)
    return snapshot

def monitor():
    print("--- Windows Registry Monitor ---")
    print("[*] Taking baseline snapshot...")
    baseline = get_snapshot()
    print(f"[*] Monitoring started. Watching {len(baseline)} keys for changes...")
    
    try:
        while True:
            time.sleep(3)
            current = get_snapshot()
            
            for key_path, current_values in current.items():
                baseline_values = baseline.get(key_path, {})
                
                # Check for added or modified
                for name, data in current_values.items():
                    if name not in baseline_values:
                        print(f"[!] NEW ALERT: Value Added to {key_path}")
                        print(f"    Name: {name}")
                        print(f"    Data: {data}")
                        baseline_values[name] = data
                    elif baseline_values[name] != data:
                        print(f"[!] MOD ALERT: Value Modified in {key_path}")
                        print(f"    Name: {name}")
                        print(f"    Old Data: {baseline_values[name]}")
                        print(f"    New Data: {data}")
                        baseline_values[name] = data
                
                # Check for deleted
                deleted = []
                for name in baseline_values:
                    if name not in current_values:
                        print(f"[-] DEL ALERT: Value Deleted from {key_path}")
                        print(f"    Name: {name}")
                        deleted.append(name)
                
                for name in deleted:
                    del baseline_values[name]
                    
    except KeyboardInterrupt:
        print("\n[*] Stopping.")

if __name__ == "__main__":
    monitor()
