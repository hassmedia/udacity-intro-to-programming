import os

'''
This is a 'prank' program that will get all files in a
directory and rename them with some characters removed.
'''

# function for renaming files
def rename_files():
	
	# get file names from folder
	file_list = os.listdir(r"/path/to/dir")
	print "Path: " + os.getcwd()
	os.chdir(r"/path/to/dir")
	
	# for each file in dir, rename file name
	for file_name in file_list:
		print "Old name: " + file_name
		print "New name: " + file_name.translate(None, "remove")
		os.rename(file_name,file_name.translate(None, "remove"))

# initialise function
#rename_files()

# for testing purposes
string = "my mom is in the room"
print string.translate(None, "remove")
