"""
Courtesy of: https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
"""

def printFib(n):
    a = 0
    b = 1
    print(a)
    if n==1:
        return True
    print(b)
    if n==2:
        return True
    for i in range(3, n+1):
        print(a+b)
        c = a
        a = b
        b = c + b
printFib(100)
