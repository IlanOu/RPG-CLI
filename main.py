from src.scripts import pageManager as pageManager
from src.scripts import menuSelection
import json
from src.scripts import tools as tool
import time


idPageSave = 0
pseudo = ""
level = 0 # 0 : easy | 1 : medium | 2 : hard

def start():
    global pseudo, level

    # get the current id of page in function of save
    idPageSave = savePage()

    pseudo = getName()

    level = getLevel()

    readPage(idPageSave)

def getLevel():
    tool.clearConsole()

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

    pageManager.writeQuestion(question="Choisis ton niveau de difficulté ", color="white", timeout=0.01)
    return pageManager.writeChoices(typeChoice="arrow", choices=levelChoices, question="Choisis ton niveau de difficulté ")

def getName():
    tool.clearConsole()

    pageManager.writeQuestion(question="C'est quoi ton joli ptit nom ?", color="white", timeout=0.01)
    return input(">")   

def savePage():

    # TODO get save existing
    nbSave = []

    if len(nbSave) > 0:
        # TODO choice between empty slot or used slot
        print("choisis ta souvegarde ;)")
        return "l'id qui a ete choisis"
    else:
        pageManager.writeQuestion(question="creation d'une nouvelle sauvegarde ...", color="white", timeout=0.05)
        return 0

def readPage(idPage):
    tool.clearConsole()

    pageManager.setPath("./src/assets/structure.json")
    page = pageManager.getPage(idPage)
    question = page["question"]
    choices = page["choices"]
    typeChoice = page["type"]

    pageManager.writeQuestion(question=question, color="white", timeout=0.01)
    nextId = pageManager.writeChoices(typeChoice=typeChoice, choices=choices, question=question)

    readPage(nextId)
    input("end")

if __name__ == '__main__':
    start()
