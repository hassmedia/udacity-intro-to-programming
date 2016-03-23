import time
import webbrowser

'''
This is a 'Take a break' program that will open a browser and display 
a website in a fixed interval and number of breaks.
'''

# number of breaks
breaks = 3

# count timer for loop
count = 0

# open browser and link
print "This program started on " + time.ctime()
while count < breaks:
	time.sleep(2)
	webbrowser.open("http://github.com/mqe")
	count = count + 1
