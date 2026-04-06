def calcula_tomadas(tomadas:list):
    total = 0
    for i in range(len(tomadas)):
        #print({i})
        if i != len(tomadas) -1:
            total += (tomadas[i] - 1)
            #print(f"i -1 = {tomadas[i] - 1}")
        else:
            total += (tomadas[i])
            #print(f"i = {i}")
    print(total)






def main():
    tomadas = list(map(int, input().split()))
    calcula_tomadas(tomadas)
    


main()