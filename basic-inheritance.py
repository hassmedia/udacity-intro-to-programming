'''
Testing basic inheritance in python.
'''

# parent class
class Parent():
	def __init__ (self, last_name, eye_color):
		self.last_name = last_name
		self.eye_color = eye_color

	# show parent info
	def show_info(self):
		print "Parent"
		print "Last Name: " + self.last_name
		print "Eye Color: " + self.eye_color

# child class, extended from 'Parent' and adding one extra argument
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

	# show child info
	def show_info(self):
		print "\nChild"
		print "Last Name: " + self.last_name
		print "Eye Color: " + self.eye_color
		print "Number of toys: " + str(self.number_of_toys)

# billy_cyrus = Parent("Cyrus", "Blue")
# billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
