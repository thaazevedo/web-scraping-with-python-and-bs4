import requests
from bs4 import BeautifulSoup
from info_filmes.models import FilmesInfos

class ScrapingFilmes():
    def get_infos(self):
        
        # Realizando requisição:
        req = requests.get(url="https://www.imdb.com/chart/moviemeter/")

        # Carregando o site com o BeautifulSoup:
        site = BeautifulSoup(req.content, 'html.parser')
        # print(site)

        # Procurando pelo elemento que possui as informações requisitadas:
        tabela_filmes = site.find('table', attrs={'class': 'chart full-width'}).find('tbody', attrs={'class': 'lister-list'}).find_all('tr')
        # print(tabela_filmes)

        # Pegando as informações requisitadas:

        lista_filmes = []
        for filme in tabela_filmes:

            # Link para o filme no site da imdb:
            link_filme = "https://www.imdb.com"+filme.find('td', attrs={'class': 'posterColumn'}).find('a').get('href')
            # print(link_filme)

            # Link para o poster do filme:
            link_poster = filme.find('td', attrs={'class': 'posterColumn'}).find('a').find('img').get('src')
            # print(link_poster)
            
            # Título do filme formado pelo nome do filme + ano de lançamento do mesmo:
            nome = filme.find('td', attrs={'class': 'titleColumn'}).find('a').text
            ano_lan = filme.find('td', attrs={'class': 'titleColumn'}).find('span').text
            titulo = nome + ano_lan
            # print(titulo)

            # Ranking do filme da IMDb:
            try:
                ranking = filme.find('td', attrs={'class': 'ratingColumn imdbRating'}).find('strong').text
            except:
                ranking = "-"
            # print(ranking)

            infos_filme = {
                "Link do Filme": link_filme,
                "Pôster do Filme": link_poster,
                "Título do Filme": titulo,
                "Ranking": ranking
            }
            lista_filmes.append(infos_filme)
        # print(infos_filme)
        print(lista_filmes)

        for i in lista_filmes:
            FilmesInfos.objects.create(titulo=i["Título do Filme"], link_filme=i["Link do Filme"], link_poster=i["Pôster do Filme"], nota=i["Ranking"])

        
   
def run():
    a = ScrapingFilmes()
    a.get_infos()

    