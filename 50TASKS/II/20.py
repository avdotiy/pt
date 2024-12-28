# def mon (*args):
#     for i in range(1, len(mon(*args))):
#         m = 0
#         while mon[i]<mon[i+1]:
#             m+=1
#         if m == len(mon(*args)):
#             print('элементы возрастают')
#         else:
#             print('чел, они убывают, ты что, сам не видишь?')
# print(mon(1,2,3,4,5))

              # ^
            #   |
# чё то тут не работает ничего



def mon(numbers):
    dop = numbers[0]
    for i in range(1, len(numbers)):
        if dop > numbers[i]:
            return 'чел, они не возрастают, ты что, сам не видишь?'
        else:
            dop = numbers[i]
    return 'элементы возрастают'
print(mon([1,2,3,4,52]))