import time
import re
from colorama import Style
from src.scripts import tools as tool


text_color = "white"

def getTextColor():
    return text_color

def setTextColor(color):
    global text_color
    text_color = color


# ---------------------------------------------------------------------------- #
#                               Fonctions locales                              #
# ---------------------------------------------------------------------------- #


def _typing_effect(string, timeout=0.05, multiplier=1.0, color='white'):
    """ 
    [Fonction outil]
    Effet de typing.
    Prend en parametre :
    - le texte
    - le temps entre chaque lettre
    - le multiplieur de temps
    """
    
    textColor = tool.getColor(color)
    if textColor:
        print(textColor, end="", flush=True)
    else:
        return False
    
    print(tool.getColor(color), end="", flush=True)
    for i in string:
        print(i, end="", flush=True)
        time.sleep(timeout * float(multiplier))
    print(Style.RESET_ALL, end="", flush=True)


def _getWordTag(string):
    """
    [Fonction outil]
    Permet d'obtenir le contenu dans les balises et entre les balises.
    """
    patternBetween2Tags = r'<(\d+)>(.*?)<\/\1>'
    matchBetween2Tags = re.findall(patternBetween2Tags, string)
    
    default_tag_value = '1'

    if matchBetween2Tags:
        return matchBetween2Tags[0]
    else:
        return (default_tag_value, string)

def _removeRepetitiveWords(string):
    """
    [Fonction outil]
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


def writeTextWithTypingEffect(text="", color='white', timeout=0.05):
    """
    [Fonction outil]
    Créé un effet de machine à écrire avec un temps entre chaque lettre
    Cette fonction prend en compte les balises pour accélerer le texte  : '<1> text </1>'
    Cette fonction permet d'écrire en couleur
    """
    words = _removeRepetitiveWords(text)
    for word in words:
        working = _typing_effect(string=_getWordTag(word)[1] + " ", timeout=timeout, multiplier=_getWordTag(word)[0], color=color)
        if working == False:
            break
        
def writeTextWithoutTypingEffect(text="", color='white'):
    print(tool.getColor(color), text, flush=True)
    print(Style.RESET_ALL, flush=False)
        
        
def normalize(string):
    """
    [Fonction outil]
    Retire les balises tout en conservant le texte qu'elles englobent.
    """
    while re.search(r'<\d+>.*?<\/\d+>', string):
        tag, content = _getWordTag(string)
        string = string.replace(f'<{tag}>{content}</{tag}>', content)

    return string

def writeEndGame():
    text = "\n\nVous avez terminé notre jeu ! \nMerci d'avoir joué !\nN'hésitez pas à rejouer car il y a plusieurs façon de terminer le jeu...\n\n"
    writeTextWithTypingEffect(text, "green", 0.05)
    input()