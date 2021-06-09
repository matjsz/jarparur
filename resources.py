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