import json
from pathlib import Path

class Config:
    TMDB_API_KEY = "7925adca9f951bddc5dab3a648b1329c"  # Obtenha em https://www.themoviedb.org/settings/api
    LINGUA = "pt-BR"
    TIMEOUT = 10

    # Mapeamento de gêneros para IDs
    GENEROS = {
        "Ação": 28, "Aventura": 12, "Animação": 16,
        "Comédia": 35, "Crime": 80, "Documentário": 99,
        "Drama": 18, "Família": 10751, "Fantasia": 14,
        "História": 36, "Terror": 27, "Música": 10402,
        "Mistério": 9648, "Romance": 10749, "Ficção científica": 878,
        "Thriller": 53, "Guerra": 10752, "Faroeste": 37
    }