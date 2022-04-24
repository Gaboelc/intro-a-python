# Instalando dependencias
print('--------------------------------------------------------')
print('Instalando dependencias...')
from os import system
system('pip install pandas')
system('pip install matplotlib')
system('pip install openpyxl')
print('Dependencias instaladas!')
print('-------------------------------------------------------- \n')
# Librerias
import pandas as pd # libreria para administrar y manejar datos
import matplotlib.pyplot as plt # Libreria para graficar los datos 
import matplotlib.dates as mdates # Libreria para manerar fechas
from matplotlib.dates import DateFormatter # Libreria para convertir fechas

# Variables
decision = 0

print('--------------------------------------------------------')
print('Bienvenido al sistema de reporteria del Taller mecanico Fidelitas')
print('-------------------------------------------------------- \n')

while True:
	if decision != 1 or decision != 2:
		print('¿Desea ingresar datos de un cliente o generar un reporte?')
		print('Ingrese 1 si quiere ingresar datos de un cliente y 2 si quiere generar un reporte')
		decision = int(input())

		if decision == 1: # Ingreso de datos de clientes
			df = pd.read_csv('proyecto final\data\clientes.csv')
			df = df.reset_index(drop=True)
			print('Ingrese la fecha de la consulta')
			fecha = str(input())
			print('ingrese la cedula del cliente (Solo ingresar los numeros)')
			cedula = int(input())
			print('Ingrese el nombre del cliente')
			nombre = str(input())
			print('Ingrese el apellido del cliente')
			apellido = str(input())
			print('Ingrese la edad del cliente')
			edad = int(input())
			print('Ingrese el correo del cliente')
			correo = str(input())
			print('Ingrese el tipo de vehiculo')
			vehiculo = str(input())
			print('Ingrese la marca del vehiculo')
			marca = str(input())
			print('ingrese el año del vehiculo')
			anno = int(input())
			print('Ingrese el coste para la empresa de la consulta')
			coste_empresa = int(input())
			print('Ingrese el valor cobrado al cliente')
			coste_cliente = int(input())
			
			remuneracion = coste_cliente-coste_empresa
			
			df = df.append({'fecha':fecha, 'cedula':cedula, 'nombre':nombre,
                   'apellido': apellido,'edad':edad, 'correo':correo,
                   'tipo de vehiculo': vehiculo,'Marca':marca, 'anno':anno,
                   'Coste del servicio':coste_empresa, 'Cantidad cobrada al cliente':coste_cliente,
                   'Remuneracion total':remuneracion}, ignore_index=True)
			
			df.to_csv('proyecto final\data\clientes.csv', index=False)
			df.to_excel('proyecto final\data\clientes.xlsx', index=False)
			print('\n--------------------------------------------------------')
			print('Cliente agregado a la base de datos!')
			print('--------------------------------------------------------\n')
			decision = 0
		elif decision == 2: # generación de reportes
			df = pd.read_csv(r'proyecto final\data\clientes.csv', parse_dates=['fecha'],
                    								 index_col= ['fecha'])
			df = df.sort_values(by=['fecha'])
   
			analisis_estadistico = round(df[['edad', 'anno', 'Coste del servicio', 'Cantidad cobrada al cliente', 'Remuneracion total']].describe(), 2)
			analisis_estadistico.insert(0, 'Metricas', ['Conteo de filas', 'Promedio', 'Desviacion Estandar', 'Min', '25%', '50%/Media', '75%', 'Max'])
			analisis_estadistico.to_excel('proyecto final/output/analisis_estadistico.xlsx', index=False)
      
			# Create figure and plot space
			fig, ax = plt.subplots(figsize=(12, 12))

			# Add x-axis and y-axis
			ax.bar(df.index.values,
       		df['Remuneracion total'],
       		color='purple')

			# Set title and labels for axes
			ax.set(xlabel='Fecha',
       		ylabel='Remuneración para el taller',
       		title='Remuneracion de la empresa a lo largo del tiempo')

			plt.savefig('proyecto final/output/Remuneracion_de_la_empresa_a_lo_largo_del_tiempo.pdf', format='pdf', bbox_inches='tight')

			print('\n--------------------------------------------------------')
			print('Reporte exportado correctamente!')
			print('--------------------------------------------------------\n')
   
			decision = 0
			