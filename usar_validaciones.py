from validaciones import es_mayor_edad
from validaciones import es_email_valido

edad1 = es_mayor_edad(32)
edad2 = es_mayor_edad(17)
print(edad1)
print(edad2)

email1 = es_email_valido("David@gmail.com")
email2 = es_email_valido("Davidgmail.com")
print(email1)
print(email2)


