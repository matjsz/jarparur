import os
import json
import sys
from terminaltables import SingleTable

class MapHandler:
    def __init__(self, loadName):
        self.loadName = loadName
        with open(f'saves/{self.loadName}/gameData.json', encoding='utf-8') as jf:
            global data
            data = json.load(jf)

        with open(f'saves/{self.loadName}/worldData.json', encoding='utf-8') as wf:
            global dataWorld
            dataWorld = json.load(wf)

        with open(f'saves/{self.loadName}/{self.loadName}.json', encoding='utf-8') as pf:
            global dataPlayer
            dataPlayer = json.load(pf)
        
        global ln
        ln = self.loadName

        os.system("cls")

    class UI:
        def start(self):
            global tableScreen, tableScreenData

            tableScreenData = [
                ['']
            ]
            tableScreen = SingleTable(tableScreenData)
            os.system("cls")
            print(tableScreen.table)
            print("Event Terminal\n")
            print("[i] - Inventário | [m] - Mover-se | [p] - Perfil | [c] - Limpar log ")
        
        def update(self, data):
            if data == "default":
                os.system("cls")
            else:
                os.system("cls")
                tableScreen.table_data = data
            
            print(tableScreen.table)
            print("Event Terminal\n")
            print("[i] - Inventário | [m] - Mover-se | [p] - Perfil | [c] - Limpar log ")

        #SPECIAL SCREENS
        def whileInProgressScreen(self):
            os.system("cls")

            print("Função em desenvolvimento!")
            input("Pressione Enter para continuar...")

            os.system("cls")
            self.update("default")

