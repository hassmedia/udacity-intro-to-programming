'''
Basic while loops in Python.
'''

# import dependencies
import random

# create empty list and max length of list
random_list = []
list_length = 20

# populate list using random numbers
while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
    
# count the number of a specific item
count = 0
for item in random_list:
    if item == 9:
        count = count + 1
    else:
        continue

print random_list
print count
