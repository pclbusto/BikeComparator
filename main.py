from bs4 import BeautifulSoup
import requests

dir_base = "https://www.canyon.com"

r = requests.get(dir_base+'/es-cl/')
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

diccionario = {}
lista = list()
for a in soup.find_all("a"):
    keys = a.attrs.keys()
    if "class" in keys and "href" in keys:
        if "header__navBarPreloadItem--level4" in a["class"] and "/es-cl/bicicletas" in a["href"]:
            lista.append(a)
            diccionario[a.text] = a["href"]

#for i in diccionario:
#    print(i)

r2 = requests.get(dir_base+diccionario["Neuron AL"])
soup = BeautifulSoup(r2.text, 'html.parser')
lista = list()
for a in  soup.find_all("a"):
    keys = a.attrs.keys()
    if "class" in keys:
        if "productTileDefault__productName" in a["class"]:
            lista.append(a)

for item in lista:
    print(item)


with open("salida.html", "w") as fp:
    for i in lista:
        fp.write(i["href"]+"\n")
