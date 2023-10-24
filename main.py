from src.scripts import writeQuestions
from src.scripts import menuSelection
import json

def start():
    writeQuestions.setPath("./src/assets/structure.json")
    # question = writeQuestions.writeQuestion(id="0", color="white", timeout=0.01)
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
    e = menuSelection.choiceSelectionWithDice("blablabla", json.dumps(x), 6 )
    # print(e)
    input("end")

if __name__ == '__main__':
    start()