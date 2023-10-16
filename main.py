from src.scripts import writeQuestions
from src.scripts import log

def start():
    writeQuestions.setPath("./src/assets/structure.json")
    question = writeQuestions.writeQuestion(id="0", color="white", timeout=0.01)

if __name__ == '__main__':
    start()