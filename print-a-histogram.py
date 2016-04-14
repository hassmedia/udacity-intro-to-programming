'''
Create a list and print occurrences of item as histogram.
'''

# import dependencies
import random

# create empty list with maximum length 20
random_list = []
list_length = 20

# populate list with random numbers
while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

# aggregate the list with random numbers, counting the number of occurrences
count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1
    
# print number and occurrence as table
n = 0
print "number" + " | " + "occurrence"
for item in count_list:
    if n == 10:
        print " "*4 + str(n) + " | " + str(count_list[n])
    else:
        print " "*5 + str(n) + " | " + str(count_list[n])
        n = n + 1

# print number and occurrence as histogram
i = 0
print "number" + " | " + "occurrence"
for item in count_list:
    if i == 10:
        print " "*4 + str(i) + " | " + "*"*count_list[i]
    else:
        print " "*5 + str(i) + " | " + "*"*count_list[i]
        i = i + 1

