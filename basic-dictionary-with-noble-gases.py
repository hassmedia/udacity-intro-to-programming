'''
Basic dictionary with noble gases.
'''

# empty dictionary
elements = {}

# add noble gases to dictionary 'elements'
elements["He"] = { 
	"Name"  	: "Helium",
	"Number"  	: 2,
	"Density"  	: 0.1786,
	"Noble gas" : True
}
elements["Ne"] = { 
	"Name"  	: "Neon",
	"Number"  	: 10,
	"Density"  	: 0.9002,
	"Noble gas" : True
}
elements["Ar"] = { 
	"Name"  	: "Argon",
	"Number"  	: 18,
	"Density"  	: 1.7818,
	"Noble gas" : True
}
elements["Kr"] = { 
	"Name"  	: "Krypton",
	"Number"  	: 36,
	"Density"  	: 3.708,
	"Noble gas" : True
}
elements["Xe"] = { 
	"Name"  	: "Xenon",
	"Number"  	: 54,
	"Density"  	: 5.851,
	"Noble gas" : True
}
elements["Rn"] = { 
	"Name"  	: "Radon",
	"Number"  	: 86,
	"Density"  	: 9.97,
	"Noble gas" : True
}

# print part of dictionary
print elements["He"]["Name"], elements["He"]["Density"]
