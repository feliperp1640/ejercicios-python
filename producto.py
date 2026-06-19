producto={
    "nombre": "shampoo",
    "precio": 2000,
    "stock": 50, 
}
print(f"El producto {producto['nombre']} cuesta {producto['precio']} y hay {producto['stock']} unidades disponibles ")

producto["stock"] = producto["stock"] - 1

print(f"El producto {producto['nombre']} cuesta {producto['precio']} y hay {producto['stock']} unidades disponibles ")