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
