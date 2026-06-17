def filtrar_mayores(edades):
    mayores=[]
    for edad in edades:
        if edad>= 18:
            mayores.append(edad)
    return mayores

print(filtrar_mayores([15, 23, 17, 30, 14, 25, 16]  ))       