import json
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
    def __init__(self, loadName, data):
        self.loadName = loadName
        self.data = data

    def firstSave(self):
        #Update FIRST SAVE
        os.system("cls")
        print("SALVANDO JOGO...")

        try:
            with open(f'saves/{self.loadName}/{self.loadName}.json', 'w', encoding='utf-8') as jf:
                json.dump(self.data, jf)
        except FileNotFoundError:
            pathlib.Path(f"saves/{self.loadName}").mkdir(parents=True, exist_ok=True)

            with open(f'saves/{self.loadName}/{self.loadName}.json', 'w', encoding='utf-8') as jf:
                json.dump(self.data, jf)

            with open(f'saves/{self.loadName}/gameData.json', 'w', encoding='utf-8') as jfg:
                json.dump(dataGame, jfg)

            with open(f'saves/{self.loadName}/worldData.json', 'w', encoding='utf-8') as jfw:
                json.dump(dataWorld, jfw)
    
    def prologueStart(self):
        with open(f'saves/{self.loadName}/{self.loadName}.json') as jfPlayer:
            dataPlayer = json.load(jfPlayer)

        #Update PROLOGO EXECUTAR
        os.system("cls")
        print("PRÓLOGO\n")

        print(f"Olá {dataPlayer['playerName']}! \n\nBem vindo ao mundo de Jarparunn!")
        input("")
        
        print(f"Aqui, você irá exporar diversas regiões em busca de aventura.")
        input("")

        print(f"Sua jornada começa em {dataWorld[dataPlayer['playerStartPoint']]['name']}. Seu personagem é um {data[dataPlayer['playerRace']]['name']}, tem {dataPlayer['playerAge']} anos e possui {dataPlayer['playerHeight']} cm de altura.")
        input("")

        print(f"Você é um {data[dataPlayer['playerClass']]['name']} e seu tipo de arma favorito é {dataPlayer['playerFavoriteWeapon']}")
        input("")

        print(f"Sua língua materna é {data[dataPlayer['playerLanguage']]['name']}")

        input("\nPressione Enter para continuar...")
        loadThis = gameEngine.GameWorld(self.loadName)
        loadThis.start()