from math import pi

a = float(input('digite a altura: '))
r = float(input('Digite o raio: '))
v = pi * ((r * r) * a)
print(f'A altura:{a} e o raio:{r} de um cilindro e seu volume é {v:.2f}')