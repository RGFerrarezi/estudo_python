def Vogal(frase):
    lista1 = [v for v in frase if v in lista_vogais]
    return lista1

frase = 'A rã arranha a aranha, e a aranaha arranaha a rã. Sou uma frase com várias vogais!'

frase2 = 'Eu te amo mamãe!!!!'

vogais = 'AEIOUaeiouáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛàèìòùÀÈÌÒÙãõÃÕäëïöüÄËÏÖÜ'
lista_vogais = []
#for letra in frase:
#    if letra in vogais:
#        lista_vogais.append(letra)
 
for letra in vogais:
    lista_vogais.append(letra) 
        
vogaisFrase = Vogal(frase)

vogais2 = Vogal(frase2)

print(vogais2) 
 
print(vogaisFrase)
print(len(vogaisFrase))