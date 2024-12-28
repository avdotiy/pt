def plus(st):
    alphabet = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in st:
        for i in range(1,len(st)-1):        
            if letter == alphabet[i]:    
                if st[i] != '+' and st[i+1] == '+' and st[i-1] == '+':
                    return True
                else:
                    return False           
print(plus('+a'))