def div(k, j):
    try:
        return round(k / j,2)
    except ZeroDivisionError as e:
        print(f"Erro: Divisão por zero não é permitida. {e}")
        return None
    except TypeError as e:
        print(f"Erro: Tipos incompatíveis para divisão. {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: Aconteceu um erro!")
        return None

def mult(k,j):
    try:
        return round(k * j,2)
    except TypeError as e:
        print(f"Erro: Tipos incompatíveis para multiplicação. {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: Aconteceu um erro!")
        return None
while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        
        resultadoDiv = div(n1, n2)
        if resultadoDiv is not None:
            print(f"Resultado da divisão: {resultadoDiv}")
        resultadoMult = mult(n1, n2)
        if resultadoMult is not None:
            print(f"Resultado da multiplicação: {resultadoMult}")
        if resultadoDiv is None and resultadoMult is None:
            print("Nenhuma operação foi realizada devido a erros.")
        if input("Deseja continuar? (s/n): ").lower() != 's':
            break
        
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")    
