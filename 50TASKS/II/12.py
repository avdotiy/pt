def double (st):
    for i in range(len(st)-1):
        if st[i] == st [i+1]:
            return True
    return False

print(double('matt'))