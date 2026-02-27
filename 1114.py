def main():
    correta = 2002
    n = 0
    while n != correta:
        n = int(input())
        if n == correta:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")

main()
    