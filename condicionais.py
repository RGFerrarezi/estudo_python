n1 = n2 = n3 = n4 = 0.0
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: ")) 
n4 = float(input("Digite a quarta nota: "))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7.0:
    print("Aprovado")
    print("Média:", media)
    print("Parabéns!")
elif media >= 5.0:
    print("Recuperação")
    print("Média:", media)
else:
    print("Reprovado")
    print("Média:", media)