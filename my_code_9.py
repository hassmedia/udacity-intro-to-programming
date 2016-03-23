# Solve problems

# Alternative 1

def nextDay(year, month, day):
	if day < 30:
		return year, month, day + 1
	else:
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1
		
	return year,month,day

print nextDay(2012, 12, 1)

# Check years

def dateIsBefore(year1, month1, day1, year2, month2, day2):
	if year1 < year2:
		return True
	if year1 == year2:
		if month1 < month2:
			return True
		if month1 == month2:
			return day1 < day2
	return False

# Calculate days between dates (30 each month, 360 a year)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	years = (year2 - year1) * 360
	months = (month2 - month1) * 30
	days = (day2 - day1) * 1

	return years + months + days

print daysBetweenDates(2012,1,1,2013,1,1)

# Alternative 2

def nextDay_alt_2(year, month, day):
	if month == 12:
		if day == 30:
			year = year + 1
			month = 1
			day = 1
		else:
			day = day + 1
		
	else:
		if day == 30:
			month = month + 1
			day = 1
		else:
			day = day + 1
		
	return year,month,day

print nextDay_alt_2(2012, 12, 1)

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]