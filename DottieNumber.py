import math

origin = input('Please input a number: ')
keepLooping = True
while(keepLooping):
    try:
        origin = float(origin)
        keepLooping = False
    except:
        origin = input('I\'m sorry, but it must be a number.')

current = math.cos(origin)
previous = origin
while(current != previous):
    previous = current
    current = math.cos(current)
print('The resulting Dottie Number of', origin, 'is', current)
