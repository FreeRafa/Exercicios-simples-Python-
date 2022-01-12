#Ler um ângulo em radianos e apresentar convertido em graus

r = int(input('Digite um valor para radianos: '))
g = r * 180 / 3.14
print('{} radianos, convertido para graus é {:.1f}'.format(r, g))
