import pyodbc

def cadena_de_conexion(SERVER, DATABASE):
    return f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'


def conectar(SERVER, DATABASE):
    cadena = cadena_de_conexion(SERVER, DATABASE)
    try:
        conex = pyodbc.connect(cadena)
        print("La conexión con la base de datos fue exitosa ")
        return conex
    except pyodbc.Error as error:
        print(f'Error al conectarse con la base de datos : {error}')
        return None

def cerrar_conexion(conex):
    if conex:
        conex.close()
        print('Conexión cerrada ')


