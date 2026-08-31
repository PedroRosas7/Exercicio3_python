# 4. Faça um programa que leia um número inteiro e verifique se ele é:
# • Par; ou
# • Ímpar.
# Utilize o operador % para realizar a verificação.
# Estrutura obrigatória: if / else.

numero = int(input("Informe um número"))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")