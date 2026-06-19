
try:
   usuario = {"nombre": "felipe", "edad": 32}
   print(usuario["telefono"])
except KeyError:
    print("Error: no existe en el diccionario")  