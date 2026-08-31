# 2. Uma empresa deseja monitorar a temperatura de uma sala.
# Faça um programa que:
# I. Leia a temperatura em graus Celsius;
# II. Verifique se a temperatura é superior a 30 °C;
# III. Caso seja, apresente:
# "Atenção: temperatura alta!"
# Estrutura obrigatória: utilize somente if.

graus = int(input("Informe quantos graus está fazendo"))
if graus > 30:
    print("Atenção: temperatura alta!")