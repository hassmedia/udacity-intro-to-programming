# Loops with counting variables

i = 0
while i < 10:
	print i
	i = i + 1

# Loop to a number

def print_numbers(a):
	n = 1
	while n <= a:
		print n
		n = n + 1

print_numbers(3)

def remove(somestring, sub):
	location = somestring.find(sub)
	if location == -1:
		return somestring
	else:
		length = len(sub)
		part_before = somestring[:location]
		part_after = somestring[location + length:]
		return part_before + part_after

print remove("ding", "do")
