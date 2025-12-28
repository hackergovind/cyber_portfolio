import winreg
import re
import random
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_random_mac():
    # 02 as first byte ensures it's a locally administered address (safe for spoofing)
    mac = [0x02, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ''.join(map(lambda x: "%02x" % x, mac)).upper()

def list_interfaces():
    # Helper to list interfaces from Registry
    interfaces = []
    reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"
    
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
    except Exception as e:
        print(f"Error opening registry: {e}")
        return []

    for i in range(100):
        try:
            subkey_name = "%04d" % i
            subkey = winreg.OpenKey(reg_key, subkey_name)
            try:
                desc, _ = winreg.QueryValueEx(subkey, "DriverDesc")
                interfaces.append((subkey_name, desc))
            except:
                pass
        except:
            break
            
    return interfaces

def change_mac(interface_index, new_mac):
    reg_path = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\%s" % interface_index
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "NetworkAddress", 0, winreg.REG_SZ, new_mac)
        winreg.CloseKey(key)
        print(f"[+] MAC Address changed to {new_mac} for interface index {interface_index}")
        print("[!] You generally need to disable and re-enable the adapter for changes to take effect.")
        return True
    except Exception as e:
        print(f"Error changing MAC: {e}")
        return False

def main():
    if not is_admin():
        print("[-] This script requires Administrator privileges.")
        # re-run as admin if possible or just exit? Exit is safer for a script.
        sys.exit(1)

    print("--- MAC Address Spoofer ---")
    print("Listing Interfaces from Registry...")
    
    interfaces = list_interfaces()
    for idx, (reg_idx, desc) in enumerate(interfaces):
        print(f"[{idx}] {desc} (RegID: {reg_idx})")
        
    choice = input("\nSelect interface index (number): ")
    try:
        selected_idx = int(choice)
        reg_idx, desc = interfaces[selected_idx]
    except:
        print("Invalid selection.")
        sys.exit(1)
        
    print(f"Selected: {desc}")
    new_mac = input("Enter new MAC (leave empty for random): ").strip().replace(":", "").replace("-", "").upper()
    
    if not new_mac:
        new_mac = get_random_mac()
        
    if len(new_mac) != 12:
        print("Invalid MAC length.")
        sys.exit(1)
        
    print(f"Spoofing to: {new_mac}")
    change_mac(reg_idx, new_mac)

if __name__ == "__main__":
    main()
