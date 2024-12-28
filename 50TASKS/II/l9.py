def doloy(names, enemies):
    for name in names:
        dopi = []
        if name not in enemies:
            dopi.append(names[name])
    return dopi
print(doloy('matvey,polina, phil, dergidver', 'dergidver'))