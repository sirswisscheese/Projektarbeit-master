from datetime import datetime
import json
DATEI_NAME = "aktivitaeten.json"


def speichern(datei, key, value):
    try:
        with open(datei, "r+") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w+") as open_file:
        json.dump(datei_inhalt, open_file)


def aktivitaet_speichern(aktivitaet):
    zeitpunkt = datetime.now()
    speichern(DATEI_NAME, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet


def aktivitaeten_laden():

    try:
        with open(DATEI_NAME, "r+") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt
