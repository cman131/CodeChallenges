def alternate(l1, l2):
	ret = []
	bool = True
	while len(l1)>0 or len(l2)>0:
		if(len(l1)<=0):
			ret.append(l2.pop(0))
		elif(len(l2)<=0):
			ret.append(l1.pop(0))
		elif bool:
			ret.append(l1.pop(0))
			bool = False
		else:
			ret.append(l2.pop(0))
			bool = True
	return ret
print(alternate([1,2,3,4,5], [1,2,3,4,5]))