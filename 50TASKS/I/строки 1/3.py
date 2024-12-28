def top3(st):
    for letter in st:
        if letter == ' ':
            letter = ''
    alphabet = {}
    
    for letter in st:
        alphabet[letter] = 0

    for letter in st:
        alphabet[letter] += 1
    c = {}
    for i in range(3):
        maxquantity = -1
        n = None
        for quantity in alphabet:
                if int(alphabet[quantity]) > int(maxquantity):
                    maxquantity = alphabet[quantity]
                    n = quantity
        c [n] = maxquantity
        alphabet[c]= 0
        top = ''
    for key,value in c.items():
        top += f"{key} - {value}\n"

    text = "Топ 3 символа:\n" + top
    return text
print(top3('maaaattveyy krutoy'))