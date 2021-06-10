import json
import random

with open(f'gameData.json', encoding='utf-8') as jf:
    data = json.load(jf)

with open(f'worldData.json', encoding='utf-8') as wf:
    dataWorld = json.load(wf)

racesDict = {
    "humano": "human",
    "elfo": "elf",
    "elfo da floresta": "woodElf",
    "anão": "dwarf",
    "nulr-nen": "nurl",
    "halfling": "halfling",
    "orc": "orc"
}

classDict = {
    "guerreiro": "warrior",
    "ranger": "ranger",
    "mago": "wizard",
    "bjoret-nen": "bjoretNen",
    "bjoret": "bjoretNen",
    "assassino": "assassin",
    "clérigo": "cleric",
    "clerigo": "cleric",
    "paladino": "paladin",
    "bárbaro": "barbarian",
    "barbaro": "barbarian"
}

itemsDict = {
    "Espada de Bronze": "101",
    "Arco de Caça": "301",
    "Tomo de Feitiços de Iniciante": "6111",
    "Raíz de Fullarët": "6151",
    "Adaga Cega": "102",
    "Martelo de Pedra": "201",
    "Machado de Ossos": "202",
    "Banjo com Pérolas": "6112",
    "Bastão de Madeira": "203",
    "Armadura de Couro": "401",
    "Robe de Mago Iniciante": "5111",
    "Calças de Couro": "402",
    "Botas Básicas": "501"
}

def convertRace(raceToConvert):
    return racesDict.get(raceToConvert)

def convertClass(classToConvert):
    return classDict.get(classToConvert)

def convertItem(itemToConvert):
    return itemsDict.get(itemToConvert)

def deconvertRace(raceToConvert):
    return data[raceToConvert]["name"]

def deconvertClass(classToConvert):
    return data[classToConvert]["name"]

def deconvertItem(itemToConvert):
    return data["items"][itemToConvert]["name"]

def plural(n, word):
    if n == 1:
        return '%d %s' % (n, word)
    return '%d %ss' % (n, word)

def convertTime(seconds):
    if seconds == 0:
        return "agora"
    
    oneMinute = 60
    oneHour = 60 * oneMinute
    oneDay = 24 * oneHour
    oneYear = 365 * oneDay

    timeUnits = (
        (oneYear, 'ano'),
        (oneDay, 'dia'),
        (oneHour, 'hora'),
        (oneMinute, 'minuto'),
        (1, 'segundo')
    )

    result = []

    for unit in timeUnits:
        timeUnit, word = unit
        if seconds >= timeUnit:
            n = int(seconds / timeUnit)
            result.append(plural(n, word))
            seconds -= n * timeUnit
    return ' e'.join(', '.join(result).rsplit(',', 1))

def convertCalendar(seconds):
    if seconds == 0:
        return "agora"
    
    oneMinute = 60
    oneHour = 60 * oneMinute
    oneDay = 24 * oneHour
    oneYear = 365 * oneDay

    timeUnits = (
        (oneYear, 'ano'),
        (oneDay, 'dia'),
        (oneHour, 'hora'),
        (oneMinute, 'minuto'),
        (1, 'segundo')
    )

    result = []

    for unit in timeUnits:
        timeUnit, word = unit
        if seconds >= timeUnit:
            n = int(seconds / timeUnit)
            if word == "dia":
                result.append(f"{word} {n}")
            elif word == "ano":
                result.append(f"{word} {n}")
            elif word == "hora":
                result.append(plural(n, word))
            elif word == "minuto":
                result.append(plural(n, word))
            elif word == "segundo":
                result.append(plural(n, word))
            seconds -= n * timeUnit
    return ','.join(', '.join(result).rsplit(',', 1))

def convertXPToLevel(xp, level):
    experienceToLevel = {
        0: 0,
        100: 1,
        250: 2,
        500: 3,
        800: 4,
        1100: 5,
        1500: 6,
        1800: 7,
        2000: 8,
        2500: 9,
        3000: 10,
        3600: 11,
        4200: 12,
        5000: 13,
        5800: 14,
        6500: 15,
        7500: 16,
        8500: 17,
        10000: 18,
        15000: 19,
        30000: 20
    }

    levelsToUp = 0

    experience = [0, 100, 250, 500, 800, 1100, 1500, 1800, 2000, 2500, 3000, 3600, 4200, 5000, 6500, 7500, 8500, 10000, 15000, 30000]

    if xp not in experienceToLevel:
        for exp in experience:
            if xp > exp and experience.index(exp)+1 > level:
                levelsToUp += 1
        return levelsToUp
    if xp in experienceToLevel:
        return experienceToLevel[xp] - level

def convertLevelToXP(level):
    levelToExperience = {
        0: 0,
        1: 100,
        2: 250,
        3: 500,
        4: 800,
        5: 1100,
        6: 1500,
        7: 1800,
        8: 2000,
        9: 2500,
        10: 3000,
        11: 3600,
        12: 4200,
        13: 5000,
        14: 5800,
        15: 6500,
        16: 7500,
        17: 8500,
        18: 10000,
        19: 15000,
        20: 30000
    }

    return levelToExperience[level]

