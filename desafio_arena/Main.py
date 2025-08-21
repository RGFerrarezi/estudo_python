def iniciar():
    from Arena import Arena  # Importando a classe Arena aqui para evitar dependency issues
    from Criaturas import Criatura  # Importando a classe Criatura aqui para evitar dependency issues
    print("Bem-vindo à Arena de Batalha!")
    print("Vamos criar duas criaturas para batalhar!")
    # Criando a primeira criatura
    print("Criando a primeira criatura:")
    especie1 = input("Digite a espécie da primeira criatura: ")
    vida1 = int(input("Digite a vida da primeira criatura: (>100) "))
    poder1 = int(input("Digite o poder da primeira criatura: (>10) "))
    defesa1 = int(input("Digite a defesa da primeira criatura: (>5) "))
    numAtributo1 = int(input("Digite o número do atributo da primeira criatura (1-Fogo, 2-Água, 3-Terra, 4-Ar (qualquer outro valor FOGO)): "))
        
    # Criando a segunda criatura
    print("Criando a segunda criatura:")
    especie2 = input("Digite a espécie da segunda criatura: ")
    vida2 = int(input("Digite a vida da segunda criatura: (>100) "))    
    poder2 = int(input("Digite o poder da segunda criatura: (>10) "))
    defesa2 = int(input("Digite a defesa da segunda criatura: (>5) "))
    numAtributo2 = int(input("Digite o número do atributo da segunda criatura (1-Fogo, 2-Água, 3-Terra, 4-Ar (qualquer outro valor FOGO)): "))

    criatura1 = Criatura(especie1, vida1, poder1, defesa1, numAtributo1)
    criatura2 = Criatura(especie2, vida2, poder2, defesa2, numAtributo2)
        

    arena = Arena(criatura1, criatura2)
    arena.batalhar()

if __name__ == "__main__":
    iniciar()