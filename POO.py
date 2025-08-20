# Definição da classe base Veiculo
class Veiculo():
    # Construtor da classe Veiculo, recebe modelo e fabricante
    def __init__(self,modelo,fabricante,):
        self.__modelo=modelo  # Atributo privado modelo
        self.__fabricante=fabricante  # Atributo privado fabricante
        self.__registro = None  # Atributo privado registro, inicializado como None
    
    # Método para obter o modelo
    def get_modelo(self):
        return self.__modelo
    
    # Método para obter o fabricante
    def get_fabricante(self):
        return self.__fabricante
    
    # Método para definir o registro
    def set_registro(self, registro):
        self.__registro = registro
    
    # Método para obter o registro
    def get_registro(self):
        return self.__registro
    
    # Método para acelerar (padrão)
    def acelerar(self):
        return ('Acelerando!!!')

# Classe Carro herda de Veiculo
class Carro(Veiculo):
    # Sobrescreve o método acelerar
    def acelerar(self):
        return 'Muito transito, não tem como!'

# Classe Moto herda de Veiculo
class Moto(Veiculo):
    # Sobrescreve o método acelerar
    def acelerar(self):
        return 'Vroom!Vroom! Acelerando no corredor!'

# Classe Aviao herda de Veiculo
class Aviao(Veiculo):
    # Sobrescreve o método acelerar
    def acelerar(self):
        return ('Voando!!!')

    # Construtor da classe Aviao, recebe modelo, fabricante e categoria
    def __init__(self, modelo, fabricante, categoria):
        super().__init__(modelo, fabricante)  # Chama o construtor da classe base
        self.__categoria = categoria  # Atributo privado categoria
    
    # Método para obter a categoria do avião
    def get_categoria(self):
        return self.__categoria

# Bloco principal de execução
if (__name__ == '__main__'):
    # Instanciação de objetos Carro
    carro1 = Carro('A6','AUDI')
    carro2 = Carro('Grand Livina','Nissan')
    # Instanciação de objetos Moto
    moto1 = Moto('CRF 300F','HONDA')
    moto2 = Moto('Hornet 500','HONDA')
    # Instanciação de objeto Aviao
    aviao1 = Aviao('A318','Airbus','Viagem')

    # Solicita e define o registro do carro1
    carro1.set_registro(input('Digite o registro do carro: '))
    # Exibe informações do carro1
    print('Carro: ', carro1.get_modelo(), ' - Fabricante: ', carro1.get_fabricante(),
           ' - Numero de Registro: ', carro1.get_registro(), ' -> ',carro1.acelerar())
    # Exibe informações do carro2 (sem registro definido)
    print('Carro: ', carro2.get_modelo(), ' - Fabricante: ', carro2.get_fabricante(),
           ' - Numero de Registro: ', carro2.get_registro(), ' -> ',carro2.acelerar())

    # Solicita e define o registro das motos
    moto1.set_registro(input('Digite o registro da moto: '))
    moto2.set_registro(input('Digite o registro da outra moto: '))

    # Exibe informações das motos
    print('Moto: ', moto1.get_modelo(), ' - Fabricante: ', moto1.get_fabricante(),
           ' - Numero de Registro: ', moto1.get_registro(), ' -> ',moto1.acelerar())
    print('Moto: ', moto2.get_modelo(), ' - Fabricante: ', moto2.get_fabricante(),
           ' - Numero de Registro: ', moto2.get_registro(), ' -> ',moto2.acelerar())

    # Solicita e define o registro do avião
    aviao1.set_registro(input('Digite o registro do avião: '))

    # Exibe informações do avião
    print('Avião: ', aviao1.get_modelo(), ' Categoria: ', aviao1.get_categoria(), ' - Fabricante: ',
           aviao1.get_fabricante(), ' - Numero de Registro: ', aviao1.get_registro(), ' -> ',aviao1.acelerar())