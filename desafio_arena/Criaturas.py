class Criatura:

    def __init__(self, especie, vida, poder, defesa, numAtributo):
        self.__especie = especie
        self.__vida = vida
        self.__poder = poder
        self.__defesa = defesa
        self.__numAtributo = numAtributo
        self.__atributo = {
            1: 'Fogo',
            2: 'Agua',
            3: 'Terra',
            4: 'Ar'
        }.get(numAtributo, 'Fogo')  # Default to 'Fogo' if numAtributo is invalid
        self.__habilidade = {
            1: 'Sopro de fogo',
            2: 'Lança de água',
            3: 'Espinho de terra',
            4: 'Vendaval',
        }.get(numAtributo, 'Sopro de fogo')
        # Default habilidade to 'Sopro de fogo' if numAtributo is invalid

    # Getters
    def get_especie(self):
        return self.__especie
    def get_vida(self):
        return self.__vida
    def get_poder(self):
        return self.__poder
    def get_defesa(self):
        return self.__defesa
    def get_numAtributo(self):
        return self.__numAtributo
    def get_atributo(self):
        return self.__atributo
    def get_habilidade(self):
        return self.__habilidade

    # Setters
    def set_vida(self, valor):
        self.__vida = valor
    def set_poder(self, valor):
        self.__poder = valor
    def set_defesa(self, valor):
        self.__defesa = valor
    def set_numAtributo(self, valor):
        self.__numAtributo = valor

    def vantagem_atributo(self, outra_criatura):
        vantagens = {
            'Fogo': 'Terra',
            'Agua': 'Fogo',
            'Terra': 'Ar',
            'Ar': 'Agua'
        }
        if self.__atributo == vantagens.get(outra_criatura.get_atributo()):
            return True
        return False
    
    def calcular_dano(self, outra_criatura):
        if self.vantagem_atributo(outra_criatura):
            dano = (self.__poder * 1.5) - outra_criatura.get_defesa()
        else:
            dano = self.__poder - outra_criatura.get_defesa()
        return max(dano, 0)

    def atacar(self, outra_criatura):
        dano = self.calcular_dano(outra_criatura)
        outra_criatura.set_vida(outra_criatura.get_vida() - dano)
        return dano
    
    def morrer(self):
        return self.__vida <= 0
    
    def calcular_dano_habilidade(self, habilidade, outra_criatura):
        if habilidade == 'Sopro de fogo':
            if outra_criatura.get_atributo() == 'Terra':
                return (30 + self.__poder) * 1.5 - outra_criatura.get_defesa()
            else:
                return (30 + self.__poder) - outra_criatura.get_defesa()
        elif habilidade == 'Lança de água':
            if outra_criatura.get_atributo() == 'Fogo':
                return (30 + self.__poder) * 1.5 - outra_criatura.get_defesa()
            else:
                return (30 + self.__poder) - outra_criatura.get_defesa()
        elif habilidade == 'Espinho de terra':
            if outra_criatura.get_atributo() == 'Ar':
                return (30 + self.__poder) * 1.5 - outra_criatura.get_defesa()
            else:
                return (30 + self.__poder) - outra_criatura.get_defesa()
        elif habilidade == 'Vendaval':
            if outra_criatura.get_atributo() == 'Agua':
                return (30 + self.__poder) * 1.5 - outra_criatura.get_defesa()
            else:
                return (30 + self.__poder) - outra_criatura.get_defesa()
        else:
            return 0

    

    def usar_habilidade(self, habilidade, outra_criatura=None):
        if habilidade == 'cura':
            self.set_vida(self.get_vida() + 10)
            return f"{self.get_especie()} usou Cura e recuperou 10 de vida!"
        elif habilidade == 'Sopro de fogo' and outra_criatura is not None:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.set_vida(outra_criatura.get_vida() - max(dano, 0))
            return f"{self.get_especie()} usou Bola de Fogo em {outra_criatura.get_especie()} causando {max(dano, 0)} de dano!"
        elif habilidade == 'Lança de água' and outra_criatura is not None:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.set_vida(outra_criatura.get_vida() - max(dano, 0))
            return f"{self.get_especie()} usou Jato de Agua em {outra_criatura.get_especie()} causando {max(dano, 0)} de dano!"
        elif habilidade == 'Espinho de terra' and outra_criatura is not None:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.set_vida(outra_criatura.get_vida() - max(dano, 0))
            return f"{self.get_especie()} usou Tremor em {outra_criatura.get_especie()} causando {max(dano, 0)} de dano!"
        elif habilidade == 'Vendaval' and outra_criatura is not None:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.set_vida(outra_criatura.get_vida() - max(dano, 0))
            return f"{self.get_especie()} usou Rajada de Vento em {outra_criatura.get_especie()} causando {max(dano, 0)} de dano!"
        else:
            return "Habilidade inválida ou alvo não especificado."