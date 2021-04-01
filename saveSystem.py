import os
import json
import pathlib
import gameEngine
from os import listdir

saveFiles = os.listdir("saves/")
saves = []
for save in saveFiles:
    saves.append(save)

with open("gameData.json", encoding='utf-8') as jfg:
    data = json.load(jfg)

def saveGame(data):
    os.system("cls")
    print("SALVAR JOGO")

    saveName = input("\nNome do Save >>> ")

    try:
        with open(f'saves/{saveName}/{saveName}.json', 'w') as jf:
            json.dump(data, jf)
    except FileNotFoundError:
        pathlib.Path(f"saves/{saveName}").mkdir(parents=True, exist_ok=True)

        with open(f'saves/{saveName}/{saveName}.json', 'w') as jf:
            json.dump(data, jf)

def loadGame():
    os.system("cls")
    print("CARREGAR JOGO\n")

    listfolder = []

    for folder in listdir('saves/'):
        print(folder)
        listfolder.append(folder)

    loadName = input("\nCarregar Save >>> ")

    if loadName in listfolder:
        loadThis = gameEngine.GameWorld(loadName)
        loadThis.start()
    else:
        os.system("cls")
        print("O nome do save inserido está incorreto!")

        input("Pressione Enter para continuar...")

        import main
        main.mainStructure()