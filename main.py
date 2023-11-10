import time
import os
from colorama import Fore
import random
import string
import ctypes
import requests
from os import system
import sys


def main(): 
    if sys.platform == "linux":
        clear = lambda: system("clear")
    else:
        clear = lambda: system("cls & mode 80,24")
    clear()
    print('''
     \x1b[38;5;199m                              
           .__  __                                                             __                
      ____ |__|/  |________  ____      ____   ____   ____   ________________ _/  |_  ___________ 
     /    \|  \   __\_  __ \/  _ \    / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \/
    |   |  \  ||  |  |  | \(  <_> )  / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
    |___|  /__||__|  |__|   \____/   \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|   
         \/                         /_____/      \/     \/     \/           \/                   \x1b[0mMade By Daddy quickyboi\x1b[0m
    ''')



    print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mInput How Many Codes to Generate and Check")
    num = int(input(f"""     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mNumber of generation: """))
    print(f"\n     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mDo you wish to use a discord webhook? - [If so type it here or press enter to ignore]")
    url = input(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mWebHook: ")
    webhook = url if url != "" else None
    valid = [] 
    invalid = 0 
    time.sleep(1)
    clear()

    for i in range(num): 
        try:
            code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16))
            url = f"https://discord.gift/{code}"
            response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if response.status_code == 200:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mVALID NITRO {url}")
                try:
                    requests.post(webhook, json={'content': url})
                except:
                    pass
                valid.append(url)
                with open("output/NitroCodes.txt", "w") as file:
                    file.write(url)
            elif response.status_code == 429:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mRate limited, please wait {response.json()['retry_after']} s")
                time.sleep(int(response.json()['retry_after']))
            else:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mINVALID NITRO {url}")
                invalid += 1
        except Exception as e:
            print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mError : {url} {e}")
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Daddy quickyboi")
    print(f"""\n
     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m Results:
           \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m Valid: {len(valid)}
           \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m Invalid: {invalid}
           \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m Valid Codes: {', '.join(valid )}""")
    input(f"""\n     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0m Press ENTER to exit""")
    main()

main()
