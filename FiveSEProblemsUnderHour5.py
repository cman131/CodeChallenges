"""
Courtesy of: https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
"""

import copy

def combineToValue(n, listy, cur=""):
	if len(listy) <= 0:
		return [cur] if eval(cur) == n else []
	elif(len(listy) == 1):
		return [cur+str(listy[0])] if eval(cur+str(listy[0])) == n else []
	thisVal = str(listy.pop(0))
	l1 = combineToValue(n, copy.deepcopy(listy), cur + thisVal + '+')
	l2 = combineToValue(n, copy.deepcopy(listy), cur + thisVal + '-')
	l1.extend(l2)
	return l1

print(combineToValue(96, [1,2,34,5,67,8,9]))
