# Padrão de Projeto Template Method

## Descrição

Este exemplo demonstra a utilização do padrão de projeto Template Method em Java.

O Template Method define a estrutura principal de um algoritmo em uma classe base, permitindo que subclasses implementem apenas etapas específicas do processo.

No exemplo apresentado, o sistema gera relatórios em diferentes formatos, como PDF e Excel.

O objetivo é comparar:
- uma implementação sem o padrão;
- e outra utilizando Template Method.

---

# Estrutura do Projeto

## `sem_template_method`

Demonstra a implementação sem utilizar o padrão Template Method.

Características:
- Duplicação de código;
- Alto acoplamento;
- Baixo reaproveitamento;
- Manutenção mais difícil;
- Necessidade de alterar várias classes em mudanças simples.

Arquivos:
- `Main.java`
- `RelatorioPDF.java`
- `RelatorioExcel.java`

---

## `com_template_method`

Demonstra a solução utilizando Template Method.

Características:
- Estrutura do algoritmo centralizada;
- Reuso de código;
- Baixa duplicação;
- Maior extensibilidade;
- Melhor manutenção;
- Uso de abstração e polimorfismo.

Arquivos:
- `AbstractRelatorio.java`
- `Main.java`
- `RelatorioPDF.java`
- `RelatorioExcel.java`

---

# Funcionamento do Template Method

A classe abstrata `AbstractRelatorio` define o fluxo principal do algoritmo:

```java
public final void gerarRelatorio() {
    buscarDados();
    processarDados();
    gerarSaida();
}
```

As subclasses implementam apenas as etapas variáveis:
- `processarDados()`
- `gerarSaida()`

Isso garante padronização e reaproveitamento do código comum.

---

# Como Executar

## Requisitos
- Java JDK instalado

---

## Executar exemplo sem Template Method

Entrar na pasta:

```bash
cd sem_template_method
```

Compilar:

```bash
javac *.java
```

Executar:

```bash
java sem_template_method.Main
```

---

## Executar exemplo com Template Method

Entrar na pasta:

```bash
cd com_template_method
```

Compilar:

```bash
javac *.java
```

Executar:

```bash
java com_template_method.Main
```

---

# Conceitos Demonstrados

- Template Method Pattern
- Herança
- Abstração
- Polimorfismo
- Reuso de código
- Padronização de algoritmos
- Princípios SOLID

---

# Tecnologias Utilizadas

- Java
- Programação Orientada a Objetos