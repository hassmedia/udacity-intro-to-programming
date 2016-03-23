import urllib

'''
This is a 'profanity filter' program for checking text files for bad words.
'''

# function for opening and reading a text file
def read_text():
	quotes = open("file_curse.txt") 	# change to 'file_safe.txt' for testing safe respons
	contents_of_file = quotes.read()

	# check and print 'contents_of_file'
	quotes.close()
	check_profanity(contents_of_file)

# function for checking file for bad words using 'www.wdyl.com/profanity'
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()

	# print output
	connection.close()
	if "true" in output:
		print "Profanity Alert!"
	elif "false" in output:
		print "This document has no curse words!"
	else:
		print "Could not scan the document properly."

# initialise program
read_text()