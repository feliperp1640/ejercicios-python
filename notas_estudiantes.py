class Notas:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        if self.nota >= 60:
            return True
        else:
            return False    

nota1 = Notas("Felipe", 60)
aprobo1 = nota1.aprobo()
print(f"{nota1.nombre} aprobó: {aprobo1}")

nota2 = Notas("Juan", 59)
aprobo2 = nota2.aprobo()
print(f"{nota2.nombre} aprobó: {aprobo2}")

nota3 = Notas("Pedro", 20)
aprobo3 = nota3.aprobo()
print(f"{nota3.nombre} aprobó: {aprobo3}")

