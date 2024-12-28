def m(*args):
    res = []
    temp = 0
    for num in args:
        for i in range(0, len(res)):
            temp += res[i]
        temp += num
        res.append(temp)
        temp = 0
    return res

print(m(52, 777, 555))