# Direcciones_URL.py
import os
import requests

try:
    from googlesearch import search
    from bs4 import BeautifulSoup as bs
    #print("Librerias instaladas")
except ImportError:
    os.system("pip install googlesearch-python")
    os.system("pip install beautifulsoup4")
    print("Instalando biblioteca de busqueda de google y BeatifulSoup... Ejecute de nuevo")
    exit()

#Variables

Artista=input("De que artista deseas buscar informacion?: ")
#Especificar el bicho xd
print()
path=os.getcwd()

# Inicializando lista
lista_dURL=[]

#Verificar si existe la carpeta, si no crearla con el nombre del artista
try:
    os.mkdir(path+"/"+Artista)
    print("Creando carpeta principal:", Artista, "\n")
except:
    print("La carpeta:", Artista," ya existe")
    op=input("Desea sobreescribir los archivos? (y/n): ")
    op.lower()
    if op=="y" or op=="yes":
        print()
    else:
        exit()

#Almacenar las direcciones URL de la busqueda de la informacion relacionada al Artista
def Almacenar_dURL():
    print("Buscando direcciones URL relacionadas a:", Artista, "...\n")
    file=open(path+"/"+Artista+"/Direcciones_URL.txt", "w")
    busqueda=search(Artista, lang= "es")
    print(busqueda)
#    for num_busq in range(0, len(busqueda)-1):
    for num_busq in busqueda:
        #print (busqueda(num_busq))
        file.write(num_busq+"\n")
#        file.write(busqueda[num_busq]+"\n")
    file.close()

def GuardarHTML_dURL():
    print("Creando archivos con contenido HTML de las direcciones URL...\n")
    #Guardar cada direccion URL en un espacio de una lista en estructura de pila
    file1=open(path+"/"+Artista+"/Direcciones_URL.txt", "r")
    for linea_dURL in file1:
        u=linea_dURL.rstrip()
        lista_dURL.append(u)
    file1.close()
    #print(lista_dURL)
    tam_lista_dURL=len(lista_dURL)
    for num_lis in range(0, tam_lista_dURL):
        file2=open(path+"/"+Artista+"/Direcciones_URL.txt", "r")
        #Descargar y confirmar que se ha descargado el codigo de la direccion URL
        page=requests.get(lista_dURL[num_lis])
        #print(page.status_code)

        #Guardar el contenido del HTML de cada direccion URL
        soup=bs(page.content,"html.parser")
        file3=open(path+"/"+Artista+"/HTML_"+str(num_lis)+"_dURL.txt", "wb")
        file3.write(soup.encode("utf-8"))
        #print(soup.prettify)
    file2.close()
    file3.close()
