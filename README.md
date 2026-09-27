<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Marketing-Pesquisa%20de%20Satisfa%C3%A7%C3%A3o-FF6B00?style=for-the-badge&logo=googleforms&logoColor=white" alt="Marketing">
</p>

<h1 align="center">📊 Pesquisa de Satisfação no Atendimento</h1>

<p align="center">
  Uma aplicação simples em Python para coletar e apurar o grau de satisfação de clientes com o atendimento prestado.
</p>

## 📌 Sobre o projeto

A **Pesquisa de Satisfação no Atendimento** foi desenvolvida para atender à necessidade da empresa de marketing **TudoWeb** de medir o grau de satisfação de seus clientes. O sistema coleta nome, idade e opinião sobre o atendimento de 50 entrevistados, validando a resposta digitada e, ao final, exibindo a quantidade de avaliações recebidas em cada categoria.

O projeto foi criado para praticar estrutura de repetição (`for` e `while`), validação de entrada de dados, estrutura condicional com `match/case` e exibição de resultados em Python. 🐍

## 🎯 Objetivo do sistema

- Coletar nome, idade e opinião de 50 entrevistados sobre o atendimento.
- Validar a opinião informada, aceitando apenas as opções previstas.
- Contabilizar as respostas por categoria de avaliação.
- Exibir ao final a quantidade de respostas "EXCELENTE" e "RUIM".
- Praticar conceitos fundamentais de programação em Python.

## 🛠️ Linguagem utilizada

- **Python 3.10+** (uso de `match/case` para estrutura condicional)

## 📋 Regras de avaliação

O programa aplica as seguintes opções de resposta:

| Opção digitada | Avaliação | Ação |
|-----------------|-----------|------|
| 1 | EXCELENTE | Incrementa o contador de respostas excelentes |
| 2 | BOM | Incrementa o contador de respostas boas |
| 3 | RUIM | Incrementa o contador de respostas ruins |
| Outro valor | Inválido | Exibe aviso e solicita nova digitação |

## ▶️ Como executar

### Pré-requisitos

- Ter o [Python](https://www.python.org/downloads/) 3.10 ou superior instalado.
- Ter acesso a um terminal ou ao Visual Studio Code.

### Execução pelo terminal

1. Clone o repositório:

```bash
git clone https://github.com/Prada-07/pesquisa-de-opinião.git
```

2. Acesse a pasta do projeto:

```bash
cd pesquisa-satisfacao-tudoweb
```

3. Execute o programa:

```bash
python app.py
```

4. Para cada um dos 50 entrevistados, informe o nome, a idade e digite `1`, `2` ou `3` conforme a opinião sobre o atendimento.

## 💻 Exemplo de resultado

```text
Digite o seu nome:
-> Maria

Digite a sua idade:
-> 34

Digite a nota de avaliação
1 para EXCELENTE
2 para BOM
3 para RUIM:
-> 1

...

----------PESQUISA DE AVALIAÇÃO----------

Excelente: 21

Bom: 18

Ruim: 11
```

## 📁 Estrutura do projeto

```text
pesquisa-satisfacao-tudoweb/
├── app.py       # Código principal da pesquisa de satisfação
└── README.md    # Documentação do projeto
```

## ℹ️ Observação

O programa não armazena os dados dos entrevistados em arquivo ou banco de dados; nome e idade são coletados apenas para simular a coleta completa da pesquisa, e a apuração final considera somente as respostas de avaliação.

## 👤 Autor

Desenvolvido por **Leonardo Moreira Prada**.

[![GitHub](https://img.shields.io/badge/Seu%20Usu%C3%A1rio-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SEU-USUARIO)

---

<p align="center">📊 Projeto desenvolvido para fins educacionais.</p>