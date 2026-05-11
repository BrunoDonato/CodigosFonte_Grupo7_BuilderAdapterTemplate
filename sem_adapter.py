# SEM O ADAPTER
# O jogo precisa falar diretamente com o SDK externo,
# conhecendo detalhes que nao deveria conhecer.

class GamepadSDK:                                   # Classe do fabricante. Nao podemos modificar.
    def pressionar_botao(self, botao: str):
        print(f"SDK: botao '{botao}' pressionado")

    def obter_eixo(self, eixo: str) -> float:
        return 1.0 if eixo == "eixo_x" else -1.0


sdk = GamepadSDK()                                  # O jogo conhece o SDK diretamente, alto acoplamento. Se o SDK mudar, o jogo quebra. ALERTA.

direcao = "direita"                                 # Comando que veio do jogador. O jogo sabe o que quer fazer.

# Logica de traducao espalhada no codigo do jogo, deveria ser responsabilidade de outro. Aqui comeca o problema.
if direcao == "cima":
    sdk.pressionar_botao("D-pad_cima")              # O jogo conhece detalhes internos do SDK.
elif direcao == "baixo":
    sdk.pressionar_botao("D-pad_baixo")
elif direcao == "direita":
    valor = sdk.obter_eixo("eixo_x")                # O jogo sabe que existe "eixo_x". Nao deveria saber disso.
    if valor > 0:
        print("Movendo para direita")
elif direcao == "esquerda":
    valor = sdk.obter_eixo("eixo_x")
    if valor < 0:
        print("Movendo para esquerda")
