/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
import datetime

def has_friday_13(month, year):
    date = datetime.date(year, month, 13)
    
    if date.day != 13:
        return False
    
    if date.weekday() == 4:
        return True
    
    return False

month = int(input("Ingrese el mes (1-12): "))
while True:
    year = int(input("Ingrese el año (debe ser 1950 o posterior): "))
    if year >= 1950:
        break
    print("El año debe ser 1950 o posterior. Intente nuevamente.")

result = has_friday_13(month, year)

if result:
    print(f"En el mes {month} del año {year} hay un viernes 13.")
else:
    print(f"En el mes {month} del año {year} no hay un viernes 13.")
