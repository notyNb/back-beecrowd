def corretos(t:int, participantes:list):
    corretos = 0
    for i in range(len(participantes)):
        if participantes[i] == t:
            corretos += 1
        else:
            corretos += 0
    print(corretos)










def main():
    t = int(input())
    participantes = list(map(int,input().split()))
    corretos(t, participantes)
main()
