n1 = int(input('Entre com o primeiro num'))
n2 = int(input('Entre com o segundo num'))

s = n1+n2
m = n1*n2
d = n1 / n2 
di = n1//n2
e = n1**n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'. format(s,m,d), end= ' >>> ')
print('Divisão inteira{} e potência{}'.format(di, e))

# end evita a quebra de linha
# /n realiza a quebra de linha
