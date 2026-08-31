# 6. Uma loja oferece 10% de desconto para compras com valor superior a R$ 500,00.
# Faça um programa que:
# 1. Leia o valor da compra;
# 2. Verifique se o cliente possui direito ao desconto;
# 3. Se possuir, calcule o valor do desconto;
# 4. Caso contrário, informe que não há desconto.
# Apresente o resultado na tela.
# Estrutura obrigatória: if / else.

compra = float(input("Informe o valor da sua compra"))
if compra > 500.00:
    desconto = compra - (compra * 0.1)
    print("O valor a se pagar será de R$",desconto)
else:
    print("Sem desconto. Valor a se pagar será de R$", compra)