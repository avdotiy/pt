def matvey_sigma (x,y):

    if len(x) != len(y):
        print('разное количество точек, ничё не выйдет')
        return
    coords = []
    for i in range (len(x)):
        coords.append(f"({x[i]};{y[i]})")
    return coords
print(matvey_sigma([52, 777, 666] , [228, 1488, 455]))