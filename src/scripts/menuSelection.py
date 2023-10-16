import test_typing as textWriter
import cleanerConsole as consoleClean
import json 
import keyboard

# id qui sera renvoyer par le script
selectedId = 0

# do not remenber to convert str into json 
###### y = json.dumps(x) ##### cf: end of this file
def choiceSelectionWithArrow( textHistoire ,jsonArrayChoice):
    
    data = json.loads(jsonArrayChoice)
    print(data)

    indexSelection = 0
    selectedId = None

    # draw text with typing effect
    _drawText(data, indexSelection, 1)
    _drawText(data, indexSelection, 0 , textHistoire)


    # affichage en boucle
    while selectedId == None:
        
        # draw text w/out typing effect and clear console
        # _drawText(data, indexSelection, 0 , textHistoire)
        
        # test input keyboard
        while True:
            if keyboard.is_pressed("up arrow"):
                if indexSelection > 0:
                    indexSelection -= 1
                    _drawText(data, indexSelection, 0 , textHistoire)

                break
            elif keyboard.is_pressed("down arrow"):
                if indexSelection < (len(data) - 1):
                    indexSelection += 1
                    _drawText(data, indexSelection, 0 , textHistoire)

                break
            elif keyboard.is_pressed("enter"):
                selectedId = data[indexSelection]["redirection_id"]
                # _drawText(data, indexSelection, 0 , textHistoire)

                break
    return selectedId


def _drawText(data, indexSelection, isTypingEffect = 1, textHistoire = "aaaa"):
    # draw all text element
    currentIndex = 0

    # for effect of smooth choice clean console and re print the history
    if not isTypingEffect:
        consoleClean.clean()
        print(textHistoire)


    for element in data:

        # draw indication selection
        if currentIndex == indexSelection:
            preText = ">"
        else:
            preText = ""

            
        # verification : is the json is correct to use it
        if element["text"]:

            # if not typing effect is for selection
            if isTypingEffect:
                textWriter.typing_effect(preText + element["text"] + "\n")
            else:
                print(preText + element["text"] + "\n")

        currentIndex += 1


x = [
            {
                "text": "Yes",
                "redirection_id": "qdfdqgf"
            },
            {
                "text": "No",
                "redirection_id": "egegerS"
            }
        ]
e = choiceSelectionWithArrow("aaa", json.dumps(x) )

print(e)