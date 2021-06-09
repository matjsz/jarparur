import os
import json
import sys
from terminaltables import SingleTable
from inventorySystem import Inventory
from gameHandler import MapHandler
import gameHandler
from dataStock import DataStock

class GameWorld:
    def __init__(self, loadName):
        self.loadName = loadName

    def start(self):
        #START MODULES
        Inventory(self.loadName)
        DataStock(self.loadName)
        myScreen = MapHandler(self.loadName)
        myScreen.UI().start()

        with open(f'saves/{self.loadName}/gameData.json', encoding='utf-8') as jf:
            data = json.load(jf)

        with open(f'saves/{self.loadName}/worldData.json', encoding='utf-8') as wf:
            dataWorld = json.load(wf)

        with open(f'saves/{self.loadName}/{self.loadName}.json', encoding='utf-8') as pf:
            dataPlayer = json.load(pf)

        with open(f'saves/{self.loadName}/npcData.json', encoding='utf-8') as nf:
            global dataNpc
            dataNpc = json.load(nf)

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

        # ["Bem", "Com fome", "Com sono", "Irritado"]
        playerMood = dataPlayer["playerMood"]
        eventsEngineSide = gameHandler.events

        while True:
            eventTerminal = input(">>> ")

            #Game Commands
            if eventTerminal == "i":
                Inventory.showInventory()

            elif eventTerminal == "p":
                profileData = [
                    [playerName],
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
                    ['Carisma', playerCharisma]
                ]
                
                tableProfile = SingleTable(profileData)
                
                MapHandler.UI().update("default")
                print(tableProfile.table)

            elif eventTerminal == "c":
                MapHandler.UI().update("default")

            #Navigation
            elif eventTerminal == "m":
                import jarparur

                jarparur.mainStructure()
            elif eventTerminal == "e":
                os.system("cls")
                exit()

            elif eventTerminal == "dev data":
                DataStock.seeAllData()

            elif eventTerminal in eventsEngineSide:
                thisEvent = gameHandler.events[eventTerminal]

                if thisEvent.eType == "sleep":
                    sleepTime = input("Horas de sono: ")
                    thisEvent.event(int(sleepTime))
                elif thisEvent.eType == "devTest":
                    thisEvent.event()
                else:
                    thisEvent.event()

            else:
                MapHandler.UI().update("default")