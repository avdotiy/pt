def pere(st):
    dopi = ' '
    for i in range(len(st)-1, -1, -1):
        dopi += st[i]
    st = ''
    for letter in dopi:
        if letter.isupper():
            st += letter.lower()
        if letter.islower():
            st += letter.upper()
    return st
print(pere('matvey'))