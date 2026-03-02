def triangulo(a:float, b:float, c:float):
    if a >= (b + c):
        print("NAO FORMA TRIANGULO")
        return
    if a * a == (b * b + c * c):
        print("TRIANGULO RETANGULO")
    if a * a > (b * b + c * c):
        print("TRIANGULO OBTUSANGULO")
    if a * a < (b * b + c * c):
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c:
        print("TRANGULO EQUILATERO")
    elif a == b and a != c or a == c and b != a or b == c and a != c:
        print("TRIANGULO ISOSCELES")

    
    
            




def main():
    a, b, c = map(float, input().split())
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    
    
    triangulo(a, b, c)
    

main()
     
