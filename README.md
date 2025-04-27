# 🎬 Bot de Recomendação de Filmes

**Um sistema inteligente de recomendação de filmes baseado em preferências pessoais, utilizando a API do TMDB**

## 📌 Visão Geral

Este projeto analisa os filmes favoritos do usuário e recomenda títulos similares utilizando:
- Análise automatizada de gêneros, diretores e palavras-chave
- Integração com a API do The Movie Database (TMDB)
- Recomendações em tempo real sem base pré-definida

## 🛠️ Tecnologias Utilizadas

- Python 3.9+
- Requests (para chamadas à API)
- Threading (para o spinner de carregamento)
- API TMDB (https://www.themoviedb.org)

## 📋 Pré-requisitos

1. Conta no TMDB (gratuita)
2. Chave de API TMDB
3. Python instalado
4. Biblioteca `requests`

```bash
pip install requests

```

## 🚀 Como Executar o Projeto

### Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/danniellcosta/bot_filme.git
   ```
2. **Configure a API**:
    - Acesse [TMDB API SETTINGS](https://www.themoviedb.org/settings/api)
    - Crie uma chave do tipo "Developer" (gratuita)
    - Edite o **config.py**:
    ```py 
    TMDB_API_KEY = "cole_sua_chave_aqui" 
    ```
3. **Instale as dependências**:
    ```bash
    pip install requests
    ```
4. **Execute o programa**:
    ```bash
    python main.py
    ```
 