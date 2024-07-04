import pyodbc

def añadir(lista, conexion):
    
    try:
        cursor = conexion.cursor()
        query = 'INSERT INTO Grados VALUES(?, ?, ?, ?)'
        cursor.execute(query, lista['id'], lista['nombre'], lista['duracion'], lista['departamento'])
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al añadir el registro de grado. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return False
    

def buscar(ID, conexion):
   
    try:
        cursor = conexion.cursor()
        query = 'SELECT * FROM Grados WHERE GradoID = ?'
        cursor.execute(query, ID)
        resultado = cursor.fetchone()
        return resultado
    except pyodbc.Error as error:
        print(f'Error al buscar el registro de grado. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def actualizar(ID,conexion):
    try:
        resultado = buscar(ID, conexion)
        if not resultado:
            print('Registro de grado no encontrado...')
            input('Presione Enter para continuar...')
            return None
        print(f"ID: {ID}\nNombre: {resultado[1]}\n Duracion : {resultado[2]}\nDepartamento: {resultado[3]}")
        print('Escoja campo a actualizar:\n1 - Nombre\n2 - Duracion\n3 - Departamento\n4 - Todos los campos\n5 - Cancelar')
        a = int(input())
        if a == 5:
            return
        cursor = conexion.cursor()
        match a:
            case 1:
                Nombre = input('Ingrese nuevo nombre: ')
                query = 'UPDATE Grados SET Nombre = ? WHERE GradoID = ?'
                cursor.execute(query, Nombre, ID)
            case 2:
                Duracion = input('Ingrese nuevo tiempo de duracion: ')
                query = 'UPDATE Grados SET Duracion = ? WHERE GradoID = ?'
                cursor.execute(query, Duracion, ID)
            case 3:
                Departamento = input('Ingrese el nuevo departamento: ')
                query = 'UPDATE Grados SET Departamento = ? WHERE GradoID = ?'
                cursor.execute(query, Departamento, ID)
            case 4: 
                Nombre = input('Ingrese nuevo nombre: ')
                Duracion = input('Ingrese nuevo tiempo de duracion')
                Departamento = input('Ingrese el nueva departamento: ')
                query = 'UPDATE Grados SET Nombre = ?, Duracion = ?, Departamento = ? WHERE GradoID = ?'
                cursor.execute(query, Nombre, Duracion, Departamento, ID)
        cursor.commit()
        cursor.close()
        return True
    except pyodbc.Error as error:
        print(f'Error al actualizar el registro de grado. Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
def eliminar(ID, conexion):
   
    try:
        resultado = buscar(ID, conexion)
        if not resultado:
            print('Registro de Grado no encontrado...')
            input('Presione Enter para continuar...')
            return None
        print('======Grados======')
        print(f"ID: {ID}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nEspecialidad: {resultado[3]}")
        print('Desea eliminarlo?:\n1 - Si\n2 - No')
        x = input('Ingrese una opción: ')
        while True:
            if not x.isdigit():
                print("Por favor ingrese un numero valido")
                input("Presione enter para continuar...")
                continue
            else:
                break
        x = int(x)
        match x:
            case 1:
                cursor = conexion.cursor()
                cursor.execute('DELETE FROM Grados WHERE GradoID = ?', ID)
                cursor.commit()
                cursor.close()
                return True
            case 2:
                return False
        
    except pyodbc.Error as error:
        print(f'Error al eliminar😓😓 . Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
    
        
    except pyodbc.Error as error:
        print(f'Error al eliminar el registro . Error: {error}')
        cursor.close()
        input('Presione Enter para continuar...')
        return None
def mostar(conexion):
    try:
        
        cursor = conexion.cursor()
        cursor.execute('SELECT GradoID, Nombre, Duracion, DepartamentoID FROM Grados')
        Grados = cursor.fetchall()
        for i in Grados:
            print(f'ID: {i[0]} - Nombre: {i[1]} - Duracion: {i[2]} - DepartamentoID: {i[3]}')
        input('Presione enter para volver al menu...')
    except pyodbc.Error as err:
        print(f'Error al encontrar el registro: {err}')
        cursor.close()
        input('Presione ENTER para continuar...')
    