#Calcular a hipotenusa de dois catetos

import math

a = int(input('Qual o valor do cateto? '))
b = int(input('Qual o valor do segundo cateto '))
h = math.hypot(a, b)
print('A hipotenusa de {} mais {} é {:.2f}'.format(a, b, h))



