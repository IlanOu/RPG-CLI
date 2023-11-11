from src.scripts import pageManager as pageManager
from src.scripts import printText
from src.scripts import tools as tool
from src.scripts import save


PROGRESS_JSON = "./src/assets/progress.json"
STRUCTURE_JSON = "./src/assets/structure.json"
GAME_XML = "./src/assets/game.xml"
END_MD = "./adventure.md"


def start():
    pageManager.setPath(STRUCTURE_JSON)
    
    
    pagesSaved = save.readFromJSON(PROGRESS_JSON)["idPages"]
    
    content = []
    for pageID in pagesSaved:
        content.append(pageManager.getPage(pageID))

    MDcontent = save.constructMarkdownFile(content)
    save.saveInMarkdown(END_MD, MDcontent)
        
    # save.clearJSON(PROGRESS_JSON)
    return
    save.saveToXML(GAME_XML, "Jean Claude", "Player_name")
    readPage(0)

def readPage(idPage):

    tool.clearConsole()

    page = pageManager.getPage(idPage)
    question = page["question"]
    choices = page["choices"]
    typeChoice = page["type"]

    pageManager.writeQuestion(question=question, color="white", timeout=0.001)
    
    if typeChoice != "end":
        nextId = pageManager.writeChoices(typeChoice=typeChoice, choices=choices, question=question, timeout=0.001)
        
        
        #& ---------- JSON Save ----------
        save.saveToJSON(PROGRESS_JSON, nextId)
        readPage(nextId)
    else :
        printText.writeEndGame()
        pass

if __name__ == '__main__':
    start()
