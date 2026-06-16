# Country Searcher
 
Site que consome uma API externa de dados geográficos. O usuário digita o nome de um país e recebe informações detalhadas sobre ele diretamente na tela.
 
---
 
## Funcionalidades
 
- Busca de países por nome
- Exibição de dados retornados pela API (capital, população, região, bandeira, etc.)
- Tratamento de erros para países não encontrados ou inválidos
---
 
## Tecnologias Utilizadas
 
| Tecnologia | Função |
|------------|--------|
| Python | Linguagem principal |
| Flask | Framework web para criação da aplicação e rotas |
| Requests | Consumo da API REST externa |
| HTML/CSS | Interface do usuário |
 
---
 
## Conceitos Aplicados
 
- Estrutura de dados Python
- Criação de aplicações web com Flask
- Definição de páginas e endpoints
- Manipulação de formulários HTML
- Consumo de APIs REST
- Tratamento de respostas HTTP
- Tratamento de exceções
- Manipulação de JSON
---
 
## Pré-requisitos
 
- Python 3.x
- Conexão com a internet (para acessar a API externa)
---
 
## Instalação
 
1. Clone o repositório:
```bash
git clone https://github.com/natapereirax-cmd/CountrySearcher.git
cd CountrySearcher
```
 
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
 
---
 
## Como Usar
 
Execute o arquivo principal dentro da pasta `web_page`:
 
```bash
cd web_page
python app.py
```
 
Acesse no navegador: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
 
Digite o nome de um país no campo de busca e pressione Enter. As informações do país serão exibidas na tela.
 
---
 
## Estrutura do Projeto
 
```
CountrySearcher/
├── web_page/
│   └── app.py          # Código principal da aplicação Flask
├── requirements.txt    # Dependências do projeto
└── LEIAME.txt          # Instruções em texto simples
```
