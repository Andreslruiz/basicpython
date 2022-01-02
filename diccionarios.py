def run():
    print
    mi_diccionario={
        'llave 1':1,
        'llave 2':2,
        'llave 3':3,
        'llave 4':3,
        
    }
    # print(mi_diccionario['llave 1'])
    # print(mi_diccionario['llave 2'])
    # print(mi_diccionario['llave 3'])

    poblacion_pais={
        'Argentina': 44456765,
        'Brasil': 89000000,
        'Colombia': 469844099,
    }

    # print(poblacion_pais['Colombia'])

    # for llave in poblacion_pais:
    #     print(llave)

    # for value in poblacion_pais.values():
    #     print(value)

    # for items in poblacion_pais.items():
    #     print(items)

    for pais, poblacion in poblacion_pais.items():
        print(pais + "tiene " + str(poblacion) + "habitantes.")

if __name__=="__main__":
    run()