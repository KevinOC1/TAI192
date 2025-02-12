from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title="Mi Primer API 192",
    description="Kevin Oredaz",
    version="1.0.1",
)

usuarios = [
    {"id": 1, "nombre": "Ivan", "edad": 37},
    {"id": 2, "nombre": "Carlos", "edad": 15},
    {"id": 3, "nombre": "María", "edad": 18},
    {"id": 4, "nombre": "Lucía", "edad": 37},
]

# Endpoint home
@app.get("/", tags=["Hola Mundo"])
def home():
    return {"hello": "world FastAPI"}


# Endpoint consulta todos
@app.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leerUsuarios():
    return {"los usuarios registrados son": usuarios}

# Endpoint Agregar usuarios nuevos
@app.post("/usuario/", tags=["Operaciones CRUD"])
def AgregarUsuarios(usuario:dict):
    for usr in usuarios: 
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="Id ya existe")

    usuarios.append(usuario)
    return usuario

# Endpoint Actualizar 
@app.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leerUsuarios():
    return {"los usuarios registrados son": usuarios}

# Endpoint para actualizar un usuario
@app.put("/usuario/{id}", tags=["Operaciones CRUD"])
def actualizar_usuario(id: int, usuarioActualizado: dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")












# Endpoint de promedio
@app.get("/promedio", tags=["Operaciones"])
def promedio():
    return {"promedio": 6.1}

# Endpoint con parámetro obligatorio en la URL
@app.get("/usuario/{id}", tags=["Parámetro Obligatorio"])
def consulta_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return {"mensaje": "Usuario encontrado", "usuario": usuario}
    return {"mensaje": f"Usuario con id {id} no encontrado"}

@app.get("/usuario", tags=["Parámetro Opcional"])
def consulta_usuario2(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usuario}
        return {"mensaje": f"Usuario con id {id} no encontrado"}
    return {"mensaje": "No se proporcionó un id"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios3(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}