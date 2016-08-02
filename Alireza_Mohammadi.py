#Alireza_Mohammadi
def e0() :
	var = 7
	print (var)

	var = "HALA_MADRID"
	# Python is a high level language that we dont need to define types for it !!
	# In other words PYTHON is a smart programing_language ;))

	print (var)

	tup = (7, "CR7", "RealMadrid is my life :))")
	print (tup[2])

	#tup[2] = "I_HATE_FCBarcelona" ;)
	#that is not possible because tuple is immutable

	mylist = ["CR7", "Karim", "Gareth"]
	print (mylist[1])
	print (mylist)

	mylist[1] = "Antoine Griezmann"
	#list is mutable !!
	#So that is possible
	print (mylist)

	mydictionary = {
		"FirstName" : "Alireza",
		"LastName" : "Mohammadi",
		"Age" : 18,
		"Grades" : {
				"English" : 0,
				"Arabic" : 0,
				"Math" : 5,
				"Playing_Games" : 22
			}
	}

	print (mydictionary)

def e1(start, end) :
	if (start < 0 or end < 0 or start > end) : 
		print (list())
	else :
		print (list (range (start, end + 1))) 

print ("Exercise_0")
e0 ()
print ("\n\n\n")

print ("Exercise_ 1")
start = int (input ("start : "))
end = int(input("end : "))
e1(start, end)
