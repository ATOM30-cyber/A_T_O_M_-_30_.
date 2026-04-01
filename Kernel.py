import base64
import hashlib
import webbrowser

# --- NUCLEUS CORE PROTOCOL V.5 ---
# [SYSTEM_NOTE]: The Core V6 is unstable. 7 is the divisor of failure. Patch the gate.

def _verify(s):
    if len(s) != 16:
        return False
    
    # Mathematical Constraints
    _c1 = sum(ord(i) for i in s) == 956
    _c2 = ord(s[0]) + ord(s[-1]) == 157
    _c3 = all((ord(s[i]) % 2 != 0) for i in range(1, 5))

    return _c1 and _c2 and _c3

def main():
    print("------------------------------------------")
    print("   A.T.O.M IP-CORE: RESTRICTED ACCESS     ")
    print("------------------------------------------")
    
    # Encrypted payload
    _target = "VmxSR2FrMVhSbk5pUm1SWFlURndNMVpyV2t0V2JHeDBaTVZ3V0Zac2JETlhhMUpQWVRBeFZWWnRhRlpXVmtwT1ZsWmtXbFpXYkhObFZUVldVbFJXVlRWWFYwWkdXbXhXY0hCV2JHdz0="
    
    try:
        user_input = input("ENTER KERNEL ACCESS KEY: ")
        
        if _verify(user_input):
            print("\n[+] LOGIC VALIDATED. DECRYPTING NUCLEUS...")
            
            # Triple Base64 Decode
            _res = base64.b64decode(base64.b64decode(base64.b64decode(_target))).decode()
            
            print(f"\n>> ACCESS GRANTED: {_res}")
            print("------------------------------------------")
            print("[!] INITIALIZING FINAL CORE DOWNLOAD...")
            
            # Automated redirect to C++ Stage
            webbrowser.open("https://atom30-cyber.github.io/.A_T_O_M_-_30_/Final_Logic_Gate.cpp")
            
        else:
            print("\n[!] ACCESS DENIED: INVALID LOGIC SEQUENCE.")
            
    except Exception:
        print("\n[!] KERNEL PANIC: DATA CORRUPTION.")

if __name__ == "__main__":
    main()