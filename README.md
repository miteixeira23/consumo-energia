# ⚡ Calculadora de Consumo Elétrico

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github\&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Elétrica-yellow)

## 📌 Sobre o projeto

A **Calculadora de Consumo Elétrico** é um programa desenvolvido em **Python** que permite estimar o consumo mensal de energia elétrica de um aparelho.

O sistema solicita ao usuário:

* 🔌 Nome do aparelho;
* ⚡ Potência do aparelho em watts (W);
* ⏱️ Tempo médio de uso diário em horas.

Com essas informações, o programa calcula o consumo estimado em **kWh por mês** e o **custo mensal da energia elétrica**, considerando o valor de **R$ 0,65 por kWh**.

## 🐍 Linguagem utilizada

O projeto foi desenvolvido utilizando a linguagem:

**Python 🐍**

## 🧮 Fórmula utilizada

Para calcular o consumo mensal, é utilizada a seguinte fórmula:

```text
Consumo mensal = (Potência × Horas por dia × 30) / 1000
```

O resultado é apresentado em **kWh/mês**.

### 💰 Cálculo do custo

O custo mensal é calculado considerando:

```text
Custo mensal = Consumo mensal × 0,65
```

Onde **R$ 0,65** é o valor considerado para cada kWh.

## ▶️ Como executar o programa

### 1. Tenha o Python instalado

O projeto utiliza Python 3.x.

### 2. Abra o terminal na pasta do projeto

Acesse a pasta:

```text
consumo-energia
```

### 3. Execute o programa

No terminal, digite:

```bash
python app.py
```

## 💻 Exemplo de utilização

```text
====================================
   CALCULADORA DE CONSUMO ELÉTRICO
====================================

Digite o nome do aparelho: Geladeira
Digite a potência do aparelho em watts (W): 60
Digite o tempo médio de uso diário (em horas): 24

====================================
            RESULTADO
====================================
Aparelho: Geladeira
Consumo mensal: 43.20 kWh/mês
Custo mensal: R$ 28.08/mês
```

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🐙 GitHub
* 🔗 Git
* ⚡ Cálculo de consumo de energia

## 🎯 Objetivo do projeto

O objetivo deste projeto é desenvolver uma aplicação simples para estimar o consumo de energia elétrica de aparelhos e praticar conceitos básicos de programação em Python.

## 🚀 Possíveis melhorias

* 💰 Permitir que o usuário informe o valor do kWh;
* 📋 Calcular o consumo de vários aparelhos;
* 📊 Mostrar o consumo total;
* 💵 Calcular o custo total mensal;
* 🖥️ Criar uma interface gráfica;
* 🌐 Transformar o projeto em uma aplicação web.

## 👩‍💻 Autora

**Michelle Teixeira**

Projeto desenvolvido como parte de um programa de iniciação em tecnologia.
