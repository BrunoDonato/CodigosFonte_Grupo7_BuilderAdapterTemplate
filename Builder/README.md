# Padrão de Projeto Builder

## Descrição

Este exemplo demonstra a utilização do padrão de projeto Builder em Python.

O padrão Builder é utilizado para construir objetos complexos passo a passo, separando a lógica de construção da representação final do objeto.

No exemplo apresentado, um pedido é criado de forma gradual, permitindo configurar diferentes atributos antes da construção final do objeto.

Esse padrão melhora a legibilidade do código e facilita a criação de objetos com muitos parâmetros.

---

## Estrutura do Arquivo

### `Builder.py`

Implementa a criação de um objeto `Pedido` utilizando o padrão Builder.

O objeto é montado em etapas:
- Cliente;
- Endereço;
- Forma de pagamento.

Ao final, o método `build()` retorna o objeto completamente construído.

---

## Funcionamento

O Builder permite encadear chamadas de métodos para configurar o objeto antes de criá-lo.

Exemplo utilizado no código:

```python
pedido = (Pedido.Builder()
          .cliente("João")
          .endereco("Rua A, 123")
          .pagamento("PIX")
          .build())
```

Esse processo torna a construção mais organizada e compreensível.

---

## Como Executar

### Requisitos
- Python 3 instalado

### Executar o exemplo

```bash
python Builder.py
```

---

## Conceitos Demonstrados

- Builder Pattern
- Construção gradual de objetos
- Encadeamento de métodos
- Separação da lógica de construção
- Programação Orientada a Objetos

---

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos