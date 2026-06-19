empleado={
    "nombre":"Felipe",
    "cargo": "Caracterizador",
    "salario": 4000000,
}
print(f"Me llamo {empleado['nombre']}, soy {empleado['cargo']} mi salario es {empleado['salario']}")
empleado["salario"] = empleado["salario"] + (empleado["salario"] * 0.10)
print(f"Me llamo {empleado['nombre']}, soy {empleado['cargo']} mi salario es {empleado['salario']}")