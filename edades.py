edad=[15,23,17,30,14,25,16]

#for edades in edad:
    #if edades >= 18:
     # print(f"{edades} es mayor de edad")

contador = 0
for edades in edad:
    if edades >= 18:
        contador = contador + 1
print(f"Hay {contador} mayores de edad")
