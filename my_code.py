# GRAMMAR ---------------
# Expression 	-> Expression Operator Expression
# Expression 	-> Number
# Operator 		-> + 
# Operator 		-> *
# Number 		-> 0,1, ... 

# Expression -> Expression (Number(1)) Operator (+) Expression (Number(1))

# Speed of Light in Vacuum, centimeters by nanoseconds
print (299792458 * 100) / (1.0 * 1000000000)

# VARIABLES -------------
# Name = Expression

speed_of_light = 299792458
billionth = 1.0 / 1000000000
nanostick = speed_of_light * billionth * 100
print nanostick

# STRINGS ---------------
# Name = "string"
# Name[0] -> s
# Name[3] -> i

name = "Michael"
print name
print "lol" + name[3:-2]

# FIND ------------------
# Not found -> -1
# string = "Some random text."
# string.find("me") -> 2
# string.find("m", 3) -> 10

myString = "Some random text."
a = myString.find("me")
print a
b = myString.find("m", 3)
print b
