'''
This is a program for finding where, and if, an input is in a list.
'''

# function for finding if input is in list
def find_element(a,b):
	if b in a:
		return a.index(b)
	else:
		return -1

# a few tests
print find_element([1,2,3],3) 					# 2
print find_element(['alpha','beta'],'gamma') 	# -1