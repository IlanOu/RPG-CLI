from src.scripts import pageManager as pageManager
from src.scripts import menuSelection
import json
from src.scripts import tools as tool

def start():
    readPage(0)

def readPage(idPage):

    tool.clearConsole()

    pageManager.setPath("./src/assets/structure.json")
    page = pageManager.getPage(idPage)
    question = page["question"]
    choices = page["choices"]
    typeChoice = page["type"]

    pageManager.writeQuestion(question=question, color="white", timeout=0.01)
    if typeChoice != "end":
        nextId = pageManager.writeChoices(typeChoice=typeChoice, choices=choices, question=question)

        readPage(nextId)
        input("end")
    else :
        # lancer le générique de fin
        pass

if __name__ == '__main__':
    start()
