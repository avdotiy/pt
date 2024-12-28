def first_last(letter, st):
    if letter in st:
        m = 0
        n = 0
        for i in st:
            if i == letter:
                m+=1
            if m == 1:
                return i
    else:
        m = 'None'
        n = 'None'
    return m, n
print (first_last('a','matvey'))