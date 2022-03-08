while True:
    print("El estudiante tiene ")

cantidad_merienda = 100
cantidad_no_merienda = 30
cantidad_tranporte = 70
cantidad_no_tranporte = 60
cantidad_juego = 45
cantida_no_juego = 85

promedio_estatura = 145

total_ninos = cantidad_tranporte+cantidad_no_tranporte

print("================================")
print("Estadisticas de la escuela 'Los tres mosqueteros'")
print("================================")
print("Cantidad de niños que van a la escuela:", total_ninos)
print("De los", total_ninos, cantidad_merienda,"llevan merienda y",
      cantidad_no_merienda, "no llevan merienda.")
print("================================")
print("De los", total_ninos, cantidad_tranporte,"necesitan transporte y",
      cantidad_no_tranporte, "no necesitan transporte.")
print("================================")
print("De los", total_ninos, cantidad_juego,"llevan algún tipo de juego y",
      cantida_no_juego, "no llevan algún tipo de juego.")
print("================================")
print("Adicionalmete, el promedio de estatura entre los niños es de:", promedio_estatura)