""""
Desenvolva um programa que leia um número inteiro qualquer 
 e que apresete o número informado, seguido do seu antecessor e do seu sucessor
 """
def numero_antecessor_sucessor():
    import random
    print("Gerando um número aleatório entre 1 e 100...")
    numero = random.randint(1, 100)
    print(f"Número gerado: {numero}")
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"O número informado é {numero}, seu antecessor é {antecessor} e seu sucessor é {sucessor}")
    return numero, antecessor, sucessor
numero_antecessor_sucessor()