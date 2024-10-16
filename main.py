.# Modulo fastApi para la creación de la API con python
from fastapi import FastAPI

# Importación de la conexión a la base de datos.
import conexion_bd
app = FastAPI()

# Descripcion de la API 
@app.get("/")
async def home():
    
    message = {
        "tecnology":"fastApi",
        "version-fastApi":"0.0.5",
        "version-python":"3.13.0",
        "Descrition": "API básica para la gestión de usuarios en una base de datos",
        f"estructure":{
        "id": "int",
        "name":"str",
        "rol": "str"},
    }
    
    message_2 ={
        "Database":"users",
        "table":"user",
        "columns":{
            "iduser":"int",
            "nameuser":"str",
            "rol":"str"
        }
    }
    return message, message_2

#OPERACION CRUD(Create, Read, Update, Delete)
#Obtener todos los ususarios
@app.get("/users")
async def get_users():
    return conexion_bd.get_users()


#Obtener usuarios individuales
@app.get("/users/{id_user}/")
async def get_user(id_user:  int):
    return {"user":conexion_bd.get_user(id_user)}


#Crear un usuario
@app.post("/users/post")
async def create_user(iduser, username, rol):
    return {conexion_bd.create_user(iduser, username, rol)}


#Actualiar usuario
@app.put("/users/update/{id_user}")
async def update_user(iduser: int, username : str, rol: str):
    if conexion_bd.update_user(iduser, username, rol):
        return conexion_bd.update_user[iduser].update(
            {
                "id": iduser,
                "name": username,
                "rol": rol,
            }
        )

#Borrar usuario
@app.delete("/users/delete/{iduser}")
async def delete_user(iduser: int):
    if conexion_bd.delete_user(iduser):
        return f"El usuario {iduser} fue eliminado correctamente"
    else:
        return f"Error al eliminar el usuario {iduser}"