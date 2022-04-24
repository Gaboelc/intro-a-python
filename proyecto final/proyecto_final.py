# Librerias
import pandas as pd # libreria para administrar y manejar datos
# Variables
decision = 0

print("--------------------------------------------------------")
print("Bienvenido al sistema de reporteria del Taller mecanico Fidelitas \n")

while True:
	if decision != 1 or decision != 2:
		print("¿Desea ingresar datos de un cliente o generar un reporte?")
		print("Ingrese 1 si quiere ingresar datos de un cliente y 2 si quiere generar un reporte")
		decision = int(input())

		if decision == 1: # Ingreso de datos de clientes
			df = pd.read_csv('proyecto final\data\clientes.csv')
			print("Ingrese la fecha de la consulta")
			fecha = str(input())
			print("ingrese la cedula del cliente (Solo ingresar los numeros)")
			cedula = int(input())
			print("Ingrese el nombre del cliente")
			nombre = str(input())
			print("Ingrese el apellido del cliente")
			apellido = str(input())
			print("Ingrese la edad del cliente")
			edad = int(input())
			print("Ingrese el correo del cliente")
			correo = str(input())
			print("Ingrese el tipo de vehiculo")
			vehiculo = str(input())
			print("Ingrese la marca del vehiculo")
			marca = str(input())
			print("ingrese el año del vehiculo")
			anno = int(input())
			print("Ingrese el coste para la empresa de la consulta")
			coste_empresa = int(input())
			print("Ingrese el valor cobrado al cliente")
			coste_cliente = int(input())
			
			remuneracion = coste_cliente-coste_empresa
   
			df = df.append({'fecha':fecha, 'cedula':cedula, 'nombre':nombre, 'apellido': apellido,
                   'edad':edad, 'correo':correo, 'tipo de vehiculo': vehiculo,'Marca':marca,
                   'anno':anno, 'Coste del servicio':coste_empresa, 'cantidad cobrada al cliente':coste_cliente,
                   'Remuneracion total':remuneracion}, ignore_index=True)
			
			print('Cliente agregado a la base de datos!')
			print('------------------------------------------------')
			decision = 0
		elif decision == 2: # generación de reportes
			print("2")
			break