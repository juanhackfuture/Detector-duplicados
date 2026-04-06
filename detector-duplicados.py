import os
import hashlib

def obtener_hash(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        contenido= f.read()
        return hashlib.md5(contenido).hexdigest()

ruta = input("ingresa la ruta de la carpeta: ")

if not os.path.exists(ruta):
    print("Ruta no valida")
    exit()

archivos= os.listdir(ruta)

hashes={}
duplicados=[]

for archivo in archivos:
    ruta_completa=os.path.join(ruta, archivo)

    if os.path.isdir(ruta_completa):
        continue

    hash_archivo= obtener_hash(ruta_completa)

    if hash_archivo in hashes:
        duplicados.append(archivo)
    else:
        hashes[hash_archivo]=archivo

print("\nArchivos duplicados encontrados: ")
for dup in duplicados:
    print (dup)

print("\nTotal duplicados: ", len(duplicados))