def seeIfLevelUp(xp, level):
    experience = [0, 100, 250, 500, 800, 1100, 1500, 1800, 2000, 2500, 3000, 3600, 4200, 5000, 6500, 7500, 8500, 10000, 15000, 30000]

    if xp in experience:
        return True
    else:
        for exp in experience:
            if xp > exp and experience.index(exp) > level:
                return True
        return False

def convertLevelToUpgradePoints(level, previousLevel):
    levelToUpgradePoints = {
        0: 1,
        1: 1,
        2: 1,
        3: 2,
        4: 2,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 3,
        10: 3,
        11: 3,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 5,
        17: 5,
        18: 5,
        19: 5,
        20: 5
    }

    if level - previousLevel == 1:
        return levelToUpgradePoints[level]
    else:
        count = level - previousLevel
        points = 0
        while count > 0:
            points += levelToUpgradePoints[previousLevel+count]
            count -= 1
        return points

def convertLevelToTitle(level, thisClass):
    realMagicalClasses = ["bjoretNen"]
    arcaneMagicalClasses = ["wizard", "bard"]
    supportiveClasses = ["cleric", "paladin"]
    meeleeClasses = ["warrior", "monk", "assassin", "barbarian"]
    rangedClasses = ["ranger", "druid"]

    levelToTitle = {}

    if thisClass in realMagicalClasses:
        # Mágico (Real):
        # 18 - Lenda
        # 17 - Ascendido
        # 16 - Iluminado
        # 15 - Fraco
        
        levelToTitle = {
            0: "Novato",
            1: "Fraco",
            2: "Fraco",
            3: "Fraco",
            4: "Fraco",
            5: "Fraco",
            6: "Iluminado",
            7: "Iluminado",
            8: "Iluminado",
            9: "Iluminado",
            10: "Iluminado",
            11: "Ascendido",
            12: "Ascendido",
            13: "Ascendido",
            14: "Ascendido",
            15: "Ascendido",
            16: "Lenda",
            17: "Lenda",
            18: "Lenda",
            19: "Lenda",
            20: "Lenda"
        }
    
    elif thisClass in arcaneMagicalClasses:
        # Mágico (Arcano):
        # 14 - Mestre
        # 13 - Perito
        # 12 - Experiente
        # 11 - Iniciante

        levelToTitle = {
            0: "Novato",
            1: "Iniciante",
            2: "Iniciante",
            3: "Iniciante",
            4: "Iniciante",
            5: "Iniciante",
            6: "Experiente",
            7: "Experiente",
            8: "Experiente",
            9: "Experiente",
            10: "Experiente",
            11: "Perito",
            12: "Perito",
            13: "Perito",
            14: "Perito",
            15: "Perito",
            16: "Mestre",
            17: "Mestre",
            18: "Mestre",
            19: "Mestre",
            20: "Mestre"
        }

    elif thisClass in supportiveClasses:
        # Suporte
        # 1 - Bastião da Justiça
        # 2 - Defensor
        # 3 - Protetor
        # 4 - Ajudante

        levelToTitle = {
            0: "Novato",
            1: "Ajudante",
            2: "Ajudante",
            3: "Ajudante",
            4: "Ajudante",
            5: "Ajudante",
            6: "Protetor",
            7: "Protetor",
            8: "Protetor",
            9: "Protetor",
            10: "Protetor",
            11: "Defensor",
            12: "Defensor",
            13: "Defensor",
            14: "Defensor",
            15: "Defensor",
            16: "Bastião da Justiça",
            17: "Bastião da Justiça",
            18: "Bastião da Justiça",
            19: "Bastião da Justiça",
            20: "Bastião da Justiça"
        }

    elif thisClass in meeleeClasses:
        # Corpo a Corpo:
        # 1 - Lendário
        # 8 - Herói
        # 4 - Aventureiro
        # 0 - Iniciante

        levelToTitle = {
            0: "Novato",
            1: "Iniciante",
            2: "Iniciante",
            3: "Iniciante",
            4: "Iniciante",
            5: "Iniciante",
            6: "Aventureiro",
            7: "Aventureiro",
            8: "Aventureiro",
            9: "Aventureiro",
            10: "Aventureiro",
            11: "Herói",
            12: "Herói",
            13: "Herói",
            14: "Herói",
            15: "Herói",
            16: "Lendário",
            17: "Lendário",
            18: "Lendário",
            19: "Lendário",
            20: "Lendário"
        }

    elif thisClass in rangedClasses:
        # A distancia:
        # 1 - Lendário
        # 2 - Águia
        # 3 - Caçador
        # 4 - Iniciante

        levelToTitle = {
            0: "Novato",
            1: "Iniciante",
            2: "Iniciante",
            3: "Iniciante",
            4: "Iniciante",
            5: "Iniciante",
            6: "Caçador",
            7: "Caçador",
            8: "Caçador",
            9: "Caçador",
            10: "Caçador",
            11: "Águia",
            12: "Águia",
            13: "Águia",
            14: "Águia",
            15: "Águia",
            16: "Lendário",
            17: "Lendário",
            18: "Lendário",
            19: "Lendário",
            20: "Lendário"
        }

    return levelToTitle[level]