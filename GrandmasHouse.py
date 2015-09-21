# From: https://www.reddit.com/r/dailyprogrammer/comments/3l61vx/20150916_challenge_232_intermediate_where_should/

import math

def getDistance(pos1, pos2):
	return math.fabs(pos1[0]-pos2[0]) + math.fabs(pos1[1]-pos2[1]);

def findClosest(positions):
	closest = (positions[0],positions[1])
	for position1 in positions:
		for position2 in positions:
			if(position1==position2):
				continue
			if(getDistance(closest[0], closest[1]) > getDistance(position1, position2)):
				closest = (position1, position2)
	return closest

file = open(input('Filename: '))
shouldIgnore = True
positions=[]
for line in file:
	if(shouldIgnore):
		shouldIgnore = False
		continue
	val = line.split('(')[1].split(')')[0].split(', ')
	positions.append([float(val[0]), float(val[1])])
print(findClosest(positions))
