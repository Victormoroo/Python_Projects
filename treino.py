resposta = input(str('Você possui CNH (s/n)? '))

if resposta == 's' or resposta == 'sim':
    print('Ok! Você pode dirigir')
elif resposta == 'n' or resposta == 'nao':
    print('Você não pode dirigir!')
else:
    print('Valor inválido!')
