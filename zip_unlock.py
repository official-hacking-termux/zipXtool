import os
import time
import random
from colorama import Fore, Style, init

 # Initialize colorama for colored output

init(autoreset=True)

 # Banner design

def banner():
    os.system('clear')
    print(Fore.GREEN + Style.BRIGHT + """                ╔══════════════════════════════════════════════╗
║ 🔐 ZIP PASSWORD CRACKER TOOL                 ║
║       📺 YouTube: https://www.youtube.com/@Official_Hacking_Termux  >
║       👤 Created By: Anonymous               ║
║       🔗 Telegram: https://t.me/Official_Hacking_Termux             >
║       📸 Instagram: https://www.instagram.com/official_hacking_termu>
╚══════════════════════════════════════════════╝                                   """)
    print(Fore.CYAN + "🔥 Wordlist Brute Force Simulation")
    print(Fore.RED + "⚠️  For Educational Purposes Only!\n")

# Fake cracking process
def fake_crack(zip_path, wordlist_path):
    try:
        open(zip_path, 'rb')  # Just to simulate file check
    except:
        print(Fore.RED + "[!] ZIP file not found or invalid.")
        return

    try:
        with open(wordlist_path, 'r', errors='ignore') as wordlist:
            passwords = wordlist.readlines()
            total = len(passwords)

            # Safe range for fake event point
            safe_min = max(1, total // 2)
            safe_max = max(safe_min + 1, total - 1)
            fake_success_point = random.randint(safe_min, safe_max)

            for count, password in enumerate(passwords, start=1):
                password = password.strip()
                print(Fore.YELLOW + f"[-] Trying: {password}")
                time.sleep(random.uniform(0.2, 0.5))  # Simulated delay

                if count == fake_success_point:
                    print(Fore.CYAN + "[*] Still trying... this may take time.")

                if count == total:
                    print(Fore.RED + "\n❌ Password not found in wordlist.")
                    return
    except FileNotFoundError:
        print(Fore.RED + "[!] Wordlist file not found.")
        return

# Main function
def main():
    banner()
    zip_path = input(Fore.CYAN + "📦 Enter ZIP file path: " + Fore.WHITE)
    wordlist_path = input(Fore.CYAN + "📜 Enter wordlist path: " + Fore.WHITE)
    print(Fore.MAGENTA + "\n🔎 Cracking in progress...\n")
    fake_crack(zip_path, wordlist_path)

# Run the tool
if __name__ == "__main__":
    main()
