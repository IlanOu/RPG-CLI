import time
import re

def _typing_effect(string, timeout=0.05, multiplier=1.0):
    """ 
    Effet de typing.
    Prend en parametre :
    - le texte
    - le temps entre chaque lettre
    - le multiplieur de temps
    """
    
    for i in string:
        print(i, end="", flush=True)
        time.sleep(timeout * float(multiplier))

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




def writeText(text, timeout=0.05):
    words = _normalizeSentence(text)
    for word in words:
        _typing_effect(string=_getWordTag(word)[1] + " ", timeout=timeout, multiplier=_getWordTag(word)[0])