# Atena G.Mohammadi

def function():
    var = 5
    print(var)
    
    var = "salam" # python is a typeless programming language
	# as a consequence, we can define anything of any type to a previously
	# defined variable
    print(var)
    
    tup = (3, 3.5, True)
    print(tup[2])
    
    # tup[1] = 1 raises an error since a tuple is immutable
    
    lst = [1, -0.5, "Hi"]
    print(lst[2])
    
    lst[1] = False # this does not raise an error 'cause list is mutable
    print(lst)
    
    di = {"name":["atena", "jack"], "grades":[[19, 16.5, 15], [2, 6, 9.9]],
    	"graduted":[True, False]}
    print(di)


def F(start, end):
    list = []
    start = float(start)
    end = float(end)
    if(start > 0 and end > 0):
        if(end >= start):
            if(start - int(start) < 1):
                start = int(start) + 1
            else:
                start = int(start)
            end = int(end)
            list = [i for i in range(start, end + 1)]
    return list


function()
a = [input("Enter start: "), input("Enter end: ")]
print(F(*a))
