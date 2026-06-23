class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"El producto {self.nombre} cuesta {self.precio} pesos") 

producto1 = Producto("Mouse",25000)
producto1.mostrar_info()

producto2 = Producto("teclado", 45000)  
producto2.mostrar_info()
