media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Robson', 22
teste = True

print('{} tem {} anos de idade'.format(nome, idade))

#Função Type, retorna o tipo da variável
print(type(nome))
print(type(idade))
print(type(n3))
print(type(teste))
print(type(1+2j))

#Função Isinstance, verifica se a variável é do tipo especificado
a = 10
b = 'Sol'
print(isinstance(a, int))  # True
print(isinstance(a, float))  # False
print(isinstance(a,(int, float)))  # True
print(isinstance(b, str))  # True