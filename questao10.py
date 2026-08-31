# 10. Faça um programa que:
# 1. Leia dois números;
# 2. Leia uma operação matemática entre +, -, * ou /;
# 3. Realize a operação escolhida;
# 4. Apresente o resultado.
# O programa deverá apresentar uma mensagem de erro caso o usuário informe uma operação diferente das
# quatro opções.

num1 = float(input("Infomre o primeiro número"))
num2 = float(input("Informe o segundo número"))
operador = input("Qual calculo será? Utilize + ou - ou * ou / para calcular")
if operador == "+" :
    soma = num1 + num2
    print("A resposta é", soma)
elif operador == "-" :
    subtracao = num1 - num2
    print("A resposta é", subtracao)
elif operador == "*":
    multiplicacao = num1 * num2
    print("A resposta é", multiplicacao)
else:
    divisao = num1 / num2
    print("A resposta é", divisao)