from src.scripts import printText
import json
from src.scripts import tools as tool
from src.scripts import menuSelection

"""
Les fonctions qui commencent par _ sont des fonctions 
qui ne serviront que dans ce module pour ce module.
"""

jsonPath = ''


def getPage(question_id):
    
    #? Gestion d'erreur
    if jsonPath == '':
        tool.logError('jsonPath is not set !')
        return
    
    
    file = open(jsonPath)
    data = json.load(file)
    # with open(jsonPath, 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    
    question_id = str(question_id)
    
    for id in data:
        if id == question_id:
            content = data[id]
            return content
    
    
    file.close()
    
    #? Gestion d'erreur
    tool.logError(f'Id not found : {str(question_id)}')
    return


def setPath(path):
    global jsonPath
    jsonPath = path


def writeQuestion(question, color="white", timeout=0.05):
    printText.writeTextWithTypingEffect(text=question, color=color, timeout=timeout)
    print()

def writeChoices(typeChoice, choices , question):
    if typeChoice == "arrow":
        return menuSelection.choiceSelectionWithArrow( question , json.dumps(choices))
    elif typeChoice == "dice":
        return menuSelection.choiceSelectionWithDice( question , json.dumps(choices))
    else:
        tool.logError("error while write choice in page manager")