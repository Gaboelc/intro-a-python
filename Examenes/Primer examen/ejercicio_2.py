while True:
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