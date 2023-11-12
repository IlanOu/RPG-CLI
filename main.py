from src.scripts import pageManager as pageManager
from src.scripts import printText
from src.scripts import tools as tool
from src.scripts import save
import time
import keyboard
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

    save.clearXML(GAME_XML)
    pageManager.setPath(STRUCTURE_JSON)
    # get the current id of page in function of save
    idPageSave = savePage()

    if idPageSave == 0:
        pseudo = getName()
        level = getLevel()

    save.saveToXML(GAME_XML, pseudo, "Player_name")
    save.saveToXML(GAME_XML, level, "Level")
    readPage(idPageSave)
    
    
    pagesSaved = save.readFromJSON(PROGRESS_JSON)["idPages"]
    
    content = []
    for pageID in pagesSaved:
        content.append({"page": pageManager.getPage(pageID), "id": pageID})

    MDcontent = save.constructMarkdownFile(content)
    save.saveInMarkdown(END_MD, MDcontent)
    save.clearJSON(PROGRESS_JSON)
    


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
    input('')
    name = input(">")
    return name

def savePage():
    savesFile = []
    indexSaves = 0
    
    ##### enumerate all saves #####
    rootdir = 'src/assets/saves/'
    for file in os.listdir(rootdir):
        fileName = os.path.join(rootdir, file)
        # print(fileName)
        # ! limit to 1 savesFile for not multiple progress json => but it's can be a feature
        if file != ".gitkeep" and len(savesFile) < 1:
            savesFile.append({
                "text": file,
                "redirection_id": indexSaves
            })
            indexSaves += 1
            
        # if os.path.isdir(d):
    ##### append empty game for create a new one ##### ( -1 ) to redirect to the last index of array
    savesFile.append({
                "text": "New Game",
                "redirection_id": -1
            })
    
    # select Saves
    idSaveSelected = selectSaves(savesFile)
    return idSaveSelected

# select Saves
def selectSaves(savesFile):
    
    # already have a save
    if len(savesFile) > 0:
        ##### get selection #####
        question_choice_save = "Choisis ta sauvegarde ;)"
        pageManager.writeQuestion(question=question_choice_save, color="white", timeout=0.05)
        idSave = pageManager.writeChoices(typeChoice="arrow", choices=savesFile, question=question_choice_save, timeout=0.001)

        ##### Detect if Save is not finish if the selection is not new save #####
        if(idSave != -1):
            
            # get the type of last page id
            idLastPage = save.readFromJSON(PROGRESS_JSON)["idPages"][-1]
            typeOfPage = save.readFromJSON(STRUCTURE_JSON)[idLastPage]["type"]
            # if end page create new save
            # TODO @IlanOu choose effect of end page => overwrite latest save or write new file ( /!\ cannot be display )
            if typeOfPage != 'end':
                time.sleep(1)
                return idLastPage
            else:
                pageManager.writeQuestion(question="Oh oh... :/ Votre ancienne partie est déjà fini on dirait ...", color="white", timeout=0.05)
                time.sleep(1)
                pageManager.writeQuestion(question="Selectionnez un autre choix ^^", color="red", timeout=0.05)
                time.sleep(1)
                # selectSaves(savesFile) #empty for go to the first page when there is already a save
                exit()
        else:
            # new page
            return 0
    else:
        pageManager.writeQuestion(question="Creation d'une nouvelle sauvegarde ...", color="white", timeout=0.05)
        time.sleep(1)
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
