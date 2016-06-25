def exercise_0():
	var = 12 #In python threr is no need to declare variable type
	print(var)

	var = "python :D" #"""Because Python is a typeless language and when you set a va			with a particular type in make and object and assign var			by the address of it"""
	print(var)
	tup = (1.0, "tuple", True)
	print(tup[2])
	#if we set tup[2] 3 the programm errors because the tuple is an immutable type .
	lst = [45, "list", False]
	print(lst[2])
	lst[2] = "hello" #it doesnt error because the list is mutable type .
	print(lst[2])
	dic = {'Name' : "asma", 'grades' : "10, 12, 13", 'graduated' : True}
	print(dic['graduated'])

def showInterval(start, end):
		li = []
		if start > 0 and end > 0:
			if end >= start:
				for i in range(start - 1, end):
					li.append(i + 1)
		return li
exercise_0()
num1 = float(raw_input("Enter the start :"))
num2 = float(raw_input("Enter the end :"))
if num1 - int(num1) > 0.0000000000000000001:
	li = showInterval(int(num1) + 1, int(num2))
else: 
	li = showInterval(int(num1), int(num2))
for i in range(0, len(li)):
	print(li[i])
