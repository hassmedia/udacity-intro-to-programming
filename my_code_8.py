# Find index of item in list
#def find_element(a,b):
#	n = 0
#	while n < len(a):
#		for item in a:
#			if item == b:
#				return n
#			else:
#				n = n + 1
#	return -1

#print find_element([1,2,3],3)

def find_element(a,b):
	if b in a:
		return a.index(b)
	else:
		return -1

print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')