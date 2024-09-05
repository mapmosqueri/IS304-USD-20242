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
