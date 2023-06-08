import requests
import time
from colorama import Fore, Style

# Rengarenk bir şekilde yazdırma
print(Fore.RED + Style.BRIGHT + '''

''' + Fore.GREEN + Style.BRIGHT + ''' ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▄▄▄▄   ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄   ▄▀▀▄ █ 
''' + Fore.YELLOW + Style.BRIGHT + '''█  █   ▄▀ █      █ █ █   ▐ █    █  ▐ █ █    ▌ █  █   ▄▀ ▐  ▄▀   ▐ █ █    ▌ █  █ ▄▀ 
''' + Fore.BLUE + Style.BRIGHT + '''▐  █▄▄▄█  █      █    ▀▄   ▐   █     ▐ █      ▐  █▄▄▄█    █▄▄▄▄▄  ▐ █      ▐  █▀▄  
''' + Fore.MAGENTA + Style.BRIGHT + '''   █   █  ▀▄    ▄▀ ▀▄   █     █        █         █   █    █    ▌    █        █   █ 
''' + Fore.CYAN + Style.BRIGHT + '''  ▄▀  ▄▀    ▀▀▀▀    █▀▀▀    ▄▀        ▄▀▄▄▄▄▀   ▄▀  ▄▀   ▄▀▄▄▄▄    ▄▀▄▄▄▄▀ ▄▀   █  
''' + Fore.WHITE + Style.BRIGHT + ''' █   █              ▐      █         █     ▐   █   █     █    ▐   █     ▐  █    ▐  
''' + Fore.RED + Style.BRIGHT + ''' ▐   ▐                     ▐         ▐         ▐   ▐     ▐        ▐        ▐       



                                                                                                 
                                                        LAHANACİ HOST KONTROL >
                                                        DDOS İÇİN HOST KONTROLU YAPAR >

''' + Style.RESET_ALL)


print(Style.RESET_ALL)


url = input("Kontrol etmek istediğiniz web sitesi URL'sini girin: ")
print()
print()

while True:
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("\033[92mSite çalışıyor!")
        else:
            print("\033[92msite çalışıyor")

    except requests.exceptions.RequestException:
        print("\033[91mSite çalışmıyor!")

    print("\033[0m") 
    print("\n") 

    time.sleep(1)
