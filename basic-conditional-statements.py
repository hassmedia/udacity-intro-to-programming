'''
Basic conditional statements in python.
'''

# function for 'greater than'
def bigger(a,b):
	if a > b:
		return a
	else:
		return b

print bigger(2,7) 				# 7

# function for boolean
def is_friend(a):
	if a[0] == "D":
		return True
	elif a[0] == "N":
		return True
	else:
		return False

print is_friend("Diane") 		# True
print is_friend("Ned")			# True
print is_friend("Fred")			# False

# function for boolean using a different method
def is_friend_2(name):
	return name[0] == "D" or name[0] == "N"

print is_friend_2("Diane")		# True
print is_friend_2("Ned")		# True
print is_friend_2("Fred")		# False

# function for finding greatest value from input
def biggest(a,b,c):
	if a > b and a > c or a > b and a == c or a > c and a == b:
		return a
	elif b > a and b > c or b > a and b == c or b > c and b == a:
		return b
	elif c > a and c > b or c > a and c == b or c > b and c == a:
		return c

print biggest(2,1,3) 			# 3

# function for finding greatest value from input using
# a different method
def bigger(a,b,c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

print bigger(2,1,3) 			# 3
