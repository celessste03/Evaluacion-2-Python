import os
import pyodbc
from db.graduados import *
from db.conexion import *



SERVER = 'LAPTOP-D9CATUR6\SQLSERVERVE'
DATABASE = 'Escuela'
TABLE = 'Grados'


def main():
    conexion = conectar(SERVER, DATABASE)
    while True:
        os.system('cls')
        print("==============Grados==============")
        print(f'BASE DE DATOS: {DATABASE} | TABLA: {TABLE}')
        print('1 - Agregar \n2 - Actualizar  \n3 - Mostrar \n4 - Buscar \n5 - Eliminar  \n')
        a = int(input('Ingrese una opción: '))
        match a :
            case 1:
                os.system('cls')
                ID = None
                while not ID:
                    print("======Agregar Registro de Grado======")
                    ID = input('Ingrese el ID del registro: ')
                    if not ID.isdigit():
                        print('Error, Solo puede ingresar numeros. ')
                        input('Presiona enter para continuar...')
                        ID = None
                        continue
                ID = int(ID)
                Nombre = input('Ingrese nombre: ')
                Duracion = input('Ingrese Duracion: ')
                Departamento = input('Ingrese Departamento: ')
                list = {
                    'id': ID,
                    'nombre': Nombre,
                    'duracion': Duracion,
                    'departamento': Departamento
                }
                result = añadir(list, conexion)
                if(result):
                    print('Distribuidor registrado exitosamente! 💕💕💕')
                    input("Presione enter para continuar")
            case 2:
                os.system('cls')
                ID = None
                while not ID:
                    print("======Actualizar el Registro de Grado======")
                    ID = input('Ingrese el ID del registro: ')
                    if not ID.isdigit():
                        print('Error, Solo puede ingresar numeros. ')
                        input('Presiona enter para continuar...')
                        ID = None
                        continue
                    ID = int(ID)
                resultado = actualizar(ID, conexion)
                print('Datos actualizados exitosamente! 💕💕💕')
                input('Presiona enter para continuar...')
            case 3: 
                print("======Mostrar Lista de Registro de Grado======")
                mostar(conexion)
            case 4: 
                os.system('cls')
                ID = None
                while not ID:
                    print("======Buscar Registro de Grado======")
                    ID = input('Ingrese el ID del registro: ')
                    if not ID.isdigit():
                        print('Error, Solo puede ingresar numeros. ')
                        input('Presiona enter para continuar...')
                        ID = None
                        continue
                    ID = int(ID)
                resultado = buscar(ID, conexion)
                if resultado:
                    print(f"ID: {ID}\nNombre: {resultado[1]}\nDuracion: {resultado[2]}\nDepartamento: {resultado[3]}")
                    input('Presione Enter para volver al menu...')
                else:
                    print('Registro de Grado no encontrado...')
                    input('Presione Enter para continuar...')
            case 5:
                
                os.system('cls')
                print("======Eliminar el registro de Grado======")
                ID = input('Ingrese el ID: ')
                resultado = eliminar(ID, conexion)
                if(resultado):
                    os.system('cls')
                    print('Registro de Grado eliminado exitosamente!🥳🥳🥳 ')
                    input("Presione enter para continuar...")
        
if __name__ == '__main__':
    main()
                

