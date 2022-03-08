ciclo = 1
contador_merienda, contador_no_merienda = 0, 0
contador_transporte, contador_no_transporte = 0, 0
contador_juego, contador_no_juego = 0, 0
estaturas, total_ninos = 0, 0
while ciclo == 1:
    print("\n=====================================================================")
    print("¿Desea ingresar datos de un niño o ver los resultados de la escuela?")
    print("Ingrese 0 si desea ingresar datos o 1 si desea ver los resultados")
    decision = int(input())
    if decision == 0:
        print("")
        print("¿El estudiante lleva merienda?")
        print("ingrese 0 si sí lleva merienda o 1 si no lleva merienda")
        
        merienda = int(input())
        if merienda == 0:
            contador_merienda += 1
        elif merienda == 1:
            contador_no_merienda += 1
        else:
            print("ingresó un valor incorrecto")
        
        print("")    
        print("¿El estudiante necesita transporte?")
        print("ingrese 0 si sí necesita transporte o 1 si no necesita transporte")
        transporte = int(input())
        
        if transporte == 0:
            contador_transporte += 1
        elif transporte == 1:
            contador_no_transporte += 1
        else:
            print("ingresó un valor incorrecto")
        
        print("")    
        print("¿El estudiante lleva algún juego?")
        print("ingrese 0 si sí lleva algún juego o 1 si no lleva algún juego")
        juego = int(input())
        
        if juego == 0:
            contador_juego += 1
        elif juego == 1:
            contador_no_juego += 1
        else:
            print("ingresó un valor incorrecto")
            
        total_ninos = contador_transporte + contador_no_transporte
        
        print("Ingrese la estatura del niño en centimetros")
        estaturas += int(input())
        
    if decision == 1:
        
        print("====================================================")
        print("Estadisticas de la escuela 'Los tres mosqueteros'\n")
        print("Cantidad de niños que van a la escuela:", total_ninos)
        print("De los", total_ninos, "niños,", contador_merienda,"llevan merienda y",
          contador_no_merienda, "no llevan merienda.")
        print("De los", total_ninos, "niños,", contador_transporte,"necesitan transporte y",
              contador_no_transporte, "no necesitan transporte.")
        print("De los", total_ninos, "niños,", contador_juego,"llevan algún tipo de juego y",
              contador_no_juego, "no llevan algún tipo de juego.")
        
        if total_ninos == 0:
            print("Adicionalmete, el promedio de estatura entre los niños es de: 0")
        else:
            print("Adicionalmete, el promedio de estatura entre los niños es de:", estaturas/total_ninos)
    
    print("\n¿Desea terminar el programa?")
    print("Ingrese 0 si desea terminarlo o 1 si desea continuar")
    
    decision_1 = int(input())
    if decision_1 == 0:
        ciclo = 0