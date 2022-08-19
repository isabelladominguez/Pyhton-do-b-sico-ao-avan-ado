peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Saúdavel')
elif imc < 29.9:
    print('Peso em excesso')
elif imc < 34.9:
    print('Obesidade Grau I')
elif imc < 39.9:
    print('Obesidade Grau II(severa)')
else:
    print('Obesidade Grau III(mórbida)')
