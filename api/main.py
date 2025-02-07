"""Punto de inicio del proyecto para gestion de inventario"""

#External libraries
import uvicorn

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from model.inventario import Inventario
from typing import List


app = FastAPI(
    title='Inventario',
    version='v1.0.0',
    description='proyecto para gestion de inventario'
)


@app.get(path='/listar-inventario',
         description="Muestra todos los objetos presentes en el inventario",
         response_description="",
         response_model=List[Inventario],
         status_code=status.HTTP_200_OK
         )
def listar_inventario() -> JSONResponse:
    return JSONResponse('',status_code=status.HTTP_200_OK)


@app.get(path='/listar-objeto/{nombre}',
         description="Muestra uno de los objetos presentes en el inventario",
         response_model=Inventario,
         status_code=status.HTTP_200_OK
         )
def listar_inventario() -> JSONResponse:
    return JSONResponse('',status_code=status.HTTP_200_OK)


@app.post(path='/agregar-objeto',
         description="Saluda",
         response_description="Agrega un nuevo objeto al inventario",
         status_code=status.HTTP_200_OK,
         )
def menu() -> str:
    return JSONResponse('',status_code=status.HTTP_200_OK)


@app.delete(path='/eliminar-objeto',
         description="Saluda",
         response_description="Texto plano con saludo",
         status_code=status.HTTP_200_OK
         )
def menu() -> str:
    return 'Hola mundo'


@app.put(path='/actualizar-objeto',
         description="Saluda",
         response_description="Texto plano con saludo",
         status_code=status.HTTP_200_OK
         )
def menu() -> str:
    return 'Hola mundo'


if __name__ == '__main__':
    """
    Punto de entrada principal para ejecutar la aplicación con Uvicorn.
    """
    uvicorn.run(app="main:app", host="localhost", port=8080, reload=True)
