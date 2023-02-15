n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInteira = n1 // n2
pot = n1 ** n2
resto = n1 % n2

print(f'A soma é {soma}, a subtração é {sub}, a multiplicação é {mult} e a divisão é {div:.2f}', end=' ') #'.2f' = duas casas após a vírgula e end='' = não pular linha
print(f'A divisão inteira é {divInteira}, a potência é {pot} e o resto da divisão é {resto}')