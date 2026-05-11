# COM O ADAPTER
# O jogo so conhece a interface simples. O Adapter cuida da traducao.

from abc import ABC, abstractmethod

class ControladorPersonagem(ABC):   # Qualquer coisa que queira ser um controlador de personagem no 
    @abstractmethod                    # jogo precisa ter um metodo chamado mover que recebe uma direcao.
    def mover(self, direcao: str): pass

class GamepadSDK:                                   # SDK Enterno, identico ao do codigo sem Adapter,
    def pressionar_botao(self, botao: str):         # pois e o codigo do fabricante.
        print(f"SDK: botao '{botao}' pressionado")

    def obter_eixo(self, eixo: str) -> float:
        return 1.0 if eixo == "eixo_x" else -1.0

class GamepadAdapter(ControladorPersonagem):        # ADAPTER, herda de ControladorPersonagem, portanto esta concordando
    def __init__(self, sdk: GamepadSDK):            # em utilizar o mover() exigido por ele, e passa a ser tratado como um
        self._sdk = sdk                             # controlador qualquer.

    def mover(self, direcao: str):                      # Entao quando o jogo chamar o mover com a direcao,
        if direcao == "cima":                           # este e o metodo que sera executado.
            self._sdk.pressionar_botao("D-pad_cima")
        elif direcao == "baixo":                          # Traducao acontecendo. O jogo em si nao ve nada acontecendo.
            self._sdk.pressionar_botao("D-pad_baixo")      # Se o jogo disse "cima", o adapter pega isso e traduz para a lingua
        elif direcao == "direita":                          # que o SDK entende.
            valor = self._sdk.obter_eixo("eixo_x")
            if valor > 0:
                print("Movendo para direita")
        elif direcao == "esquerda":
            valor = self._sdk.obter_eixo("eixo_x")
            if valor < 0:
                print("Movendo para esquerda")


# O jogo nao sabe nada sobre o SDK, baixo acoplamento
controlador = GamepadAdapter(GamepadSDK())                  # USO. Neste ponto o controlador e tratado como um 
controlador.mover("direita")
controlador.mover("cima")
