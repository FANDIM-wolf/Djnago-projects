def numProg(start,x):
	if x < start:
		return 0 
	if x == start:
		return 1
	K = numProg(start,x-1)
	K +=numProg(start,x-2)
	if x%3 ==0:
		K += numProg(start,x//3)
	return K 

print(numProg(2,8)*numProg(8,10)*numProg(10,12))
