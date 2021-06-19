import saveSystem
import os
import uuid
import json
import prologue
import art
import names
from terminaltables import SingleTable
import random 
from resources import *
from textwrap import wrap

dragonBeforeName = art.characterCreatorDragonIdling

availabeLanguages = ['1', '2', '3']

languagesDict = {
    "1": "espocioComum",
    "2": "espocioAntigo",
    "3": "nulrfanghe"
}

regionsDict = {
    "1": "nulr",
    "2": "grenkeparur",
    "3": "desertoDosOssos",
    "4": "sul"
}

with open(f'gameData.json', encoding='utf-8') as jf:
    data = json.load(jf)

with open(f'worldData.json', encoding='utf-8') as wf:
    dataWorld = json.load(wf)

def createCharacter():
    #Update LOCAL DE INICIO
    regionScreen = True
    while regionScreen == True:
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM")

        print("\nBem-vindo aventureiro (ou aventureira)! Está pronto para adentrar no maravilhoso mundo de Japarur? Espero que sim, você não vai se arrepender!")

        print("\nVamos escolher uma região para o seu personagem!")

        tableRegiaoData = [
            ['Região', 'Descrição'],
            [dataWorld["nulr"]["name"], data["nulr"]["description"]],
            [dataWorld["grenkeparur"]["name"], dataWorld["grenkeparur"]["description"]],
            [dataWorld["desertoDosOssos"]["name"], dataWorld["desertoDosOssos"]["description"]],
            [dataWorld["sul"]["name"], dataWorld["sul"]["description"]]
        ]

        tableRegiao = SingleTable(tableRegiaoData)
        tableRegiao.inner_row_border = True

        print(tableRegiao.table)
        print("1 - Norte | 2 - Grenkëparur | 3 - Deserto dos Ossos | 4 - O Sul")
        
        playerStartPoint = input("\nSeu ponto de início: ")
        if playerStartPoint in regionsDict:
            playerStartPoint = regionsDict.get(playerStartPoint)
            regionScreen = False
        else:
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM - ERRO => Região não existe")
            print("\nA região escolhida não existe!\n")
            input("Pressione Enter para continuar...")

    raceScreen = True
    while raceScreen == True:
        #Update RAÇA
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM\n")

        #Raça
        print(f"\nCerto, sua região natal vai ser {playerStartPoint}, isso lhe dá algumas opções de raças, vejamos...\n")

        tableRaçaData = [
        ]
        racesDict = {}

        if playerStartPoint == "nulr":
            tableRaçaData = [
                ['Raça', 'Descrição'],
                [data["dwarf"]["name"], data["dwarf"]["description"]],
                [data["nulr"]["name"], data["nulr"]["description"]],
            ]
        elif playerStartPoint == "sul":
            tableRaçaData = [
                ['Raça', 'Descrição'],
                [data["human"]["name"], data["human"]["description"]],
                [data["elf"]["name"], data["elf"]["description"]],
                [data["woodElf"]["name"], data["woodElf"]["description"]],
                [data["halfling"]["name"], data["halfling"]["description"]],
            ]
        elif playerStartPoint == "desertoDosOssos":
            tableRaçaData = [
                ['Raça', 'Descrição'],
                [data["orc"]["name"], data["orc"]["description"]]
            ]
        else:
            tableRaçaData = [
                ['Raça', 'Descrição'],
                [data["human"]["name"], data["human"]["description"]],
                [data["dwarf"]["name"], data["dwarf"]["description"]],
                [data["nulr"]["name"], data["nulr"]["description"]],
                [data["elf"]["name"], data["elf"]["description"]],
                [data["woodElf"]["name"], data["woodElf"]["description"]],
                [data["halfling"]["name"], data["halfling"]["description"]],
                [data["orc"]["name"], data["orc"]["description"]]
            ]

        tableRaça = SingleTable(tableRaçaData)
        tableRaça.inner_row_border = True

        print(tableRaça.table)

        if playerStartPoint == "nulr":
            racesDict = {
                "1": "dwarf",
                "2": "nulr"
            }
            print("1 - Anão | 2 - Nulr")
        elif playerStartPoint == "sul":
            racesDict = {
                "1": "human",
                "2": "elf",
                "3": "woodElf",
                "4": "halfling"
            }
            print("1 - Humano | 2 - Elfo | 3 - Elfo da Floresta | 4 - Halfling")
        elif playerStartPoint == "desertoDosOssos":
            racesDict = {
                "1": "orc"
            }
            print("1 - Orc")
        else:
            racesDict = {
                "1": "human",
                "2": "dwarf",
                "3": "nulr",
                "4": "elf",
                "5": "woodElf",
                "6": "halfling",
                "7": "orc"
            }
            print("1 - Humano | 2 - Anão | 3 - Nulr | 4 - Elfo | 5 - Elfo da Floresta | 6 - Halfling | 7 - Orc")

        playerRace = input("\nSua raça: ")

        if playerRace in racesDict:
            playerRace = racesDict.get(playerRace)
            raceScreen = False
        else:
            #Update ERRO RAÇA
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("A Raça inserida não existe!")
            input("\nPressione Enter para continuar...")

    classScreen = True
    while classScreen == True:
        #Update CLASSE
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM")

        print(dragonBeforeName)

        print(f"\nCerto, você se tornou um(a) {data[playerRace]['name']}, muito bom! Porque não escolher uma raça?\n")
        
        tableClasseData = [
        ]
        classDict = {}

        if playerRace == "nulr":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["warrior"]["name"], data["warrior"]["description"]],
                [data["ranger"]["name"], data["ranger"]["description"]],
                [data["bjoretNen"]["name"], data["bjoretNen"]["description"]],
                [data["assassin"]["name"], data["assassin"]["description"]],
                [data["barbarian"]["name"], data["barbarian"]["description"]],
                [data["bard"]["name"], data["bard"]["description"]]
            ]
        elif playerRace == "dwarf":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["warrior"]["name"], data["warrior"]["description"]],
                [data["barbarian"]["name"], data["barbarian"]["description"]]
            ]
        elif playerRace == "human":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["warrior"]["name"], data["warrior"]["description"]],
                [data["ranger"]["name"], data["ranger"]["description"]],
                [data["wizard"]["name"], data["wizard"]["description"]],
                [data["assassin"]["name"], data["assassin"]["description"]],
                [data["cleric"]["name"], data["cleric"]["description"]],
                [data["paladin"]["name"], data["paladin"]["description"]],
                [data["monk"]["name"], data["monk"]["description"]]
            ]
        elif playerRace == "elf":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["ranger"]["name"], data["ranger"]["description"]],
                [data["wizard"]["name"], data["wizard"]["description"]],
                [data["cleric"]["name"], data["cleric"]["description"]],
            ]
        elif playerRace == "woodElf":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["warrior"]["name"], data["warrior"]["description"]],
                [data["ranger"]["name"], data["ranger"]["description"]],
                [data["assassin"]["name"], data["assassin"]["description"]]
            ]
        elif playerRace == "halfling":
            tableClasseData = [
                ['Classe', 'Descrição'],
                [data["cleric"]["name"], data["cleric"]["description"]],
                [data["bard"]["name"], data["bard"]["description"]]
            ]
        elif playerRace == "orc":
            tableClasseData = [
            ['Classe', 'Descrição'],
                [data["warrior"]["name"], data["warrior"]["description"]],
                [data["barbarian"]["name"], data["barbarian"]["description"]]
            ]

        tableClasse = SingleTable(tableClasseData)
        tableClasse.inner_row_border = True

        print(tableClasse.table)

        if playerRace == "nulr":
            print("1 - Guerreiro | 2 - Ranger | 3 - Bjoret-Nen | 4 - Assassino | 5 - Bárbaro | 6 - Bardo")
            classDict = {
                "1": "warrior",
                "2": "ranger",
                "3": "bjoretNen",
                "4": "assassin",
                "5": "barbarian",
                "6": "bard"
            }
        elif playerRace == "dwarf":
            print("1 - Guerreiro | 2 - Bárbaro")
            classDict = {
                "1": "warrior",
                "2": "barbarian"
            }
        elif playerRace == "human":
            print("1 - Guerreiro | 2 - Ranger | 3 - Mago | 4 - Assassino | 5 - Clérigo | 6 - Paladino")
            classDict = {
                "1": "warrior",
                "2": "ranger",
                "3": "wizard",
                "4": "assassin",
                "5": "cleric",
                "6": "paladin"
            }
        elif playerRace == "elf":
            print("1 - Ranger | 2 - Mago | 3 - Clérigo")
            classDict = {
                "1": "ranger",
                "2": "wizard",
                "3": "cleric"
            }
        elif playerRace == "woodElf":
            print("1 - Guerreiro | 2 - Ranger | 3 - Assassino")
            classDict = {
                "1": "warrior",
                "2": "ranger",
                "3": "assassin"
            }
        elif playerRace == "halfling":
            print("1 - Clérigo | 2 - Bardo")
            classDict = {
                "1": "cleric",
                "2": "bard"
            }
        elif playerRace == "orc":
            print("1 - Guerreiro | 2 - Bárbaro")
            classDict = {
                "1": "warrior",
                "2": "barbarian"
            }

        playerClass = input("\nSua classe: ")

        if playerClass in classDict:
            playerClass = classDict.get(playerClass)
            classScreen = False
        else:
            #Update ERRO CLASSE
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("A Classe inserida não existe!")
            input("\nPressione Enter para continuar...")

    #Update NOME
    screenNome = True
    while screenNome == True:
        thoseGenres = ["M", "m", "F", "f"]

        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM")

        print(f"\nAté aqui, sua raça é {playerRace} e sua classe é {playerClass}.")

        #Nome
        print("\nAgora, você precisa dar um nome ao seu personagem.")

        print(dragonBeforeName)

        playerName = input("\nSeu nome: ")
        print("\nAgora, seu personagem precisa de um gênero.")
        playerGenre = input("\nSeu gênero [M/F]: ")

        if playerGenre in thoseGenres:
            if playerRace == "nulr" or "dwarf":
                playerLanguage = "nulrfanghe"
            elif playerRace == "orc" or "woodElf":
                playerLanguage = "espocioAntigo"
            else:
                playerLanguage = "espocioComum"
            
            screenNome = False
        else:
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("O gênero inserido não está disponível!")
            input("\nPressione Enter para continuar...")

    #Update IDADE
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print(f"\nCerto {playerName}, agora você fala {data[playerLanguage]['name']}, é um {data[playerRace]['name']} e sua classe é {data[playerClass]['name']}. Insira sua idade para fins... inúteis.\n")

    playerAge = input("Sua idade: ")

    tall = ["orc", "woodElf"]
    medium = ["human", "elf", "nulr"]
    tiny = ["dwarf", "halfling"]

    if playerRace in tall:
        thisHeight = random.randint(190, 250)
        playerHeight = thisHeight
    elif playerRace in medium:
        thisHeight = random.randint(150, 190)
        playerHeight = thisHeight
    elif playerRace in tiny:
        thisHeight = random.randint(50, 150)
        playerHeight = thisHeight
    else:
        thisHeight = random.randint(150, 180)
        playerHeight = thisHeight


    #Update ARMA FAVORITA
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print(f"\nEm Jarparur, você precisa se defender contra monstros e criaturas perigosas, para isso, você precisa de uma arma. Não, você não vai receber esta arma, mas quando encontrar, ela terá atributos melhores!\n")
    
    classFavoriteWeapons = data[playerClass]["favoriteWeapons"]
    tempChoice = ""

    for weapon in classFavoriteWeapons:
        print("-", weapon)

    print("\n")

    for weapon in classFavoriteWeapons:
        while tempChoice == "" or tempChoice == "n":
            choice = input(f"{weapon} <- [y/n] ")

            if choice == "y":
                playerFavoriteWeapon = weapon
                tempChoice = choice
                break
            elif choice == "n":
                tempChoice = choice
                break
            else:
                continue

    #-------------------------------------------------------------------------------/

    nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]
    meeleeClasses = ["warrior", "paladin"]
    rangedClasses = ["ranger", "druid"]

    #Define Base ITEMS
    if playerClass in nonMagicalClasses:
        playerHead = ""
        playerTorso = "401"
        playerArms = ""
        playerHands = ""
        playerLegs = "402" 
        playerFoot = "501"

    else:
        playerHead = ""
        playerTorso = "5111"
        playerArms = ""
        playerHands = ""
        playerLegs = ""
        playerFoot = "501"

    #Define Base WEAPONS
    if playerClass in meeleeClasses:
        playerWeapon = "101"
    
    elif playerClass in rangedClasses:
        playerWeapon = "301"

    elif playerClass == "wizard":
        playerWeapon = "6111"
    
    elif playerClass == "bjoretNen":
        playerWeapon = "6151"
    
    elif playerClass == "assassin":
        playerWeapon = "102"
    
    elif playerClass == "barbarian":
        playerWeapon = "201"

    elif playerClass == "bard":
        playerWeapon = "6112"

    else:
        playerWeapon = "203"

    playerArmor = 0

    if playerHead != "":
        playerArmor += data["items"][playerHead]["armor"]
    elif playerTorso != "":
        playerArmor += data["items"][playerTorso]["armor"]
    elif playerArms != "":
        playerArmor += data["items"][playerArms]["armor"]
    elif playerHands != "":
        playerArmor += data["items"][playerHands]["armor"]
    elif playerLegs != "":
        playerArmor += data["items"][playerLegs]["armor"]
    elif playerFoot != "":
        playerArmor != data["items"][playerFoot]["armor"]

    baseDamage = data["items"][playerWeapon]["damage"]

    playerData = {
        "playerName": f"{playerName}", #INPUT
        "playerGenre": f"{playerGenre}", #INPUT
        "playerRace": f"{playerRace}", #INPUT
        "playerClass": f"{playerClass}",
        "playerLanguage": f"{playerLanguage}", #INPUT
        "playerAge": int(playerAge), #INPUT
        "playerHeight": (int(playerHeight)/100), #INPUT

        "playerHealth": int(data[playerClass]['constitution']),
        "playerMaxHealth": int(data[playerClass]['constitution']),
        "playerMana": int(data[playerClass]['intelligence']),
        "playerArmor": playerArmor,
        "baseDamage": baseDamage,

        "playerLevel": 0,
        "upgradePoints": 0,
        "playerXP": 0,
        "playerMood": "Bem",

        "playerStrength": int(data[playerClass]['strength']),
        "playerDexterity": int(data[playerClass]['dexterity']),
        "playerConstitution": int(data[playerClass]['constitution']),
        "playerIntelligence": int(data[playerClass]['intelligence']),
        "playerWisdom": int(data[playerClass]['wisdom']),
        "playerCharisma": int(data[playerClass]['charisma']),

        "playerStartPoint": f"{playerStartPoint}", #INPUT
        "playerFavoriteWeapon": f"{playerFavoriteWeapon}", #INPUT

        "playerInventory": {
            "head": f"{playerHead}",
            "torso": f"{playerTorso}",
            "arms": f"{playerArms}",
            "hands": f"{playerHands}",
            "legs": f"{playerLegs}",
            "foot": f"{playerFoot}",
            "ring": "",

            "slots": [f"{playerWeapon}", "", "", "", "", "", "", ""],
            "bag": ["", "", ""]
        },

        "playerWorld": {
            "worldRegion": f"{playerStartPoint}",
            "localRegion": "",
            "building": ""
        }
    }

    #Update FINAL
    os.system("cls")
    print("PERSONAGEM CRIADO COM SUCESSO!")

    print(f"\nPERSONAGEM: {playerName}")
    print(f"------------------------------/")
    print(f"Gênero: {playerGenre}")
    print(f"Raça: {data[playerRace]['name']}")
    print(f"Classe: {data[playerClass]['name']}")
    print(f"Idioma: {data[playerLanguage]['name']}")
    print(f"Idade: {playerAge}")
    print(f"Altura: {int(playerHeight)/100}")
    print(f"\n")
    print(f"Vida: {data[playerClass]['constitution']}")
    print(f"Mana: {data[playerClass]['intelligence']}")
    print(f"Armadura: {playerArmor}")
    print(f"Dano base: {baseDamage}")
    print(f"Nível: 0")
    print(f"XP: 0")
    print(f"\n")
    print(f"\n")
    print(f"Força: {data[playerClass]['strength']}")
    print(f"Destreza: {data[playerClass]['dexterity']}")
    print(f"Constituição: {data[playerClass]['constitution']}")
    print(f"Inteligência: {data[playerClass]['intelligence']}")
    print(f"Sabedoria: {data[playerClass]['wisdom']}")
    print(f"Carisma: {data[playerClass]['charisma']}")
    print(f"\n")
    print(f"Sua aventura irá começar em: {dataWorld[playerStartPoint]['name']}")
    print(f"Sua arma favorita é: {playerFavoriteWeapon}")

    input("\nPressione Enter para continuar...")

    #Create World
    os.system("cls")
    print("CRIAÇÃO DE MUNDO")
    print("\nO último passo é decidir como vai ser o seu mundo!\n")
    worldName = input("Nome do Mundo (opcional, o padrão é Jarparur): ")
    worldPopulation = input("Quantidade de NPCs (caso deixe em branco, o padrão é sempre 1000): ")
    print("\nAgora irei processar todas as informações que você me deu, aguarde um momento...")

    iterateThis = 1000
    if worldName == "":
        worldName = "Jarparur"
    if worldPopulation == "":
        iterateThis = 1000
    else:
        iterateThis = int(worldPopulation)
    npcData = {}
    ids = []

    def genId():
        newId = uuid.uuid4().int
        while newId in ids:
            newId = uuid.uuid4().int
        ids.append(newId)
        return newId

    def genName(gend):
        if gend == "M":
            return names.get_first_name(gender="male")
        else:
            return names.get_first_name(gender="female") 

    def defGend():
        poss = [random.random(), random.random()]

        if poss[0] > poss[1]:
            return "M"
        else:
            return "F"

    def defRace():
        poss = [random.random(), random.random(), random.random(), random.random(), random.random(), random.random(), random.random()]
        
        if max(poss) == poss[0]:
            return "human"
        elif max(poss) == poss[1]:
            return "dwarf"
        elif max(poss) == poss[2]:
            return "nulr"
        elif max(poss) == poss[3]:
            return "elf"
        elif max(poss) == poss[4]:
            return "woodElf"
        elif max(poss) == poss[5]:
            return "halfling"
        elif max(poss) == poss[6]:
            return "orc"
        else:
            return "human"

    def defClass(thisRace):
        humanClasses = ["warrior", "ranger", "wizard", "assassin", "cleric", "barbarian", "druid", "paladin", "bard", "monk"]
        dwarfClasses = ["warrior", "paladin", "barbarian"]
        nulrClasses = ["warrior", "ranger", "bjoretNen", "druid", "bard", "barbarian"]
        elfClasses = ["cleric", "ranger", "wizard", "bard"]
        woodElfClasses = ["ranger", "assassin", "druid", "monk"]
        halflingClasses = ["bard", "cleric"]
        orcClasses = ["barbarian", "warrior", "druid"]
        allClasses = ["warrior", "ranger", "wizard", "bjoretNen", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]

        if thisRace == "human":
            return random.choice(humanClasses)
        elif thisRace == "dwarf":
            return random.choice(dwarfClasses)
        elif thisRace == "nulr":
            return random.choice(nulrClasses)
        elif thisRace == "elf":
            return random.choice(elfClasses)
        elif thisRace == "woodElf":
            return random.choice(woodElfClasses)
        elif thisRace == "halfling":
            return random.choice(halflingClasses)
        elif thisRace == "orc":
            return random.choice(orcClasses)
        else:
            return random.choice(allClasses)

    def defLanguage(thisRace):
        nulrfangheRaces = ["nulr"]
        espocioComumRaces = ["human", "dwarf", "halfling", "elf"]
        espocioAntigoRaces = ["orc", "woodElf"]

        if thisRace in nulrfangheRaces:
            return "nulrfanghe"
        elif thisRace in espocioComumRaces:
            return "espocioComum"
        elif thisRace in espocioAntigoRaces:
            return "espocioAntigo"
        else:
            return "espocioComum"

    def getHeight(thisRace):
        tall = ["orc", "woodElf"]
        medium = ["human", "elf", "nulr"]
        tiny = ["dwarf", "halfling"]

        if thisRace in tall:
            thisHeight = random.randint(190, 250)/100
            return thisHeight
        elif thisRace in medium:
            thisHeight = random.randint(150, 190)/100
            return thisHeight
        elif thisRace in tiny:
            thisHeight = random.randint(50, 150)/100
            return thisHeight
        else:
            thisHeight = random.randint(150, 180)/100
            return thisHeight

    def defHomeLand(thisRace):
        nulrRaces = ["nulr"]
        sulRaces = ["human", "woodElf", "dwarf", "halfling", "elf"]
        desertoDosOssosRaces = ["orc"]

        if thisRace in nulrRaces:
            return "nulr"
        elif thisRace in sulRaces:
            return "sul"
        elif thisRace in desertoDosOssosRaces:
            return "desertoDosOssos"
        else:
            return "sul"

    def defFavoriteWeapon(thisClass):
        poss = data[thisClass]["favoriteWeapons"]
        
        return random.choice(poss)

    def defSlots(thisClass, level):
        t4Weapons = {
            "warrior": data["items"]["t4Warrior"][7],
            "ranger": data["items"]["t4Ranger"][7],
            "wizard": data["items"]["t4Wizard"][7],
            "bjoretNen": data["items"]["t4BjoretNen"][7],
            "cleric": data["items"]["t4Cleric"][7],
            "assassin": data["items"]["t4Assassin"][7],
            "cleric": data["items"]["t4Cleric"][7],
            "paladin": data["items"]["t4Paladin"][7],
            "barbarian": data["items"]["t4Barbarian"][7],
            "druid": data["items"]["t4Druid"][7],
            "bard": data["items"]["t4Bard"][7],
            "monk": data["items"]["t4Monk"][7]
        }

        t3Weapons = {
            "warrior": data["items"]["t3Warrior"][7],
            "ranger": data["items"]["t3Ranger"][7],
            "wizard": data["items"]["t3Wizard"][7],
            "bjoretNen": data["items"]["t3BjoretNen"][7],
            "cleric": data["items"]["t3Cleric"][7],
            "assassin": data["items"]["t3Assassin"][7],
            "cleric": data["items"]["t3Cleric"][7],
            "paladin": data["items"]["t3Paladin"][7],
            "barbarian": data["items"]["t3Barbarian"][7],
            "druid": data["items"]["t3Druid"][7],
            "bard": data["items"]["t3Bard"][7],
            "monk": data["items"]["t3Monk"][7]
        }

        t2Weapons = {
            "warrior": data["items"]["t2Warrior"][7],
            "ranger": data["items"]["t2Ranger"][7],
            "wizard": data["items"]["t2Wizard"][7],
            "bjoretNen": data["items"]["t2BjoretNen"][7],
            "cleric": data["items"]["t2Cleric"][7],
            "assassin": data["items"]["t2Assassin"][7],
            "cleric": data["items"]["t2Cleric"][7],
            "paladin": data["items"]["t2Paladin"][7],
            "barbarian": data["items"]["t2Barbarian"][7],
            "druid": data["items"]["t2Druid"][7],
            "bard": data["items"]["t2Bard"][7],
            "monk": data["items"]["t2Monk"][7]
        }

        t1Weapons = {
            "warrior": data["items"]["t1Warrior"][7],
            "ranger": data["items"]["t1Ranger"][7],
            "wizard": data["items"]["t1Wizard"][7],
            "bjoretNen": data["items"]["t1BjoretNen"][7],
            "cleric": data["items"]["t1Cleric"][7],
            "assassin": data["items"]["t1Assassin"][7],
            "cleric": data["items"]["t1Cleric"][7],
            "paladin": data["items"]["t1Paladin"][7],
            "barbarian": data["items"]["t1Barbarian"][7],
            "druid": data["items"]["t1Druid"][7],
            "bard": data["items"]["t1Bard"][7],
            "monk": data["items"]["t1Monk"][7]
        }

        if level == 0:
            return t4Weapons[thisClass]
        elif level >= 1 and level <= 5:
            return t4Weapons[thisClass]
        elif level >= 6 and level <= 10:
            return t3Weapons[thisClass]
        elif level >= 11 and level <= 15:
            return t2Weapons[thisClass]
        elif level >= 16 and level <= 20:
            return t1Weapons[thisClass]

    def defArmor(thisTorso, thisLegs, thisFoot):
        finalArmor = 0

        if thisLegs != "":
            finalArmor += data["items"][thisTorso]["armor"] + data["items"][thisLegs]["armor"] + data["items"][thisFoot]["armor"]
        else:
            finalArmor += data["items"][thisTorso]["armor"] + data["items"][thisFoot]["armor"]

        return finalArmor

    def defItems(part, thisClass, level):
        tier4Parts = {
            "warrior":{
                "head": data['items']['t4Warrior'][0],
                "torso": data['items']['t4Warrior'][1],
                "legs": data['items']['t4Warrior'][2],
                "foot": data['items']['t4Warrior'][3],
                "arms": data['items']['t4Warrior'][4],
                "hands": data['items']['t4Warrior'][5]
            },

            "ranger":{
                "head": data['items']['t4Ranger'][0],
                "torso": data['items']['t4Ranger'][1],
                "legs": data['items']['t4Ranger'][2],
                "foot": data['items']['t4Ranger'][3],
                "arms": data['items']['t4Ranger'][4],
                "hands": data['items']['t4Ranger'][5]
            },

            "wizard":{
                "head": data['items']['t4Wizard'][0],
                "torso": data['items']['t4Wizard'][1],
                "legs": data['items']['t4Wizard'][2],
                "foot": data['items']['t4Wizard'][3],
                "arms": data['items']['t4Wizard'][4],
                "hands": data['items']['t4Wizard'][5]
            },

            "bjoretNen":{
                "head": data['items']['t4BjoretNen'][0],
                "torso": data['items']['t4BjoretNen'][1],
                "legs": data['items']['t4BjoretNen'][2],
                "foot": data['items']['t4BjoretNen'][3],
                "arms": data['items']['t4BjoretNen'][4],
                "hands": data['items']['t4BjoretNen'][5]
            },

            "assassin":{
                "head": data['items']['t4Assassin'][0],
                "torso": data['items']['t4Assassin'][1],
                "legs": data['items']['t4Assassin'][2],
                "foot": data['items']['t4Assassin'][3],
                "arms": data['items']['t4Assassin'][4],
                "hands": data['items']['t4Assassin'][5]
            },

            "cleric":{
                "head": data['items']['t4Cleric'][0],
                "torso": data['items']['t4Cleric'][1],
                "legs": data['items']['t4Cleric'][2],
                "foot": data['items']['t4Cleric'][3],
                "arms": data['items']['t4Cleric'][4],
                "hands": data['items']['t4Cleric'][5]
            },

            "paladin":{
                "head": data['items']['t4Paladin'][0],
                "torso": data['items']['t4Paladin'][1],
                "legs": data['items']['t4Paladin'][2],
                "foot": data['items']['t4Paladin'][3],
                "arms": data['items']['t4Paladin'][4],
                "hands": data['items']['t4Paladin'][5]
            },

            "barbarian":{
                "head": data['items']['t4Barbarian'][0],
                "torso": data['items']['t4Barbarian'][1],
                "legs": data['items']['t4Barbarian'][2],
                "foot": data['items']['t4Barbarian'][3],
                "arms": data['items']['t4Barbarian'][4],
                "hands": data['items']['t4Barbarian'][5]
            },

            "druid":{
                "head": data['items']['t4Druid'][0],
                "torso": data['items']['t4Druid'][1],
                "legs": data['items']['t4Druid'][2],
                "foot": data['items']['t4Druid'][3],
                "arms": data['items']['t4Druid'][4],
                "hands": data['items']['t4Druid'][5]
            },

            "bard":{
                "head": data['items']['t4Bard'][0],
                "torso": data['items']['t4Bard'][1],
                "legs": data['items']['t4Bard'][2],
                "foot": data['items']['t4Bard'][3],
                "arms": data['items']['t4Bard'][4],
                "hands": data['items']['t4Bard'][5]
            },

            "monk":{
                "head": data['items']['t4Monk'][0],
                "torso": data['items']['t4Monk'][1],
                "legs": data['items']['t4Monk'][2],
                "foot": data['items']['t4Monk'][3],
                "arms": data['items']['t4Monk'][4],
                "hands": data['items']['t4Monk'][5]
            }
        }
        tier3Parts = {
            "warrior":{
                "head": data['items']['t3Warrior'][0],
                "torso": data['items']['t3Warrior'][1],
                "legs": data['items']['t3Warrior'][2],
                "foot": data['items']['t3Warrior'][3],
                "arms": data['items']['t3Warrior'][4],
                "hands": data['items']['t3Warrior'][5]
            },

            "ranger":{
                "head": data['items']['t3Ranger'][0],
                "torso": data['items']['t3Ranger'][1],
                "legs": data['items']['t3Ranger'][2],
                "foot": data['items']['t3Ranger'][3],
                "arms": data['items']['t3Ranger'][4],
                "hands": data['items']['t3Ranger'][5]
            },

            "wizard":{
                "head": data['items']['t3Wizard'][0],
                "torso": data['items']['t3Wizard'][1],
                "legs": data['items']['t3Wizard'][2],
                "foot": data['items']['t3Wizard'][3],
                "arms": data['items']['t3Wizard'][4],
                "hands": data['items']['t3Wizard'][5]
            },

            "bjoretNen":{
                "head": data['items']['t3BjoretNen'][0],
                "torso": data['items']['t3BjoretNen'][1],
                "legs": data['items']['t3BjoretNen'][2],
                "foot": data['items']['t3BjoretNen'][3],
                "arms": data['items']['t3BjoretNen'][4],
                "hands": data['items']['t3BjoretNen'][5]
            },

            "assassin":{
                "head": data['items']['t3Assassin'][0],
                "torso": data['items']['t3Assassin'][1],
                "legs": data['items']['t3Assassin'][2],
                "foot": data['items']['t3Assassin'][3],
                "arms": data['items']['t3Assassin'][4],
                "hands": data['items']['t3Assassin'][5]
            },

            "cleric":{
                "head": data['items']['t3Cleric'][0],
                "torso": data['items']['t3Cleric'][1],
                "legs": data['items']['t3Cleric'][2],
                "foot": data['items']['t3Cleric'][3],
                "arms": data['items']['t3Cleric'][4],
                "hands": data['items']['t3Cleric'][5]
            },

            "paladin":{
                "head": data['items']['t3Paladin'][0],
                "torso": data['items']['t3Paladin'][1],
                "legs": data['items']['t3Paladin'][2],
                "foot": data['items']['t3Paladin'][3],
                "arms": data['items']['t3Paladin'][4],
                "hands": data['items']['t3Paladin'][5]
            },

            "barbarian":{
                "head": data['items']['t3Barbarian'][0],
                "torso": data['items']['t3Barbarian'][1],
                "legs": data['items']['t3Barbarian'][2],
                "foot": data['items']['t3Barbarian'][3],
                "arms": data['items']['t3Barbarian'][4],
                "hands": data['items']['t3Barbarian'][5]
            },

            "druid":{
                "head": data['items']['t3Druid'][0],
                "torso": data['items']['t3Druid'][1],
                "legs": data['items']['t3Druid'][2],
                "foot": data['items']['t3Druid'][3],
                "arms": data['items']['t3Druid'][4],
                "hands": data['items']['t3Druid'][5]
            },

            "bard":{
                "head": data['items']['t3Bard'][0],
                "torso": data['items']['t3Bard'][1],
                "legs": data['items']['t3Bard'][2],
                "foot": data['items']['t3Bard'][3],
                "arms": data['items']['t3Bard'][4],
                "hands": data['items']['t3Bard'][5]
            },

            "monk":{
                "head": data['items']['t3Monk'][0],
                "torso": data['items']['t3Monk'][1],
                "legs": data['items']['t3Monk'][2],
                "foot": data['items']['t3Monk'][3],
                "arms": data['items']['t3Monk'][4],
                "hands": data['items']['t3Monk'][5]
            }
        }
        tier2Parts = {
            "warrior":{
                "head": data['items']['t2Warrior'][0],
                "torso": data['items']['t2Warrior'][1],
                "legs": data['items']['t2Warrior'][2],
                "foot": data['items']['t2Warrior'][3],
                "arms": data['items']['t2Warrior'][4],
                "hands": data['items']['t2Warrior'][5]
            },

            "ranger":{
                "head": data['items']['t2Ranger'][0],
                "torso": data['items']['t2Ranger'][1],
                "legs": data['items']['t2Ranger'][2],
                "foot": data['items']['t2Ranger'][3],
                "arms": data['items']['t2Ranger'][4],
                "hands": data['items']['t2Ranger'][5]
            },

            "wizard":{
                "head": data['items']['t2Wizard'][0],
                "torso": data['items']['t2Wizard'][1],
                "legs": data['items']['t2Wizard'][2],
                "foot": data['items']['t2Wizard'][3],
                "arms": data['items']['t2Wizard'][4],
                "hands": data['items']['t2Wizard'][5]
            },

            "bjoretNen":{
                "head": data['items']['t2BjoretNen'][0],
                "torso": data['items']['t2BjoretNen'][1],
                "legs": data['items']['t2BjoretNen'][2],
                "foot": data['items']['t2BjoretNen'][3],
                "arms": data['items']['t2BjoretNen'][4],
                "hands": data['items']['t2BjoretNen'][5]
            },

            "assassin":{
                "head": data['items']['t2Assassin'][0],
                "torso": data['items']['t2Assassin'][1],
                "legs": data['items']['t2Assassin'][2],
                "foot": data['items']['t2Assassin'][3],
                "arms": data['items']['t2Assassin'][4],
                "hands": data['items']['t2Assassin'][5]
            },

            "cleric":{
                "head": data['items']['t2Cleric'][0],
                "torso": data['items']['t2Cleric'][1],
                "legs": data['items']['t2Cleric'][2],
                "foot": data['items']['t2Cleric'][3],
                "arms": data['items']['t2Cleric'][4],
                "hands": data['items']['t2Cleric'][5]
            },

            "paladin":{
                "head": data['items']['t2Paladin'][0],
                "torso": data['items']['t2Paladin'][1],
                "legs": data['items']['t2Paladin'][2],
                "foot": data['items']['t2Paladin'][3],
                "arms": data['items']['t2Paladin'][4],
                "hands": data['items']['t2Paladin'][5]
            },

            "barbarian":{
                "head": data['items']['t2Barbarian'][0],
                "torso": data['items']['t2Barbarian'][1],
                "legs": data['items']['t2Barbarian'][2],
                "foot": data['items']['t2Barbarian'][3],
                "arms": data['items']['t2Barbarian'][4],
                "hands": data['items']['t2Barbarian'][5]
            },

            "druid":{
                "head": data['items']['t2Druid'][0],
                "torso": data['items']['t2Druid'][1],
                "legs": data['items']['t2Druid'][2],
                "foot": data['items']['t2Druid'][3],
                "arms": data['items']['t2Druid'][4],
                "hands": data['items']['t2Druid'][5]
            },

            "bard":{
                "head": data['items']['t2Bard'][0],
                "torso": data['items']['t2Bard'][1],
                "legs": data['items']['t2Bard'][2],
                "foot": data['items']['t2Bard'][3],
                "arms": data['items']['t2Bard'][4],
                "hands": data['items']['t2Bard'][5]
            },

            "monk":{
                "head": data['items']['t2Monk'][0],
                "torso": data['items']['t2Monk'][1],
                "legs": data['items']['t2Monk'][2],
                "foot": data['items']['t2Monk'][3],
                "arms": data['items']['t2Monk'][4],
                "hands": data['items']['t2Monk'][5]
            }
        }
        tier1Parts = {
            "warrior":{
                "head": data['items']['t1Warrior'][0],
                "torso": data['items']['t1Warrior'][1],
                "legs": data['items']['t1Warrior'][2],
                "foot": data['items']['t1Warrior'][3],
                "arms": data['items']['t1Warrior'][4],
                "hands": data['items']['t1Warrior'][5]
            },

            "ranger":{
                "head": data['items']['t1Ranger'][0],
                "torso": data['items']['t1Ranger'][1],
                "legs": data['items']['t1Ranger'][2],
                "foot": data['items']['t1Ranger'][3],
                "arms": data['items']['t1Ranger'][4],
                "hands": data['items']['t1Ranger'][5]
            },

            "wizard":{
                "head": data['items']['t1Wizard'][0],
                "torso": data['items']['t1Wizard'][1],
                "legs": data['items']['t1Wizard'][2],
                "foot": data['items']['t1Wizard'][3],
                "arms": data['items']['t1Wizard'][4],
                "hands": data['items']['t1Wizard'][5]
            },

            "bjoretNen":{
                "head": data['items']['t1BjoretNen'][0],
                "torso": data['items']['t1BjoretNen'][1],
                "legs": data['items']['t1BjoretNen'][2],
                "foot": data['items']['t1BjoretNen'][3],
                "arms": data['items']['t1BjoretNen'][4],
                "hands": data['items']['t1BjoretNen'][5]
            },

            "assassin":{
                "head": data['items']['t1Assassin'][0],
                "torso": data['items']['t1Assassin'][1],
                "legs": data['items']['t1Assassin'][2],
                "foot": data['items']['t1Assassin'][3],
                "arms": data['items']['t1Assassin'][4],
                "hands": data['items']['t1Assassin'][5]
            },

            "cleric":{
                "head": data['items']['t1Cleric'][0],
                "torso": data['items']['t1Cleric'][1],
                "legs": data['items']['t1Cleric'][2],
                "foot": data['items']['t1Cleric'][3],
                "arms": data['items']['t1Cleric'][4],
                "hands": data['items']['t1Cleric'][5]
            },

            "paladin":{
                "head": data['items']['t1Paladin'][0],
                "torso": data['items']['t1Paladin'][1],
                "legs": data['items']['t1Paladin'][2],
                "foot": data['items']['t1Paladin'][3],
                "arms": data['items']['t1Paladin'][4],
                "hands": data['items']['t1Paladin'][5]
            },

            "barbarian":{
                "head": data['items']['t1Barbarian'][0],
                "torso": data['items']['t1Barbarian'][1],
                "legs": data['items']['t1Barbarian'][2],
                "foot": data['items']['t1Barbarian'][3],
                "arms": data['items']['t1Barbarian'][4],
                "hands": data['items']['t1Barbarian'][5]
            },

            "druid":{
                "head": data['items']['t1Druid'][0],
                "torso": data['items']['t1Druid'][1],
                "legs": data['items']['t1Druid'][2],
                "foot": data['items']['t1Druid'][3],
                "arms": data['items']['t1Druid'][4],
                "hands": data['items']['t1Druid'][5]
            },

            "bard":{
                "head": data['items']['t1Bard'][0],
                "torso": data['items']['t1Bard'][1],
                "legs": data['items']['t1Bard'][2],
                "foot": data['items']['t1Bard'][3],
                "arms": data['items']['t1Bard'][4],
                "hands": data['items']['t1Bard'][5]
            },

            "monk":{
                "head": data['items']['t1Monk'][0],
                "torso": data['items']['t1Monk'][1],
                "legs": data['items']['t1Monk'][2],
                "foot": data['items']['t1Monk'][3],
                "arms": data['items']['t1Monk'][4],
                "hands": data['items']['t1Monk'][5]
            }
        }

        if level == 0:
            return tier4Parts[thisClass][part]
        elif level >= 1 and level <= 5:
            return tier4Parts[thisClass][part]
        elif level >= 6 and level <= 10:
            return tier3Parts[thisClass][part]
        elif level >= 11 and level <= 15:
            return tier2Parts[thisClass][part]
        elif level >= 16 and level <= 20:
            return tier1Parts[thisClass][part]

    def defAttr(thisClass, level, thisAttr):
        attr = {
            "warrior": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level
            },

            "ranger": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level
            },

            "assassin": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level
            },

            "cleric": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level
            },

            "paladin": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level
            },

            "barbarian": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
            },

            "druid": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level
            },

            "monk": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level
            },

            "wizard": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level
            },

            "bjoretNen": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level
            },

            "bard": {
                "strength": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "constitution": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "dexterity": random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level,
                "intelligence": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "wisdom": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level,
                "charisma": random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level
            }
        }

        return attr[thisClass][thisAttr]

    # skill forte = random.randint(int(convertLevelToUpgradePoints(level, level-1)/2), int(convertLevelToUpgradePoints(level, level-1)) )+ data[thisClass]["strength"] * level

    # skill mediana = random.randint(int(convertLevelToUpgradePoints(level, level-1)/4), int(convertLevelToUpgradePoints(level, (level)-1)/2)) + data[thisClass]["strength"] * level

    # skill fraca = random.randint(int(convertLevelToUpgradePoints(level, level-1)/8), int(convertLevelToUpgradePoints(level, (level)-1)/4)) + data[thisClass]["strength"] * level

    npcData = {}

    while iterateThis > 0:
        thisId = str(genId())

        thisNpcData = {
            "name": "npcName", 
            "genre": "npcGenre", 
            "race": "npcRace", 
            "class": "npcClass",
            "language": "npcLanguage",
            "age": 0,
            "height": 0,

            "health": 0,
            "mana": 0,
            "armor": 0,

            "level": 1,
            "XP": 0,
            "mood": "npcMood",

            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,

            "homeLand": "npcHomeLand",
            "favoriteWeapon": "npcFavWeapon",

            "inventory": {
                "head": "",
                "torso": "npcTorso",
                "arms": "",
                "hands": "",
                "legs": "npcLegs",
                "foot": "npcFoot",

                "slots": ["npcStarterWeapon", "", "", "", "", "", "", ""],
                "bag": ["", "", ""]
            },

            "world": {
                "worldRegion": "npcHomeLand",
                "localRegion": "",
                "building": ""
            }
        }

        nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]

        thisNpcData["level"] = random.randint(0, 20)
        thisNpcData["genre"] = defGend()
        thisNpcData["name"] = genName(thisNpcData["genre"])
        thisNpcData["race"] = defRace()
        thisNpcData["class"] = defClass(thisNpcData["race"])
        thisNpcData["language"] = defLanguage(thisNpcData["race"])
        thisNpcData["age"] = random.randint(18, 50)
        thisNpcData["height"] = getHeight(thisNpcData["race"])
        thisNpcData["XP"] = convertLevelToXP(thisNpcData["level"])
        thisNpcData["mood"] = "Bem"

        if thisNpcData["level"] > 1:
            thisNpcData["constitution"] = defAttr(thisNpcData["class"], thisNpcData["level"], "constitution")
            thisNpcData["dexterity"] = defAttr(thisNpcData["class"], thisNpcData["level"], "dexterity")
            thisNpcData["strength"] = defAttr(thisNpcData["class"], thisNpcData["level"], "strength")
            thisNpcData["intelligence"] = defAttr(thisNpcData["class"], thisNpcData["level"], "intelligence")
            thisNpcData["wisdom"] = defAttr(thisNpcData["class"], thisNpcData["level"], "wisdom")
            thisNpcData["charisma"] = defAttr(thisNpcData["class"], thisNpcData["level"], "charisma")
        else:
            thisNpcData["constitution"] = int(data[thisNpcData["class"]]["constitution"])*thisNpcData["level"]+1
            thisNpcData["intelligence"] = int(data[thisNpcData["class"]]["intelligence"])*thisNpcData["level"]+1
            thisNpcData["dexterity"] = int(data[thisNpcData["class"]]["dexterity"])*thisNpcData["level"]+1
            thisNpcData["strength"] = int(data[thisNpcData["class"]]["strength"])*thisNpcData["level"]+1
            thisNpcData["wisdom"] = int(data[thisNpcData["class"]]["wisdom"])*thisNpcData["level"]+1
            thisNpcData["charisma"] = int(data[thisNpcData["class"]]["charisma"])*thisNpcData["level"]+1

        thisNpcData["homeLand"] = defHomeLand(thisNpcData["race"])
        thisNpcData["favoriteWeapon"] = defFavoriteWeapon(thisNpcData["class"])
        thisNpcData["inventory"]["head"] = defItems("head", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["torso"] = defItems("torso", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["legs"] = defItems("legs", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["arms"] = defItems("arms", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["hands"] = defItems("hands", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["foot"] = defItems("foot", thisNpcData["class"], thisNpcData["level"])
        thisNpcData["inventory"]["slots"][0] = defSlots(thisNpcData["class"], thisNpcData["level"])
        thisNpcData["health"] = int(thisNpcData["constitution"] * thisNpcData["level"])
        thisNpcData["mana"] = int(thisNpcData["intelligence"] * thisNpcData["level"])
        if thisNpcData["class"] in nonMagicalClasses:
            thisNpcData["armor"] = defArmor(thisNpcData["inventory"]["torso"], thisNpcData["inventory"]["legs"], thisNpcData["inventory"]["foot"])
        else:
            thisNpcData["armor"] = defArmor(thisNpcData["inventory"]["torso"], "", thisNpcData["inventory"]["foot"])
        thisNpcData["world"]["worldRegion"] = thisNpcData["homeLand"]

        npcData[thisId] = thisNpcData
        iterateThis -= 1

    dataWorld["globalTime"] = random.randint(157790000000, 631150000000)
    dataWorld["worldAge"] = convertTime(dataWorld["globalTime"])
    dataWorld["worldName"] = worldName

    populationCount = 0

    for npc in npcData:
        populationCount += 1
    
    dataWorld["worldPopulation"] = populationCount+1

    os.system("cls")
    print("Mundo gerado com sucesso!\n")
    input("Continuar...")

    #Update PROLOGO
    os.system("cls")
    print("SALVAR JOGO")

    print(art.characterFinal(playerName))

    saveName = input("\nNome do Save >>> ")

    prologo = prologue.Prologue(saveName, playerData, npcData, dataWorld)
    prologo.firstSave()
    prologo.prologueStart()