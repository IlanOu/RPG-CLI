# ---------------------------------------------------------------------------- #
#                                     Logs                                     #
# ---------------------------------------------------------------------------- #

from colorama import init as colorama_init
from colorama import Fore, Back
from colorama import Style

from src.scripts import pageManager
from src.scripts import printText

colorama_init()

def logError(message):
    print(f'{Fore.LIGHTRED_EX}\n❌ | {message}{Style.RESET_ALL}')

def logWarning(message):
    print(f'{Fore.YELLOW}\n⚠️  | {message}{Style.RESET_ALL}')

def logValid(message):
    print(f'{Fore.GREEN}\n✅ | {message}{Style.RESET_ALL}')


# ---------------------------------------------------------------------------- #
#                                Cleaner Console                               #
# ---------------------------------------------------------------------------- #

import os

'''We define our own clean function to clear the screen'''
def clearConsole():
    
    # For macOS and Linux
    if os.name == 'posix':
        os.system('clear')

    # Windows
    elif os.name == 'nt':
        os.system('cls')

# ---------------------------------------------------------------------------- #
#                                  Get Colors                                  #
# ---------------------------------------------------------------------------- #

colorama_init()

def getColor(colorName):
    if colorName == "white":
        return Fore.WHITE
    elif colorName == "red":
        return Fore.LIGHTRED_EX
    elif colorName == "blue":
        return Fore.LIGHTBLUE_EX
    elif colorName == "cyan":
        return Fore.CYAN
    elif colorName == "yellow":
        return Fore.YELLOW
    elif colorName == "magenta":
        return Fore.MAGENTA
    elif colorName == "green":
        return Fore.LIGHTGREEN_EX
    elif colorName == "black":
        return Fore.BLACK
    elif colorName == "gray":
        return Back.WHITE
    else:
        #? Gestion d'erreur
        logError("Unknown color : " + colorName)
        return None


def getLevel():
    clearConsole()

    levelChoices = [
            {
                "text": "Easy",
                "redirection_id": "0"
            },
            {
                "text": "Normal",
                "redirection_id": "1"
            },
            {
                "text": "Hard",
                "redirection_id": "2"
            }
        ]

    pageManager.writeQuestion(question="Choisis ton niveau de difficulté ", timeout=0.01, color=printText.getTextColor())
    return pageManager.writeChoices(typeChoice="arrow", choices=levelChoices, question="Choisis ton niveau de difficulté ")

def getName():
    clearConsole()

    pageManager.writeQuestion(question="C'est quoi ton joli ptit nom ?", timeout=0.01, color=printText.getTextColor())
    input('')
    name = input(">")
    return name
