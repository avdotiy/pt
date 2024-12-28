def biggest_dict(*args):
    b = {'first_one':'we can do it'}
    c = {}
    for i in args:
        e = e.split(':',1)
        key = e[0]
        ekey = e[1]
        c[key] = ekey
        b.update(c) 
        return b
print (biggest_dict('name:matt', 'cost:fifteen'))