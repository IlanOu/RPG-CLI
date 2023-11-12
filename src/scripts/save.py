import xml.etree.ElementTree as ET
import os
import json
from src.scripts import tools as tool
from src.scripts import menuSelection
from src.scripts import save


def clearXML(filename):
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        # Charger le fichier XML existant
        tree = ET.parse(filename)
        root = tree.getroot()
        children = list(root)
        for item in children:
            root.remove(item)
        tree.write(filename)


def saveToXML(filename, text, row):
    
    # Vérifier si le fichier XML existe et n'est pas vide
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        # Charger le fichier XML existant
        tree = ET.parse(filename)
        root = tree.getroot()
        # children = list(root)
        # for item in children:
        #     root.remove(item)
    else:
        # Le fichier n'existe pas ou est vide, créer un nouvel élément racine
        root = ET.Element("racine")
        tree = ET.ElementTree(root)

    # Créer un nouvel élément avec le texte fourni
    nouvelle_ligne = ET.SubElement(root, row)
    nouvelle_ligne.text = text
    # Enregistrer dans le fichier XML
    tree.write(filename)


def getFromXML(xml_file_path, element_name):
    try:
        # Parsez le fichier XML
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Recherchez l'élément spécifié dans le XML
        element = root.find(element_name)

        # Si l'élément est trouvé, renvoyez son texte, sinon renvoyez None
        if element is not None:
            return element.text
        else:
            print(f"L'élément '{element_name}' n'a pas été trouvé dans le fichier XML.")
            return None

    except ET.ParseError as e:
        print(f"Erreur de parsing XML : {e}")
        return None
    
    

def saveToJSON(filename, text):
    data = {}  # Initialiser un dictionnaire vide pour stocker les données

    # Vérifier si le fichier JSON existe et n'est pas vide
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        # Charger les données existantes
        with open(filename, 'r') as file:
            data = json.load(file)

    # Ajouter la nouvelle ligne à la liste des lignes
    if 'idPages' not in data:
        data['idPages'] = []
    data['idPages'].append(text)

    # Enregistrer les données dans le fichier JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)



def readFromJSON(filename):
    data = {}  # Initialiser un dictionnaire vide pour stocker les données

    # Vérifier si le fichier JSON existe et n'est pas vide
    if os.path.exists(filename) and os.stat(filename).st_size > 0:
        # Charger les données existantes
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

    return data



def clearJSON(filename):
    with open(filename, 'w') as file:
        json.dump({}, file)
        



def constructMarkdownFile(contentList):
    questionsList = []

    for page in contentList:
        page_id = page["id"]
        page = page["page"]
        questionsList.append({"page_id": page_id, "question": page["question"], "choices": page["choices"]})

    # Construction de la chaîne de texte Markdown
    markdown_text = "# Titre principal\n\n## Votre aventure s'est déroulée de cette façon :\n\n"
    
    for item in questionsList:
        markdown_text += f"- {item['question']}\n"
        for choice in item['choices']:
            if len(choice) > 0:
                nextPage = questionsList[questionsList.index(item) + 1]
                choiceText = choice['text']
                if nextPage:
                    if choice["redirection_id"] == nextPage["page_id"]:
                        markdown_text += f"    - <u>{choiceText}</u>\n"
                    else:
                        markdown_text += f"    - {choiceText}\n"
                else:
                        markdown_text += f"    - {choiceText}\n"
                

    return markdown_text



def saveInMarkdown(filename, content):
    with open(filename, "w", encoding="utf-8") as mdFile:
        mdFile.write(content)


def loadOrNewGame(savesFolder="", progressJson="", structureJson=""):
    savesFile = getExistingSaves(savesFolder)
    savesFile.append({"text": "New Game", "redirection_id": -1})
    idSaveSelected = selectSaves(savesFile, savesFolder, progressJson, structureJson)
    return idSaveSelected


def getExistingSaves(savesFolder=""):
    savesFile = []
    for index, file in enumerate(os.listdir(savesFolder), start=-1):
        filepath = os.path.join(savesFolder, file)
        if file != ".gitkeep" and os.path.isfile(filepath):
            save_info = {"text": file, "redirection_id": index}
            savesFile.append(save_info)
    return savesFile


def savePage(filename="", savesFolder="", progressJson=""):
    if filename == "":
        filename = f"save_{len(os.listdir(savesFolder))-1}.json"

    filepath = os.path.join(savesFolder, filename)

    with open(progressJson, "r") as target, open(filepath, "w") as destination:
        destination.write(target.read())


def selectSaves(savesFile, savesFolder="", progressJson="", structureJson=""):
    global fileSave
    selectedSave = menuSelection.choiceSelectionWithArrow("Choisissez votre sauvegarde :", json.dumps(savesFile))
    if savesFile[selectedSave]["redirection_id"] >= 0:
        loadedFile = os.path.join(savesFolder, savesFile[selectedSave]["text"])
        with open(loadedFile, "r") as target, open(progressJson, "w") as destination:
            file_content = json.load(target)  # Convertir la chaîne JSON en objet Python

            if file_content and "idPages" in file_content:
                destination.write(json.dumps(file_content))
                lastPage = file_content["idPages"][-1]
                if save.readFromJSON(structureJson)[lastPage]["type"] == "end":
                    return -1
                    # Create Mardown and open it ---
                fileSave = savesFile[selectedSave]["text"]
                return lastPage
            else:
                tool.logError("Error: file is empty or missing 'idPages'")
                return 0
    else:
        return 0