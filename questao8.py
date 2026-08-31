# 8. Faça um programa que leia uma temperatura em graus Celsius e apresente:
# • Temperatura abaixo de 15 °C → "Frio"
# • Temperatura entre 15 °C e 30 °C → "Temperatura agradável"
# • Temperatura acima de 30 °C → "Calor"
# Estrutura obrigatória: if / elif / else.

graus = int(input("Infomre a temperatura"))
if graus <= 15:
    print("Frio")
elif graus <= 30:
    print("Temperatura agradável")
else:
    print("Calor")