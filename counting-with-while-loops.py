'''
Counting items in list using Python.
'''

# import dependencies
import random

# create empty list with max length 20
random_list = []
list_length = 20

# populate list with random numbers
while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

# create a list with eleven zeros
count_list = [0] * 11

# counting number of same items
for item in random_list:
	count_list[item] = count_list[item] + 1

# test
print random_list
print count_list
print sum(count_list) 		# 20
