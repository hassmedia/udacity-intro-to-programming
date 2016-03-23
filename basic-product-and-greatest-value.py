'''
Basic product and finding greatest value from list using functions.
'''

# function for returning a product of values in list 
def product_list(list_of_numbers):
	total = 1
	for item in list_of_numbers:
		total = total * item
	return total

# function for returning the greatest value in list
def greatest(list_of_numbers):
	best = 0
	for i in list_of_numbers:
		if i > best:
			best = i
	return best

# testing multiplication
print product_list([9])				# 9
print product_list([1,2,3,4]) 		# 24

# testing greatest value
print greatest([4,23,1]) 			# 23
