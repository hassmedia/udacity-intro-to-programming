'''
This is a program for validating inputs for dates (day and year).
'''

# function for validing the day
def valid_day(day):
	if day.isdigit() == True:
		day = int(day)
		if day > 0 and day <= 31:
			return day

# a few tests for day
print valid_day("0") 		# None
print valid_day("1") 		# 1
print valid_day("26") 		# 26
print valid_day("10,.") 	# None
print valid_day("500") 		# None

# function for validating the year
def valid_year(year):
	if year.isdigit() == True:
		year = int(year)
		if year > 1900 and year < 2020:
			return year

# a few tests for year
print valid_year("0") 		# None
print valid_year("-11")		# None
print valid_year("1950") 	# 1950
print valid_year("2000")	# 2000
print valid_year("1920")	# 1920