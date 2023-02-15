from random import randint

num = int(randint(0, 100))  # executa um número inteiro

print('Vamos jogar um jogo onde você irá tentar adivinhar o número que estou pensando!')
palpite = int(input('Digite um número: '))

while palpite != num:

    if palpite > num:
        print('O número é menor!')
    else:
        print('O número é maior!')

    palpite = int(input('Tente novamente: '))

    if palpite == num:
        print('PARABENS! VOCÊ ACERTOU!')
