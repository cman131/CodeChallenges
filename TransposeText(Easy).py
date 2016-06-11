def getDimensions(arr):
	temp = len(arr)
	for i in arr:
		temp = temp if temp > len(i) else len(i)
	return temp

def transposeMe(arr):
	arr = arr.split("\n")
	newArr = []
	dim = getDimensions(arr)
	for i in range(dim):
		newArr.append([])
		if i<len(arr):
			arr[i] = list(arr[i])
		for j in range(len(arr)):
			newArr[i].append(" ")
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			newArr[j][len(arr) - 1 - i] = arr[i][j]
	return newArr
test = "panda\nbanana\nsamuel\npatric\nwalrus"

print(transposeMe(test))
