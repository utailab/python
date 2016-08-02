def exercise_0():
	var = 5 
	print(var)
	#soal 1 : na ba tavajoh be meghdari ke behesh nesbat midim typesh moshakhas mishe  ye pointer be ye object azoon meghdarie ke behesh nesbat midim
	var= "hello"
	print(var)
	#soal 2 : chonke be oon objecte faghat dare eshare mikone va oon pointero bar midare be ye jaye dige ke object az stringast eshare mikone vali java khode meghdaro mirize too moteghayer va type moteghayero nmitoone avaz kone(ehtemalan be interpreteri boodane python ham rabt dare :-? chon ke java aval bayad compile kone bayad no moteghayer too kole code(scop tarifesh) yeksan bashe vali python chon khat be khat codo mikhoone mitoone to jahaye mokhtalef estefadehaye motefavet kone az moteghaayer:-?)
	tup = (10,5.3,True)
	print(tup[2])
	#tup[1] = 'h'
	#eror mide . chon ke type tuples yek object immutable ast va ghabele taghir nist 
	lst=[10,5.3,True]
	print(lst) 
	lst[1]='h'
	print(lst) 
	di={"name":"ghazal" ,"grades":[14,16,18] , "graduated":False}
	print(di) 
exercise_0()
def  exercise_1(start,end):
	if start > 0 and end> 0:
		print(" har 2 mosbat")
	elif start >0:
		print("start mosbat")
	elif end>0:
		print("end mosbat")
	else:
		print("har 2manfi")
	x =[]
	if start <= end :
		for i in range(start,end+1):
			print(i)
			y=[i]
			x+y
		return x
exercise_1(2,10)
