# contador=0
# print("El numero 2 elevado a " + str(contador) + "Es igual a " + str(2**contador))

def run():
    LIMITE=100000
    contador=0
    
    while contador<LIMITE:
        potencia=2**contador
        print(" El numero 2 elevado a " + str(contador) + " Es igual a " + str(potencia))
        contador=contador+1

if __name__ == '__main__':
    run()