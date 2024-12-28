def volume(args):
    al = []
    for i in args:
        size = 1
        for j in i:
            size *= j
        al.append(size)
    result = 0
    for i in al:
        result += i
    return result
print(volume([52,228,666], [7,77,777]))
