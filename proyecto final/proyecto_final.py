# Instalando dependencias
print('--------------------------------------------------------')
print('Instalando dependencias...')
from os import system # Libreria para controlar el OS
system('pip install pandas') # Instala Pandas
system('pip install matplotlib') # Instala matplotlib
system('pip install openpyxl') # Instala openpyxl (usada para exportar a XLSX)
print('Dependencias instaladas!')
print('--------------------------------------------------------\n')

# Librerias
import pandas as pd # libreria para administrar y manejar datos
import matplotlib.pyplot as plt # Libreria para graficar los datos 
import matplotlib.dates as mdates # Libreria para manerar fechas
from matplotlib.dates import DateFormatter # Libreria para convertir fechas

# Configuracion de las librerias
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Variables
decision = 0 # variable auxiliar para navegar dentro del menu

print('--------------------------------------------------------')
print('Bienvenido al sistema de reporteria del Taller mecanico Fidelitas')
print('--------------------------------------------------------\n')

while True: # Ejecuta el programa de manera infinita
	if decision != 1 or decision != 2: # Si la variable decision es diferente de 1 o 2 le va a preguntrar al usuario que quiere hacer
		print('¿Desea ingresar datos de un cliente o generar un reporte?')
		print('Ingrese 1 si quiere ingresar datos de un cliente y 2 si quiere generar un reporte')
		decision = int(input())

		if decision == 1: # Ingreso de datos de clientes # Si elige 1 ingresa en el modo de agregar clientes
			df = pd.read_csv('proyecto final\data\clientes.csv') # Lee el CSV
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
			
			remuneracion = coste_cliente-coste_empresa # Calcula la ganancia total de la consulta del cliente
			
			df = df.append({'fecha':fecha, 'cedula':cedula, 'nombre':nombre,
                   'apellido': apellido,'edad':edad, 'correo':correo,
                   'tipo de vehiculo': vehiculo,'Marca':marca, 'anno':anno,
                   'Coste del servicio':coste_empresa, 'Cantidad cobrada al cliente':coste_cliente,
                   'Remuneracion total':remuneracion}, ignore_index=True) # Agrega los datos del nuevo cliente al dataframe 
			
			df.to_csv('proyecto final\data\clientes.csv', index=False) # Exporta el dataframe como CSV con el nuevo cliente agregado
			df.to_excel('proyecto final\data\clientes.xlsx', index=False) # Exporta el dataframe como XLSX con el nuevo cliente agregado
			print('\n--------------------------------------------------------')
			print('Cliente agregado a la base de datos!')
			print('--------------------------------------------------------\n')
			decision = 0 # reinicia el estado
   
		elif decision == 2: # generación de reportes
			df = pd.read_csv(r'proyecto final\data\clientes.csv', parse_dates=['fecha'],
                    								 index_col= ['fecha']) # Lee el CSV y formatea la columna de fechas
			df = df.sort_values(by=['fecha']) # Ordena las filas por la columna de fecha
   
			analisis_estadistico = round(df[['edad', 'anno', 'Coste del servicio',
                                    		 'Cantidad cobrada al cliente', 'Remuneracion total']].describe(), 2) # Se crea el analisis estadistico basico
			analisis_estadistico.insert(0, 'Metricas', ['Conteo de filas', 'Promedio',
                                           'Desviacion Estandar', 'Min', '25%',
                                           '50%/Media', '75%', 'Max']) # Se inserta la columna que describe las filas
			analisis_estadistico.to_excel('proyecto final/output/analisis_estadistico.xlsx', index=False) # Se exporta a un XLSX
      
			fig, ax = plt.subplots(figsize=(12, 12)) # Se crea el lienzo para graficar los datos 

			ax.bar(df.index.values,
       		df['Remuneracion total'],
       		color='purple') # Se agregan el eje X y Y al grafico

			# Se agrega los titulos y leyendas a los ejes del grafico
			ax.set(xlabel='Fecha',
       		ylabel='Remuneración para el taller',
       		title='Remuneracion de la empresa a lo largo del tiempo')

			plt.savefig('proyecto final/output/Remuneracion_de_la_empresa_a_lo_largo_del_tiempo.pdf',
               			format='pdf', bbox_inches='tight') # Se exporta el grafico a PDF

			print('\n--------------------------------------------------------')
			print('Reporte exportado correctamente!')
			print('--------------------------------------------------------\n')
   
			decision = 0 # reinicia el estado