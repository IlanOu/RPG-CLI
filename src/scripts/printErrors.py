from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def errorMessage(message):
    print(f'{Fore.LIGHTRED_EX}====================')
    print(f'Error :\n-> {message}')
    print(f'===================={Style.RESET_ALL}')