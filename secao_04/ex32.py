#A soma do sucessor de seu triplo mais o  atecessor de seu dobro é

n1 = int(input('Digite um numero inteir:'))
triple = (n1 * 3)
doble = (n1 ** n1)
print('O sucessor do seu triplo é {}'.format(triple + 1))
print('O antecessor do dobro é {}'.format(doble - 1))
dt = (triple + 1) + (doble - 1)
print('A soma do sucessor de seu triplo mais o  atecessor de seu dobro é {}'.format(dt))