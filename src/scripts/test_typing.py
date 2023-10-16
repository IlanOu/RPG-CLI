import time
import re
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from src.scripts import log

colorama_init()

def _getColor(colorName):
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
    else:
        #? Gestion d'erreur
        log.error("Unknown color : " + colorName)
        return None

def _typing_effect(string, timeout=0.05, multiplier=1.0, color="white"):
    """ 
    Effet de typing.
    Prend en parametre :
    - le texte
    - le temps entre chaque lettre
    - le multiplieur de temps
    """
    
    textColor = _getColor(color)
    if textColor:
        print(textColor, end="", flush=True)
    else:
        return False
    
    for i in string:
        print(_getColor(color) + i, end="", flush=True)
        time.sleep(timeout * float(multiplier))
    print(Style.RESET_ALL, end="", flush=True)


def _getWordTag(string):
    """
    Permet d'obtenir le contenu dans les balises et entre les balises.
    """
    patternBetween2Tags = r'<(\d+)>(.*?)<\/\1>'
    matchBetween2Tags = re.findall(patternBetween2Tags, string)
    
    default_tag_value = '1'

    if matchBetween2Tags:
        return matchBetween2Tags[0]
    else:
        return (default_tag_value, string)

def _normalizeSentence(string):
    """
    Permet de normaliser la liste de mots en retirant 
    les doublons dans la liste de mots
    """
    resultat = re.split(r'(\s*(<\d+>.*?</\d+>)\s*)', string)

    resultat = [item for item in resultat if item.strip() != '']
    result_list = [resultat[0]]
    for i in range(1, len(resultat)):
        if resultat[i].strip() != resultat[i - 1].strip():
            result_list.append(resultat[i])
    
    return result_list



# ---------------------------------------------------------------------------- #
#                Fonctions utilisables en dehors de ce module                  #
# ---------------------------------------------------------------------------- #


def writeText(text="", color="white", timeout=0.05):
    words = _normalizeSentence(text)
    for word in words:
        working = _typing_effect(string=_getWordTag(word)[1] + " ", timeout=timeout, multiplier=_getWordTag(word)[0], color=color)
        if working == False:
            break
