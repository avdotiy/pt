def change(lst): 
    lst[len(lst)-1], lst[0] = lst[0], lst[len(lst)-1]
    return lst
print (change([228, 777, 52]))
