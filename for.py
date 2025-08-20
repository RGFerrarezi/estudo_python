#importando a biblioteca random
import random

# Laços de repetição - for
for x in range (10):
    print(x)

# Contagem crescente
print('---')
for x in range (1,11):
    print(x)

# Contagem regressiva
print('---')
for x in range (20,-1,-2):
    print(x)

# pegando valores de uma string
print('---')
for letra in 'Python':
    print(letra)

# pegando valores de uma string, menos o ultimo character, sem saber o tamanho da string
print('---')
frase = 'Curso de Python'
for i in range(len(frase)-1):
    print(frase[i])
    
# pegando valores de uma lista, e pulando itens específicos
print('\n---')
frutas = ['maçã', 'banana', 'laranja', 'uva', 'pera', 'abacaxi', 'melancia', 'morango', 'caju', 'goiaba']
for fruta in frutas:
    if fruta == 'abacaxi':
        continue  # pula o item abacaxi
    print(fruta)
    
# Gerando valores aleatórios, com laços for intercalados
print('\n---')
for A in range(1,6):
    print('Conjunto {0}:'.format(A))
    for b in range(5):
        valor = random.randint(1,100)
        print(valor, end=' ')
    print('\n')  # pular linha apos cada conjunto