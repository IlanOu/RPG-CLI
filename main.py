from src.scripts import pageManager as pageManager
from src.scripts import printText
from src.scripts import tools as tool
from src.scripts import save
import time

idPageSave = 0
fileSave = ""
pseudo = ""
level = 0 # 0 : easy | 1 : medium | 2 : hard


PROGRESS_JSON = "./src/assets/progress.json"
STRUCTURE_JSON = "./src/assets/structure.json"
GAME_XML = "./src/assets/game.xml"
END_MD = "./adventure.md"
SAVES_FOLDER = "./src/assets/saves/"


def start():
    global pseudo, level
    
    save.clearJSON(PROGRESS_JSON)
    save.clearXML(GAME_XML)
    pageManager.setPath(STRUCTURE_JSON)
    # get the current id of page in function of save
    idPageSave = save.loadOrNewGame(savesFolder=SAVES_FOLDER, progressJson=PROGRESS_JSON, structureJson=STRUCTURE_JSON)

    if idPageSave == 0:
        pseudo = tool.getName()
        level = tool.getLevel()

        if int(level) == 1:
            printText.setTextColor("gray")
        elif int(level) == 2:
            printText.setTextColor("black")
        else:
            printText.setTextColor("white")


    # ===x=== Save into the XML ===x===
    save.saveToXML(GAME_XML, pseudo, "Player_name")
    save.saveToXML(GAME_XML, level, "Level")
    
    # ===x=== Launch the game ===x===
    page = readPage(idPageSave)
    if page:
        save.savePage(fileSave, savesFolder=SAVES_FOLDER, progressJson=PROGRESS_JSON)
    
    # ===x=== Save into the JSON / MD ===x===
    pagesSaved = save.readFromJSON(PROGRESS_JSON)["idPages"]
    
    content = []
    for pageID in pagesSaved:
        content.append({"page": pageManager.getPage(pageID), "id": pageID})

    MDcontent = save.constructMarkdownFile(content)
    save.saveInMarkdown(END_MD, MDcontent)
    save.clearJSON(PROGRESS_JSON)



def readPage(idPage):
    tool.clearConsole()
    if idPage == -1:
        printText.writeTextWithoutTypingEffect("Vous avez déjà terminé cette partie ! Vous pouvez rejouer ou voir le résumé de la partie dans le fichier 'adventure.md'")
        return False
    
    page = pageManager.getPage(idPage)
    
    question = page["question"]
    choices = page["choices"]
    typeChoice = page["type"]
    winPage = page["win"]

    if typeChoice != "end":
        playerName = save.getFromXML(GAME_XML, "Player_name")
    
        if playerName == "" or playerName == None:
            playerName = "Banane Anonyme"
    
        if "{{player}}" in question:
            question = question.replace("{{player}}",playerName)
            
        pageManager.writeQuestion(question=question, timeout=0.01, color=printText.getTextColor())
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
    return True

if __name__ == '__main__':
    start()
