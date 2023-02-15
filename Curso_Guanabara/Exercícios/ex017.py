from math import hypot

cat1 = float(input('Digite o valor do cateto oposto e do cateto adjacente do traângulo:\n'))
cat2 = float(input())

print(f'A hipotenusa é igual a: {hypot(cat1, cat2):.2f}')
