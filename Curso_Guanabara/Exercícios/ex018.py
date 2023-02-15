import math

ang = float(input('Digite um angulo qualquer: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f'O angulo de {ang}° tem o SENO de {sen:.2f}')
print(f'O angulo de {ang}° tem o COSSENO de {cos:.2f}')
print(f'O angulo de {ang}° tem o TANGENTE de {tan:.2f}')