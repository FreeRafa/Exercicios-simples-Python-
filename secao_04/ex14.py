#Ler um angulo em graus, e apresentar em radianos.

g = int(input(('Digite um valor em graus: ')))
r = g * 3.14 / 180
print('{} graus convertido em radianos é {:.2f}'.format(g, r))