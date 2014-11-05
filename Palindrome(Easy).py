def isPalindrome(word):
    for i in range(0,len(word)//2):
        if(word[i].lower()!=word[len(word)-i-1].lower()):
            return False
    return True

print(isPalindrome("bolton"))
print(isPalindrome("boltonnotlob"))
print(isPalindrome("boltonotlob"))
print(isPalindrome("boltonNOTLOB"))
print(isPalindrome(""))
