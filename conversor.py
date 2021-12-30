def conversor(tipo_pesos, valor_dolar):
    pesos=input("Cuantos pesos " + tipo_pesos + " tienes? ")
    pesos=float(pesos)
    dolares=pesos/valor_dolar
    dolares=round(dolares)
    dolares=str(dolares)
    print("Tienes $" + dolares + " dolares")
    


menu="""
Bienvenido al conversor de monedas 💲

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos Mexicanos

Elige una opcion:
"""


opcion=input(menu)

if opcion=='1':
    conversor("Colombianos", 4000)
elif opcion=='2':
    conversor("Argetinos", 4000)
elif opcion=='3':
    conversor("Mexicanos", 4000)
else:
    print("Ingrese una opcion correcta men")
