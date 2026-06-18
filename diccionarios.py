usuario = {
    "nombre": "felipe",
    "email": "felipe@gmail.com",
    "edad": 32,
    "activo": True
}

print(usuario["nombre"])
print(usuario["email"])
print(f"Hola, {usuario['nombre']}. Tienes {usuario['edad']} anos.")

usuario["telefono"] = "3001234567"   # agrega una clave nueva
usuario["edad"] = 33                  # modifica un valor existente

print(usuario.keys())     # todas las claves
print(usuario.values())   # todos los valores