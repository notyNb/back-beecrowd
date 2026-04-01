def fatorial(m:int, n:int):
    primeiro = m - 1
    resultado1 = m
    segundo = n - 1
    resultado2 = n
    if m == 0:
        resultado1 += 1
    else:
        while primeiro != 0:
            resultado1 *= primeiro
            primeiro -= 1
   
    if n == 0:
        resultado2 += 1
    else:
        while segundo != 0:
            resultado2 *= segundo
            segundo -= 1

    print(resultado1 + resultado2)


def main():
    while True:
        try:
            m, n = map(int, input().split())
            fatorial(m, n)
        except EOFError:
            break

main()


    
        

