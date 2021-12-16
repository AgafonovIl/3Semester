f = open('17.txt')
a = [int(i) for i in f]
f.close()

c = 0
mx = -100000000
for i in range(len(a) - 1):
    if (a[i] % 2 == 0 and a[i] % 4 == 0 and a[i + 1] % 2 != 0 and a[i + 1] % 11 == 0) or \
            (a[i + 1] % 2 == 0 and a[i + 1] % 4 == 0 and a[i] % 2 != 0 and a[i] % 11 == 0):
        c += 1
        mx = max(mx, a[i] + a[i + 1])

print(c, mx)
