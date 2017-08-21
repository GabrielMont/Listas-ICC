a = float(input())
b = float(input())
c = float(input())

if c > b:
    b, c = c, b
if b > a:
    b, a = a, b

print(a)

if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a*a == b*b + c*c:
    print('TRIANGULO RETANGULO')
elif a == b and b == c:
    print('TRIANGULO EQUILATERO')
elif (a == b and b != c) or (b == c and a != c) or (a == c and b != c):
    print('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ACUTANGULO OU OBTUSANGULO')
