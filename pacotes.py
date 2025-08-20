#instalando pacotes externos
# cmd -- py -m pip list
# cmd -- py -m pip install nome_pacote
import math as m
#ou from math import sqrt
import numpy as np
 
n = int(input('Digite um número: '))
print('A raiz quadrada de {0} é: {1}'.format(n,m.sqrt(n))) 

print('\n\n---')
L = np.array([1,2,3,4,5])
print(L)