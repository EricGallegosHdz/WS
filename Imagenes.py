#Imagenes.py
import requests
import os
from Direcciones_URL import Artista, path
from bs4 import BeautifulSoup as bs

#Inicializar una lista
txtImg=[]

def buscarImg(link):

    #Verificar si la carpeta donde se guardaran las imagenes existe
    try:
        os.mkdir(path+"/"+Artista+"/Imagenes")
        print("Creando carpeta: Imagenes\n")
    except:
        print("La carpeta: Imagenes ya existe")
        op=input("Desea sobreescribir los archivos? (y/n): ")
        op.lower()
        if op=="y" or op=="yes":
            print()
        else:
            exit()
    print("Buscando direcciones URL de las imagenes...\n")

    #Busca todas las etiquetas <img> de un html en una direccion URL
    page=requests.get(link)
    soup=bs(page.content, "html.parser")
    #po es una lista con todas las coincidencias de la etiqueta <img>
    po=soup.find_all("img")
    #print(len(po))
    #Se abre un archivo en el cual se guardaran las direcciones URL de cada imagen
    fo=open(path+"/"+Artista+"/Imagenes/linking.txt", "w")
    for nParrafo in range(len(po)):
        #Se sacaran las coincidencias con "src"
        src=po[nParrafo].get("src")
        #Se filtran las coincidencias de "src" que comiencen con "http" y terminen con ".jpg"
        if src.startswith("http") and src.endswith(".jpg"):
            fo.write((src+"\n"))#.encode("utf-8")
    fo.close()

    #Del archivo anteriormente creado se toma cada direccion URL de las imagenes y se almacenan
    file4=open(path+"/"+Artista+"/Imagenes/linking.txt", "r")
    for line in file4:
        u=line.rstrip()
        txtImg.append(u)
    file4.close()

def guardarImg(n):

    nom_img=path+"/"+Artista+"/Imagenes/Imagen_"+str(n)+".jpg"
    imag=requests.get(txtImg[n])
    with open(nom_img, "wb") as file:
        for ima in imag.iter_content(chunk_size=50000):
            file.write(ima)
        print("Se descargo correctamente la imagen", n)
