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
