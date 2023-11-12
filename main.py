from src.scripts import pageManager as pageManager
from src.scripts import printText
from src.scripts import tools as tool
from src.scripts import save
import time
import os


idPageSave = 0
pseudo = ""
level = 0 # 0 : easy | 1 : medium | 2 : hard


PROGRESS_JSON = "./src/assets/progress.json"
STRUCTURE_JSON = "./src/assets/structure.json"
GAME_XML = "./src/assets/game.xml"
END_MD = "./adventure.md"


def start():
    global pseudo, level

    pageManager.setPath(STRUCTURE_JSON)
    # get the current id of page in function of save
    idPageSave = savePage()

    pseudo = getName()

    level = getLevel()


    readPage(idPageSave)
    
    
    # pagesSaved = save.readFromJSON(PROGRESS_JSON)["idPages"]
    
    # content = []
    # for pageID in pagesSaved:
    #     content.append(pageManager.getPage(pageID))

    # MDcontent = save.constructMarkdownFile(content)
    # save.saveInMarkdown(END_MD, MDcontent)
        
    # save.clearJSON(PROGRESS_JSON)
    return
    save.saveToXML(GAME_XML, "Jean Claude", "Player_name")

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
    nbSave = []
    
    rootdir = 'src/assets/saves/'
    for file in os.listdir(rootdir):
        fileName = os.path.join(rootdir, file)
        # print(fileName)
        if file != ".gitkeep":
            nbSave.append(fileName)
            
        # if os.path.isdir(d):

    
    time.sleep(5)
    if len(nbSave) > 0:
        # TODO choice between empty slot or used slot
        print("choisis ta souvegarde ;)")
        return "l'id qui a ete choisis"
    else:
        pageManager.writeQuestion(question="creation d'une nouvelle sauvegarde ...", color="white", timeout=0.05)
        return 0

def readPage(idPage):
    tool.clearConsole()

    page = pageManager.getPage(idPage)
    # print(page)
    question = page["question"]
    choices = page["choices"]
    typeChoice = page["type"]
    winPage = page["win"]

    
    if typeChoice != "end":
        pageManager.writeQuestion(question=question, color="white", timeout=0.01)
        nextId = pageManager.writeChoices(typeChoice=typeChoice, choices=choices, question=question, timeout=0.01)
        
        
        #& ---------- JSON Save ----------
        save.saveToJSON(PROGRESS_JSON, nextId)
        readPage(nextId)
    else :
        if winPage == True:
            pageManager.writeQuestion(question=question, color="green", timeout=0.01)
        elif winPage == False:
            pageManager.writeQuestion(question=question, color="red", timeout=0.01)
        time.sleep(3)
        printText.writeEndGame()
        pass

if __name__ == '__main__':
    start()
