import base64
import webbrowser
import time

# --- NUCLEUS CORE PROTOCOL V.6.1 (STABLE) ---

def _verify(s):
    # Core Logic: Sum of ASCII values must match the target.
    return sum(ord(i) for i in s) == 956

def main():
    print("------------------------------------------")
    print("    A.T.O.M IP-CORE: RESTRICTED ACCESS    ")
    print("------------------------------------------")
    
    # Encrypted Endpoint
    _target = "YXRvbTMwLWN5YmVyLmdpdGh1Yi5pby9BX1RfT19NXy1fMzBfLi9GaW5hbF9Mb2dpY19HYXRlLmNwcA=="
    
    try:
        user_input = input("ENTER KERNEL ACCESS KEY: ")
        
        if _verify(user_input):
            print("\n[+] LOGIC VALIDATED. ACCESSING SOURCE...")
            time.sleep(1.5)
            
            # Decoding and forming the final URL
            _res = base64.b64decode(_target).decode()
            full_url = "https://" + _res
            
            print(f"\n>> ESTABLISHING CONNECTION: {full_url}")
            webbrowser.open(full_url)
            
            # Prevents immediate console closure
            input("\n[SUCCESS] Press Enter to terminate session.")
            
        else:
            # Displays the sum for the user to figure out the logic
            current_sum = sum(ord(i) for i in user_input)
            print(f"\n[!] ACCESS DENIED. LOG_SUM: {current_sum} / TARGET: 956")
            input("\nPress Enter to retry...")
            
    except Exception as e:
        print(f"\n[!] KERNEL PANIC: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()