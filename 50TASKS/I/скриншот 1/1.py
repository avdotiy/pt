a =[2,3,4,5,3,5,5,23,3,4]
b = len (a) 
c = []
for i in range(b-1, -1,-1):
    c.append(a[i])
print(c)