def to_dict(lst):
    dictionary = {}
    for name in lst:
        dictionary[name] = name
    for cost in lst:
        dictionary [cost] = cost
    return dictionary

print(to_dict(['cost','name']))