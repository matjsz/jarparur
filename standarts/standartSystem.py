import os, json

class System:
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

    def systemFeature():
        pass