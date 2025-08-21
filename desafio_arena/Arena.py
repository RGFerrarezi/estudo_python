import random

class Arena:
    def __init__(self, criatura1, criatura2):
        self.criaturas = [criatura1, criatura2]  # Lista com as duas criaturas
        self.vencedor = None

    def batalhar(self):
        atacante, defensor = self.criaturas
        rodada = 1
        vez = True

        while not atacante.morrer() and not defensor.morrer():
            print()
            if vez:
                print(f"\nRodada {rodada}: vez do {atacante.especie}")

                # Testa cura antes de qualquer movimento
                if random.randint(1, 24) > 14:
                    resultado_cura = atacante.usar_habilidade('cura')
                    print(resultado_cura)
                    print(f"{atacante.especie} ficou com {max(atacante.vida, 0)} de vida. \n")

                ataque_valor = random.randint(1, 24)
                esquiva_valor = random.randint(1, 24)

                if ataque_valor == 24:
                    # Ataque crítico: habilidade especial, não pode esquivar
                    resultado = atacante.usar_habilidade(atacante.habilidade, defensor)
                    print(resultado)
                elif ataque_valor > 18:
                    # Tenta usar habilidade especial, mas pode ser esquivado
                    if esquiva_valor > ataque_valor:
                        print(f"{defensor.especie} esquivou da habilidade especial!")
                    else:
                        resultado = atacante.usar_habilidade(atacante.habilidade, defensor)
                        print(resultado)
                else:
                    # Ataque normal
                    if esquiva_valor > ataque_valor:
                        print(f"{defensor.especie} se esquivou do ataque!")
                    else:
                        dano = atacante.atacar(defensor)
                        print(f"{atacante.especie} atacou causando {dano} de dano!")

                print(f"{defensor.especie} ficou com {max(defensor.vida, 0)} de vida.")
                vez = False
            else:
                print(f"\nRodada {rodada}: vez do {defensor.especie}")

                # Testa cura antes de qualquer movimento
                if random.randint(1, 24) > 14:
                    resultado_cura = defensor.usar_habilidade('cura')
                    print(resultado_cura)
                    print(f"{defensor.especie} ficou com {max(defensor.vida, 0)} de vida. \n")

                ataque_valor = random.randint(1, 24)
                esquiva_valor = random.randint(1, 24)

                if ataque_valor == 24:
                    # Ataque crítico: habilidade especial, não pode esquivar
                    resultado = defensor.usar_habilidade(defensor.habilidade, atacante)
                    print(resultado)
                elif ataque_valor > 18:
                    # Tenta usar habilidade especial, mas pode ser esquivado
                    if esquiva_valor > ataque_valor:
                        print(f"{atacante.especie} esquivou da habilidade especial!")
                    else:
                        resultado = defensor.usar_habilidade(defensor.habilidade, atacante)
                        print(resultado)
                else:
                    # Ataque normal
                    if esquiva_valor > ataque_valor:
                        print(f"{atacante.especie} se esquivou do ataque!")
                    else:
                        dano = defensor.atacar(atacante)
                        print(f"{defensor.especie} atacou causando {dano} de dano!")

                print(f"{atacante.especie} ficou com {max(atacante.vida, 0)} de vida.")
                vez = True

            rodada += 1
            input("Pressione Enter para continuar...")

        # Define vencedor
        if(atacante.morrer()):
            vencedor = defensor.especie
        else:
            vencedor = atacante.especie
        print(f'atacante {atacante.especie} vida: {atacante.vida} ataque: {atacante.poder} defesa: {atacante.defesa} atributo: {atacante.atributo}')
        print(f'defensor {defensor.especie} vida: {defensor.vida} ataque: {defensor.poder} defesa: {defensor.defesa} atributo: {defensor.atributo}')
        print(f"\nVencedor: {vencedor}")