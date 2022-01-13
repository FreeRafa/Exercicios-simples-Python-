#Ler 3 valores, apresentar o valor da soma dos quadrados dos valores.

n1 = int(input('Digite o primeiro valor '))
n2 = int(input('Digite o segundo valor '))
n3 = int(input('Digite o terceiro valor '))

n1q = n1 * n1
n2q = n2 * n2
n3q = n3 * n3

soma = n1q + n2q + n3q

print('O quadrado da soma de {}, {} e {} é {:,.2f}'.format(n1, n2, n3, soma))
