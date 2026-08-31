# 7. Faça um programa que leia a nota de um aluno e classifique seu desempenho:
# • Nota de 0 a 4,9 → "Reprovado"
# • Nota de 5,0 a 6,9 → "Recuperação"
# • Nota de 7,0 a 10,0 → "Aprovado"
# Estrutura obrigatória: if / elif / else.

nota = float(input("Informe a sua nota"))
if nota <= 4.9:
    print("Reprovado")
elif nota <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")