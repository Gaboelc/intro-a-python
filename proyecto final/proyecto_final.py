# Variables
decision = 2

print('--------------------------------------------------------')
print('Bienvenido al sistema de reporteria del Taller mecanico Fidelitas')
print('--------------------------------------------------------\n')

while True: # Ejecuta el programa de manera infinita
    if decision != 1 or decision != 0:
        print('--------------------------------------------------------\n')
        print('Ingrese 1 si desea agregar un cliente nuevo o 0 si desea finalizar el programa')
        decision = int(input())
        
        if decision == 1:
            print('--------------------------------------------------------')
            print('Ingrese los datos del cliente nuevo')
            print('--------------------------------------------------------\n')
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
            
            with open('data\clientes.csv', 'a') as f:
                f.write(f'\n{fecha},{cedula},{nombre},{apellido},{edad},{correo},{vehiculo},{marca},{anno},{coste_empresa},{coste_cliente},{remuneracion}')
                
            print('\n--------------------------------------------------------')
            print('Cliente agregado a la base de datos!')
            print('--------------------------------------------------------\n')
            
    if decision == 0:
        break