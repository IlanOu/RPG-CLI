from src.scripts import printText as textWriter
from src.scripts import tools as tool
import json
import keyboard
import random
import time

# Id qui sera renvoyé par le script
selectedId = 0



# ---------------------------------------------------------------------------- #
#                               Fonctions locales                              #
# ---------------------------------------------------------------------------- #


"""
Permet d'écrire le texte de la page en typing effect ou non
"""
def _drawText(arrayOfProposition, indexSelection, isTypingEffect=1, textHistoire="", preTextOfCurrentSelection="", timeout=0.05):
    # draw all text element
    currentIndex = 0

    # for effect of smooth choice clean console and re print the history
    if not isTypingEffect:
        tool.clearConsole()
        print(textHistoire)


    for element in arrayOfProposition:

        # draw indication selection
        if currentIndex == indexSelection:
            preText = preTextOfCurrentSelection
        else:
            preText = ""

            
        # verification : is the json is correct to use it
        if element["text"]:

            # if not typing effect is for selection
            if isTypingEffect:
                textWriter.writeTextWithTypingEffect(text=preText + element["text"] + "\n", timeout=timeout)
            else:
                print(preText + element["text"] + "\n")

        currentIndex += 1





# ---------------------------------------------------------------------------- #
#                   Fonctions utilisables en dehors du script                  #
# ---------------------------------------------------------------------------- #




# Remember to convert str into json 
###### y = json.dumps(x) ##### cf: end of this file
def choiceSelectionWithArrow(textHistoire , jsonArrayChoice, timeout=0.05):
    
    pointerCharacter = "▶ "

    data = json.loads(jsonArrayChoice)
    
    textWriter.writeTextWithoutTypingEffect(data, "yellow")
    
    indexSelection = 0
    selectedId = None

    
    # draw text with typing effect and without effect
    _drawText(data, indexSelection, 1, "", pointerCharacter, timeout)
    _drawText(data, indexSelection, 0 , textHistoire, pointerCharacter)


    # affichage en boucle
    while selectedId == None:
        
        # Input keyboard
        while True:
            if keyboard.is_pressed("up arrow"):
                if indexSelection > 0:
                    indexSelection -= 1
                    _drawText(data, indexSelection, 0 , textHistoire, pointerCharacter)

                    time.sleep(0.2)
                break
            elif keyboard.is_pressed("down arrow"):
                if indexSelection < (len(data) - 1):
                    indexSelection += 1
                    _drawText(data, indexSelection, 0 , textHistoire, pointerCharacter)

                    time.sleep(0.2)
                break
            elif keyboard.is_pressed("enter"):
                selectedId = data[indexSelection]["redirection_id"]
                break
    return selectedId




def choiceSelectionWithDice( textHistoire , jsonArrayChoice, timeout=0.05):
    
    # load json file
    data = json.loads(jsonArrayChoice)

    # check and tranform the number of face 
    nbFaceDice = int(len(data) - 1)

    # draw text with typing effect
    _drawText(data, 0, 1, timeout=timeout)
    _drawText(data, 0, 0 , textHistoire, "")

    # selection a number
    randomNumber = random.randrange(0, nbFaceDice, 1)

    # indication for player
    textWriter.writeTextWithTypingEffect("Lancer le dé !")
    keyboard.wait("enter")
    # effect of rotative dice
    nbCurrentRound = 0
    nbRound = -1
    
    number = []
    pages = []
    
    for i in range(len(data)):
        item = data[i]
        number.append(i)
        pages.append(item["redirection_id"])
    
    while nbCurrentRound <= nbRound :

        # draw text 
        # _drawText(data, 0, 0 , textHistoire)
        tool.clearConsole()
        # time.sleep(0.2)
        print(number[random.randrange(0, (len(number) - 1), 1)])
        print("")

        nbCurrentRound += 1

    print("le numero est : ")
    print(randomNumber)
    print("appuyer sur entrer pour continuer")
    keyboard.wait("enter")
    tool.clearConsole()
    return pages[randomNumber]







