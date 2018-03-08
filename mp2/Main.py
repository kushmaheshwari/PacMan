from smartManufacturing import *
from queue import *

def maxLetter(letterA, letterB, letterC, letterD, letterE):
    letterDict = {}
    letterDict['A'] = letterA
    letterDict['B'] = letterB
    letterDict['C'] = letterC
    letterDict['D'] = letterD
    letterDict['E'] = letterE

    return max(letterDict, key=letterDict.get)

def partOne():
    data = smartManufacturing()
    path = []
    val = 13
    
    while (val > 0):
    
        letterA = 0
        letterB = 0
        letterC = 0
        letterD = 0
        letterE = 0
        
        for item in data.widgets:
            if len(item) != 0:
            #np.delete(widgets, item)
            #else:
                character = item.pop()
                if (character == 'A'):
                    letterA += 1
                if (character == 'B'):
                    letterB += 1
                if (character == 'C'):
                    letterC += 1
                if (character == 'D'):
                    letterD += 1
                if (character == 'E'):
                    letterE += 1
                item.append(character)

        toPop = maxLetter(letterA, letterB, letterC, letterD, letterE)
        path.append(toPop)
        
        for item in data.widgets:
            if len(item) > 0:
                character = item.pop()
                if (character != toPop):
                    item.append(character)
        val = val - 1

    print(path)
        

    return path

if __name__ == "__main__":
    partOne()
