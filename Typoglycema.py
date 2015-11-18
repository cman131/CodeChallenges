import random

def typoglycemasize(sentence):
	parted = sentence.split(' ')
	for i in range(len(parted)):
		if(len(parted[i]) <= 3):
			continue
		begin = parted[i][0]
		mid = list(parted[i][1:-1])
		random.shuffle(mid)
		mid = ''.join(mid)
		end = parted[i][-1]
		parted[i] = begin+mid+end
	return ' '.join(parted)
	
print(typoglycemasize(input('Gimme a sentence: ')))