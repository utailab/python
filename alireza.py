def exercise_0():
    var = 3
    print (var)
    var = ':D' # because python is dynamically-typed language and java is not
    #python does not have declaration for variables because python is a dynamically-typed language and not statically-typed one.
    tup = (1.2, 3, False)

    print (tup[2])

    # tup[1] = ':)' tuples are immutable

    lst = ['alireza', 19, ':)']

    lst[1] = 20 #lists are mutable

    di = {  
            "name" : "alireza", 
            "age" : 19,
            "grades" : {
                "bekhanim" : 20, 
                "benevisim" : 20,
                "hedie haye asemani" : 20,
                },
            "graduated" : False,
        }

    print (di)

def my_range(start, end):
    lst = list()
    if start < 0 or end < 0:
        return lst
    while start <= end:
        print(start, end=' ')
        lst += [start]
        start += 1
    return lst

print(my_range(1, 10))

print(my_range(-1, 20))

print(my_range(11, 2))
