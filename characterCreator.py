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

availabeRaces = ["1", "2", "3", "4", "5", "6", "7"]

availabeClasses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

availabeLanguages = ['1', '2', '3']

racesDict = {
    "1": "human",
    "2": "dwarf",
    "3": "nulr",
    "4": "elf",
    "5": "woodElf",
    "6": "halfling",
    "7": "orc"
}

classDict = {
    "1": "warrior",
    "2": "ranger",
    "3": "wizard",
    "4": "bjoretNen",
    "5": "assassin",
    "6": "cleric",
    "7o": "paladin",
    "8": "barbarian",
    "9": "bard",
    "10": "monk"
}

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
    #Update NOME
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print("\nBem-vindo aventureiro (ou aventureira)! Está pronto para adentrar no maravilhoso mundo de Japarur? Espero que sim, você não vai se arrepender!")

    #Nome
    print("\nPrimeiramente, você precisa dar um nome ao seu personagem.")

    print(dragonBeforeName)

    playerName = input("\nSeu nome: ")
    print("\nAgora, seu personagem precisa de um gênero.")
    playerGenre = input("\nSeu gênero [M/F]: ")

    while True:
        #Update RAÇA
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM\n")

        print(art.characterName(playerName))

        #Raça
        print(f"\nOk {playerName}, você tem um nome... mas oque você é? Digo, qual a sua raça. Sim, existem raças no mundo de Jarparur assim como em qualquer outro plano existencial, digo... RPG.\n")

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

        print("1 - Humano | 2 - Anão | 3 - Nulr | 4 - Elfo | 5 - Elfo da Floresta | 6 - Halfling | 7 - Orc")

        playerRace = input("\nSua raça: ")

        if playerRace in availabeRaces:
            playerRace = racesDict.get(playerRace)
            break
        else:
            #Update ERRO RAÇA
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("A Raça inserida não existe!")
            input("\nPressione Enter para continuar...")

    while True:
        #Update CLASSE
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM")

        print(dragonBeforeName)

        print(f"\nCerto, você se tornou um(a) {data[playerRace]['name']}, muito bom! Porque não escolher uma raça?\n")
        
        tableClasseData = [
            ['Classe', 'Descrição'],
            [data["warrior"]["name"], data["warrior"]["description"]],
            [data["ranger"]["name"], data["ranger"]["description"]],
            [data["wizard"]["name"], data["wizard"]["description"]],
            [data["bjoretNen"]["name"], data["bjoretNen"]["description"]],
            [data["assassin"]["name"], data["assassin"]["description"]],
            [data["cleric"]["name"], data["cleric"]["description"]],
            [data["paladin"]["name"], data["paladin"]["description"]],
            [data["barbarian"]["name"], data["barbarian"]["description"]],
            [data["bard"]["name"], data["bard"]["description"]],
            [data["monk"]["name"], data["monk"]["description"]]
        ]

        tableClasse = SingleTable(tableClasseData)
        tableClasse.inner_row_border = True

        print(tableClasse.table)

        print("1 - Guerreiro | 2 - Ranger | 3 - Mago | 4 - Bjoret-Nen | 5 - Assassino | 6 - Clérigo | 7 - Paladino | 8 - Bárbaro | 9 - Bardo | 10 - Monge")

        playerClass = input("\nSua classe: ")

        if playerClass in availabeClasses:
            playerClass = classDict.get(playerClass)
            break
        else:
            #Update ERRO CLASSE
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("A Classe inserida não existe!")
            input("\nPressione Enter para continuar...")

    while True:
        #Update LINGUAGEM
        os.system("cls")
        print("CRIAÇÃO DE NOVO PERSONAGEM")

        print(art.characterClass(playerClass))

        print(f"Vejamos, você é {playerName}, um(a) {data[playerRace]['name']} {data[playerClass]['name']}(a), até aqui, tudo parece perfeito, mas agora você deve escolher um idioma para o seu personagem.")

        tableLinguaData = [
            ['Idioma', 'Descrição'],
            [data["espocioComum"]["name"], data["espocioComum"]["description"]],
            [data["espocioAntigo"]["name"], data["espocioAntigo"]["description"]],
            [data["nulrfanghe"]["name"], data["nulrfanghe"]["description"]],
        ]

        tableLingua = SingleTable(tableLinguaData)
        tableLingua.inner_row_border = True

        print(tableLingua.table)
        print("1 - Espócio Comum | 2 - Espócio Antigo | 3 - Nulrfanghë")

        playerLanguage = input("\nSeu Idioma: ")

        if playerLanguage in availabeLanguages:
            playerLanguage = languagesDict.get(playerLanguage)
            break
        else:
            #Update ERRO CLASSE
            os.system("cls")
            print("CRIAÇÃO DE NOVO PERSONAGEM")

            print("O Idioma inserido não existe!")
            input("\nPressione Enter para continuar...")

    #Update IDADE
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print(f"\nCerto {playerName}, agora você fala {data[playerLanguage]['name']}, insira sua idade para fins... inúteis.\n")

    playerAge = input("Sua idade: ")

    #Update ALTURA
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print(art.characterAge(playerAge))

    print(f"\nOk {playerName}, a sua altura por favor.\n")

    playerHeight = input("Sua altura (em cm): ")

    #Update ARMA FAVORITA
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    print(f"\nEm Jarparur, você precisa se defender contra monstros e criaturas perigosas, para isso, você precisa de uma arma. Não, você não vai receber esta arma, mas quando encontrar, ela terá atributos melhores!\n")

    count = 0
    
    classFavoriteWeapons = data[playerClass]["favoriteWeapons"]
    tempChoice = ""

    for weapon in classFavoriteWeapons:
        print("-", weapon)

    print("\n")

    for weapon in classFavoriteWeapons:
        while tempChoice != "y" or tempChoice != "n":
            choice = input(f"{weapon} <- [y/n] ")

            if choice == "y":
                tempChoice = choice
                playerFavoriteWeapon = weapon
                break
            elif choice == "n":
                tempChoice = choice
                break
            else:
                continue

    #Update LOCAL DE INICIO
    os.system("cls")
    print("CRIAÇÃO DE NOVO PERSONAGEM")

    count = 0

    print(f"Certo {playerName}, você está pronto para entrar no mundo de Jarparur!\n")

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
    playerStartPoint = regionsDict.get(playerStartPoint)

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

    #Define Base ABILITIES
    if playerClass == "wizard":
        playerAbility1 = "111"
        playerAbility2 = "112"
    
    elif playerClass == "bjoretNen":
        playerAbility1 = "151"
        playerAbility2 = "152"
    
    else:
        playerAbility1 = ""
        playerAbility2 = ""


    playerData = {
        "playerName": f"{playerName}", #INPUT
        "playerGenre": f"{playerGenre}", #INPUT
        "playerRace": f"{playerRace}", #INPUT
        "playerClass": f"{playerClass}",
        "playerLanguage": f"{playerLanguage}", #INPUT
        "playerAge": int(playerAge), #INPUT
        "playerHeight": (int(playerHeight)/100), #INPUT

        "playerHealth": int(data[playerClass]['health']),
        "playerMana": int(data[playerClass]['mana']),
        "playerArmor": int(data[playerClass]['armor']),

        "playerLevel": 0,
        "upgradePoints": 0,
        "playerXP": 0,
        "playerMood": "Bem",
        
        "playerVelocity": int(data[playerClass]['velocity']),

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

            "slots": [f"{playerWeapon}", "", "", "", "", "", "", ""],
            "bag": ["", "", ""]
        },

        "playerAbilities": {
            "ability1": f"{playerAbility1}",
            "ability2": f"{playerAbility2}"
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
    print(f"Vida: {data[playerClass]['health']}")
    print(f"Mana: {data[playerClass]['mana']}")
    print(f"Armadura: {data[playerClass]['armor']}")
    print(f"Nível: 1")
    print(f"XP: 0")
    print(f"\n")
    print(f"Velocidade: {data[playerClass]['velocity']}")
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
        nulrfangheRaces = ["nulr", "elf"]
        espocioComumRaces = ["human", "dwarf", "halfling"]
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
        nulrRaces = ["nulr", "elf"]
        sulRaces = ["human", "woodElf", "dwarf", "halfling"]
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

    def defTorsoItem(thisClass):
        nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]
        meeleeClasses = ["warrior", "paladin"]
        rangedClasses = ["ranger", "druid"]

        if thisClass in nonMagicalClasses:
            return "401"
        else:
            return "5111"

    def defLegsItem(thisClass):
        nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]
        meeleeClasses = ["warrior", "paladin"]
        rangedClasses = ["ranger", "druid"]

        if thisClass in nonMagicalClasses:
            return "402"
        else:
            return ""

    def defFootItem(thisClass):
        nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]
        meeleeClasses = ["warrior", "paladin"]
        rangedClasses = ["ranger", "druid"]

        if thisClass in nonMagicalClasses:
            return "501"
        else:
            return "501"

    # #Define Base ABILITIES
    # if thisClass == "wizard":
    #     playerAbility1 = "111"
    #     playerAbility2 = "112"
    
    # elif thisClass == "bjoretNen":
    #     playerAbility1 = "151"
    #     playerAbility2 = "152"
    
    # else:
    #     playerAbility1 = ""
    #     playerAbility2 = ""

    def defSlots(thisClass):
        nonMagicalClasses = ["warrior", "ranger", "assassin", "cleric", "paladin", "barbarian", "druid", "bard", "monk"]
        meeleeClasses = ["warrior", "paladin"]
        rangedClasses = ["ranger", "druid"]

        if thisClass in meeleeClasses:
            return "101"
        elif thisClass in rangedClasses:
            return "301"
        elif thisClass == "wizard":
            return "6111"
    
        elif thisClass == "bjoretNen":
            return "6151"
        
        elif thisClass == "assassin":
            return "102"
        
        elif thisClass == "barbarian":
            return "201"

        elif thisClass == "bard":
            return "6112"
        else:
            return "203"

    def defAbility1(thisClass):
        if thisClass == "wizard":
            return "111"
        elif thisClass == "bjoretNen":
            return "151"
        else:
            return ""
    
    def defAbility2(thisClass):
        if thisClass == "wizard":
            return "112"
        elif thisClass == "bjoretNen":
            return "152"
        else:
            return ""

    # "name": "npcName", 
    # "genre": "npcGenre", 
    # "race": "npcRace", 
    # "class": "npcClass",
    # "language": "npcLanguage",
    # "age": 0,
    # "height": 0,

    # "health": 0,
    # "mana": 0,
    # "armor": 0,

    # "level": 1,
    # "XP": 0,
    # "mood": "npcMood",
    
    # "velocity": 0,

    # "strength": 0,
    # "dexterity": 0,
    # "constitution": 0,
    # "intelligence": 0,
    # "wisdom": 0,
    # "charisma": 0,

    # "homeLand": "npcHomeLand",
    # "favoriteWeapon": "npcFavWeapon",

    # "inventory": {
    #     "head": f"",
    #     "torso": "npcTorso",
    #     "arms": "",
    #     "hands": "",
    #     "legs": "npcLegs",
    #     "foot": "npcFoot",

    #     "slots": ["npcStarterWeapon", "", "", "", "", "", "", ""],
    #     "bag": ["", "", ""]
    # },

    # "abilities": {
    #     "ability1": "npcStarterAbility1",
    #     "ability2": f"npcStarterAbility2"
    # },

    # "world": {
    #     "worldRegion": "npcHomeLand",
    #     "localRegion": "",
    #     "building": ""
    # }

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
            
            "velocity": 0,

            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,

            "homeLand": "npcHomeLand",
            "favoriteWeapon": "npcFavWeapon",

            "inventory": {
                "head": f"",
                "torso": "npcTorso",
                "arms": "",
                "hands": "",
                "legs": "npcLegs",
                "foot": "npcFoot",

                "slots": ["npcStarterWeapon", "", "", "", "", "", "", ""],
                "bag": ["", "", ""]
            },

            "abilities": {
                "ability1": "npcStarterAbility1",
                "ability2": f"npcStarterAbility2"
            },

            "world": {
                "worldRegion": "npcHomeLand",
                "localRegion": "",
                "building": ""
            }
        }

        thisNpcData["genre"] = defGend()
        thisNpcData["name"] = genName(thisNpcData["genre"])
        thisNpcData["race"] = defRace()
        thisNpcData["class"] = defClass(thisNpcData["race"])
        thisNpcData["language"] = defLanguage(thisNpcData["race"])
        thisNpcData["age"] = int(random.random()*100)
        thisNpcData["height"] = getHeight(thisNpcData["race"])
        thisNpcData["health"] = int(data[thisNpcData["class"]]["health"])
        thisNpcData["mana"] = int(data[thisNpcData["class"]]["mana"])
        thisNpcData["armor"] = int(data[thisNpcData["class"]]["armor"])
        thisNpcData["level"] = 1
        thisNpcData["XP"] = 0
        thisNpcData["mood"] = "Bem"
        thisNpcData["velocity"] = int(data[thisNpcData["class"]]["velocity"])
        thisNpcData["dexterity"] = int(data[thisNpcData["class"]]["dexterity"])
        thisNpcData["constitution"] = int(data[thisNpcData["class"]]["constitution"])
        thisNpcData["intelligence"] = int(data[thisNpcData["class"]]["intelligence"])
        thisNpcData["wisdom"] = int(data[thisNpcData["class"]]["wisdom"])
        thisNpcData["charisma"] = int(data[thisNpcData["class"]]["charisma"])
        thisNpcData["homeLand"] = defHomeLand(thisNpcData["race"])
        thisNpcData["favoriteWeapon"] = defFavoriteWeapon(thisNpcData["class"])
        thisNpcData["inventory"]["torso"] = defTorsoItem(thisNpcData["class"])
        thisNpcData["inventory"]["legs"] = defLegsItem(thisNpcData["class"])
        thisNpcData["inventory"]["foot"] = defFootItem(thisNpcData["class"])
        thisNpcData["inventory"]["slots"][0] = defSlots(thisNpcData["class"])
        thisNpcData["abilities"]["ability1"] = defAbility1(thisNpcData["class"])
        thisNpcData["abilities"]["ability2"] = defAbility2(thisNpcData["class"])
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