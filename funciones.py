# def imprimir_mensaje():
#     print("Special Message")
#     print("Learning to use functions")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def converzacion(mensaje):
    print('Hola')
    print('como estas?')
    print(mensaje)
    print('Adios')


opcion=input("Elige una opcion (1, 2, 3)")

if opcion=='1':
    converzacion('Elegiste la opcion 1')
elif opcion=='2':
    converzacion('Elegiste la opcion 2')
elif opcion=='3':
    converzacion('Elegiste la opcion 1')
else: print('Elige opcion correcta')
