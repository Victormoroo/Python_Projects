from random import choice

a1 = str(input('Digite o nome dos quatro alunos consecutivamente:\n'))
a2 = str(input())
a3 = str(input())
a4 = str(input())

lista = [a1, a2, a3, a4]

print(f'O aluno escolhido foi {choice(lista)}')
