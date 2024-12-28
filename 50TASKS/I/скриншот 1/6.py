def all_eq(lst):
    maxlen = 0
    b = []
    for st in lst:
        if len(st) > maxlen:
            maxlen = len(st)
    for st in lst:
        if len(st) == maxlen:
            b.append(st)
        else:
            st = st + ('_')*(maxlen - len(st))
            b.append(st)
    return b
print(all_eq(['филипп_бот', 'матвей_крутой', 'абобус']))