def mul_to_int (a,b):
    c = a*b
    if type(c) != int:
        c = float (c)
    else:
        c = int(c)
    return c
print (mul_to_int (6, 5.2))