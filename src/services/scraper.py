import requests
from bs4 import BeautifulSoup



URL = 'https://www.metrovalencia.es/horarios.mobi.php'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())


#TODO https://www.youtube.com/watch?v=Bg9r_yLk7VY