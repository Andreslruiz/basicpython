def run():
    # for contador in range(1000):
    #     if contador%2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     if i == 5678:
    #         break
    #     print(i)
    # print("SE ACABO")

    texto=input("Escribe un texto men: ")
    for letra in texto:
        if letra=='o':
            break
        print(letra)




if __name__ == '__main__':
    run()