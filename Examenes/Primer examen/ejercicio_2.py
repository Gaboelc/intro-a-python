ciclo = 1
while ciclo == 1:
    print("")
    print("================================================================")
    print("Ingrese el radio del rectangulo")
    radio = float(input())
    
    diametro = radio*2
    
    perimetro = (radio*2) + (diametro*2)
    area = diametro * radio
    
    print("El perimetro del rectangulo es:", perimetro)
    print("El area del rectangulo:", area)
    
    if perimetro > 50:
        print("Rectangulo muy grande")
    
    print("\n¿Desea terminar el programa?")
    print("Ingrese 0 si desea terminarlo o 1 si desea continuar")
    
    decision = int(input())
    if decision == 0:
        ciclo = 0