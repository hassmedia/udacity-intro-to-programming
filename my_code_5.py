# Median without Math

def bigger(a,b):
	if a > b:
		return a
	else:
		return b

def biggest(a,b,c):
	return bigger(a,bigger(b,c))

def median(a,b,c):
	if bigger(a, bigger(b,c)) == a:
		return bigger(b,c)
	if bigger(a, bigger(b,c)) == b:
		return bigger(a,c)
	if bigger(a, bigger(b,c)) == c:
		return bigger(a,b)

print(median(1,2,3))