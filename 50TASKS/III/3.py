def black(cards):
    s = 0
    for i in cards:
        s+=i
    if s> 21:
        print('true')
    else:
         print('false')
print(black([1, 7, 52]))