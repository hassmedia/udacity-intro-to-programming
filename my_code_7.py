# Lists supports mutation, Strings supports aliasing

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]
print countries[0][2] / countries[2][2]

# Mutation of a list

p = ['H', 'e', 'l', 'l', 'o']
print p
p[0] = 'Y'
print p

# List Operations

myList = ['Moe', 'Larry', 'Curly']
print myList, len(myList)

myList.append('Shemp')
print myList, len(myList)

list_1 = [0, 1]
list_2 = [2, 3]

list_all = list_1 + list_2
print list_all

# For Loops

def sum_list(a):
	sum = 0
	for number in a:
		sum = sum + number
	return sum

print sum_list([1, 7, 4])

def measure_udacity(a):
    count = 0
    for item in a:
        if item[0] == "U":
            count = count + 1
    return count

print measure_udacity(['Dave','Sebastian','Katy'])

print measure_udacity(['Umika','Umberto'])