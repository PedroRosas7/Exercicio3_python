# 5. Uma instituição considera aprovado o estudante que obtiver média maior ou igual a 7,0.
# Faça um programa que:
# 1. Leia a média do aluno;
# 2. Verifique a situação;
# 3. Apresente:
# o "Aluno aprovado."
# o ou "Aluno reprovado."
# Estrutura obrigatória: if / else.

media = float(input("Informe a sua média"))
if media >=7:
    print("Aprovado")
else:
    print("Reprovado")