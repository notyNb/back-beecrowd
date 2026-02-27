def main():
    tempo = int(input())
    velocidade = int(input())

    distancia = tempo * velocidade
    combustivel = distancia / 12

    print(f"{combustivel:.3f}")

main()