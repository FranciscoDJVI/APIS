# Modulo que permite la conexion entre la BD en mysql workbench y python.
import mysql.connector

# Proceso de conexión a la BD.
try:
    # Datos esenciales para la conexión a la BD.
    conect = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "",
        database = "users"
        )
    #Comprobación de conexión a la BD.
    if conect:
        print(f"Conexión a la base de datos {conect.database} exitosa!")
        cursor = conect.cursor() # Creación del cursor para poder relizar las multiples operaciones en la BD.
except TypeError as error:
        print(f"Error en la conexión a la base de datos {conect.database} {error}")

#OPERACION CRUD(Create, Read, Update, Delete)

# Obtención de todos los usuarios registrado en la tabla user de la BD.
def get_users():
    try:
        sql = f"select * from  user"
        cursor.execute(sql)
        results = cursor.fetchall() # Metodo para que toma todos los usuarios guardados en la tabla user de la BD.
        return results
    except TypeError as error:
        print(f"Error al obtener los usuarios {error}")

# Obtención de usuarios individuales registrado en la tabla user de la BD.
def get_user(id):
    sql = f"select * from user where iduser = {id}"
    cursor.execute(sql)
    results = cursor.fetchone() # Metodo para que toma usuarios unicos guardados en la tabla user de la BD.
    return results

# Creacipon de un nuevo usuario en la tabla user de la BD.
def create_user(iduser: int, username: str, rol: str):
    sql = f"insert into user(iduser, username, rol)values(%s,%s,%s)"
    val = (iduser, username, rol) # Variable con los cada uno de los datos de la tabla para la cración de un nuevo usuario.
    cursor.execute(sql, val)
    conect.commit()

# Actualización de usuarios individuales en la tabla user de la BD.
def update_user(iduser: int, username: str, rol: str):
    old_user = f"select * from user where iduser = {iduser}"
    cursor.execute(old_user)
    results = cursor.fetchone()
    if results[0] == iduser:
        sql = f"UPDATE user SET username = (%s), rol = (%s) WHERE iduser = (%s);"
        val = (username, rol,iduser,)
        cursor.execute(sql, val);
        results_final = cursor.fetchone()
        conect.commit()
        print(results_final)

# Borrar un usuario
def delete_user(iduser):
    old_user = f"select * from user where iduser = {iduser}"
    cursor.execute(old_user)
    results = cursor.fetchone()
    if results[0] == iduser:
        sql = f"delete from user WHERE iduser = {iduser}"
        cursor.execute(sql)
        conect.commit()
        print(f"Se elimino correctamente el usuario {results}")
    else:
        print(f"Error al eliminar el usuario {results}")