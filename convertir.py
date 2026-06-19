texto="abc"
try:
    convertir=int(texto)
    print(convertir)
except ValueError:
    print("Error: no se puede convertir a numero")    