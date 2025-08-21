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
                print(f"\nRodada {rodada}: vez do {atacante.get_especie()}")

                # Testa cura antes de qualquer movimento
                if random.randint(1, 24) > 14:
                    resultado_cura = atacante.usar_habilidade('cura')
                    print(resultado_cura)
                    print(f"{atacante.get_especie()} ficou com {max(atacante.get_vida(), 0)} de vida. \n")

                ataque_valor = random.randint(1, 24)
                esquiva_valor = random.randint(1, 24)

                if ataque_valor == 24:
                    # Ataque crítico: habilidade especial, não pode esquivar
                    resultado = atacante.usar_habilidade(atacante.get_habilidade(), defensor)
                    print(resultado)
                elif ataque_valor > 18:
                    # Tenta usar habilidade especial, mas pode ser esquivado
                    if esquiva_valor > ataque_valor:
                        print(f"{defensor.get_especie()} esquivou da habilidade especial!")
                    else:
                        resultado = atacante.usar_habilidade(atacante.get_habilidade(), defensor)
                        print(resultado)
                else:
                    # Ataque normal
                    if esquiva_valor > 18:
                        print(f"{defensor.get_especie()} se esquivou do ataque!")
                    else:
                        dano = atacante.atacar(defensor)
                        print(f"{atacante.get_especie()} atacou causando {dano} de dano!")

                print(f"{defensor.get_especie()} ficou com {max(defensor.get_vida(), 0)} de vida.")
                vez = False
            else:
                print(f"\nRodada {rodada}: vez do {defensor.get_especie()}")

                # Testa cura antes de qualquer movimento
                if random.randint(1, 24) > 14:
                    resultado_cura = defensor.usar_habilidade('cura')
                    print(resultado_cura)
                    print(f"{defensor.get_especie()} ficou com {max(defensor.get_vida(), 0)} de vida. \n")

                ataque_valor = random.randint(1, 24)
                esquiva_valor = random.randint(1, 24)

                if ataque_valor == 24:
                    # Ataque crítico: habilidade especial, não pode esquivar
                    resultado = defensor.usar_habilidade(defensor.get_habilidade(), atacante)
                    print(resultado)
                elif ataque_valor > 18:
                    # Tenta usar habilidade especial, mas pode ser esquivado
                    if esquiva_valor > ataque_valor:
                        print(f"{atacante.get_especie()} esquivou da habilidade especial!")
                    else:
                        resultado = defensor.usar_habilidade(defensor.get_habilidade(), atacante)
                        print(resultado)
                else:
                    # Ataque normal
                    if esquiva_valor > 18:
                        print(f"{atacante.get_especie()} se esquivou do ataque!")
                    else:
                        dano = defensor.atacar(atacante)
                        print(f"{defensor.get_especie()} atacou causando {dano} de dano!")

                print(f"{atacante.get_especie()} ficou com {max(atacante.get_vida(), 0)} de vida.")
                vez = True

            rodada += 1
            input("Pressione Enter para continuar...")

        # Define vencedor
        if(atacante.morrer()):
            vencedor = defensor.get_especie()
        else:
            vencedor = atacante.get_especie()
        print(f'atacante {atacante.get_especie()} vida: {atacante.get_vida()} ataque: {atacante.get_poder()} defesa: {atacante.get_defesa()} atributo: {atacante.get_atributo()}')
        print(f'defensor {defensor.get_especie()} vida: {defensor.get_vida()} ataque: {defensor.get_poder()} defesa: {defensor.get_defesa()} atributo: {defensor.get_atributo()}')
        print(f"\nVencedor: {vencedor}")