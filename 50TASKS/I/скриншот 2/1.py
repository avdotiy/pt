def to_float(num):
    if type(num) != int:
        print ('Невозможно преобразовать')
    else:
        num = float(num)
        return num
print(to_float(52))