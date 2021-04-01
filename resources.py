import json

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