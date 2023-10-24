from src.scripts import printText
import json
from src.scripts import tools as tool

"""
Les fonctions qui commencent par _ sont des fonctions 
qui ne serviront que dans ce module pour ce module.
"""

jsonPath = ''


def _getQuestion(question_id):
    
    #? Gestion d'erreur
    if jsonPath == '':
        tool.logError('jsonPath is not set !')
        return
    
    
    file = open(jsonPath)
    data = json.load(file)
    
    question_id = str(question_id)
    
    for id in data:
        if id == question_id:
            content = data[id]
            question = content['question']
            return question
    
    
    file.close()
    
    #? Gestion d'erreur
    tool.logError(f'Id not found : {str(question_id)}')
    return


def setPath(path):
    global jsonPath
    jsonPath = path


def writeQuestion(id, color="white", timeout=0.05):
    question = _getQuestion(id)
    printText.writeTextWithTypingEffect(text=question, color=color, timeout=timeout)
    print()
    return question