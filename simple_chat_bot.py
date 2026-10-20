"""
Bot sencillo que interactua

Vamos a calcular la edad del amigo
"""

import datetime 
HOY = datetime.datetime.now()
CURRENT_YEAR = HOY.year
CURRENT_MONTH = HOY.month
CURRENT_DAY = HOY.day

meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}

#pedir nombre
name = input ("¿Como te llamas?: ")

#pedir año
year = int(input("Dime tu año de nacimiento: "))

#pedir mes
month = input("Dime tu mes de nacimiento (mes): ")

#convertir el mes a numero
month_number = meses[month.lower()]

#pedir dia 
day = int(input("Que dia? "))

#calculamos la edad
print("Dia:",day, "Mes:", month, "Mes en numero:", month_number , "Año" , year)

edad = CURRENT_MONTH - year

if month_number == CURRENT_MONTH:
    if day == CURRENT_DAY:
        print(f"Felicidades {name}, a que te invitas?")
    elif day > CURRENT_DAY:
        edad -= 1
elif month_number > CURRENT_MONTH:
    edad -= 1

if edad > 25 and edad <= 40:
    print(f"¿Tienes {edad} años? Ojala llegues a la edad que aparentas")
elif edad > 40:
    print(f"¿Que tal el padel con Marcos?")
else: 
    print(f"¿{edad} quien los pillara?")