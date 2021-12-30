import random

def generar_contrasena():
    mayusculas=['A','B','C','D','E','F','G']
    minusculas=['a','s','b','c','d','e','g']
    simbolos=['#','-','%','$','/','?','&','!']
    numeros=['1','2','3','4','5','6','7','8']

    caracteres=mayusculas+minusculas+numeros
    contrasena=[]
    for i in range(15):
        caracter_random=random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena=''.join(contrasena)
    return contrasena
    

def run():
    contrasena=generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)



if __name__=="__main__":
    run()