# Proyecto Final de Programacion I universidad Fidelitas

### Prerequisitos

1. Pandas
2. matplotlib
3. openpyxl

para ejecutar el programa debe abrir una terminal nueva dentro de la carpeta donde está el proyecto y usar el siguiente comando:

```
python proyecto_final.py
```

Este codigo se divide en 3 principales partes:

1. Instalación de depentencias, importar librerias y configuración de las librerias.
2. Ingreso de nuevos datos de clientes.
3. Generación de un reporte básico.

## Explicación del código

### 1. Instalación de depentencias, importar librerias y configuración de las librerias

Iniciando el codigo se encuentra la siguiente sección:

```
print('--------------------------------------------------------')
print('Instalando dependencias...')
from os import system
system('pip install pandas')
system('pip install matplotlib')
system('pip install openpyxl')
print('Dependencias instaladas!')
print('--------------------------------------------------------\n')
```

En la cual desglosando un poco cada linea se encuentra que:

```
from os import system
```

Es la libreria usada para controlar el sistema operativo e instalar las librerias.

```
system('pip install pandas')
system('pip install matplotlib')
system('pip install openpyxl')
```

En esta parte se instalan todas las librerias necesarias para ejecutar el programa (Si ya están instaladas en el sistema no se reinstalaran).

##### Warning: Dura un poco en instalar todas las librerias y ejecutarse el programa

Una vez insataladas las librerias se proceden a importar al código.

```
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
```

- **Pandas:** Es usada para leer, manejar y guardar los datos de los clientes.
- **matplotlib:** Es la libreria encargada de gráficar los datos de los clientes y convertir las fechas a un formato que sea fácil de utilizar.
- **openpyxl:** Es usada para exportar los dataframes a XLSX.

```
decision = 0
```

la variable _decision_ es usada como una variable auxiliar para navegar en el programa.

### 2. Ingreso de nuevos datos de clientes

Lo primero que nos encontramos en esta sección del código es lo siguiente:

```
if decision != 1 or decision != 2:
	print('¿Desea ingresar datos de un cliente o generar un reporte?')
	print('Ingrese 1 si quiere ingresar datos de un cliente y 2 si quiere generar un reporte')
	decision = int(input())
```

Este _if_ es usado para obtener la decisión de lo que quiera hacer el usuario.

Una vez eligió la opción 1 salta a la siguiente sección del código:

```
if decision == 1:
	df = pd.read_csv('proyecto final\data\clientes.csv')
```

En el cual entra a la sección de ingresar datos nuevos de clientes.
Lo primero que hace es abrir el archivo _clientes.csv_ en donde se encuentran los datos de los clientes y los guarda en la variable df.

Luego Procede a solicitarle al usuario los datos del cliente nuevo que quiere ingresar y los guarda en sus respectivas variables.

```
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
```

Luego de eso procede a calcular las ganancias del taller por el servicio que se le bridó al cliente usando las variables _coste_empresa_ y _coste_cliente_ con la siguiente linea de código:

```
remuneracion = coste_cliente-coste_empresa
```

Luego se procede a agregar el nuevo cliente a la variable _df_:

```
df = df.append({'fecha':fecha, 'cedula':cedula, 'nombre':nombre,
                   'apellido': apellido,'edad':edad, 'correo':correo,
                   'tipo de vehiculo': vehiculo,'Marca':marca, 'anno':anno,
                   'Coste del servicio':coste_empresa, 'Cantidad cobrada al cliente':coste_cliente,
                   'Remuneracion total':remuneracion}, ignore_index=True)
```

Y se exporta la variable _df_ como un archivo **CSV** y **XLSX** ubicados en la carpeta _output_.

```
df.to_csv('proyecto final\data\clientes.csv', index=False)
df.to_excel('proyecto final\data\clientes.xlsx', index=False)
print('\n--------------------------------------------------------')
print('Cliente agregado a la base de datos!')
print('--------------------------------------------------------\n')
decision = 0
```

Así terminando la sección de ingreso de nuevos clientes

### 3. Generación de un reporte básico.

Comienza similar a la sección 2:

```
elif decision == 2: # generación de reportes
	df = pd.read_csv(r'proyecto final\data\clientes.csv, parse_dates=['fecha'],
							     index_col= ['fecha'])
	df = df.sort_values(by=['fecha'])
```

la diferencia con la sección 2 es que en esta empieza leyendo el archivo **CSV** y luego transforma la columna de _fechas_ en un formato que sea más fácil de utilizar y gráficar.

Luego de eso se procede a hacer un pequeño analisis estadístico:

```
analisis_estadistico = round(df[['edad', 'anno', 'Coste del servicio', 'Cantidad cobrada al cliente', 'Remuneracion total']].describe(), 2)
analisis_estadistico.insert(0, 'Metricas', ['Conteo de filas', 'Promedio', 'Desviacion Estandar', 'Min', '25%', '50%/Media', '75%', 'Max'])
analisis_estadistico.to_excel('proyecto final/output/analisis_estadistico.xlsx', index=False)
```

Se usa la función _.describe()_ para realizar el analisis estadistico básico de las variables **'edad', 'anno', 'Coste del servicio', 'Cantidad cobrada al cliente' y 'Remuneracion total'** y se redondea los resultados a 2 decimales usando la función _round_.
Para luego proceder a exportar la variable a un archivo XLSX dentro de la carpeta _output_.

Después de esto se procede a crear el gráfico:

Con esta linea de código se crea un lienzo en blanco de 12x12 en el cual se añadira el gráfico.

```
fig, ax = plt.subplots(figsize=(12, 12))
```

Luego se procede a agregar las barras del eje X y sus respectivos valores en el eje Y con la siguiente linea de código:

```
ax.bar(df.index.values,
       df['Remuneracion total'],
       color='purple')
```

Luego se procede a agregarle el título al gráfico y los nombres de los ejes.

```
ax.set(xlabel='Fecha',
       ylabel='Remuneración para el taller',
       title='Remuneracion de la empresa a lo largo del tiempo')
```

Por último se guarda el gráfico en formato PDF y se exporta dentro de la carpeta "output".

## Author

- **Gabriel León** - _Initial work_ - [Gaboelc](https://github.com/Gaboelc)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
