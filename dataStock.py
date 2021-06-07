import os, json, sys
from terminaltables import SingleTable

class DataStock:
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
        global playerName, playerRace, playerClass, playerLanguage, playerAge, playerHeight, playerHealth, playerMana, playerArmor, playerLevel, playerXP, playerStrength, playerDexterity, playerConstitution, playerIntelligence, playerWisdom, playerCharisma, playerFavoriteWeapon, playerAbilities, playerInventory
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
        playerInventory = dataPlayer['playerInventory']
        playerAbilities = dataPlayer['playerAbilities']

        #GLOBALS WORLD DATA
        global worldName, worldType, worldAge, worldPopulation, nulr, grenkeparur, desertoDosOssos, sul
        worldName = dataWorld["worldName"]
        worldAge = dataWorld["worldAge"]
        worldPopulation = dataWorld["worldPopulation"]
        worldType = dataWorld["worldType"]
        nulr = dataWorld["nulr"]
        grenkeparur = dataWorld["grenkeparur"]
        desertoDosOssos = dataWorld["desertoDosOssos"]
        sul = dataWorld["sul"]

        #GLOBALS GAME DATA
        global human, dwarf, nulrnen, elf, woodElf, halfling, orc, warrior, ranger, wizard, bjoretNen, assassin, cleric, paladin, barbarian, druid, bard, monk, espocioComum, espocioAntigo, nulfanghe, items, abilities
        human = data["human"]
        dwarf = data["dwarf"]
        nulrnen = data["nulr"]
        elf = data["elf"]
        woodElf = data["woodElf"]
        halfling = data["halfling"]
        orc = data["orc"]
        warrior = data["warrior"]
        ranger = data["ranger"]
        wizard = data["wizard"]
        bjoretNen = data['bjoretNen']
        assassin = data["assassin"]
        cleric = data["cleric"]
        paladin = data["paladin"]
        barbarian = data["barbarian"]
        druid = data["druid"]
        bard = data["bard"]
        monk = data["monk"]
        espocioComum = data['espocioComum']
        espocioAntigo = data["espocioAntigo"]
        nulfanghe = data["nulrfanghe"]
        items = data["items"]
        abilities = data["abilities"]

    def seeAllData():
        allPlayerData = [playerName, playerRace, playerClass, playerLanguage, playerAge, playerHeight, playerHealth, playerMana, playerArmor, playerLevel, playerXP, playerStrength, playerDexterity, playerConstitution, playerIntelligence, playerWisdom, playerCharisma, playerFavoriteWeapon, playerInventory, playerAbilities]

        allWorldData = [worldName, worldAge, worldPopulation, worldType, nulr, grenkeparur, desertoDosOssos, sul]

        allGameData = [human, dwarf, nulrnen, elf, woodElf, halfling, orc, warrior, ranger, wizard, bjoretNen, assassin, cleric, paladin, barbarian, druid, bard, monk, espocioComum, espocioAntigo, nulfanghe, items, abilities]

        print("Player Data")
        for data in allPlayerData:
            print(data)

        print("\nWorld Data")
        for data in allWorldData:
            print(data)

        print("\nGame Data")
        for data in allGameData:
            print(data)

