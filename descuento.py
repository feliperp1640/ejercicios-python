def calcular_descuento(precio,descuento):
    precio_final= precio-(precio * descuento / 100)
    return int(precio_final)

precio = calcular_descuento(50000,10)
print(precio)

precio = calcular_descuento(120000,25)
print(precio)