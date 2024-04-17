import pprint
import requests
from bs4 import BeautifulSoup


#url que le vamos hacer web scraping
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


#hacemos un get requests para obtener el contenido de la pagina web
response = requests.get(URL)
website_html=response.text


# Crea un objeto BeautifulSoup
soup=BeautifulSoup(website_html, "html.parser")


#desemos Todos los titulos de las peliculas que inspeccionando la pagina se encuntran en el tag "h3" con la clase "title"
all_movies=soup.find_all(name="h3", class_="title")
# pprint.pp(all_movies)


#obtenemos el text de todos los h3 tags, itirenando sobre la lista de elementos "all_movies" y guardando los nombres en una lista
movies_titles=[tag.get_text() for tag in all_movies]
# pprint.pp(movies_titles)


#imprimiendo la lista alreves es decir de atras hacia delante
movies_titles_backwards=movies_titles[::-1]


#guardando la informacion en formato file.txt
with open("movies.txt", "w") as file:
    
    #movies_titles_backwards es una lista por lo que itirenamos en la lista para guardar linea por linea "str"
    for movies in movies_titles_backwards:
        file.write(movies)
        file.write("\n") #salto de linea