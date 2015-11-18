"""
Courtesy of: https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
"""

def largeCombo(listy):
    stringed = ''
    for i in listy:
        stringed += str(i)
    newListy = []
    for i in stringed:
        newListy.append(int(i))
    newListy.sort()
    stringed = ''
    for i in newListy[::-1]:
        stringed += str(i)
    return int(stringed)

print(largeCombo([1, 2, 4, 9, 1, 2]))
