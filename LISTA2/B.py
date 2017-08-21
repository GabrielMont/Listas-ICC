peso = float(input())
altura = float(input())

imc = peso/(altura*altura)
print('%.2f' % (imc))
if imc <= 18.5:
    print('Baixo Peso')
elif imc <= 24.9:
    print('Peso Normal')
else:
    if imc <= 29.9:
        print('Sobre Peso')
    elif imc <= 34.9:
        print('Obesidade Grau 1')
    elif imc <= 39.0:
        print('Obesidade Grau 2')
    else:
        print('Obesidade Grau 3')
    print('%.2f' % (peso - (24.9*(altura*altura))))
    
