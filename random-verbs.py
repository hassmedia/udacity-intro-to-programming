'''
Random verbs function in python.
'''

from random import randint

# function for getting random number and return as verb
def random_verb():
    num = randint(0, 1)

    if num == 0:
    	return "run"
    else:
    	return "kayak"

random_verb()