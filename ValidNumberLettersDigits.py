def getValidLetters(digits):
    valid = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z'}
    mapping = {}
    for i in range(len(digits)):
        sin = digits[i]
        doub = sin
        if i+1 < len(digits):
            doub = digits[i:i+2]
        if str(sin) in valid:
            mapping[valid[sin]] = True
        if str(doub) in valid:
            mapping[valid[doub]] = True
    return list(mapping.keys())
def getValidLetterCount(digits):
    return len(getValidLetters(digits))

digits = input('Give me a string of digits: ')

print(getValidLetters(digits))
print(getValidLetterCount(digits))
