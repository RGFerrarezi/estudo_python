#lambda, função anônima
# Função lambda para verificar se um número é par ou ímpar
# A função lambda é uma forma concisa de definir funções pequenas e simples

par = lambda  x: x % 2 == 0

impar = lambda x: x % 2 != 0

print('Números pares de 1 a 100: \n')
for i in range(1,101):
    if par(i):
        print(i)

print('\n\nNúmeros ímpares de 1 a 100: \n')
for i in range(1,101):
    if impar(i):
        print(i)
        
#ou
#for i in range(1, 101):
#   if not par(i):
#       print(f'{i} é ímpar')