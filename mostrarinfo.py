def mostrar_info(empleado):
    print(f"Me llamo {empleado['nombre']}, soy {empleado['cargo']} mi salario es {empleado['salario']}")

mostrar_info({
    "nombre":"Felipe",
    "cargo": "Caracterizador",
    "salario": 4000000,
}    )