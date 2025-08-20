#recursividade

#fatorial de um numero
def fatorial(n):
    #caso seja negativo, cria um erro
    #caso seja 0 ou 1, retorna 1
    if n < 0:
        raise ValueError("O número deve ser não negativo.")
    elif n > 200:
        raise ValueError("O número é muito grande para calcular o fatorial.")
    elif n == 0 or n == 1:
        return 1
    else:
        #chamada recursiva
        return n * fatorial(n-1)
    
#teste
if __name__ == "__main__":
    try:            
        num = int(input('Digite um numero: '))
        print(f'O fatorial de {num} é: {fatorial(num)}')
    except ValueError as e:
        print(f'Erro: {e}')
    except RecursionError:
        print('Erro: A recursão excedeu o limite máximo. Verifique se o número é muito grande.')