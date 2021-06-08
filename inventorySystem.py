import os, json
from terminaltables import SingleTable
from gameHandler import MapHandler

class Inventory:
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

        #GLOBALS PLAYER DATA
        global playerName, playerRace, playerClass, playerLanguage, playerAge, playerHeight, playerHealth, playerMana, playerArmor, playerLevel, playerXP, playerStrength, playerDexterity, playerConstitution, playerIntelligence, playerWisdom, playerCharisma, playerFavoriteWeapon
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

    def discard(partInventory):
        partsDict = {
            "torso": "torso",
            "cabeça": "head",
            "braços": "arms",
            "mãos": "hands",
            "pernas": "legs",
            "pés": "foot"
        }

        if partInventory == "torso" or partInventory == "cabeça" or partInventory == "braços" or partInventory == "mãos" or partInventory == "pés" or partInventory == "pernas":
            dataPlayer["playerInventory"][partsDict.get(partInventory)] = ""
        else:
            if partInventory[4] != " ":
                slot = int(partInventory[4])-1

                try:
                    dataPlayer["playerInventory"]["slots"][slot] = ""
                except KeyError:
                    print("O Slot ou parte do corpo inserido não existe!")
                    input("\nPressione Enter para continuar...")
                    Inventory.showInventory()
            else:
                print("O comando foi inserido de maneira incorreta!")
                input("\nPressione Enter para continuar...")
                Inventory.showInventory()

        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
            json.dump(dataPlayer, saveChanges)

        os.system("cls")
        Inventory.showInventory()

    def addItem(partInventory, itemID):
        if partInventory == "torso" and data["items"][itemID]["type"] == "Roupa" or partInventory == "torso" and data["items"][itemID]["type"] == "Armadura":
            dataPlayer["playerInventory"][partInventory] = itemID
            
        elif partInventory == "head" and data["items"][itemID]["type"] == "Capacete" or partInventory == "head" and data["items"][itemID]["type"] == "Chapéu":
            dataPlayer["playerInventory"][partInventory] = itemID

        elif partInventory == "legs" and data["items"][itemID]["type"] == "Calça":
            dataPlayer["playerInventory"][partInventory] = itemID

        elif partInventory == "hands" and data["items"][itemID]["type"] == "Luvas":
            dataPlayer["playerInventory"][partInventory] = itemID
        
        elif partInventory == "arms" and data["items"][itemID]["type"] == "Bracelete":
            dataPlayer["playerInventory"][partInventory] = itemID

        elif partInventory == "foot" and data["items"][itemID]["type"] == "Calçado":
            dataPlayer["playerInventory"][partInventory] = itemID
        
        elif "slot" in partInventory:
            if partInventory[4] != " ":
                slot = int(partInventory[4])-1

                try:
                    dataPlayer["playerInventory"]["slots"][slot] = itemID
                except KeyError:
                    print("O Slot ou parte do corpo inserido não existe!")
                    input("\nPressione Enter para continuar...")
            else:
                print("O comando foi inserido de maneira incorreta!")
                input("\nPressione Enter para continuar...")

        else:
            try:
                os.system("cls")
                print(f"Você não pode adicionar {data['items'][itemID]['name']} no componente '{partInventory}'")
                input("Pressione Enter para continuar...")
            except KeyError:
                os.system("cls")
                print(f"O itemID {itemID} não está existe no gameData!")
                input("Pressione Enter para continuar...")

        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
            json.dump(dataPlayer, saveChanges)

        Inventory.showInventory()

    def showInventory():
        os.system("cls")

        print(f"Inventário de {playerName}\n")

        torsoData = ""
        braçosData = ""
        maosData = ""
        pesData = ""
        pernasData = ""
        cabeçaData = ""

        #Item Cabeça
        try:
            cabeçaData = data["items"][dataPlayer["playerInventory"]["head"]]["name"]
        except KeyError:
            cabeçaData = ""

        #Item Torso
        try:
            torsoData = data["items"][dataPlayer["playerInventory"]["torso"]]["name"]
        except KeyError:
            torsoData = ""

        #Item Braços
        try:
            braçosData = data["items"][dataPlayer["playerInventory"]["arms"]]["name"]
        except KeyError:
            braçosData = ""

        #Item Mãos
        try:
            maosData = data["items"][dataPlayer["playerInventory"]["hands"]]["name"]
        except KeyError:
            maosData = ""

        #Item Pernas
        try:
            pernasData = data["items"][dataPlayer["playerInventory"]["legs"]]["name"]
        except KeyError:
            pernasData = ""

        #Item Pés
        try:
            pesData = data["items"][dataPlayer["playerInventory"]["foot"]]["name"]
        except KeyError:
            pesData = ""

        bodyItemsData = [
            ['Cabeça', cabeçaData],
            ['Torso', torsoData],
            ['Braços', braçosData],
            ['Mãos', maosData],
            ['Pernas', pernasData],
            ['Pés', pesData]
        ]

        bodyItemsTable = SingleTable(bodyItemsData)
        bodyItemsTable.inner_row_border = True
        print("Vestuário")
        print(bodyItemsTable.table)

        slotData = []

        slotCount = 0
        for slot in dataPlayer["playerInventory"]["slots"]:
            slotCount += 1
            try:
                slotData.append([str(slotCount), data['items'][slot]['name']]) 
            except KeyError:
                slotData.append([str(slotCount), ""])

        slotTable = SingleTable(slotData)
        slotTable.inner_row_border = True
        print("Inventário (Slots)")
        print(slotTable.table)

        print("\n[slot[n]] ex: slot1 - Mostra detalhes do item no slot escolhido\n[parteInventario] ex: cabeça - Mostra detalhes do item no componente escolhido\n[back] - Volta para a tela de jogo\n[d] [parteInventario] - Descarta item no componente escolhido\n[c] - Limpa o log")

        while True:
            cmds = ["cabeça", "torso", "braços", "mãos", "pernas", "pés"]

            inventoryEvent = input("\n[i] >>> ")

            if inventoryEvent in cmds:
                if inventoryEvent == "pés":
                    try:
                        data["items"][dataPlayer["playerInventory"]["foot"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["foot"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["foot"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["foot"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["foot"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["foot"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["foot"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["foot"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try :
                            data["items"][dataPlayer["playerInventory"]["foot"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["foot"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["foot"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["foot"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["foot"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["foot"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["foot"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                elif inventoryEvent == "pernas":
                    try:
                        data["items"][dataPlayer["playerInventory"]["legs"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["legs"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["legs"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["legs"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["legs"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["legs"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["legs"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["legs"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try :
                            data["items"][dataPlayer["playerInventory"]["legs"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["legs"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["legs"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["legs"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["legs"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["legs"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["legs"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                elif inventoryEvent == "mãos":
                    try:
                        data["items"][dataPlayer["playerInventory"]["hands"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["hands"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["hands"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["hands"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["hands"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["hands"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["hands"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["hands"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try :
                            data["items"][dataPlayer["playerInventory"]["hands"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["hands"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["hands"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["hands"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["hands"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["hands"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["hands"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                elif inventoryEvent == "braços":
                    try:
                        data["items"][dataPlayer["playerInventory"]["arms"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["arms"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["arms"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["arms"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["arms"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["arms"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["arms"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["arms"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try :
                            data["items"][dataPlayer["playerInventory"]["arms"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["arms"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["arms"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["arms"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["arms"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["arms"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["arms"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                elif inventoryEvent == "torso":
                    try:
                        data["items"][dataPlayer["playerInventory"]["torso"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["torso"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["torso"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["torso"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["torso"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["torso"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["torso"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["torso"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try :
                            data["items"][dataPlayer["playerInventory"]["torso"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["torso"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["torso"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["torso"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["torso"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["torso"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["torso"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                elif inventoryEvent == "cabeça":
                    try:
                        data["items"][dataPlayer["playerInventory"]["head"]]["name"]

                        try:
                            data["items"][dataPlayer["playerInventory"]["head"]]["armor"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["head"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["head"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["head"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["head"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["head"]]["armor"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["head"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                        try:
                            data["items"][dataPlayer["playerInventory"]["head"]]["mana"]

                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["head"]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["head"]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["head"]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["head"]]["type"]],
                                ['\n'],
                                ['Armadura', data["items"][dataPlayer["playerInventory"]["head"]]["mana"]],
                                ['Custo', data["items"][dataPlayer["playerInventory"]["head"]]["cost"]]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)
                        except KeyError:
                            pass

                    except KeyError:
                        print("Não há itens aqui!")

                else:
                    print("O comando foi inserido de maneira incorreta!")
            
            elif "d " in inventoryEvent:
                Inventory.discard(inventoryEvent[2:])

            elif inventoryEvent == "back":
                os.system("cls")
                MapHandler(ln)
                MapHandler.UI().update('default')
                break

            elif inventoryEvent == "c":
                os.system("cls")
                Inventory.showInventory()

            elif inventoryEvent == "dev add":
                component = input("[onde adicionar] >> ")
                item = input("[item para adicionar] >>> ")
                Inventory.addItem(component, item)

            elif "slot" in inventoryEvent:
                if inventoryEvent[4] != " ":
                    slot = int(inventoryEvent[4])-1
                else:
                    print("O comando foi inserido de maneira incorreta!")
                    input("\nPressione Enter para continuar...")
                    Inventory.showInventory()
                
                try:
                    data["items"][dataPlayer["playerInventory"]["slots"][slot]]["name"]
                    
                    itemData = [
                        [data["items"][dataPlayer["playerInventory"]["slots"][slot]]["name"]],
                        ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["slots"][slot]]["description"]}"""],
                        ['Tier', data["items"][dataPlayer["playerInventory"]["slots"][slot]]["tier"]],
                        ['Tipo', data["items"][dataPlayer["playerInventory"]["slots"][slot]]["type"]],
                        ['\n'],
                        ['Dano', str(data["items"][dataPlayer["playerInventory"]["slots"][slot]]["damage"])],
                        ['Custo', str(data["items"][dataPlayer["playerInventory"]["slots"][slot]]["cost"])]
                    ]

                    tableItem = SingleTable(itemData)
                    print(tableItem.table)
                except KeyError:
                    print("O Slot está vazio!")
                    continue

            else:
                print("O comando foi inserido de maneira incorreta!")