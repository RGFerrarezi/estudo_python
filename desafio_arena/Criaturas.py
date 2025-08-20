class Criatura:
    magia =Magias()

    def __init__(self, especie, vida, poder, defesa, atributo):
        self.especie = especie
        self.vida = vida
        self.poder = poder
        self.defesa = defesa
        self.atributo = atributo

    def vantagem_atributo(self, outra_criatura):
        vantagens = {
            'Fogo': 'Terra',
            'Agua': 'Fogo',
            'Terra': 'Ar',
            'Ar': 'Agua'
        }
        if self.atributo == vantagens.get(outra_criatura.atributo):
            return True
        return False
    
    def calcular_dano(self, outra_criatura):
        if self.vantagem_atributo(outra_criatura):
            dano = (self.poder * 1.5) - outra_criatura.defesa
        else:
            dano = self.poder - outra_criatura.defesa
        return max(dano, 0)

    def atacar(self, outra_criatura):
        dano = self.calcular_dano(outra_criatura)
        outra_criatura.vida -= dano
        return dano
    
    def morrer(self):
        return self.vida <= 0
    
    def calcular_dano_habilidade(self, habilidade, outra_criatura):
        if habilidade == 'Sopro de fogo':
            if outra_criatura.atributo == 'Terra':
                return 30 * 1.5 - outra_criatura.defesa
            else:
                return 30 - outra_criatura.defesa
        elif habilidade == 'Lança de água':
            if outra_criatura.atributo == 'Fogo':
                return 30 * 1.5 - outra_criatura.defesa
            else:
                return 30 - outra_criatura.defesa
        elif habilidade == 'Espinho de terra':
            if outra_criatura.atributo == 'Ar':
                return 30 * 1.5 - outra_criatura.defesa
            else:
                return 30 - outra_criatura.defesa
        elif habilidade == 'Vendaval':
            if outra_criatura.atributo == 'Agua':
                return 30 * 1.5 - outra_criatura.defesa
            else:
                return 30 - outra_criatura.defesa
        else:
            return 0

    

    def usar_habilidade(self, habilidade, outra_criatura=None):
        if habilidade == 'cura':
            self.vida += 20
            return f"{self.especie} usou Cura e recuperou 20 de vida!"
        elif habilidade == 'Sopro de fogo' and outra_criatura:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.vida -= max(dano, 0)
            return f"{self.especie} usou Bola de Fogo em {outra_criatura.especie} causando {max(dano, 0)} de dano!"
        elif habilidade == 'Lança de água' and outra_criatura:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.vida -= max(dano, 0)
            return f"{self.especie} usou Jato de Agua em {outra_criatura.especie} causando {max(dano, 0)} de dano!"
        elif habilidade == 'terra' and outra_criatura:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.vida -= max(dano, 0)
            return f"{self.especie} usou Tremor em {outra_criatura.especie} causando {max(dano, 0)} de dano!"
        elif habilidade == 'ar' and outra_criatura:
            dano = self.calcular_dano_habilidade(habilidade, outra_criatura)
            outra_criatura.vida -= max(dano, 0)
            return f"{self.especie} usou Rajada de Vento em {outra_criatura.especie} causando {max(dano, 0)} de dano!"
        else:
            return "Habilidade inválida ou alvo não especificado."