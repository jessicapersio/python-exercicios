"""
Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
"""
    
def verificar_numero():
    import random
    print("Gerando um número aleatório entre 1 e 100...")
    numero = random.randint(1, 100)
    print(f"Número gerado: {numero}")
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
    return numero
verificar_numero()