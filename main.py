from src.scripts import writeQuestions
from src.scripts import log
from src.scripts import menuSelection
import json

def start():
    writeQuestions.setPath("./src/assets/structure.json")
    question = writeQuestions.writeQuestion(id="0", color="white", timeout=0.01)
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
    e = menuSelection.choiceSelectionWithArrow("aaa", json.dumps(x) )
    print(e)

if __name__ == '__main__':
    start()