'''
Word transformer function in python.
'''

from random import randint

# function for random verb
def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

# function for random noun        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

# function for returning either verb, noun, 
# or first character in input
def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    if word == "VERB":
        return random_verb()
    else:
        return word[:1]

print word_transformer("YOLO")