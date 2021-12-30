

def palindromo(palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    palabra_rev=palabra[::-1]
    if palabra==palabra_rev:
        print("Es palindromo")
    else: print("No es palindromo")

def run():
    palabra=input("Escribe una palabra:")
    palindromo(palabra)

if __name__ =='__main__':
    run()