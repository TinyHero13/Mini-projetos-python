import math

def Bhaskara():
    a = int(input("Insira o valor de a: "))
    b = int(input("Insira o valor de b: "))
    c = int(input("Insira o valor de c: "))

    b2 = math.pow(b,2)
    ac4 = (4 * a * c)
    delta = (b2) - (ac4) 

    print("\n")
    print("*"*10)
    print("Calculando o Δ... ")
    print("Δ = {}² - 4 . {} . {}".format(b,a,c))
    print("Δ = {} - {}".format(b2,ac4))
    print("Δ = {}".format(math.floor(delta)))

    if(delta < 0):
        print ("\nNão existe raízes reais")
    else:
        
        deltaraiz = math.sqrt(delta)
        a2 = 2 * a
        x1 = (-b + (deltaraiz)) / (a2)
        x2 = (-b - (deltaraiz)) / (a2)

        print("\nCalculando o X... ")
        print("X = (-{} ± ✓{}) / ( 2 . {})".format(b,delta,a))
        print("X = (-{} ±  {}) / ({})".format(b,deltaraiz,a2))
        print("X1 = {}".format(x1))
        print("X2 = {}".format(x2))
        print("*"*10)
    

Bhaskara()