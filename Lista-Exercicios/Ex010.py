#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

taxa_dolar = 6.04
valor_reais = float(input('Entre com o valor em reais: '))

quantidade_dolares = valor_reais / taxa_dolar

print(f'Com R${valor_reais:.2f}, você pode comprar US${quantidade_dolares:.2f}')
