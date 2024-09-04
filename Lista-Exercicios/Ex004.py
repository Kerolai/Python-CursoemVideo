#Faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

A = input('Digite algo:')

# Mostra o tipo primitivo
print('Tipo primitivo:', type(A))

# Verifica se a string é numérica
print('É numérico?', A.isnumeric())

# Verifica se a string é alfabética
print('É alfabético?', A.isalpha())

# Verifica se a string é alfanumérica
print('É alfanumérico?', A.isalnum())

# Verifica se a string é apenas espaços
print('É apenas espaços?', A.isspace())

# Verifica se a string está em maiúsculas
print('Está em maiúsculas?', A.isupper())

# Verifica se a string está em minúsculas
print('Está em minúsculas?', A.islower())

# Verifica se a string é capitalizada
print('É capitalizada?', A.istitle())