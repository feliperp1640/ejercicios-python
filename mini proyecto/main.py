from inventario import Producto

inventario = {}   

def agregar_producto(nombre, stock, id, precio):
    if stock < 0:
        print("Error: el stock no puede ser negativo.")
        return
    nuevo_producto = Producto(nombre, stock, id, precio)
    inventario[nuevo_producto.id] = nuevo_producto   
       
agregar_producto("Shampoo", 60, 100, 20000)
agregar_producto("Arepas", 100, 101, 2000)
agregar_producto("Jamon", 30, 102, 14000)
agregar_producto("Cafe", 80, 103, 11000)
agregar_producto("Arroz", 150, 104, 1650)
agregar_producto("Detergente", 20, 105, 9000)    # válido, debería agregarse
agregar_producto("Cloro", -5, 106, 4000)          # inválido, NO debería agregarse


def listar_inventario():
    for id, producto in inventario.items():
        producto.mostrar()

listar_inventario()

def eliminar_producto(id):
    if id in inventario:
        del inventario [id]
        print(f"'{id}' eliminado.")
    else:
        print(f"'{id}' no existe en el inventario.")
        
eliminar_producto(99)
eliminar_producto(100)