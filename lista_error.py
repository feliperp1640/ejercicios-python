paises=["colombia","peru","mexico"]
try:
    print (f"{paises[5]}")
except IndexError:
    print("Error: no existe ese elemento en la lista")    