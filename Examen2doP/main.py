
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field
from typing import  List


app = FastAPI(
    title="Esamen 2doP"
)


class modeloUsuario(BaseModel):
    nombre: str = Field(..., min_length=3, description="solo caracteres minimo 3")
    No_Licencia: str = Field(...,min_length=12, max_length=12, description="solo caracteres 12")
    Tipo_Licencia: str = Field(...,min_length=1, max_length=1, description="ID unico y solo numeros positivos")
                               
conductores = [
    {"nombre": "Ivan", "Tipo_Licencia": "A", "No_Licencia": "1f9uhf9uh2fu"},
    {"nombre": "Carlos", "Tipo_Licencia": "B", "No_Licencia": "2f9uhf9uh2fu"},
    {"nombre": "María", "Tipo_Licencia": "C", "No_Licencia": "3f9uhf9uh2fu"},
    {"nombre": "Lucía", "Tipo_Licencia": "D", "No_Licencia": "4f9uhf9uh2fu"},
]

@app.get("/getconductores",response_model=List[modeloUsuario], tags=["Operaciones CRUD"])
def leerconductores():
    return conductores

@app.put("/usuario/{No_Licencia}",response_model=modeloUsuario, tags=["Operaciones CRUD"])
def actualizar_usuario(No_Licencia: str, conductorActualizado: dict):
    for index, usr in enumerate(conductores):
        if usr["No_Licencia"] == No_Licencia:
            conductores[index].update(conductorActualizado)
            return conductores[index]
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")