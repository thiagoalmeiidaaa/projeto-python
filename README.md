# Projeto: Apache Spark com Delta Lake e Apache Iceberg

Trabalho desenvolvido para a disciplina **Engenharia de Dados** do curso de Engenharia de Software.

## 📁 Estrutura do Projeto

```
C:\Projetos\apache-spark-delta-iceberg
├── README.md
├── pyproject.toml
├── mkdocs.yml
├── data/
│   └── sample_data.csv
├── src/
│   ├── delta_operations.py
│   └── iceberg_operations.py
├── notebooks/
│   ├── delta_scenario.ipynb
│   └── iceberg_scenario.ipynb
├── mkdocs/
│   ├── delta.md
│   └── iceberg.md
```

---

## ⚙️ Requisitos

- Python 3.10+
- Java 8+
- [Poetry](https://python-poetry.org/docs/#installation)
- Spark 3.5.0+
- Delta Lake & Apache Iceberg

---

## 🧪 Instalação do Ambiente

### 1. Instale o Poetry
```bash
pip install poetry
```

### 2. Vá até a pasta do projeto
```bash
cd C:\Projetos\apache-spark-delta-iceberg
```

### 3. Instale as dependências
```bash
poetry install
```

### 4. Ative o ambiente virtual
```bash
poetry shell
```

---

## 🚀 Executando os Notebooks

### 1. Inicialize o Jupyter Lab
```bash
jupyter lab
```

### 2. Acesse os notebooks em:
- `notebooks/delta_scenario.ipynb`
- `notebooks/iceberg_scenario.ipynb`

---

## 🧾 Explicação do Projeto

- O projeto simula um cenário de e-commerce.
- As tabelas `vendas` e `produtos` são carregadas a partir de um `.csv`.
- Cada notebook apresenta comandos DDL e manipulação dos dados.
- Os scripts `.py` executam as mesmas ações via código puro PySpark.

---

## 📚 Documentação

A documentação pode ser visualizada usando o [MKDocs](https://www.mkdocs.org/):

### Para visualizar:
```bash
mkdocs serve
```

Depois acesse em `http://127.0.0.1:8000`

---

## 👥 Autores

- Gabriel Frello
- Thiago Almeida
- Gabriel Boelter

