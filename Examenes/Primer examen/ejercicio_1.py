ciclo = 1
while ciclo == 1:
    print("================================================================")
    print("Ingrese la edad del niño")
    edad_nino = int(input())
    
    # First error handler
    if edad_nino < 5 or edad_nino > 14:
        print("Error con la edad del niño")
    else:
        print("ingrese la cantidad de horas que jugó el niño")
        horas = int(input())
        total_no_descuento = horas*1000
        
        if edad_nino >= 5 and edad_nino <= 10:
            total_descuento = total_no_descuento - (total_no_descuento*0.05)
            print("El total a pagar sin el descuento aplicado es de:", total_no_descuento)
            print("El total a pagar con el descuento aplicado de 5% es de:", total_descuento)
        elif edad_nino >= 11 and edad_nino <= 13:
            total_descuento = total_no_descuento - (total_no_descuento*0.1)
            print("El total a pagar sin el descuento aplicado es de:", total_no_descuento)
            print("El total a pagar con el descuento aplicado de 10% es de:", total_descuento)
        elif edad_nino == 14:
            total_descuento = total_no_descuento - (total_no_descuento*0.15)
            print("El total a pagar sin el descuento aplicado es de:", total_no_descuento)
            print("El total a pagar con el descuento aplicado de 15% es de:", total_descuento)
        
    print("\n¿Desea terminar el programa?")
    print("Ingrese 0 si desea terminarlo o 1 si desea continuar")
    
    decision = int(input())
    if decision == 0:
        ciclo = 0