import saveSystem
import os
import json
import prologue
import art
from terminaltables import SingleTable
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
        "playerRace": f"{playerRace}", #INPUT
        "playerClass": f"{playerClass}",
        "playerLanguage": f"{playerLanguage}", #INPUT
        "playerAge": int(playerAge), #INPUT
        "playerHeight": (int(playerHeight)/100), #INPUT

        "playerHealth": int(data[playerClass]['health']),
        "playerMana": int(data[playerClass]['mana']),
        "playerArmor": int(data[playerClass]['armor']),

        "playerLevel": 1,
        "playerXP": 0,
        
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
        }
    }

    #Update FINAL
    os.system("cls")
    print("PERSONAGEM CRIADO COM SUCESSO!")

    print(f"\nPERSONAGEM: {playerName}")
    print(f"------------------------------/")
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

    #Update PROLOGO
    os.system("cls")
    print("SALVAR JOGO")

    print(art.characterFinal(playerName))

    saveName = input("\nNome do Save >>> ")

    prologo = prologue.Prologue(saveName, playerData)
    prologo.firstSave()
    prologo.prologueStart()