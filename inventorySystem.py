import gameEngine
import os, json
from typing import final
from terminaltables import SingleTable
from gameHandler import MapHandler

isOnInv = True
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
        
        global ln, isOnInv
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
        vest = ["torso", "head", "arms", "hands", "legs", "foot"]
        inv = []

        finalArmor = 0
        finalMana = 0
        finalBaseDamage = 0

        for slot in dataPlayer["playerInventory"]["slots"]:
            inv.append(dataPlayer["playerInventory"]["slots"].index(slot))

        if partInventory in vest:
            dataPlayer["playerInventory"][partInventory] = ""
        elif partInventory in inv:
            dataPlayer["playerInventory"]["slots"][partInventory] = ""

        for part in vest:
            if dataPlayer["playerInventory"][part] != "":
                finalArmor += data["items"][dataPlayer["playerInventory"][part]]["armor"]
                finalMana += data["items"][dataPlayer["playerInventory"][part]]["mana"]

        for slot in inv:
            if dataPlayer["playerInventory"]["slots"][slot] != "":
                finalBaseDamage += data["items"][dataPlayer["playerInventory"]["slots"][int(slot)]]["damage"]

        dataPlayer["playerArmor"] = finalArmor
        if dataPlayer["playerLevel"] == 0:
            dataPlayer["playerMana"] = finalMana + dataPlayer["playerIntelligence"]
        else:
            dataPlayer["playerMana"] = finalMana + (dataPlayer["playerIntelligence"] * dataPlayer["playerLevel"])
        dataPlayer["baseDamage"] = finalBaseDamage

        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
            json.dump(dataPlayer, saveChanges, indent=4)

        Inventory(ln)
        Inventory.showInventory()

    def addItem(itemID):
        parts = {
            "torso": ["Roupa", "Armadura"],
            "head": ["Capacete", "Chapéu"],
            "legs": ["Calça"],
            "hands": ["Luvas", "Anel"],
            "arms": ["Bracelete"],
            "foot": ["Calçado"]
        }

        invParts = []

        added = False
        finalArmor = 0
        finalMana = 0
        finalBaseDamage = 0

        for slot in dataPlayer["playerInventory"]["slots"]:
            if slot == "":
                invParts.append(dataPlayer["playerInventory"]["slots"].index(slot))

        for part in parts:
            if added == False:
                if data["items"][itemID]["type"] in parts[part]:
                    dataPlayer["playerInventory"][part] = itemID
                    added = True

        for part in parts:
            if dataPlayer["playerInventory"][part] != "":
                finalArmor += data["items"][dataPlayer["playerInventory"][part]]["armor"]
                finalMana += data["items"][dataPlayer["playerInventory"][part]]["mana"]

        for availablePart in invParts:
            if added == False:
                dataPlayer["playerInventory"]["slots"][availablePart] = itemID
                added = True

        for slot in dataPlayer["playerInventory"]["slots"]:
            if slot != "":
                slotNum = dataPlayer["playerInventory"]["slots"].index(slot)
                finalBaseDamage += data["items"][dataPlayer["playerInventory"]["slots"][slotNum]]["damage"]
        
        dataPlayer["playerArmor"] = finalArmor
        if dataPlayer["playerLevel"] == 0:
            dataPlayer["playerMana"] = finalMana + dataPlayer["playerIntelligence"]
        else:
            dataPlayer["playerMana"] = finalMana + (dataPlayer["playerIntelligence"] * dataPlayer["playerLevel"])
        dataPlayer["baseDamage"] = finalBaseDamage

        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
            json.dump(dataPlayer, saveChanges, indent=4)

        Inventory(ln)
        Inventory.showInventory()

    def use(slotNum):
        if data["items"][dataPlayer["playerInventory"]["slots"][slotNum]]["usesFor"] == "healing":
            if dataPlayer["playerHealth"] == dataPlayer["playerMaxHealth"]:
                pass
            elif dataPlayer["playerHealth"] < dataPlayer["playerMaxHealth"]:
                valuesToAdd = data["items"][dataPlayer["playerInventory"]["slots"][slotNum]]["value"]

                while valuesToAdd > 0:
                    if dataPlayer["playerHealth"] < dataPlayer["playerMaxHealth"]:
                        dataPlayer["playerHealth"] += 1
                        valuesToAdd -= 1
                    else:
                        valuesToAdd = 0 
                dataPlayer["playerInventory"]["slots"][slotNum] = ""
        elif data["items"][dataPlayer["playerInventory"]["slots"][slotNum]]["usesFor"] == "mana":
            dataPlayer["playerMana"] += data["items"][dataPlayer["playerInventory"]["slots"][slotNum]]["value"]
            dataPlayer["playerInventory"]["slots"][slotNum]

        with open(f'saves/{ln}/{ln}.json', 'w') as saveChanges:
            json.dump(dataPlayer, saveChanges, indent=4)

        Inventory(ln)
        Inventory.showInventory()

    def showInventory():
        global isOnInv
        isOnInv = True
        while isOnInv == True:
            os.system("cls")

            print(f"Inventário de {playerName}\n")
            cmds = {
                "back": "Voltar"
            }
            slotCmds = {}
            vestCmds = {}
            invCmds = {}
            nCmd = 1

            torsoData = ""
            braçosData = ""
            maosData = ""
            pesData = ""
            pernasData = ""
            cabeçaData = ""

            #Item Cabeça
            try:
                cabeçaData = data["items"][dataPlayer["playerInventory"]["head"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["head"]]["name"]
                vestCmds[str(nCmd)] = "head"
                nCmd += 1
            except KeyError:
                cabeçaData = ""

            #Item Torso
            try:
                torsoData = data["items"][dataPlayer["playerInventory"]["torso"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["torso"]]["name"]
                vestCmds[str(nCmd)] = "torso"
                nCmd += 1
            except KeyError:
                torsoData = ""

            #Item Braços
            try:
                braçosData = data["items"][dataPlayer["playerInventory"]["arms"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["arms"]]["name"]
                vestCmds[str(nCmd)] = "arms"
                nCmd += 1
            except KeyError:
                braçosData = ""

            #Item Mãos
            try:
                maosData = data["items"][dataPlayer["playerInventory"]["hands"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["hands"]]["name"]
                vestCmds[str(nCmd)] = "hands"
                nCmd += 1
            except KeyError:
                maosData = ""

            #Item Pernas
            try:
                pernasData = data["items"][dataPlayer["playerInventory"]["legs"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["legs"]]["name"]
                vestCmds[str(nCmd)] = "legs"
                nCmd += 1
            except KeyError:
                pernasData = ""

            #Item Pés
            try:
                pesData = data["items"][dataPlayer["playerInventory"]["foot"]]["name"]
                cmds[str(nCmd)] = data["items"][dataPlayer["playerInventory"]["foot"]]["name"]
                vestCmds[str(nCmd)] = "foot"
                nCmd += 1
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
                    slotCmds[str(nCmd)] = data['items'][slot]['name']
                    invCmds[str(nCmd)] = dataPlayer["playerInventory"]["slots"].index(slot)
                    nCmd += 1
                except KeyError:
                    slotData.append([str(slotCount), ""])

            slotTable = SingleTable(slotData)
            slotTable.inner_row_border = True
            print("Inventário (Slots)")
            print(slotTable.table)

            # print("\nWIP => [slot[n]] ex: slot1 - Mostra detalhes do item no slot escolhido\n[parteInventario] ex: cabeça - Mostra detalhes do item no componente escolhido\n[back] - Volta para a tela de jogo\n[d] [parteInventario] - Descarta item no componente escolhido\n[c] - Limpa o log")
            for command in cmds:
                if command == "back":
                    print(f"[{command}] {cmds[command]}\n")
            print("Vestuário")
            for command in cmds:
                if command != "back":
                    print(f"[{command}] {cmds[command]}")
            print("\n")
            print("Inventário")
            for slotCommand in slotCmds:
                print(f"[{slotCommand}] {slotCmds[slotCommand]}")

            inventoryEvent = input("\n[i] >>> ")

            if inventoryEvent in cmds or inventoryEvent in slotCmds:
                os.system("cls")
                if inventoryEvent in vestCmds:
                    try:
                        data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["name"]
                        try:
                            isOnItem = True

                            while isOnItem == True:
                                os.system("cls")
                                itemData = [
                                    [data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["name"]],
                                    ['Descrição', f"""{data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["description"]}"""],
                                    ['Tier', data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["tier"]],
                                    ['Tipo', data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["type"]],
                                    ['\n'],
                                    ['Armadura', data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["armor"]],
                                    ['Mana', data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["mana"]],
                                    ['Custo', data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["cost"]]
                                ]

                                tableItem = SingleTable(itemData)
                                print(tableItem.table)
                                print("d - Descarta o item | u - Usa o item caso seja um utilizável | back - Volta para o Inventário")
                                itemEvent = input(">>> ")

                                if itemEvent == "back":
                                    isOnItem = False
                                    Inventory.showInventory()

                                elif itemEvent == "d":
                                    Inventory.discard(vestCmds[inventoryEvent])

                                elif itemEvent == "u":
                                    if data["items"][dataPlayer["playerInventory"][vestCmds[inventoryEvent]]]["type"] == "Utilizável":
                                        Inventory.use(vestCmds[inventoryEvent])
                                    else:
                                        print("Este item não pode ser utilizado!")
                                        input("Pressione qualquer tecla para continuar...")
                        except KeyError:
                            pass

                    except KeyError:
                        isOnInv = False
                        loadThis = gameEngine.GameWorld(ln)
                        loadThis.start()

                elif inventoryEvent in invCmds:
                    try:
                        isOnItem = True

                        while isOnItem == True:
                            os.system("cls")

                            data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["name"]
                        
                            itemData = [
                                [data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["name"]],
                                ['Descrição', f"""{data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["description"]}"""],
                                ['Tier', data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["tier"]],
                                ['Tipo', data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["type"]],
                                ['\n'],
                                ['Dano', str(data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["damage"])],
                                ['Custo', str(data["items"][dataPlayer["playerInventory"]["slots"][invCmds[inventoryEvent]]]["cost"])]
                            ]

                            tableItem = SingleTable(itemData)
                            print(tableItem.table)

                            print("d - Descarta o item | u - Usa o item caso seja um utilizável | back - Volta para o Inventário")
                            itemEvent = input(">>> ")

                            if itemEvent == "back":
                                isOnItem = False
                                Inventory.showInventory()

                            elif itemEvent == "d":
                                Inventory.discard(invCmds[inventoryEvent])

                            elif itemEvent == "u":
                                Inventory.use(invCmds[inventoryEvent])
                    except KeyError:
                        isOnInv = False
                        loadThis = gameEngine.GameWorld(ln)
                        loadThis.start()
                
                elif inventoryEvent == "back":
                    isOnInv = False
                    loadThis = gameEngine.GameWorld(ln)
                    loadThis.start()

            elif inventoryEvent == "dev add":
                item = input("[item para adicionar] >>> ")
                os.system("cls")
                Inventory.addItem(item)