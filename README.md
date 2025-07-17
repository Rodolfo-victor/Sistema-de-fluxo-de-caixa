# 💰 Sistema de Fluxo de Caixa em Python

Este projeto é um sistema de **controle de fluxo de caixa** desenvolvido em **Python puro**, com interface em linha de comando. Ele permite o cadastro, consulta, alteração e exclusão de movimentações financeiras (entradas e saídas), além de gerar relatórios de **fechamento diário** e **balanço por período**.

---

## 🚀 Funcionalidades

- ✅ Cadastro de entradas e saídas com:
  - Número do documento
  - Descrição
  - Valor
  - Data (automática)
- ✅ Operações de:
  - Inclusão
  - Consulta
  - Alteração
  - Exclusão
- 📊 Relatórios:
  - Fechamento diário do caixa
  - Balanço mensal por período (entradas, saídas e saldo)
- 💾 Armazenamento em arquivo `.json` (persistência local)
- 📆 Formato de data: `DD/MM/AAAA`
- 🔐 Validações de entrada e tratamento de erros com `try/except`

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `json` (persistência de dados)
- Módulo `datetime` (data e hora)
- Interface em terminal (`CLI`)

---

## 📦 Como executar o projeto

1. **Clone este repositório:**

```bash
git clone https://github.com/Rodolfo-victor/Sistema-de-fluxo-de-caixa.git
cd sistema-fluxo-caixa

Execute o sistema:

python fluxo_caixa.py
Certifique-se de ter o Python 3 instalado e o terminal configurado corretamente.