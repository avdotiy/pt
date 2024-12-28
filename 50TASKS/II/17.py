# def okrug(e):
#     ip = int(e * 10**5)
#     f = e * 10**5 - ip
#     if f >=1/2:
#         ip +=1
#     return ip/10**5
# def avg_5 (a, b, c, d):
#     srednee = (a+b+c+d)/4
#     return okrug(srednee)

# это задача из первой части задач

import math
def okrug(e):
    ip = int(e * 10**3)
    f = e * 10**5 - ip
    if f >=1/2:
        ip +=1
    return ip/10**3

def pythagoras(dict):

    x = dict.get('x')[0] - dict.get('x')[1]
    y = dict.get('y')[0] - dict.get('y')[1]


    length = math.sqrt(x**2 + y**2)

    length = okrug(length)
    return length
print(pythagoras({'x':[0,0], 'y': [3,4]}))