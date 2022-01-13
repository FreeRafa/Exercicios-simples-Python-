#Ler quatro notas, calcular a média e imprimir o resultado.

n1 = float(input('Digite o valor da primeira nota '))
n2 = float(input('Digite o valor da segunda nota '))
n3 = float(input('Digite o valor da terceira nota '))
n4 = float(input('Digite o valor da quarta nota '))

m = (n1 + n2 + n3 + n4) / 4

print('A média de {}, {}, {} e {} é {:.2f} '.format(n1, n2, n3, n4, m))
