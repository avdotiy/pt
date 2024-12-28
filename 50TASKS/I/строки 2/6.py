def cleaned_str (st):
    word = ''
    for i in st:
        if i =='@':
            word = word[:-1]
        else:
            word += i

    return word
print (cleaned_str('Mat@tve@y @  KrU@tOy@'))