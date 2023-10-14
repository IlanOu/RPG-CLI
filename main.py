from src.scripts import writeQuestions

def start():
    writeQuestions.setPath("./src/assets/structure.json")
    question = writeQuestions.writeQuestion("0")

if __name__ == '__main__':
    start()