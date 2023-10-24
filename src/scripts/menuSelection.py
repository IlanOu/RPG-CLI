from src.scripts import printText as textWriter
from src.scripts import tools as tool
import json
import keyboard
import random
import time

# id qui sera renvoyer par le script
selectedId = 0

# do not remenber to convert str into json 
###### y = json.dumps(x) ##### cf: end of this file
def choiceSelectionWithArrow( textHistoire ,jsonArrayChoice):
    
    data = json.loads(jsonArrayChoice)
    # print(data)

    indexSelection = 0
    selectedId = None

    # draw text with typing effect and without effect
    _drawText(data, indexSelection, 1)
    _drawText(data, indexSelection, 0 , textHistoire, ">")


    # affichage en boucle
    while selectedId == None:
        
        # draw text w/out typing effect and clear console
        # _drawText(data, indexSelection, 0 , textHistoire)
        
        # test input keyboard
        while True:
            if keyboard.is_pressed("up arrow"):
                if indexSelection > 0:
                    indexSelection -= 1
                    _drawText(data, indexSelection, 0 , textHistoire, ">")

                break
            elif keyboard.is_pressed("down arrow"):
                if indexSelection < (len(data) - 1):
                    indexSelection += 1
                    _drawText(data, indexSelection, 0 , textHistoire, ">")

                break
            elif keyboard.is_pressed("enter"):
                selectedId = data[indexSelection]["redirection_id"]
                # _drawText(data, indexSelection, 0 , textHistoire)

                break
    return selectedId

# arrayOfProposition = text of element String[] , indexSelection = arrow position int, istypingEffect, textHistoire = prevoius history
def _drawText(arrayOfProposition, indexSelection, isTypingEffect = 1, textHistoire = "", preTextOfCurrentSelection = ""):
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
                textWriter.writeTextWithTypingEffect(preText + element["text"] + "\n")
            else:
                print(preText + element["text"] + "\n")

        currentIndex += 1


def choiceSelectionWithDice( textHistoire , jsonArrayChoice, nbFaceDice):

    # check and tranform the number of face 
    nbFaceDice = int(nbFaceDice)
    
    # load json file
    data = json.loads(jsonArrayChoice)

    # draw text with typing effect
    _drawText(data, 0, 1)
    _drawText(data, 0, 0 , textHistoire, "")

    # selection a number
    randomNumber = random.randrange(0, nbFaceDice, 1)

    # indication for player
    # input(textWriter.writeTextWithTypingEffect("appuyer sur entrer pour lancé le super dé de la mort qui tue"))
    input(textWriter.writeTextWithTypingEffect("lancer !"))

    # effect of rotative dice
    nbCurrentRound = 0
    nbRound = 0
    number = [0,1,2,3,4,5,6,7,8,9]
    while nbCurrentRound <= nbRound :

        # draw text 
        # _drawText(data, 0, 0 , textHistoire)
        tool.clearConsole()
        # time.sleep(0.2)
        print(number[random.randrange(0, (len(number) - 1), 1)])
        print("")

        nbCurrentRound += 1

    tool.clearConsole()
    return randomNumber

    


