from src.scripts import pageManager as pageManager
from src.scripts import menuSelection
from src.scripts import printText
import json
from src.scripts import tools as tool

def start():
    test = printText.normalize("Votre <3>téléphone</3> dernier cri fait étalage <1>de</1> ses talents en affichant fièrement l'heure : 5h00, précision ultime au rendez-vous !")
    print(test)
    return
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
        # input("end")
    else :
        # lancer le générique de fin
        pass

if __name__ == '__main__':
    start()
