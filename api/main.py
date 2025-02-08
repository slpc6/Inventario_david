"""Punto de inicio del proyecto para gestion de inventario"""

#External libraries
import uvicorn

from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse
from typing import List


#Own libraries
from model.inventario import Inventario
from mongoclient import get_client


app = FastAPI(
    title='Inventario',
    version='v1.0.0',
    description='proyecto para gestion de inventario'
)


@app.post(path='/agregar-objeto',
         description='Agrega un objeto al inventario.',
         response_description='Mensaje de OK',
         status_code=status.HTTP_201_CREATED,
         response_model=Inventario
         )
def agregar_objeto(item: Inventario, collenction=Depends(get_client)) -> JSONResponse:
    """Permite agregar un objeto al inventario, si el objeto ya existe no lo agrega.

    :args:
        - item: Objeto que sera insertado y que cuenta con los campos prensente en modelo/inventario.
        - collection: intancia de mongo.

    :Returns:
        Un Jsonresponse con un mensaje indicando si se pudo registrar correctamente el mensaje.

    """
    if collenction.find_one({'nombre': item.nombre}):
        return  JSONResponse({'msg': 'Este objeto ya esta registrado.'}, status_code=status.HTTP_400_BAD_REQUEST)

    result = collenction.insert_one(item.model_dump())
    return JSONResponse({'msg': 'OK', 'id': str(result.inserted_id)}, status_code=status.HTTP_201_CREATED)


@app.get(path='/listar-inventario',
         description="Muestra todos los objetos presentes en el inventario",
         response_description="",
         response_model=List[Inventario],
         status_code=status.HTTP_200_OK
         )
def listar_inventario(collection=Depends(get_client)) -> JSONResponse:
    """Permite listar todos los objetos registrados en la base de datos.

    :args:
        - item: Objeto que sera insertado y que cuenta con los campos prensente en modelo/inventario.
    :returns:
        Un Jsonresponse con la lista de los diferentes objetos que tiene la base de datos,
        pued estar vacia.
    
    """
    try:
        productos = list(collection.find({}))
        for producto in productos:
            producto["_id"] = str(producto["_id"])
        
    except Exception as e:
        print(e)
        return JSONResponse({'msg': 'Ocurrio un Error inesperado'}, status_code=status.HTTP_400_BAD_REQUEST)
    return productos


@app.get(path='/listar-objeto/{nombre}',
         description="Muestra uno de los objetos presentes en el inventario",
         response_model=Inventario,
         status_code=status.HTTP_200_OK
         )
def listar_inventario(nombre: str, collection=Depends(get_client)):
    try:
        producto = collection.find_one({"nombre": nombre}, {"_id": 0})
        if not producto:
            return JSONResponse({'msg': 'Producto no encontrado'}, status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse({'msg':'Ocurrio un Error inesperado'}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return producto


@app.delete("/inventario/{nombre}",
            response_model=dict)
def eliminar_inventario(nombre: str, collection=Depends(get_client)):
    result = collection.delete_one({"nombre": nombre})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto '{nombre}' eliminado"}


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
