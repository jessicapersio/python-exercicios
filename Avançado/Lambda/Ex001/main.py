"""
Desenvolva um programa que leia o seu nome completo
 e que apresente somente o seu primeiro e último nomes
"""

nome = input('Nome Completo: ')
Primeiro_ultimo_nome = lambda nome: nome.split(" ")[0] + " " + nome.split(" ")[-1]
print(f'Seu primeiro e último nome são: {Primeiro_ultimo_nome(nome)}')