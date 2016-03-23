'''
Basic string substitution using python.
'''

# the string to substitute
given_string1 = "I think %s and %s are perfectly normal things to do in public."

# function for substituting 'given_string1'
def sub1(s1, s2):
	return given_string1 % (s1, s2)

# another string to substitute
given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."

# function for substituting 'given_string2'
def sub2(name, nickname):
	return given_string2 % {"name": name, "nickname": nickname}

print sub1("runnning", "sleeping")
print sub2("Andy", "Dr. A")