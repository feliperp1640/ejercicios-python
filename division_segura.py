def dividir_seguro(a, b):
    try:
        division = a / b
        return division
    except ZeroDivisionError:
        return "No se puede dividir por cero"

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))