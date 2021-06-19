import json
from textwrap import indent
import time
import os
import pathlib
import gameEngine
from resources import *

with open(f'gameData.json', encoding='utf-8') as jf:
    dataGame = json.load(jf)

with open(f'worldData.json', encoding='utf-8') as jfw:
    dataWorld = json.load(jfw)

class Prologue:
    def __init__(self, loadName, data, dataNpc, dataWorldNew):
        self.loadName = loadName
        self.data = data
        self.dataNpc = dataNpc
        self.dataWorldNew = dataWorldNew

    def firstSave(self):
        #Update FIRST SAVE
        os.system("cls")
        print("SALVANDO JOGO...")

        try:
            with open(f'saves/{self.loadName}/{self.loadName}.json', 'w', encoding='utf-8') as jf:
                json.dump(self.data, jf, indent=4)
        except FileNotFoundError:
            pathlib.Path(f"saves/{self.loadName}").mkdir(parents=True, exist_ok=True)

            with open(f'saves/{self.loadName}/{self.loadName}.json', 'w', encoding='utf-8') as jf:
                json.dump(self.data, jf, indent=4)

            with open(f'saves/{self.loadName}/gameData.json', 'w', encoding='utf-8') as jfg:
                json.dump(dataGame, jfg, indent=4)

            with open(f'saves/{self.loadName}/worldData.json', 'w', encoding='utf-8') as jfw:
                json.dump(self.dataWorldNew, jfw, indent=4)

            with open(f'saves/{self.loadName}/npcData.json', 'w', encoding='utf-8') as nf:
                json.dump(self.dataNpc, nf, indent=4)
    
    def prologueStart(self):
        with open(f'saves/{self.loadName}/{self.loadName}.json') as jfPlayer:
            dataPlayer = json.load(jfPlayer)

        #Update PROLOGO EXECUTAR
        if dataPlayer["playerGenre"] == "M" or "m":
            os.system("cls")
            print("PRÓLOGO\n")

            print(f"Olá {dataPlayer['playerName']}! \n\nBem vindo ao mundo de Jarparunn!")
            input("")
            
            print(f"Aqui, você irá exporar diversas regiões em busca de aventura.")
            input("")

            print(f"Sua jornada começa em {dataWorld[dataPlayer['playerStartPoint']]['name']}. Sua raça é {data[dataPlayer['playerRace']]['name']}, seu personagem tem {dataPlayer['playerAge']} anos e possui {dataPlayer['playerHeight']} cm de altura.")
            input("")

            print(f"Sua classe é {data[dataPlayer['playerClass']]['name']} e seu tipo de arma favorito é {dataPlayer['playerFavoriteWeapon']}")
            input("")

            print(f"Sua língua materna é {data[dataPlayer['playerLanguage']]['name']}")

            input("\nPressione Enter para continuar...")
        else:
            os.system("cls")
            print("PRÓLOGO\n")

            print(f"Olá {dataPlayer['playerName']}! \n\nBem vinda ao mundo de Jarparunn!")
            input("")
            
            print(f"Aqui, você irá exporar diversas regiões em busca de aventura.")
            input("")

            print(f"Sua jornada começa em {dataWorld[dataPlayer['playerStartPoint']]['name']}. Sua raça é {data[dataPlayer['playerRace']]['name']}, sua personagem tem {dataPlayer['playerAge']} anos e possui {dataPlayer['playerHeight']} cm de altura.")
            input("")

            print(f"Sua classe é {data[dataPlayer['playerClass']]['name']} e seu tipo de arma favorito é {dataPlayer['playerFavoriteWeapon']}")
            input("")

            print(f"Sua língua materna é {data[dataPlayer['playerLanguage']]['name']}")

            input("\nPressione Enter para continuar...")
        loadThis = gameEngine.GameWorld(self.loadName)
        loadThis.start()