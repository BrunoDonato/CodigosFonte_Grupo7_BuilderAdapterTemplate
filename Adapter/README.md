# Padrão de Projeto Adapter

## Descrição

Este exemplo demonstra a utilização do padrão de projeto Adapter em Python.

O objetivo do Adapter é permitir que classes com interfaces incompatíveis trabalhem juntas, funcionando como um intermediário responsável por traduzir chamadas entre o sistema principal e uma biblioteca externa.

No exemplo apresentado, um jogo precisa utilizar um SDK externo de gamepad. Sem o Adapter, o jogo fica fortemente acoplado ao SDK, conheendo detalhes internos que não deveriam fazer parte da lógica principal.

Com o Adapter, o jogo passa a utilizar apenas uma interface simples e padronizada, enquanto o Adapter realiza toda a tradução necessária para o SDK externo.

---

## Estrutura dos Arquivos

### `sem_adapter.py`

Demonstra o problema sem utilizar o padrão Adapter.

Características:
- Alto acoplamento;
- O jogo conhece detalhes internos do SDK;
- A lógica de tradução fica espalhada pelo código;
- Alterações no SDK podem quebrar o sistema.

### `com_adapter.py`

Demonstra a solução utilizando o padrão Adapter.

Características:
- Baixo acoplamento;
- O jogo utiliza apenas uma interface simples;
- O Adapter centraliza a tradução das chamadas;
- Mudanças no SDK afetam apenas o Adapter.

---

## Como Executar

### Requisitos
- Python 3 instalado

### Executar exemplo sem Adapter

```bash
python sem_adapter.py
```

### Executar exemplo com Adapter

```bash
python com_adapter.py
```

---

## Conceitos Demonstrados

- Adapter Pattern
- Baixo acoplamento
- Encapsulamento de dependências externas
- Separação de responsabilidades
- Interface de adaptação

---

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos
