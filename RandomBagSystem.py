from random import shuffle
from copy import copy

def getPieces(pieces):
    base = ['O','I','S','Z','L','J','T']
    resultingBag = ""
    while pieces>0:
        if len(currentBag)<1:
            currentBag = copy(base)
            shuffle(currentBag)
        pieces-=1
        resultingBag += currentBag.pop()
    return resultingBag
print(getPieces(50))
