def cesar(alfaOriginal:list, lista:list, quantidade:int):
    listaNova = []

    for i in range(len(lista)):
        j = i
        while lista[i] != alfaOriginal[j]:
            j += 1
            if j > 25:
                j = 0
        
        novo_indice = (j - quantidade) % 26

        listaNova.append(alfaOriginal[novo_indice])
    print("".join(listaNova))







def main():
    n = int(input())
    alfaOriginal = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(n):
        alfa = input()
        lista = list(alfa)
        quantidade = int(input())

        cesar(alfaOriginal, lista, quantidade)



main()

    

