from bs4 import BeautifulSoup
import requests

# Fazendo uma requisição para um site
url = "https://quotes.toscrape.com//"
response = requests.get(url)

# Criando um objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extraindo o título da página
titulo = soup.title.text
print("Título da página:", titulo)
