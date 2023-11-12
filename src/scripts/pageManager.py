from src.scripts import printText
import json
from src.scripts import tools as tool
from src.scripts import menuSelection



jsonPath = ''



def setPath(path):
    """
    Met à jour le json path
    """
    
    global jsonPath
    jsonPath = path



def getPage(question_id):
    """
    Permet d'obtenir une page par son ID
    """
    
    #? Gestion d'erreur
    if jsonPath == '':
        tool.logError('jsonPath is not set !')
        return
    
    
    with open(jsonPath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    question_id = str(question_id)
    
    for id in data:
        if id == question_id:
            content = data[id]
            return content
    
    
    file.close()
    
    #? Gestion d'erreur
    tool.logError(f'Id not found : {str(question_id)}')
    return



def writeQuestion(question, color="white", timeout=0.05):
    """
    Permet d'écrire uniquement la question
    """
    
    printText.writeTextWithTypingEffect(text=question, color=color, timeout=timeout)
    print()
    print("============================================================")



def writeChoices(typeChoice, choices , question, timeout=0.05):
    """
    Permet d'écrire uniquement les choix
    """
    if typeChoice == "arrow":
        return menuSelection.choiceSelectionWithArrow( question , json.dumps(choices), timeout)
    elif typeChoice == "dice":
        return menuSelection.choiceSelectionWithDice( question , json.dumps(choices), timeout)
    else:
        tool.logError("error while write choice in page manager")