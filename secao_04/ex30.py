#Ler um valor em reais, e imprimir sua cotação em Dólares.

r = float(input('Quantos reais você tem na carteira R$ '))
d = r / 5.52
print('O valor de R${} reais, convertido para dólar é US${:.2f}'.format(r, d))
