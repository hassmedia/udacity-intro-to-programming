import cgi

'''
This is a program for HTML escaping in python.
'''

# function for escaping certain characters
def escape_html1(s):
	for (i, o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
		s = s.replace(i, o)
	return s

# function for escaping certain characters
# using built in escape library
def escape_html2(s):
	return cgi.escape(s, quote = True)

print escape_html1("test>")
print escape_html2('Dude"')