def camel(st):
    result = []
    upper = True  
    for char in st:
        if char.isalpha():  
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper  
        else:
            result.append(char)  
    return ''.join(result)
print(camel("MatVey KrUTOy"))  
print(camel("FiLLiPp BoTIK"))  
