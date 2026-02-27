def main():
    maior = 0
    
    for i in range(100):
        n = int(input())
        if n > maior:
            maior = n
            pos = i + 1
    
    print(maior)
    print(pos)


main()