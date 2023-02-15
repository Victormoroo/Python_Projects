from random import shuffle

a1 = str(input('Digite o nome dos quatro grupos consecutivamente:\n'))
a2 = str(input())
a3 = str(input())
a4 = str(input())

lista = [a1, a2, a3, a4]

shuffle(lista)
print(f'A ordem de apresentação será:\n{lista}')
