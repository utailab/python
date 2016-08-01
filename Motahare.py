def exercise_0() :
	var = 2
	print (var)
	var = "x can be the name of any object"
	print (var)
	# In python we don't declare variables with certain types or initialize them , we don't create variables at all ,
	# we just give name to values and objects , so we can use a name for any object of any type
	tup = ( 12 , 200.1 , True )
	print (tup[2])
	# tup[1] = ":D"
	# This action is not valid because tuples are immutable which means their elements can not be modified
	lst = [ 12 , 200.1 , True ]
	print (lst[2])
	# but list elements can be changed
	lst[1] = ":D"
	print (lst)
	grades = [ 14.5 , 17 , 18 , 16.5 , 19.25 ] ;
	di = { 'Name' : "Motahare" , 'Grades' : grades , 'Gratuated' : False }
	print (di)
	return

def exercise_1(start , end):
	ls = []
	if start<end and start>0  :
		for x in range(start, end+1):
			ls.append(x)			
	return ls


print (exercise_1(-1,1))
print (exercise_1(8,3))
print (exercise_1(1,4))
