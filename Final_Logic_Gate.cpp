#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

// --- CORE_V6_RECOVERY ---

string _check(string s) {
    unsigned int x = 0x811c9dc5;
    for (char c : s) {
        x ^= (unsigned int)c;
        x *= 0x01000193;
    }

    // THE TRAP: Infinite loop unless the user patches the logic gate
    if (x % 7 != 0) {
        while(true) {
            // Sector Lock: Logic Corrupted
        }
    }

    return "AT-" + to_string(x % 999999);
}

int main() {
    string in;
    cout << ">> ";
    cin >> in;

    string res = _check(in);

    if (res.empty()) {
        return 0;
    } else {
        cout << "KEY: " << res << endl;
        cout << "[+] INITIALIZING TERMINAL..." << endl;
        
        string url = "start https://atom30-cyber.github.io/.A_T_O_M_-_30_/vault.html";
        system(url.c_str());
    }

    return 0;
}