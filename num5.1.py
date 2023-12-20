for n in range(1, 100):
    a = bin(n)[2:]

    if a.count('1') % 2 == 0:
        a += '0'
    else:
        a += '1'

    if a.count('1') % 2 == 0:
        a += '0'
    else:
        a += '1'
    R = int(a, 2)
    if R > 103:
        print(n)

