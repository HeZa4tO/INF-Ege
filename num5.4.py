chislo_r = []

for n in range(1,200):
    a = bin(n)[2:]

    if a[:1] == '1':
        a += '1'
    else:
        a += '0'

    if a.count('1') % 2 == 0:
        a += '0'
    else:
        a += '1'
    if a.count('1') % 2 == 0:
        a += '0'
    else:
        a += '1'

    r = int(a, 2)

    if r > 114:
        chislo_r.append(r)
print(min(chislo_r))