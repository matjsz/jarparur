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

    i = 1
    folderListeners = {}
    print("[0] VOLTAR")

    for folder in listdir('saves/'):
        print(f"[{str(i)}] {folder}")
        folderListeners[str(i)] = folder
        i += 1

    loadNum = input("\n>>> ")

    if loadNum in folderListeners:
        loadThis = gameEngine.GameWorld(folderListeners[loadNum])
        loadThis.start()
    elif loadNum == "0":
        import jarparur
        jarparur.mainStructure()
    else:
        os.system("cls")
        print("O identificador do save inserido está incorreto!")

        input("Pressione Enter para continuar...")
        import jarparur
        jarparur.mainStructure()