'''
Basic list and string operations in python.
'''

# list of countries
countries = [
    ['China','Beijing',1350],
    ['India','Delhi',1210],
    ['Romania','Bucharest',21],
    ['United States','Washington',307]]

# print 'Delhi'
print countries[1][1]                       # Delhi

# print result of 'Beijing' divided by 
#'Bucharest' population
print countries[0][2] / countries[2][2]     # 64

# mutation of a list
p = ['H', 'e', 'l', 'l', 'o']
print p
p[0] = 'Y'
print p

# append item to a list
myList = ['Moe', 'Larry', 'Curly']
print len(myList)                           # 3

myList.append('Shemp')
print len(myList)                           # 4

# adding lists together
list_1 = [0, 1]
list_2 = [2, 3]

list_all = list_1 + list_2
print list_all

# adding items in list with loop
def sum_list(a):
	sum = 0
	for number in a:
		sum = sum + number
	return sum

print sum_list([1, 7, 4])                   # 12

# find how many times a character appears in list
def measure_udacity(a):
    count = 0
    for item in a:
        if item[0] == "U":
            count = count + 1
    return count

print measure_udacity(
    ['Dave','Sebastian','Katy'])            # 0
print measure_udacity(
    ['Umika','Umberto'])                    # 2
