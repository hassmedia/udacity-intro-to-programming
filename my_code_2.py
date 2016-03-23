# Using functions

s = "Some random text."

def rest_of_string(s):
	return s[1:]

print rest_of_string(s)

def sum(a,b):
	a = a + b
	return a

print sum("Hello ", "world!")
print sum(4,2)