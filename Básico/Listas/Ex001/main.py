"""
Desenvolva um programa que armazene quatro notas em uma lista
e que apresente: a média final, a maior nota e a menor nota
"""
notas = []

for i in range(4):
    notas.append(float(input(f'Digite sua nota: ')))
    
media = sum(notas)/4
minimo = min(notas)
maximo = max(notas)
print(f'A média das suas notas é {media} a nota máxima é {maximo} e a mínima é {minimo}')
   