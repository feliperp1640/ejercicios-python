def verificar_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"
       
print(verificar_edad(15))
print(verificar_edad(22))   
print(verificar_edad(17))   
print(verificar_edad(30))       