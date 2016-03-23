# Multiply all in list 

def product_list(list_of_numbers):
	total = 1
	for item in list_of_numbers:
		total = total * item
	return total

print product_list([9])
print product_list([1,2,3,4])

# Return greatest value in list

def greatest(list_of_numbers):
	best = 0
	for i in list_of_numbers:
		if i > best:
			best = i
	return best

print greatest([4,23,1])