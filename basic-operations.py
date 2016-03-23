'''
Basic operations in python, just for fun.
'''

# speed of Light in Vacuum, centimeters by nanoseconds
print "Speed of light in cm/ns: " + str((299792458 * 100) / (1.0 * 1000000000))

# more speed of light stuff
speed_of_light = 299792458
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100
print nanostick

# playing with strings
name = "michael"
print name
print name[:1] + "q" + name[4:5] + " rocks!"

# find characters in strings
myString = "Some random text."
a = myString.find("me")
print a
b = myString.find("m", 3)
print b
