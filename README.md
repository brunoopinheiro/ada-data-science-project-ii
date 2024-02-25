# __ADA-Data-Science-Project-II__
Repository made initially as a project for the Data Science course at Ada Tech | Santander Coders.

# Dataset URL:
O dataset em questão é bastante grande para ser hospedado no github, mas pode ser obtido no link abaixo: <br>
[Scryfall Default Cards Dataset](https://data.scryfall.io/default-cards/default-cards-20240216220537.json)

# Instalando e Executando o projeto
Dependências:
- Python 3.12 ou superior.
- Demais dependencias instaladas via `pip`.
  - [requirements.txt](requirements.txt)

Depois de clonar o repositório:
- Utilizando o `powershell`, navegue até o diretório raiz do projeto.
- Inicie um ambiente virtual.
  - `python -m venv .venv`
  - `.\.venv\Scripts\activate`
- Instale as dependências com `pip`.
  - `pip install -r .\requirements.txt`
- Coloque o arquivo .json baixado anteriormente na pasta `.\datasets`.

O _notebook_ de análise dos dados é chamado [mtg_analysis](mtg_analysis.ipynb), e contém a visualização dos dados e criação dos gráficos.

O _notebook_ [data_consistency_analysis](data_consistency_analysis.ipynb) contém apenas alguns testes feitos para na etapa de análise de consistência dos dados.

o módulo [get_dataset.py](datasets\get_dataset.py) possui as funções implementadas para obtenção e tratamento dos dados do projeto.


# Futuras Implementações:
- [ ] CLI interface para obtenção do dataset.
- [ ] CLI interface para execução e exibição de alguns gráficos mais comuns.
- [ ] Importação de arquivo de deck, com chamada à API do Scryfall para obtenção dos dados completos de cada carta.
- [ ] Análise de deck list.
- [ ] Sugestões de alteração em deck list.