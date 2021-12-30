import random

def num():
    numero=int(input("Elige un numero entre 1 y 100: "))
    numero_rand=random.randint(1,100)
    if numero>100:
        print("Ingresa un numero valido: ")
    
    vidas=10
    while vidas>0:
        if numero<numero_rand:
            print("Elige un numero mas grande: ")
            vidas-=1
        elif numero>numero_rand:
            print("Elige un numero mas pequeño: ")
            vidas-=1
        if numero==numero_rand:
            print('GANASTE!!!!')
            break
        
        numero=int(input("Ingresa otro numero: "))
    
    if vidas==0:
        print("GAME OVER!!!!")


if __name__=="__main__":
    num()