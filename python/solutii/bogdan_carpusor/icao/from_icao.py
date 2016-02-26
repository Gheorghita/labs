#!/usr/bin/env python
# *-* coding: UTF-8 *-*
"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuviânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""
# pylint: disable=unused-argument
from __future__ import print_function

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}

def readFile(filePath):
    """Functia primeste citeste un fisier
    si returneaza continutul fisierului respectv
    """
    try:
        inputFile = open(filePath)
        message = inputFile.read()
        inputFile.close()
    except IOError:
        print ("Could not open file")
        return

    return message

def din_icao(mesaj):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    message = readFile(mesaj)
    wordsList = []
    wordLines = message.splitlines()
    invertedDictionary = {value: key for key, value in ICAO.items()}
    del (wordLines[-1])
    for line in wordLines:
        words = line.split(" ")
        tempList = [ invertedDictionary[word] \
                        for word in words ]

        wordsList.append("".join(tempList))
        wordsList.append(" ")
    decodedMessage = "".join(wordsList)

    fileOutput = open("icao.intrare", "w+")
    fileOutput.write(decodedMessage)
    fileOutput.close()

if __name__ == "__main__":
    din_icao("../../../date_intrare/mesaj.icao")
