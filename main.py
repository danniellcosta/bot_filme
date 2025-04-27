from tmdb_client import TMDBClient
from recomendador import Recomendador
from interface import Interface

def main():
    print("=== 🍿 Sistema de Recomendação Automática de Filmes ===")
    
    # Inicializa componentes
    client = TMDBClient()
    recomendador = Recomendador(client)
    interface = Interface()
    
    # 1. Obtém filmes do usuário
    filmes_usuario = interface.obter_filmes()
    
    if not filmes_usuario:
        print("❌ Nenhum filme informado.")
        return
    
    # 2. Gera recomendações COM indicador de carregamento
    @interface.com_carregamento
    def gerar_recomendacoes():
        return recomendador.recomendar(filmes_usuario)
    
    recomendacoes = gerar_recomendacoes()
    
    # 3. Mostra resultados
    interface.mostrar_recomendacoes(recomendacoes)


if __name__ == "__main__":
    main()