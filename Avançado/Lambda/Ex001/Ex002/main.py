#Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar
numero = int(input('Digite um número: '))
par_ou_impar = lambda numero: numero % 2 == 0
if par_ou_impar(numero):
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')
