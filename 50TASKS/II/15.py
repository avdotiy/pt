def mult (st):
    number = ''
    numbers = []
    multiple = 1
    for i in range(len(st)):
        if st[i]!=',':
            number += st[i]
        elif st[i] == ' ':
            number += 0
        else:
            numbers.append(int(number))
            number = ''
    for i in numbers:
        multiple *= i
    return multiple

print(mult('52, 32, 12'))