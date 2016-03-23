'''
Basic while loop in python.
'''

# while loop with counter
i = 0
while i < 10:
	print i
	i = i + 1

# function for while loop until input
def print_numbers(a):
	n = 1
	while n <= a:
		print n
		n = n + 1

print_numbers(3)
