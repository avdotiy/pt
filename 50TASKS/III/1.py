def game(a,c):
    if a or c != 'k' or 'n' or 'b':
        print('введите k, b  или n')
    if a == c:
        print('ничья')
    if a =='k':
        if c == 'n':
            print('победил первый')
        if c == 'b':
            print('победил второй')
    if a =='n':
        if c == 'b':
            print('победил первый')
        if c == 'n':
            print('победил второй')
    if a =='b':
        if c == 'k':
            print('победил первый')
        if c == 'n':
            print('победил второй')
print(game('k','b'))