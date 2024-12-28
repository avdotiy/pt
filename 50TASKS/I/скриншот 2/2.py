def okrug(e):
    ip = int(e * 10**5)
    f = e * 10**5 - ip
    if f >=1/2:
        ip +=1
    return ip/10**5
def avg_5 (a, b, c, d):
    srednee = (a+b+c+d)/4
    return okrug(srednee)
print(avg_5(52.53545556575859510, 8, 8, 2))