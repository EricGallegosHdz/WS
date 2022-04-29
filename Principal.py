# Web scrapping principal
import os
from openpyxl import Workbook

try:
    from bs4 import BeautifulSoup as bs
    from googlesearch import search
    # print("Librerias instaladas")
except ImportError:
    os.system("pip install googlesearch-python")
    os.system("pip install beautifulsoup4")
    print("Instalando biblioteca de busqueda de google y beautifulsoup4... Ejecute de nuevo")
    # Principal es el nombre del archivo actual
    os.system("python Principal.py")

import requests
import re
import Imagenes
import Busqueda_inf
import Direcciones_URL
from Direcciones_URL import Artista, path, lista_dURL
#from Busqueda_inf import Lista_tel, Lista_correo, Lista_naci, Lista_head, p1, p2, p3

#Inicializando listas
listaURL=[]
lista_image=[]

if __name__ == "__main__":
    Direcciones_URL.Almacenar_dURL()
    Direcciones_URL.GuardarHTML_dURL()

    print("Buscando informacion relacionada a: ", Artista, "...\n")

    dirpath=path+"/"+Artista+"/parrafos"
    for nUrl in range(len(lista_dURL)):
        Busqueda_inf.buscarP(lista_dURL[nUrl], nUrl, dirpath)
    for nUrll in range(0, len(lista_dURL)):
        Busqueda_inf.buscarInfdeP(dirpath, nUrll)

    dirpath=path+"/"+Artista+"/parrafosh"
    for nUrl in range(len(lista_dURL)):
        Busqueda_inf.buscarH(lista_dURL[nUrl], nUrl, dirpath)
    for nUrll in range(0, len(lista_dURL)):
        Busqueda_inf.buscarInfdeH(dirpath, nUrll)

#    Busqueda_inf.OpenWeather()
    Busqueda_inf.Excel()

    urlfile = open(path+"/"+Artista+"/Direcciones_URL.txt","r")
    for line in urlfile:
        u=line.rstrip()
        listaURL.append(u)
    urlfile.close()

    n=0
    while listaURL[n].startswith("https://www.youtube") or listaURL[n].startswith("https://twitter"):
        n+=1
    else:
        Imagenes.buscarImg(listaURL[n])


    for posImg in range(3):
        Imagenes.guardarImg(posImg)
