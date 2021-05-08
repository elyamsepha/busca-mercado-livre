import requests
from lxml import html
from bs4 import BeautifulSoup
import re

header = {
	'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
}

pesquisa = input("digite a sua pesquisa no mercado livre: ").replace(' ', '-')

URL = f"https://lista.mercadolivre.com.br/{pesquisa}"

response = requests.get(URL, headers=header)
print("codigo de requesição: ", response.status_code)

content = response.content
site = BeautifulSoup(content, 'html.parser')

titulos = []
precos = []


for titulo in site.find_all('h2', attrs={'class': "ui-search-item__title"}):
	for titu in titulo:
		titulos.append(titu)

p = site.find_all('span', attrs={'class': "price-tag ui-search-price__part"})

for preco in p:
	a = str((preco.find('span', attrs={'class': "price-tag-fraction"}))).replace('<span class="price-tag-fraction">', '')
	b = a.replace('</span>', '')
	precos.append(b)

num = 0
arq = open('itens.txt', 'w')
for c in range(len(titulos)):
	arq.write(f'titulo: {titulos[num]}\npreço: {precos[num]}\n\n')
	num = num + 1
arq.close()