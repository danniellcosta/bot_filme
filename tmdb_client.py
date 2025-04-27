import requests
from config import Config

class TMDBClient:
    def __init__(self):
        self.config = Config()
        self.base_url = "https://api.themoviedb.org/3"

    def _make_request(self, endpoint, params=None):
        """Faz requisições à API"""
        params = params or {}
        params["api_key"] = self.config.TMDB_API_KEY
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                timeout=self.config.TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na API: {e}")
            return None

    def buscar_filme(self, titulo):
        """Busca filme por título"""
        params = {
            "query": titulo,
            "language": self.config.LINGUA
        }
        data = self._make_request("search/movie", params)
        if data and data.get("results"):
            return data["results"][0]  # Retorna o primeiro resultado
        return None

    def obter_detalhes(self, filme_id):
        """Obtém detalhes completos de um filme"""
        return self._make_request(f"movie/{filme_id}", {
            "language": self.config.LINGUA,
            "append_to_response": "keywords,credits"
        })

    def obter_recomendacoes(self, filme_id):
        """Busca recomendações baseadas em um filme específico"""
        return self._make_request(f"movie/{filme_id}/recommendations", {
            "language": self.config.LINGUA
        })