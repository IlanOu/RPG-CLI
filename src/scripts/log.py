from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def error(message):
    print(f'{Fore.LIGHTRED_EX}\n❌ | {message}{Style.RESET_ALL}')

def warning(message):
    print(f'{Fore.YELLOW}\n⚠️  | {message}{Style.RESET_ALL}')

def valid(message):
    print(f'{Fore.GREEN}\n✅ | {message}{Style.RESET_ALL}')