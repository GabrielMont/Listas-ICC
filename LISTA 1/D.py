from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()

x1, y1 = float(x1), float(y1)
x2, y2 = float(x2), float(y2)
result1 = sqrt((x2 - x1)**2 + (y1 - y2)**2)


c = complex(input())
result = sqrt((c.real**2 + c.imag**2))

print ('%.4f' % (result1))
print ('%.4f' % (result))
