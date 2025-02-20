from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI(
    title="REPASO",
    description="Kevin Oredaz",
    version="1.0.1",
)

tareas = [
    {"id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI", "vencimiento": "14-02-24", "estado": "completada"},
    {"id": 2, "titulo": "Resolver problemas de álgebra", "descripcion": "Practicar ecuaciones de segundo grado", "vencimiento": "20-02-24", "estado": "pendiente"},
    {"id": 3, "titulo": "Revisar geometría", "descripcion": "Estudiar los teoremas de Pitágoras y Tales", "vencimiento": "22-02-24", "estado": "pendiente"},
    {"id": 4, "titulo": "Hacer ejercicios de cálculo", "descripcion": "Resolver derivadas e integrales", "vencimiento": "25-02-24", "estado": "pendiente"},
    {"id": 5, "titulo": "Estudiar trigonometría", "descripcion": "Repasar identidades trigonométricas", "vencimiento": "28-02-24", "estado": "pendiente"},
    {"id": 6, "titulo": "Leer sobre teoría de números", "descripcion": "Investigar sobre números primos y divisibilidad", "vencimiento": "02-03-24", "estado": "pendiente"},
    {"id": 7, "titulo": "Resolver problemas de matrices", "descripcion": "Practicar operaciones con matrices", "vencimiento": "05-03-24", "estado": "pendiente"},
    {"id": 8, "titulo": "Estudiar estadística", "descripcion": "Revisar medidas de tendencia central", "vencimiento": "07-03-24", "estado": "pendiente"},
    {"id": 9, "titulo": "Hacer ejercicios de probabilidad", "descripcion": "Resolver problemas de combinatoria y eventos", "vencimiento": "10-03-24", "estado": "pendiente"},
    {"id": 10, "titulo": "Revisar lógica matemática", "descripcion": "Estudiar proposiciones y conectores lógicos", "vencimiento": "12-03-24", "estado": "pendiente"}
]

# Obtener todas las tareas
@app.get("/tareas/", tags=["Operaciones CRUD"])
def obtenertareas():
    return {"tareas": tareas}

# Obtener una tarea por ID
@app.get("/tareas/obtenet/{id}", tags=["Operaciones CRUD"])
def obtenertarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Crear una nueva tarea
@app.post("/tareas/agregar", tags=["Operaciones CRUD"])
def creartarea(nuevatarea: Dict):
    for tarea in tareas:
        if tarea["id"] == nuevatarea.get("id"):
            raise HTTPException(status_code=400, detail="ID ya existe")
    tareas.append(nuevatarea)
    return nuevatarea

# Actualizar una tarea existente
@app.put("/tareas/actualizar/{id}", tags=["Operaciones CRUD"])
def actualizartarea(id: int, tareaactualizada: Dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index].update(tareaactualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Eliminar una tarea
@app.delete("/tareas/del/{id}", tags=["Operaciones CRUD"])
def eliminartarea(id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            del tareas[index]
            return (tareas[index])
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
