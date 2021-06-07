import saveSystem, characterCreator, prologue
import os
import art

#select game save
#if character -> game screen
#else -> character creator

def mainStructure():
    os.system("cls")
    print(art.gameTitle)

    while True:
        action = input("\n| Novo Jogo     [1] |\n| Carregar Jogo [2] |\n| Sair [3] | \n\n>>> ")
        actions = ['1', '2', '3']

        if action in actions:
            if action == "1":
                characterCreator.createCharacter()
            elif action == "2":
                saveSystem.loadGame()
            elif action == "3":
                exit()
        else:
            exit()

        break

mainStructure()
