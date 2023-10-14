from src.scripts import writeQuestions

def start():
    writeQuestions.setPath("./src/assets/structure.json")
    question = writeQuestions.writeQuestion("0", color="red", timeout=0.01)

if __name__ == '__main__':
    start()