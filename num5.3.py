kolichestvo = []

for n in range(1,100):
    a = bin(n)[2:]

    if a.count('1') % 2 == 0:
        a += '1'
    else:
        a += '0'

    if a.count('1') % 2 == 0:
        a += '1'
    else:
        a += '0'

    r = int(a, 2)
    if 16 <= r <= 32:
        kolichestvo.append(r)
print(len(kolichestvo))

