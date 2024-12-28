# def lst_sort(lst):
#     b =[]
#     for a in range(0, len(b)-1, 1):
#         if lst[a] < lst[a+1]:
#             lst_sort(lst) = b(lst)
#             return lst
#         else:
#             for i in range(0, len(lst)-1, 1):
#                 if lst[i]<lst[i+1]:
#                     b.append(i)
#                 else:
#                     lst[i], lst[i+1] = lst[i+1], lst[i]
# print(lst_sort([52, 14, 3, 7, 200, 52, 52, 40]))

# попробую ещё раз

# def lst_sort(lst):
#     for i in range(0, len(lst)):
#         for i in range(0, len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#         return lst

# print(lst_sort([52, 14, 3, 7, 200, 52, 52, 40]))


# и ещё раз

def lst_sort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                return lst
print(lst_sort([5, 1, 6, 7]))