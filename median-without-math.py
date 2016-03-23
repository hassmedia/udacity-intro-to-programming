'''
This is a program for finding median without using any mathematics.
'''

# function for deciding greatest value of two input values
def bigger(a,b):
	if a > b:
		return a
	else:
		return b

# function for returning greatest value of all three values
def biggest(a,b,c):
	return bigger(a,bigger(b,c))

# function for deciding greatest value of three input values
# using function 'bigger'.
def median(a,b,c):
	if bigger(a, bigger(b,c)) == a:
		return bigger(b,c)
	if bigger(a, bigger(b,c)) == b:
		return bigger(a,c)
	if bigger(a, bigger(b,c)) == c:
		return bigger(a,b)

# print results
print median(1,8,3) 		# 3
