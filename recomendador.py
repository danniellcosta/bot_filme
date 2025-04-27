from collections import defaultdict
import statistics

class Recomendador:
    def __init__(self, client):
        self.client = client

    def _extrair_perfil(self, filmes):
        """Analisa os filmes e cria um perfil"""
        perfil = {
            "generos": defaultdict(int),
            "palavras_chave": defaultdict(int),
            "anos": [],
            "diretores": defaultdict(int)
        }

        for filme_info in filmes:
            detalhes = self.client.obter_detalhes(filme_info["id"])
            if not detalhes:
                continue

            # Gêneros
            for genero in detalhes.get("genres", []):
                perfil["generos"][genero["name"]] += 1

            # Palavras-chave
            for keyword in detalhes.get("keywords", {}).get("keywords", []):
                perfil["palavras_chave"][keyword["name"]] += 1

            # Ano
            if detalhes.get("release_date"):
                perfil["anos"].append(int(detalhes["release_date"][:4]))

            # Diretores
            for pessoa in detalhes.get("credits", {}).get("crew", []):
                if pessoa["job"] == "Director":
                    perfil["diretores"][pessoa["name"]] += 1

        return perfil

    def recomendar(self, filmes_usuario, n=5):
        """Gera recomendações personalizadas"""
        # 1. Busca os filmes informados
        filmes = []
        for titulo in filmes_usuario:
            filme = self.client.buscar_filme(titulo)
            if filme:
                filmes.append(filme)

        if not filmes:
            return []

        # 2. Analisa o perfil
        perfil = self._extrair_perfil(filmes)

        # 3. Prepara parâmetros de busca
        generos_principais = sorted(
            perfil["generos"].items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        params = {
            "language": self.client.config.LINGUA,
            "sort_by": "popularity.desc",
            "with_genres": ",".join([str(self.client.config.GENEROS[g[0]]) for g in generos_principais]),
            "primary_release_year": statistics.median(perfil["anos"]) if perfil["anos"] else None,
            "include_adult": False
        }

        # 4. Busca recomendações
        resultados = self.client._make_request("discover/movie", params)
        if resultados and resultados.get("results"):
            return resultados["results"][:n]
        
        return []