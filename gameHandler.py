import os
import json
import sys
import gameEngine
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
        
        global ln, playerWorldRegion, playerLocalRegion, playerBuilding, playerMood, processedPlayerLocalRegion, processedPlayerWorldRegion, processedPlayerBuilding, playerOptions, events, tableScreen, tableScreenData
        ln = self.loadName
        playerOptions = []
        travelTime = 0
        playerWorldRegion = dataPlayer["playerWorld"]["worldRegion"]
        playerLocalRegion = dataPlayer["playerWorld"]["localRegion"]
        playerBuilding = dataPlayer["playerWorld"]["building"]

        events = {
            "dev": MapHandler.EventManager(ln).CreateEvent("devTest", "dev")
        }

        # ["Bem", "Com fome", "Com sono", "Irritado"]
        playerMood = dataPlayer["playerMood"]

        if playerWorldRegion != "":
            processedPlayerWorldRegion = dataWorld[playerWorldRegion]
        if playerLocalRegion != "":
            processedPlayerLocalRegion = dataWorld[playerWorldRegion][playerLocalRegion]
        if playerBuilding != "":
            processedPlayerBuilding = dataWorld[playerWorldRegion][playerLocalRegion][playerBuilding]

        if playerBuilding == "" and playerLocalRegion == "" and playerWorldRegion == "":
            for i in range(len(dataWorld["options"])):
                playerOptions.append(f"[{str(i+1)}] Viajar para {dataWorld[dataWorld['options'][i]]['name']}")
                events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), playerBuilding, playerLocalRegion, dataWorld[dataWorld['options'][i]]["id"])

        elif playerBuilding != "":
            try:
                for i in range(len(processedPlayerBuilding["options"])):
                    if processedPlayerBuilding["options"][i] == "sleep":
                        playerOptions.append(f"[{str(i+1)}] Dormir")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("sleep", str(i+1))
                    else:
                        pass
            except KeyError:
                pass
            playerOptions.append(f"[0] Sair desta área")
            events["0"] = MapHandler.EventManager(ln).CreateEvent("changeLocation", "0", "", playerLocalRegion, playerWorldRegion)

        elif playerLocalRegion != "":
            for i in range(len(processedPlayerLocalRegion["options"])):
                try:
                    if processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]["type"] == "house":
                        playerOptions.append(f"[{str(i+1)}] Visitar a casa {processedPlayerLocalRegion[processedPlayerLocalRegion['options'][i]]['name']}")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]['id'], playerLocalRegion, playerWorldRegion)
                    elif processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]["type"] == "tavern":
                        playerOptions.append(f"[{str(i+1)}] Visitar a taverna {processedPlayerLocalRegion[processedPlayerLocalRegion['options'][i]]['name']}")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]['id'], playerLocalRegion, playerWorldRegion)
                    elif processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]["type"] == "castle":
                        playerOptions.append(f"[{str(i+1)}] Visitar o castelo {processedPlayerLocalRegion[processedPlayerLocalRegion['options'][i]]['name']}")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), processedPlayerLocalRegion[processedPlayerLocalRegion["options"][i]]['id'], playerLocalRegion, playerWorldRegion)
                    else:
                        pass
                except KeyError:
                    pass
            playerOptions.append(f"[0] Sair desta área")
            events["0"] = MapHandler.EventManager(ln).CreateEvent("changeLocation", "0", "", "", playerWorldRegion)
                
        elif playerWorldRegion != "":
            for i in range(len(processedPlayerWorldRegion["options"])):
                try:
                    if processedPlayerWorldRegion[processedPlayerWorldRegion["options"][i]]["type"] == "city":
                        playerOptions.append(f"[{str(i+1)}] Visitar a cidade {processedPlayerWorldRegion[processedPlayerWorldRegion['options'][i]]['name']}")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1))
                    elif processedPlayerWorldRegion[processedPlayerWorldRegion["options"][i]]["type"] == "plain":
                        playerOptions.append(f"[{str(i+1)}] Visitar a planície {processedPlayerWorldRegion[processedPlayerWorldRegion['options'][i]]['name']}")
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), playerBuilding, processedPlayerWorldRegion[processedPlayerWorldRegion['options'][i]]["id"], playerWorldRegion)
                    else:
                        pass
                except KeyError:
                    pass
            playerOptions.append(f"[0] Sair desta área")
            events["0"] = MapHandler.EventManager(ln).CreateEvent("changeLocation", "0", "", "", "")
        else:
            for i in range(len(dataWorld["options"])):
                playerOptions.append(f"[{str(i+1)}] Viajar para {dataWorld['options'][i]}")
                events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), )

        tableScreenData = [
            ['']
        ]
        tableScreen = SingleTable(tableScreenData)

        mapData = f"Dia {str(dataWorld['day'])}, mês {str(dataWorld['month'])}, ano {str(dataWorld['year'])}.\n\nVocê está se sentindo: {playerMood}."

        if playerBuilding != "":
            MapHandler.UI().update(
            [
                [f"Você está em: {processedPlayerWorldRegion['name']}, {processedPlayerLocalRegion['name']}, {processedPlayerBuilding['name']}"], [mapData]
            ])
        elif playerLocalRegion != "":
            MapHandler.UI().update(
            [
                [f"Você está em: {processedPlayerWorldRegion['name']}, {processedPlayerLocalRegion['name']}"], [mapData]
            ])
        elif playerWorldRegion != "":
            MapHandler.UI().update(
            [
                [f"Você está em: {processedPlayerWorldRegion['name']}"], [mapData]
            ])
        else:
            MapHandler.UI().update(
            [
                [f"Você está em: {dataWorld['worldName']}."], [mapData]
            ])

        os.system("cls")

    class UI:
        def start(self):
            os.system("cls")
            print(tableScreen.table)
            for option in playerOptions:
                print(option)
            print("\n")
            print("[i] - Inventário | [m] Menu | [e] Sair | [p] - Perfil | [c] - Limpar log ")
        
        def update(self, data):
            if data == "default":
                os.system("cls")
            else:
                os.system("cls")
                tableScreen.table_data = data
            
            print(tableScreen.table)
            for option in playerOptions:
                print(option)
            print("\n")
            print("[i] - Inventário | [m] Menu | [e] Sair | [p] - Perfil | [c] - Limpar log ")

        #SPECIAL SCREENS
        def whileInProgressScreen(self):
            os.system("cls")

            print("Função em desenvolvimento!")
            input("Pressione Enter para continuar...")

            os.system("cls")
            self.update("default")

        def errorScreen(self, errHeader, errorMessage):
            os.system("cls")

            print(f"ERRO! => {errHeader}")
            print("\n")
            print(errorMessage)
            print("\n")

            input("Pressione Enter para continuar...")
            os.system("cls")
            self.update("default")

        def travelScreen(self):
            os.system("cls")

            print("Viajando...")
            input("Enter para continuar...")

            os.system("cls")
            self.update("default")

    class EventManager:
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
        
        class CreateEvent:
            def __init__(self, eType, userOption, *argv):
                self.eType = eType
                self.userOption = userOption
                self.argv = argv

            def event(self, *args):
                if self.eType == "changeLocation":
                    try:
                        dataPlayer["playerWorld"]["building"] = self.argv[0]
                        dataPlayer["playerWorld"]["localRegion"] = self.argv[1]
                        dataPlayer["playerWorld"]["worldRegion"] = self.argv[2]

                        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
                            json.dump(dataPlayer, saveChanges, indent=4)

                        MapHandler.UI().travelScreen()
                        loadThis = gameEngine.GameWorld(ln)
                        loadThis.start()
                    except KeyError:
                        MapHandler.UI().errorScreen("changeLocation | thisEvent.event()", "A localização enviada não existe! [gameWorld.json]")

                elif self.eType == "sleep":
                    try:
                        if args[0] > 1:
                            sleepTime = args[0]
                            print(f"Você irá dormir {str(sleepTime)} horas")
                        else:
                            MapHandler.UI().errorScreen("MapHandler.EventManager.CreateEvent.event()", "Não há argumentos na função! [eType = sleep]")
                    except IndexError:
                        MapHandler.UI().errorScreen("MapHandler.EventManager.CreateEvent.event()", "Não há argumentos na função! [eType = sleep]")

                elif self.eType == "devTest":
                    print("All Events:\n")
                    for i in events:
                        print(f"Event => {i:5} | EventHandler => {events[i]}")
                    print("="*16)
                    for i in events:
                        print(f"Event => {i:5} | {i} eType => {events[i].eType}")

                        

