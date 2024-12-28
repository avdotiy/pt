def useless (lst):
    e = lst[0]
    for i in range(0, len(lst)-1, 1):
        if e < lst[i]:
            e = lst[i]
    e = e/len(lst)
    return e
print(useless([52, 10000, 777, 52, 1488]))