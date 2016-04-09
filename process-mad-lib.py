'''
Program for processing, and replacing, words in strings in python.
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

# function for transforming the word
def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

# function for processing string
def process_madlib(mad_lib):
    processed = ""
    words = mad_lib.split()

    for item in words:
        if item == "NOUN" or item == "VERB":
            item = word_transformer(item)
        processed = processed + " " + item

    return processed[1:]

    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)