"""
Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. 
Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", 
caso contrário, armazenar a nota da prova final e recalcular a média. 
Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", 
caso contrário, apresentar a mensagem "REPROVADO"

"""
notas = []

for i in range(4):
    notas.append(float(input(f'Digite sua nota: ')))
media = sum(notas)/ len(notas)
if media >= 7:
    print(f'A média das suas notas é {media}. APROVADO')
else:
    prova_final = float(input('Digite a nota da prova final:'))
    nova_media = (media + prova_final) / 2
    if nova_media >=5:
        print(f'A media das suas notas é {nova_media:.2f}. APROVADO')
    else:
        print(f'A media das suas notas é {nova_media:.2f}. REPROVADO')