def money(coins):
    for i in coins:
        sum = 0
        sum+=i
        if sum % 3 == 0:
            return True
        else:
            return False
print(money([333, 666]))