'''
Basic functions in python.
'''

# string
s = "Some random text."

# functions for slicing string
def rest_of_string(s):
	return s[3:]

# function for adding two inputs
def sum(a,b):
	a = a + b
	return a

# test for string slicing
print rest_of_string(s)

# test for addition of inputs
print sum("Hello ", "world!")
print sum(4,2)
