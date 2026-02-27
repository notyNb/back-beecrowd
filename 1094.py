def analisa(soma: int, coelhos: int, ratos: int, sapos: int):
    teste = input()
    numero, letra = teste.split()
    numero = int(numero)
    
    
    soma += numero
    
    
    if letra == "C":
        coelhos += numero
    elif letra == "R":
        ratos += numero
    else:
        sapos += numero
   
    return sapos, coelhos, ratos, soma
    

def calculaPercentual(soma: int, coelhos: int, ratos: int, sapos: int): 
    percentualC = (coelhos / soma * 100)
    percentualR = (ratos / soma * 100)
    percentualS = (sapos / soma * 100)
    print(f"Total: {soma} cobaias")
    print(f"Total de coelhos: {coelhos}")
    print(f"Total de ratos: {ratos}")
    print(f"Total de sapos: {sapos}")
    imprimir(percentualC, percentualR, percentualS)
    

def imprimir(percentualC: int, percentualR: int, percentualS: int):
    print(f"Percentual de coelhos: {percentualC:.2f} %")
    print(f"Percentual de ratos: {percentualR:.2f} %")
    print(f"Percentual de sapos: {percentualS:.2f} %")

    
   



def main():
    soma = 0
    coelhos = 0
    ratos = 0
    sapos = 0
    n = int(input())
    for i in range(n):
        
        sapos, coelhos, ratos, soma = analisa(soma, coelhos, ratos, sapos)
    calculaPercentual(soma, coelhos, ratos, sapos)
    
        
    
    
  
    
main()