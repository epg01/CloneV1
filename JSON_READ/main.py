import json

''' def cargar_datos(route):
   with open(route) as contenido:
       personas = json.load(contenido)
       
if __name__ == '__main__':
    route = '/home/dkbarb10/REPOS/PERSONAL_REPO/Desarrollo/PYTHON/DB/JSON_READ/personas.json'
    cargar_datos(route)
 '''

with open("personas.json") as mis_datos:
    datos = json.loads(mis_datos.read())

print(type(datos))
print(datos)
    