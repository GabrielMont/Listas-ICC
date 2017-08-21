c = input()
a, b = [int(x) for x in c.split()]

if b == a or b == a + 1:
    print(a, b, 'ok')
else:
    print(a, b, 'errados')
