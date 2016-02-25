#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""Tuxy dorește să împlementeze un nou paint pentru consolă.

În timpul dezvoltării proiectului s-a izbit de o problemă
pe care nu o poate rezolva singur și a apelat la ajutorul tău.

Aplicația ține un istoric al tuturor mișcărilor pe care le-a
făcut utlizatorul în fișierul istoric.tuxy

Exemplu de istoric.tuxy:

    STÂNGA 2
    JOS 2
    DREAPTA 5

Fișierul de mai sus ne spune că utilizatorul a mutat cursorul
2 căsuțe la stânga după care 2 căsuțe in jos iar ultima acțiune
a fost să poziționeze cursorul cu 5 căsuțe în dreapta față de
ultima poziție.

El dorește un utilitar care să îi spună care este distanța dintre
punctul de origine (0, 0) și poziția curentă a cursorului.
"""
from __future__ import print_function
import math
from copy import deepcopy

def readFile(filePath):
     try:
         inputFile = open(filePath)
         textContent = inputFile.read()
         inputFile.close()
     except IOError:
         print ("Can not read from file")
	 raise Exception("No file found")
         return
     return textContent

def parseFile(line, position):
    movement = line.split(" ")
    if movement[0] == "SUS":
        position["x"] += float(movement[1])
    elif movement[0] == "JOS":
        position["x"] -= float(movement[1])
    elif movement[0] == "STANGA":
        position["y"] -= float(movement[1])
    elif movement[0] == "DREAPTA":
        position["y"] += float(movement[1])
    else:
        print( "Incorrect input")
        exit

def distanta():
    """
    Calculează distanța dintre origine și poziția curentă.

    Funcția citește conținutul fișierului istoric.tuxy și
    calculează distanța dintre punctul de origine și poziția
    curentă a cursorului.
    """
    origin = { "x": 0.0, "y": 0.0}
    currentPosition = deepcopy(origin)

    try:
    	textContent = readFile("../../../date_intrare/istoric.tuxy")
    except Exception as error:
	print (repr(error))
	return

    for fileLine in textContent.splitlines():
        parseFile(fileLine, currentPosition)

    print ("Final position: %d %d" % (currentPosition["x"], currentPosition["y"]))
    print ("Starting position: %d %d" % (origin["x"], origin["y"]))
    distance = math.sqrt(
               (origin["x"] - currentPosition["x"])**2 + \
               (origin["y"] - currentPosition["y"])**2 \
               )
    print ("Distance between points: %d" % (distance))

if __name__ == "__main__":
    distanta()
