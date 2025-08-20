# Inicializa a variável documento como string vazia
documento =""

# Solicita ao usuário que digite o RG ou CPF
print('Digite seu RG ou CPF: ')
documento = input()

# Remove caracteres especiais do documento digitado
documentoLimpo = documento.replace('.', '').replace('-', '').replace(' ', '').replace('/', '')

# Verifica o tipo de documento pelo tamanho
if len(documentoLimpo) == 11:
    tipoDocumento = 'CPF'
elif len(documentoLimpo) == 9:
    tipoDocumento = 'RG'
else:
    tipoDocumento = 'Invalido'

# Se o documento for inválido, exibe mensagem de erro
if tipoDocumento == 'Invalido':
    print('Documento inválido!')
    print('O documento digitado é um {}: {}'.format(tipoDocumento, documentoLimpo))
else:
    # Validação do RG
    if tipoDocumento == 'RG':
        soma = 0
        # Calcula a soma ponderada dos dígitos do RG
        for car in range(len(documentoLimpo)-1):
            dig = int(documentoLimpo[car])
            soma += dig * (2 + car)
        conta = 11- (soma % 11)
        # Se o resultado for maior ou igual a 10, define como 'x'
        if conta >= 10:
            conta = 'x'
        
        # Verifica se o dígito verificador confere
        if documentoLimpo[-1] == str(conta) or documentoLimpo[-1].lower() == str(conta):
            print('O {} digitado é válido!'.format(tipoDocumento))
            docuValido = True
        
    else:
        # Validação do CPF
        soma = soma2 = 0
        # Calcula a soma ponderada para o primeiro dígito verificador
        for car in range(len(documentoLimpo)-2):
            dig = int(documentoLimpo[car])
            soma += dig * (10 - car)
        # Calcula a soma ponderada para o segundo dígito verificador
        for car in range(len(documentoLimpo)-2, len(documentoLimpo)-1):
            dig = int(documentoLimpo[car])
            soma2 += dig * (11 - car)
        conta = 11 - (soma % 11)
        conta2 = 11 - (soma2 % 11)
        # Se o resultado for maior ou igual a 10, define como '0'
        if conta >= 10:
            conta = '0'
        if conta2 >= 10:
            conta2 = '0'
        
        # Verifica se os dígitos verificadores conferem
        if documentoLimpo[-1] == str(conta2) and documentoLimpo[-2] == str(conta):
            print('O {} digitado é válido!'.format(tipoDocumento))
            docuValido = True

# Se a variável docuValido não foi definida, o documento é inválido
if 'docuValido' not in locals():
    print('O {} digitado é inválido!'.format(tipoDocumento))
else:
    print('O {} digitado é: {}'.format(tipoDocumento, documentoLimpo))