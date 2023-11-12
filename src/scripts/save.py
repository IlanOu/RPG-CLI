import xml.etree.ElementTree as ET
import os
import json


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
        print(item)
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