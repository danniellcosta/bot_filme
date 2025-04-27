import sys
import time
from threading import Thread
from itertools import cycle

class Interface:
    @staticmethod
    def obter_filmes():
        """Pede os filmes favoritos ao usuário"""
        print("\n🎬 Digite seus filmes favoritos (1 por linha, 'fim' para terminar):")
        filmes = []
        while True:
            entrada = input("> ").strip()
            if entrada.lower() == 'fim':
                break
            if entrada:
                filmes.append(entrada)
        return filmes

    @staticmethod
    def mostrar_recomendacoes(recomendacoes):
        """Exibe as recomendações"""
        if not recomendacoes:
            print("\n❌ Não foi possível gerar recomendações.")
            return

        print("\n🎭 Recomendações baseadas nos seus filmes:")
        for i, filme in enumerate(recomendacoes, 1):
            ano = filme.get("release_date", "")[:4]
            print(f"{i}. {filme['title']} ({ano})")
            print(f"   ⭐ Avaliação: {filme.get('vote_average', '?')}/10")
        
    @staticmethod
    def _mostrar_carregamento(ativo):
        """Mostra um spinner de carregamento (usado em thread separada)"""
        spinner = cycle(['⣾','⣽','⣻','⢿','⡿','⣟','⣯','⣷'])
        while ativo[0]:
            sys.stdout.write('\r' + next(spinner) + ' Processando...')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * 20 + '\r')  # Limpa a linha

    @staticmethod
    def com_carregamento(funcao):
        """Decorador para mostrar carregamento durante execução"""
        def wrapper(*args, **kwargs):
            ativo = [True]
            t = Thread(target=Interface._mostrar_carregamento, args=(ativo,))
            t.start()
            
            try:
                resultado = funcao(*args, **kwargs)
            finally:
                ativo[0] = False
                t.join()
            
            return resultado
        return wrapper