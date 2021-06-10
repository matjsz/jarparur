import os
import json
import sys
import gameEngine
import time
import random
import resources
import progressbar
from terminaltables import SingleTable

class MapHandler:
    def __init__(self, loadName):
        self.loadName = loadName
        try:
            with open(f'saves/{self.loadName}/gameData.json', encoding='utf-8') as jf:
                global data
                data = json.load(jf)
        except FileNotFoundError:
            MapHandler.UI().errorScreen("Arquivo 'gameData' não encontrado!", "O arquivo 'gameData' não foi encontrado, está corrompido ou não está disponível para esta versão do jogo, considere atualizar o jogo e criar um novo save.")
            import jarparur

            jarparur.mainStructure()

        try:
            with open(f'saves/{self.loadName}/worldData.json', encoding='utf-8') as wf:
                global dataWorld
                dataWorld = json.load(wf)
        except FileNotFoundError:
            MapHandler.UI().errorScreen("Arquivo 'worldData' não encontrado!", "O arquivo 'worldData' não foi encontrado, está corrompido ou não está disponível para esta versão do jogo, considere atualizar o jogo e criar um novo save.")
            import jarparur

            jarparur.mainStructure()

        try:
            with open(f'saves/{self.loadName}/{self.loadName}.json', encoding='utf-8') as pf:
                global dataPlayer
                dataPlayer = json.load(pf)
        except FileNotFoundError:
            MapHandler.UI().errorScreen(f"Arquivo '{loadName}' não encontrado!", f"O arquivo '{loadName}' não foi encontrado ou está corrompido, considere criar um novo save.")
            import jarparur

            jarparur.mainStructure()

        try:
            with open(f'saves/{self.loadName}/npcData.json', encoding='utf-8') as nf:
                global dataNpc
                dataNpc = json.load(nf)
        except FileNotFoundError:
            MapHandler.UI().errorScreen("Arquivo 'npcData' não encontrado!", "O arquivo 'npcData' não foi encontrado, está corrompido ou não está disponível para esta versão do jogo, considere atualizar o jogo e criar um novo save.")
            import jarparur

            jarparur.mainStructure()
        
        global ln, playerWorldRegion, playerLocalRegion, playerBuilding, playerMood, processedPlayerLocalRegion, processedPlayerWorldRegion, processedPlayerBuilding, playerOptions, events, tableScreen, tableScreenData, playerName, playerRace, playerClass, playerLanguage, playerAge, playerHeight, playerHealth, playerMana, playerArmor, playerLevel, playerXP, playerStrength, playerDexterity, playerConstitution, playerIntelligence, playerWisdom, playerCharisma, playerFavoriteWeapon
        ln = self.loadName

        #GLOBALS
        playerOptions = []
        playerWorldRegion = dataPlayer["playerWorld"]["worldRegion"]
        playerLocalRegion = dataPlayer["playerWorld"]["localRegion"]
        playerBuilding = dataPlayer["playerWorld"]["building"]

        #GLOBALS PLAYER DATA
        playerName = dataPlayer['playerName']
        playerRace = data[dataPlayer['playerRace']]['name']
        playerClass = data[dataPlayer['playerClass']]['name']
        playerLanguage = data[dataPlayer['playerLanguage']]['name']
        playerAge = dataPlayer['playerAge']
        playerHeight = dataPlayer['playerHeight']
        playerHealth = dataPlayer['playerHealth']
        playerMana = dataPlayer['playerMana']
        playerArmor = dataPlayer['playerArmor']
        playerLevel = dataPlayer['playerLevel']
        playerXP = dataPlayer['playerXP']
        playerStrength = dataPlayer['playerStrength']
        playerDexterity = dataPlayer['playerDexterity']
        playerConstitution = dataPlayer['playerConstitution']
        playerIntelligence = dataPlayer['playerIntelligence']
        playerWisdom = dataPlayer['playerWisdom']
        playerCharisma = dataPlayer['playerCharisma']
        playerFavoriteWeapon = dataPlayer['playerFavoriteWeapon']

        playerWorldRegion = dataPlayer["playerWorld"]["worldRegion"]
        playerLocalRegion = dataPlayer["playerWorld"]["localRegion"]
        playerBuilding = dataPlayer["playerWorld"]["building"]

        #NATIVE EVENTS
        events = {
            "dev": MapHandler.EventManager(ln).CreateEvent("devTest", "dev"),
            "h": MapHandler.EventManager(ln).CreateEvent("infoMap", "h"),
            "npcs": MapHandler.EventManager(ln).CreateEvent("infoNpc", "npcs"),
            "items": MapHandler.EventManager(ln).CreateEvent("infoItem", "items"),
            "addxp": MapHandler.EventManager(ln).CreateEvent("devTest", "addxp"),
            "l": MapHandler.EventManager(ln).CreateEvent("info", "l"),
            "e": MapHandler.EventManager(ln).CreateEvent("terminal", "e"),
            "m": MapHandler.EventManager(ln).CreateEvent("terminal", "m"),
            "c": MapHandler.EventManager(ln).CreateEvent("terminal", "c")
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
                        events[str(i+1)] = MapHandler.EventManager(ln).CreateEvent("changeLocation", str(i+1), playerBuilding, processedPlayerWorldRegion[processedPlayerWorldRegion['options'][i]]["id"], playerWorldRegion)
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

        playerTitle = resources.convertLevelToTitle(dataPlayer["playerLevel"], dataPlayer["playerClass"])

        mapData = f"{resources.convertCalendar(dataWorld['globalTime'])}.\n\nVocê está se sentindo: {playerMood}.\n\n{dataPlayer['playerName']}, {data[dataPlayer['playerClass']]['name']} {playerTitle} nível {dataPlayer['playerLevel']}"

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
            print("[e] Sair | [m] Menu | [l] Informações | [i] - Inventário | [c] - Limpar log ")
        
        def update(self, data):
            global globalGeoLocation, globalGeoCounts
            globalGeoLocation = {}
            globalGeoCounts = {}
            populationCount = 0
            globalTime = resources.convertCalendar(dataWorld["globalTime"])

            if playerBuilding != "":
                globalGeoLocation["player"] = playerBuilding
                globalGeoCounts[playerBuilding] = globalGeoCounts[playerBuilding]+1 if playerBuilding in globalGeoCounts else 1
            elif playerLocalRegion != "":
                globalGeoLocation["player"] = playerLocalRegion
                globalGeoCounts[playerLocalRegion] = globalGeoCounts[playerLocalRegion]+1 if playerLocalRegion in globalGeoCounts else 1
            elif playerWorldRegion != "":
                globalGeoLocation["player"] = playerWorldRegion
                globalGeoCounts[playerWorldRegion] = globalGeoCounts[playerWorldRegion]+1 if playerWorldRegion in globalGeoCounts else 1
            else:
                globalGeoLocation["player"] = dataWorld["worldName"]
                globalGeoCounts[dataWorld["worldName"]] = globalGeoCounts[dataWorld["worldName"]]+1 if dataWorld["worldName"] in globalGeoCounts else 1

            for npc in dataNpc:
                populationCount += 1
                if dataNpc[npc]["world"]["building"] != "":
                    globalGeoLocation[npc] = dataNpc[npc]["world"]["building"]
                    globalGeoCounts[dataNpc[npc]["world"]["building"]] = globalGeoCounts[dataNpc[npc]["world"]["building"]]+1 if dataNpc[npc]["world"]["building"] in globalGeoCounts else 1
                elif dataNpc[npc]["world"]["localRegion"] != "":
                    globalGeoLocation[npc] = dataNpc[npc]["world"]["localRegion"]
                    globalGeoCounts[dataNpc[npc]["world"]["localRegion"]] = globalGeoCounts[dataNpc[npc]["world"]["localRegion"]]+1 if dataNpc[npc]["world"]["localRegion"] in globalGeoCounts else 1
                elif dataNpc[npc]["world"]["worldRegion"] != "":
                    globalGeoLocation[npc] = dataNpc[npc]["world"]["worldRegion"]
                    globalGeoCounts[dataNpc[npc]["world"]["worldRegion"]] = globalGeoCounts[dataNpc[npc]["world"]["worldRegion"]]+1 if dataNpc[npc]["world"]["worldRegion"] in globalGeoCounts else 1
                else:
                    globalGeoLocation[npc] = dataWorld["worldName"]
                    globalGeoCounts[dataWorld["worldName"]] = globalGeoCounts[dataWorld["worldName"]]+1 if dataWorld["worldName"] in globalGeoCounts else 1

            dataWorld["worldPopulation"] = populationCount

            with open(f'saves/{ln}/worldData.json', 'w') as saveChanges:
                json.dump(dataWorld, saveChanges, indent=4)

            if data == "default":
                os.system("cls")
            else:
                os.system("cls")
                tableScreen.table_data = data
            
            print(tableScreen.table)
            for option in playerOptions:
                print(option)
            print("\n")
            print("[e] Sair | [m] Menu | [l] Informações | [i] - Inventário | [c] - Limpar log ")

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
            try:
                self.update("default")
            except KeyError:
                pass

        def waitScreen(self, activity, widget, waitTime):
            os.system("cls")

            print(f"{activity} - {resources.convertTime(waitTime)}")
            for i in progressbar.progressbar(range(50), widgets=widget):
                time.sleep(0.1)

            dataWorld["globalTime"] += waitTime

            with open(f'saves/{ln}/worldData.json', 'w') as saveChanges:
                json.dump(dataWorld, saveChanges, indent=4)

            loadThis = gameEngine.GameWorld(ln)
            loadThis.start()

            os.system("cls")
            self.update("default")

        def upgradeScreen(self, xp, previousLevel):
            os.system("cls")

            dictPoints = {
                "0": "Voltar",
                "1": "Força",
                "2": "Destreza",
                "3": "Constituição",
                "4": "Inteligência",
                "5": "Sabedoria",
                "6": "Carisma"
            }

            dictPointsFinal = {
                "1": "playerStrength",
                "2": "playerDexterity",
                "3": "playerConstitution",
                "4": "playerIntelligence",
                "5": "playerWisdom",
                "6": "playerCharisma"
            }

            dataPlayer["playerLevel"] += resources.convertXPToLevel(xp, dataPlayer["playerLevel"])
            dataPlayer["upgradePoints"] += resources.convertLevelToUpgradePoints(dataPlayer['playerLevel'], previousLevel)
            pointsToUse = dataPlayer['upgradePoints']

            while pointsToUse > 0:
                os.system("cls")
                print(f"VOCÊ SUBIU DE NÍVEL! | {previousLevel} -> {dataPlayer['playerLevel']}\n")
                print(f"Pontos para usar: {pointsToUse}")
                for option in dictPoints:
                    print(f"[{option}] {dictPoints[option]}")
                whereToUse = input(">>>")

                if whereToUse == "0":
                    os.system("cls")
                    self.update("default")
                elif whereToUse not in dictPoints:
                    os.system("cls")
                    self.update("default")
                else:
                    dataPlayer[dictPointsFinal[whereToUse]] += 1
                    pointsToUse -= 1
                    dataPlayer['upgradePoints'] = pointsToUse

            with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
                json.dump(dataPlayer, saveChanges, indent=4)

            loadThis = gameEngine.GameWorld(ln)
            loadThis.start()

        def reportScreen(self, message):
            os.system("cls")
            print(f"{message}")
            input('Pressione qualquer tecla para continuar...')
            loadThis = gameEngine.GameWorld(ln)
            loadThis.start()

        def infoScreen(self):
            waitingCommands = True
            while waitingCommands == True:
                os.system("cls")
                print("INFORMAÇÕES DO MUNDO\n")
                print("[w] -> Mostra informações sobre a região atual | [p] -> Mostra informações sobre o seu personagem\n[back] -> Volta para a tela principal\n")

                whatInfo = input(">>> ")
                if whatInfo == "w":
                    try:
                        if dataPlayer["playerWorld"]["worldRegion"] != "":
                            worldRegionData = [
                                ['Nome', dataWorld[dataPlayer["playerWorld"]["worldRegion"]]["name"]],
                                ['Descrição', dataWorld[dataPlayer["playerWorld"]["worldRegion"]]["description"]],
                                ['Idioma', data[dataWorld[dataPlayer["playerWorld"]["worldRegion"]]["language"]]["name"]]
                            ]

                            worldRegionTable = SingleTable(worldRegionData)
                            worldRegionTable.inner_row_border = True
                            print(worldRegionTable.table)
                            if dataPlayer["playerWorld"]["localRegion"] != "":
                                localRegionData = [
                                    ['Nome', dataWorld[dataPlayer["playerWorld"]["worldRegion"]][dataPlayer["playerWorld"]["localRegion"]]["name"]],
                                    ['Descrição', dataWorld[dataPlayer["playerWorld"]["worldRegion"]][dataPlayer["playerWorld"]["localRegion"]]["description"]],
                                ]

                                localRegionTable = SingleTable(localRegionData)
                                localRegionTable.inner_row_border = True
                                print(localRegionTable.table)
                                if dataPlayer["playerWorld"]["building"] != "":
                                    buldingData = [
                                        ['Nome', dataWorld[dataPlayer["playerWorld"]["worldRegion"]][dataPlayer["playerWorld"]["localRegion"]][dataPlayer["playerWorld"]["building"]]["name"]],
                                        ['Descrição', dataWorld[dataPlayer["playerWorld"]["worldRegion"]][dataPlayer["playerWorld"]["localRegion"]][dataPlayer["playerWorld"]["building"]]["description"]   ],
                                    ]

                                    buldingTable = SingleTable(buldingData)
                                    buldingTable.inner_row_border = True
                                    print(buldingTable.table)
                        else:
                            worldData = [
                                ['Nome', dataWorld["worldName"]],
                                ['Descrição', dataWorld["worldDescription"]],
                                ['Idiomas', f"{data[dataWorld['worldLanguages'][0]]['name']}, {data[dataWorld['worldLanguages'][1]]['name']}, {data[dataWorld['worldLanguages'][2]]['name']}"],
                                ['Idade do Mundo', resources.convertTime(dataWorld["globalTime"])],
                                ['População', dataWorld["worldPopulation"]],
                                ['Tipo', dataWorld["worldType"]]
                            ]

                            worldTable = SingleTable(worldData)
                            worldTable.inner_row_border = True
                            print(worldTable.table)
                    except IndexError:
                        MapHandler.UI().errorScreen("MapHandler.EventManager.CreateEvent.event()", "Não há argumentos na função, ou a localização enviada não existe. [eType = infoMap]")
                    input("Continuar...")
                elif whatInfo == "p":
                    profileData = [
                        ['Nome', playerName],
                        ['Raça', playerRace],
                        ['Classe', playerClass],
                        ['Idioma', playerLanguage],
                        ['Idade', playerAge],
                        ['Altura', playerHeight],
                        ['\n'],
                        ['Vida:', playerHealth],
                        ['Mana:', playerMana],
                        ['Armadura:', playerArmor],
                        ['Nível: ', str(playerLevel)+f" ({str(playerXP)} XP)"],
                        ['\n'],
                        ['Força', playerStrength],
                        ['Destreza', playerDexterity],
                        ['Constituição', playerConstitution],
                        ['Inteligência', playerIntelligence],
                        ['Sabedoria', playerWisdom],
                        ['Carisma', playerCharisma],
                        ['Terra natal', dataWorld[dataPlayer['playerStartPoint']]['name']],
                        ['Arma favorita', dataPlayer['playerFavoriteWeapon']]
                    ]
                    
                    tableProfile = SingleTable(profileData)
                    
                    print(tableProfile.table)
                    input("Continuar...")
                elif whatInfo == "back":
                    waitingCommands = False
                    loadThis = gameEngine.GameWorld(ln)
                    loadThis.start()
                else:
                    pass

        def npcFinder(self):
            thisHolder = True

            while thisHolder == True:
                os.system("cls")

                print("Bem vindo à interface de pesquisa de NPCs!\n")
                print("npc [id] - Mostra todos os dados do NPC por meio da id | npc all - Mostra todos os NPCs | npc all-name - Mostra todos os nomes dos NPCs | [back] Volta para a tela principal")
                promptNpc = input(">>> ")
                eventNpc = promptNpc[4:]

                if "npc" in promptNpc:
                    if eventNpc == "all":
                        for npc in dataNpc:
                            npcTableData = [
                                [npc, dataNpc[npc]["name"]],
                                ['Está se sentindo', dataNpc[npc]["mood"]],
                                ['Localização atual', dataWorld[dataNpc[npc]["world"]["worldRegion"]]["name"]],
                                ['Gênero', dataNpc[npc]["genre"]],
                                ['Raça', data[dataNpc[npc]["race"]]['name']],
                                ['Classe', data[dataNpc[npc]["class"]]['name']],
                                ['Idioma', data[dataNpc[npc]["language"]]['name']],
                                ['Idade', dataNpc[npc]["age"]],
                                ['Altura', f'{dataNpc[npc]["height"]} metros'],
                                ['Pontos de vida', dataNpc[npc]['health']],
                                ['Pontos de mana', dataNpc[npc]['mana']],
                                ['Pontos de armadura', dataNpc[npc]['armor']],
                                ['Nível', f'{dataNpc[npc]["level"]} ({dataNpc[npc]["XP"]} XP)'],
                                ['Arma favorita', dataNpc[npc]["favoriteWeapon"]],
                                ['Velocidade', dataNpc[npc]['velocity']],
                                ['Força', dataNpc[npc]['strength']],
                                ['Destreza', dataNpc[npc]['dexterity']],
                                ['Constituição', dataNpc[npc]['constitution']],
                                ['Inteligência', dataNpc[npc]['intelligence']],
                                ['Sabedoria', dataNpc[npc]['wisdom']],
                                ['Carisma', dataNpc[npc]['charisma']],
                                ['Terra natal', dataWorld[dataNpc[npc]['homeLand']]['name']],
                                ['Item primário', data['items'][dataNpc[npc]['inventory']['slots'][0]]['name']]
                            ]

                            npcTable = SingleTable(npcTableData)
                            print(npcTable.table)
                        input("Pressione qualquer tecla para voltar...")
                    elif eventNpc == "all-id":
                        print("\n")
                        for npc in dataNpc:
                            print(npc)
                        print("\n")
                        input("Pressione qualquer tecla para voltar...")
                    elif eventNpc == "all-text":
                        print("\n")
                        for npc in dataNpc:
                            print(dataNpc[npc]["name"])
                        print("\n")
                        input("Pressione qualquer tecla para voltar...")
                    elif len(eventNpc)>10:
                        try:
                            npcTableData = [
                                [eventNpc, dataNpc[eventNpc]["name"]],
                                ['Está se sentindo', dataNpc[eventNpc]["mood"]],
                                ['Localização atual', dataWorld[dataNpc[eventNpc]["world"]["worldRegion"]]["name"]],
                                ['Gênero', dataNpc[eventNpc]["genre"]],
                                ['Raça', data[dataNpc[eventNpc]["race"]]['name']],
                                ['Classe', data[dataNpc[eventNpc]["class"]]['name']],
                                ['Idioma', data[dataNpc[eventNpc]["language"]]['name']],
                                ['Idade', dataNpc[eventNpc]["age"]],
                                ['Altura', f'{dataNpc[eventNpc]["height"]} metros'],
                                ['Pontos de vida', dataNpc[eventNpc]['health']],
                                ['Pontos de mana', dataNpc[eventNpc]['mana']],
                                ['Pontos de armadura', dataNpc[eventNpc]['armor']],
                                ['Nível', f'{dataNpc[eventNpc]["level"]} ({dataNpc[eventNpc]["XP"]} XP)'],
                                ['Arma favorita', dataNpc[eventNpc]["favoriteWeapon"]],
                                ['Velocidade', dataNpc[eventNpc]['velocity']],
                                ['Força', dataNpc[eventNpc]['strength']],
                                ['Destreza', dataNpc[eventNpc]['dexterity']],
                                ['Constituição', dataNpc[eventNpc]['constitution']],
                                ['Inteligência', dataNpc[eventNpc]['intelligence']],
                                ['Sabedoria', dataNpc[eventNpc]['wisdom']],
                                ['Carisma', dataNpc[eventNpc]['charisma']],
                                ['Terra natal', dataWorld[dataNpc[eventNpc]['homeLand']]['name']],
                                ['Item primário', data['items'][dataNpc[eventNpc]['inventory']['slots'][0]]['name']]
                            ]

                            npcTable = SingleTable(npcTableData)
                            print(npcTable.table)
                        except KeyError:
                            print("\nO id informado não existe!\n")
                        input("Pressione qualquer tecla para voltar...")
                elif promptNpc == "back":
                    thisHolder = False
                    MapHandler.UI().update('default')
                else:
                    input("O id inserido está incorreto!")

        def itemFinder(self):
            thisHolder = True

            while thisHolder == True:
                os.system("cls")

                print("Bem vindo à interface de pesquisa de Itens!\n")
                print("item [id] - Mostra detalhes do item com base em sua id | item all - Mostra dados de todos os itens \nitem all-text - Mostra todos os nomes dos itens | item-all-id - Mostra todas as ids | back - Volta para a tela principal")
                promptItem = input(">>> ")
                eventItem = promptItem[5:]

                if "item" in promptItem:
                    if eventItem == "all":
                        for item in data["items"]:
                            if item != "all":
                                itemTableData = [["Nenhum item encontrado"]]

                                try:
                                    itemTableData = [
                                        ['Nome', data["items"][item]["name"]],
                                        ['Descrição', data["items"][item]["description"]],
                                        ['Tier', data["items"][item]["tier"]],
                                        ['Tipo', data["items"][item]["type"]],
                                        ['Armadura', data["items"][item]["armor"]],
                                        ['Custo', data["items"][item]["cost"]]
                                    ]
                                except KeyError:
                                    try:
                                        itemTableData = [
                                            ['Nome', data["items"][item]["name"]],
                                            ['Descrição', data["items"][item]["description"]],
                                            ['Tier', data["items"][item]["tier"]],
                                            ['Tipo', data["items"][item]["type"]],
                                            ['Mana', data["items"][item]["mana"]],
                                            ['Custo', data["items"][item]["cost"]]
                                        ]
                                    except KeyError:
                                        try:
                                            itemTableData = [
                                                ['Nome', data["items"][item]["name"]],
                                                ['Descrição', data["items"][item]["description"]],
                                                ['Tier', data["items"][item]["tier"]],
                                                ['Tipo', data["items"][item]["type"]],
                                                ['Dano', data["items"][item]["damage"]],
                                                ['Custo', data["items"][item]["cost"]]
                                            ]
                                        except KeyError:
                                            pass

                                itemTable = SingleTable(itemTableData)
                                print(itemTable.table)
                        input("Pressione qualquer tecla para continuar...")
                    elif eventItem == "all-id":
                        print("\n")
                        for item in data["items"]:
                            if item != "all":
                                print(item)
                        print("\n")
                        input("Pressione qualquer tecla para continuar...")
                    elif eventItem == "all-text":
                        print("\n")
                        for item in data["items"]:
                            if item != "all":
                                print(data["items"][item]["name"])
                        print("\n")
                        input("Pressione qualquer tecla para continuar...")
                    elif eventItem in data["items"]["all"]:
                        itemTableData = [["Nenhum item encontrado"]]

                        try:
                            itemTableData = [
                                ['Nome', data["items"][eventItem]["name"]],
                                ['Descrição', data["items"][eventItem]["description"]],
                                ['Tier', data["items"][eventItem]["tier"]],
                                ['Tipo', data["items"][eventItem]["type"]],
                                ['Armadura', data["items"][eventItem]["armor"]],
                                ['Custo', data["items"][eventItem]["cost"]]
                            ]
                        except KeyError:
                            try:
                                itemTableData = [
                                    ['Nome', data["items"][eventItem]["name"]],
                                    ['Descrição', data["items"][eventItem]["description"]],
                                    ['Tier', data["items"][eventItem]["tier"]],
                                    ['Tipo', data["items"][eventItem]["type"]],
                                    ['Mana', data["items"][eventItem]["mana"]],
                                    ['Custo', data["items"][eventItem]["cost"]]
                                ]
                            except KeyError:
                                try:
                                    itemTableData = [
                                        ['Nome', data["items"][eventItem]["name"]],
                                        ['Descrição', data["items"][eventItem]["description"]],
                                        ['Tier', data["items"][eventItem]["tier"]],
                                        ['Tipo', data["items"][eventItem]["type"]],
                                        ['Dano', data["items"][eventItem]["damage"]],
                                        ['Custo', data["items"][eventItem]["cost"]]
                                    ]
                                except KeyError:
                                    pass

                        itemTable = SingleTable(itemTableData)
                        print(itemTable.table)
                        input("Pressione qualquer tecla para continuar...")
                    else:
                        input("A id inserida está incorreta ou o comando foi inserido de forma incorreta!")
                elif promptItem == "back":
                    thisHolder = False
                    MapHandler.UI().update('default')
                else:
                    input("O comando foi inserido de maneira incorreta!")

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

            # eType sleep | argv[0] = hours to sleep
            # eType changeLocation | argv[0] = time of travel

            def event(self, *args):
                if self.eType == "changeLocation":
                    try:
                        dataPlayer["playerWorld"]["building"] = self.argv[0]
                        dataPlayer["playerWorld"]["localRegion"] = self.argv[1]
                        dataPlayer["playerWorld"]["worldRegion"] = self.argv[2]

                        widgets = [f" placeholder ", progressbar.Bar(), f" placeholder2"]
                        waitTime = 0

                        if playerBuilding != "":
                            waitTime = random.randint(60, 300)
                            widgets = [f" {dataWorld[playerWorldRegion]['name']}, {dataWorld[playerWorldRegion][playerLocalRegion]['name']}, {dataWorld[playerWorldRegion][playerLocalRegion][playerBuilding]['name']} ", progressbar.Bar(), f" {dataWorld[playerWorldRegion][self.argv[1]]['name']}"]
                        elif playerLocalRegion != "":
                            if self.argv[0] != "":
                                waitTime = random.randint(60, 300)
                                widgets = [f" {dataWorld[playerWorldRegion]['name']}, {dataWorld[playerWorldRegion][playerLocalRegion]['name']} ", progressbar.Bar(), f" {dataWorld[playerWorldRegion][playerLocalRegion][self.argv[0]]['name']}"]
                            elif self.argv[2] != "":
                                waitTime = random.randint(1800, 7200)
                                widgets = [f" {dataWorld[playerWorldRegion]['name']}, {dataWorld[playerWorldRegion][playerLocalRegion]['name']} ", progressbar.Bar(), f" {dataWorld[self.argv[2]]['name']}"]
                        elif playerWorldRegion != "":
                            if self.argv[1] != "":
                                waitTime = random.randint(1800, 7200)
                                widgets = [f" {dataWorld[playerWorldRegion]['name']} ", progressbar.Bar(), f" {dataWorld[playerWorldRegion][self.argv[1]]['name']}"]
                            else:
                                waitTime = random.randint(86400, 200000)
                                widgets = [f" {dataWorld[playerWorldRegion]['name']} ", progressbar.Bar(), f" {dataWorld['worldName']}"]
                        else:
                            waitTime = random.randint(86400, 200000)
                            widgets = [f" {dataWorld['worldName']} ", progressbar.Bar(), f" {dataWorld[self.argv[2]]['name']}"]

                        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
                            json.dump(dataPlayer, saveChanges, indent=4)

                        MapHandler.UI().waitScreen("Viajando", widgets, waitTime)
                        loadThis = gameEngine.GameWorld(ln)
                        loadThis.start()
                    except KeyError:
                        MapHandler.UI().errorScreen("changeLocation | thisEvent.event()", "A localização enviada não existe! [gameWorld.json]")

                elif self.eType == "sleep":
                    try:
                        if args[0] >= 1:
                            sleepTime = args[0]
                            print(f"Você irá dormir {str(sleepTime)} horas")
                            dataWorld["globalTime"] += 3600 * int(sleepTime)

                            with open(f'saves/{ln}/worldData.json', 'w') as saveChanges:
                                json.dump(dataWorld, saveChanges, indent=4)
                            
                            loadThis = gameEngine.GameWorld(ln)
                            loadThis.start()
                        else:
                            MapHandler.UI().errorScreen("MapHandler.EventManager.CreateEvent.event()", "Não há argumentos na função! [eType = sleep]")
                    except IndexError:
                        MapHandler.UI().errorScreen("MapHandler.EventManager.CreateEvent.event()", "Não há argumentos na função! [eType = sleep]")

                elif self.eType == "infoMap": 
                    if self.userOption == "h":
                        for creature in globalGeoLocation:
                            print(SingleTable([["ID", f"{creature}"], ["Localização", f"{globalGeoLocation[creature]}"]]).table)
                        for count in globalGeoCounts:
                            print(SingleTable([["Região", f"{count}"], ["Quantidade", f"{globalGeoCounts[count]}"]]).table)

                elif self.eType == "devTest":
                    if self.userOption == "dev":
                        print("All Events:\n")
                        for i in events:
                            print(f"Event => {i:5} | EventHandler => {events[i]}")
                        print("="*16)
                        for i in events:
                            print(f"Event => {i:5} | {i} eType => {events[i].eType}")
                    elif self.userOption == "addxp":
                        xp = args[0]
                        dataPlayer["playerXP"] += xp
                        if resources.seeIfLevelUp(dataPlayer["playerXP"], dataPlayer["playerLevel"]) == True:
                            MapHandler.UI().upgradeScreen(dataPlayer["playerXP"], dataPlayer["playerLevel"])
                        else:
                            with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
                                json.dump(dataPlayer, saveChanges, indent=4)
                            MapHandler.UI().reportScreen(f"Você ganhou {xp} xp!")                       

                elif self.eType == "infoNpc":
                    MapHandler.UI().npcFinder()

                elif self.eType == "infoItem":
                    MapHandler.UI().itemFinder()

                elif self.eType == "info":
                    MapHandler.UI().infoScreen()

                elif self.eType == "terminal":
                    if self.userOption == "e":
                        os.system("cls")
                        exit()
                    elif self.userOption == "m":
                        import jarparur

                        jarparur.mainStructure()
                    elif self.userOption == "c":
                        MapHandler.UI().update("default")