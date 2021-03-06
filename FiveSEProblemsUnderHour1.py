"""
Courtesy of: https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
"""

def forLooping(listy):
	ret = 0
	for e in listy:
		ret+=e
	return ret

def looping(listy):
	ret = 0
	while len(listy)>0:
		ret+=listy.pop()
	return ret

def recursive(listy):
	if(len(listy)<=0):
		return 0
	return listy.pop()+recursive(listy)

a = [1, 2, 3, 4, 5, 6]
print(forLooping(a))
a = [1, 2, 3, 4, 5, 6]
print(looping(a))
a = [1, 2, 3, 4, 5, 6]
print(recursive(a))
