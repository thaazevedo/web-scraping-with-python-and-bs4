# Projeto tutorial de Web Scraping usando Python, Django, RunScript e BeautifulSoup

## Definições:
   
  - [Python](https://docs.python.org/pt-br/3/): Python é uma linguagem Open-Source de propósito geral usado bastante em data science, machine learning, desenvolvimento de web, desenvolvimento de aplicativos, automação de scripts, fintechs e mais.
  - [Request](https://docs.python-requests.org/en/latest/): A biblioteca de requests é uma parte integrante do Python para fazer solicitações HTTP para uma URL especificada. Elas são usadas em tecnologias como APIs REST ou Web Scrapping, no caso de solicitações. O request também permite adicionar conteúdos quando for fazer a solicitação ou ainda um acesso aos dados retornados pela resposta da requisição.
  - [Web Scraping](https://rockcontent.com/br/blog/web-scraping/): Uma espécie de “garimpo” da internet que envolve a extração de informações relevantes de determinado site para posterior análise. Esses dados serão usados para aprimorar a tomada de decisões com maior chance de acerto e sucesso. É possível fazer o mesmo processo manualmente, mas quando se fala de Web Scraping a ideia é automatizar o trabalho usando bots. Assim, é possível coletar um número muito maior de dados em uma curta fração do tempo.
  - [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/): é uma biblioteca Python de extração de dados de arquivos HTML e XML. Ela funciona com o seu interpretador (parser) favorito a fim de prover maneiras mais intuitivas de navegar, buscar e modificar uma árvore de análise (parse tree). Ela geralmente economiza horas ou dias de trabalho de programadores ao redor do mundo. [Construa um Web Scraper com Python](https://realpython.com/beautiful-soup-web-scraper-python/)
  - [Django](https://tutorial.djangogirls.org/pt/installation/): é um framework para aplicações web gratuito e de código aberto, escrito em Python. Um web framework é um conjunto de componentes que ajuda você a desenvolver sites de forma mais rápida e fácil.
  - [RunScript](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html): uma extensão do django utilizada para rodar os scripts quando existe no mesmo query no banco com o uso do ORM do django.
  - O [ORM](https://www.alura.com.br/artigos/django-query-sets-e-orm?gclid=CjwKCAjwlcaRBhBYEiwAK341jRQAGStqghnRLXG7CPForomrMgGZ7G6z7_gGUZXIusR19EMjQuhfvhoCUzkQAvD_BwE) é conhecido como o mapeador objeto-relacional do Django. Em outras palavras, no lugar de realizar uma ação direta no banco de dados com código SQL por exemplo, utilizamos o ORM como ponte de comunicação entre o banco e a aplicação;


## Pratique:
  1. Preparando o ambiente:
  - Inicialmente, seguindo o [tutorial](https://tutorial.djangogirls.org/pt/installation/) de instalação, instale o python conforme o seu sistema operacional. Seguindo o mesmo tutorial, escolha um editor de código de sua preferência e faça a instalação;
  - Depois, dentro do seu editor de código,crie um diretório para o desenvolvimento desse projeto;
  - Após isso, dentro da pasta tutorial, crie o ambiente virtual (seguindo o tutorial acima e confirme o seu sistema operacional) e ative o mesmo com o comando;
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/6cdd62fb-eca5-4804-9857-b2d04fd8f414">
    </p>

  - Depois, finalizada a instalação do python e a criação do ambiente virtual, instale o Requests, Django, o Django Extensions e o Beautiful Soup conforme os comandos abaixo:
```
pip install requests
python -m pip install Django
pip install django-extensions
pip install bs4
```
  - Após isso temos a preparação inicial do projeto finalizada!

  2. Iniciando o projeto Django:
  - Com o ambiente virtual ativado, inicie o projeto django com o comando abaixo:
``
django-admin startproject filmes . 
``
  - Assim ficará a base do projeto:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/486a4ab7-de40-4c1f-abbb-7b8248ad803e">
    </p> 

  - Ao seguir os passos presentes nesse [tutorial](https://tutorial.djangogirls.org/pt/django_start_project/), altere no arquivo settings.py as linhas contendo o TIME_ZONE e LANGUAGE_CODE, para que fiquem como abaixo:
```
TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-BR'
```

  - Ainda em settings.py, adicione o import do os, juntamente ao import já existente. Logo, seu código ficará assim:
```
from pathlib import Path
import os
```
 
  - Ainda no arquivo de settings.py, procure a variável STATIC_URL e, abaixo dela, adicione outra, STATIC_ROOT, conforme abaixo:
```
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

  - Ainda no arquivo de settings.py, adicione o seguinte trecho no final do arquivo, responsável por determinar o banco de dados que usaremos para salvar nossas informações. No caso, utilizaremos o dbsqlite3, o padrão do Django;
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/55112541-4fe9-4ffd-9e7e-f03195d181fd">
    </p>

  - Adicione também no settings, mais precisamente no conjunto INSTALLED_APPS, o django_extensions que será usado para execução do script de Web Scraping;
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/5fb9b1ea-067d-4760-b82e-09c879c58bb5">
    </p>

  - Depois, vamos rodar as migrações iniciais do django. Estando no mesmo nível onde está localizado o arquivo manage.py, rode o seguinte comando:
``
python manage.py migrate
``
  - O django permite também a criação de um usuário, execute o seguinte comando e siga os passos:
``
python manage.py createsuperuser
``

  - Como forma de verificar o funcionamento inicial do projeto django, rode o seguinte comando, ainda no mesmo nível do manage.py:
``
python manage.py runserver
``
  - Caso seu projeto esteja funcional, você terá a seguinte saída no seu terminal:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/b2c64f85-ec8d-4162-9edb-2c12121b8dd4">
    </p>

  - Poderá ver também, acessando endereço `http://127.0.0.1:8000` no seu navegador com o comando python manage.py runserver rodando:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/b28bf2a8-ddf7-41d2-bacf-7f099fdea908">
    </p>
  - Ao acessa o endereço `http://127.0.0.1:8000/admin` no seu navegador, você poderá acessar com o usuário e a senha criada pelo comando python manage.py createsuperuser:
   <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/2e487151-0c36-43aa-978d-c5f289b2abd3">
    </p>

  3. Criando o script para Web Scraping:
  - No mesmo nível da pasta de ambiente virtual, crie o diretório scripts com um arquivo chamado get_filmes.py dentro do diretório:
   <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/0d7ebfcd-da10-479d-962b-7125c8cba308">
    </p>
    
  - Seguindo o exemplo demonstrado no [Tutorial](https://realpython.com/beautiful-soup-web-scraper-python/), mais precisamente a etapa chamada de “Inspect the Site Using Developer Tools” analise a página localizada no endereço `https://www.imdb.com/chart/moviemeter/` mais precisamente a parte que contém a tabela de filmes;
   <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/be258074-fe44-4dba-9352-78684cd54f1d">
    </p>
    
  - Para a montagem do script em get_filmes, usaremos uma estrutura para possibilitar a execução do script com e extensão runscript (ATENÇÃO!! Para funcionar, necessita ter a função def run() e estar dentro de uma pasta scripts);
   <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/7b824c45-7d51-46a3-ba7e-333a47c63110">
    </p>

  - Após a análise, inicie o processo de Web Scraping, seguindo modelo acima, como exemplo o mesmo link sobre o assunto acima, faça a requisição utilizando a biblioteca requests e a retirada das seguintes informações com o uso do Beautiful Soup:
```
Link do filme;
Imagem do pôster do filme;
Título do filme (contendo nome do filme e ano de lançamento do mesmo);
Nota do filme obtida pela avaliação do IMDb (ATENÇÃO!! Nem todos os filmes possuem avaliações no site, os que não tiverem, substitua a avaliação por um “-”).
```
  - Depois, monte uma lista com as informações obtidas assunto acima;
  - Para executar o script você deverá utilizar o comando (trocando get_filmes pelo nome que deu ao arquivo em scripts):
``python manage.py runscript get_filmes``

  - Depois, pause a construção do script de Web Scraping. Vamos a construção do modelo com uso do Django;

  4. Criando seu app Django:

  - No mesmo nível do arquivo manage.py, execute o seguinte comando:
``python manage.py startapp info_filmes``

  - Agora, sua raiz de diretórios, deverá ficar assim:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/7ea00892-8a3a-48ec-bbaa-a732b22f7a7e">
    </p>

  - No arquivo settings.py, localizado em filmes, adicione ao bloco INSTALLED_APPS, o nome do seu app iniciado e o arquivo ficará assim:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/a37f39c5-5d0d-4b2d-9454-8465225c8613">
    </p>

  - No arquivo models.py, localizado em info_filmes, vamos criar nosso modelo, contendo as informações que queremos salvar sobre os filmes:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/d0d2bb18-75ec-4bd4-8e70-56f7d08bbf01">
    </p>

  - De forma bem resumida no código acima, temos as seguintes informações:
```
class FilmesInfos: determina uma classe;
CharField: determina um campo que pode ser considerado uma string, no caso o tamanho máximo dela será 100 (max_length=100) ou 255 (max_length=255). Esse último representa o tamanho máximo do CharField;
TextField: campo também usado para armazenar strings, porém que tenham mais que o max_length=255 (determinado por CharField);
O método def__str__(self), representa o retorno para essa chamada;
```

  - Para mais [informações](https://docs.djangoproject.com/en/4.0/ref/models/fields/) sobre os fields django;
  - No mesmo nível que o arquivo manage.py, atualize suas migrações para aplicar o modelo criado, com o comando abaixo: ``python manage.py makemigrations info_filmes``. Você deverá ver a seguinte saída:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/ecde0179-190e-40f3-84f4-d14ea8666a3a">
    </p>

  - Depois execute o seguinte comando: ``python manage.py migrate info_filmes``. Você deverá ver a seguinte saída:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/0f59e7a1-66c1-4ec0-b6e9-a5fc73ed7691">
    </p>

  - Após isso, em admin.py, adicione o código, responsável por adicionar ao painel admin do django, o modelo recém criado:
     <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/4798e4fe-6c62-4dd7-b8d6-f57a55113750">
    </p>

  - Dessa forma, ao rodar o comando ``python manage.py runserver`` novamente e acessar o endereço ``http://127.0.0.1:8000/admin``, ao clickar em Filmes infoss, você verá que não possuímos itens desse modelo no banco de dados: 
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/4f024952-e7f2-4529-918c-09c859b72c39">
    </p>

  - Então, vamos adicionar os itens tratados e retirados com web scraping ao nosso banco de dados, na próxima etapa

  5. Criando filmes obtidos com web Scraping

  - De volta ao arquivo script.py em script, adicione o import do modelo criado: ``from info_filmes.models import FilmesInfos``
  - Desenvolva também, um trecho de código que cadastre no banco de dados as informações obtidas dos filmes e colocadas em lista, utilizando o mecanismo de [query](https://www.alura.com.br/artigos/django-query-sets-e-orm?gclid=CjwKCAjwlcaRBhBYEiwAK341jRQAGStqghnRLXG7CPForomrMgGZ7G6z7_gGUZXIusR19EMjQuhfvhoCUzkQAvD_BwE) do django, mais especificamente o create;

  6. Finalizando o projeto!!
  - Após a criação da query de create, execute novamente seu script com o comando runscript: ``python manage.py runscript get_filmes``
  - Caso dê certo o cadastro das informações, ao executar novamente o comando ``python3 manage.py runserver`` a acessar o endereço ``http://127.0.0.1:8000/admin/`` e clickar em info_filmes, deve-se observar a existências de novas informações, como abaixo:
    <p float="center">
      <img src="https://github.com/thaazevedo/web-scraping-with-python-and-bs4/assets/76017955/0d58cc87-fe28-4493-bd19-5b05f406efb3">
    </p>  

