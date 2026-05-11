class Pedido:
    def __init__(self, builder):
        self.cliente = builder._cliente
        self.endereco = builder._endereco
        self.pagamento = builder.pagamento

    def descreve(self):
        print(f"Cliente: {self.cliente} Endereço: {self.endereco} Pagamento: {self.pagamento}")

    class Builder:
        def __init__(self):
            self._cliente = None
            self._endereco = None
            self._pagamento = None

        def cliente(self, cliente):
            self._cliente = cliente
            return self

        def endereco(self, endereco):
            self._endereco = endereco
            return self

        def pagamento(self, pagamento):
            self._pagamento = pagamento
            return self

        def build(self):
            return Pedido(self)


# Uso:
pedido = (Pedido.Builder()
          .cliente("João")
          .endereco("Rua A, 123")
          .pagamento("PIX")
          .build())

pedido.descreve()