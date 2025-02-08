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
        - collection: instancia de mongo.

    :Returns:
        Un Jsonresponse con un mensaje indicando si se pudo registrar correctamente el mensaje.

    """
    if collenction.find_one({'nombre': item.nombre}):
        return  JSONResponse({'msg': 'Este objeto ya esta registrado.'}, status_code=status.HTTP_400_BAD_REQUEST)

    result = collenction.insert_one(item.model_dump())
    return JSONResponse({'msg': 'OK', 'id': str(result.inserted_id)}, status_code=status.HTTP_201_CREATED)


@app.get(path='/listar-inventario',
         description="Muestra todos los objetos presentes en el inventario",
         response_model=List[Inventario],
         status_code=status.HTTP_200_OK
         )
def listar_inventario(collection=Depends(get_client)) -> JSONResponse:
    """Permite listar todos los objetos registrados en la base de datos.

    :args:
        - collection: instancia de mongo.
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
def listar_inventario(nombre: str, collection=Depends(get_client)) -> JSONResponse | Inventario:
    """Permite consultar un objeto especifico por su nombre
    :args:
        - nombre: nombre del objeto que quiere ser consultado
        - collection: instancia de mongo.
    :returns:
        el producto encontrado o un Jsonresponse con un mejsaje de error
    """
    try:
        producto = collection.find_one({"nombre": nombre}, {"_id": 0})
        if not producto:
            return JSONResponse({'msg': 'Producto no encontrado'}, status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse({'msg':'Ocurrio un Error inesperado'}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return producto


@app.delete('/eliminar-objeto/{nombre}',
            response_model=dict,
            status_code=status.HTTP_200_OK
            )
def eliminar_inventario(nombre: str, collection=Depends(get_client)) -> JSONResponse:
    """Permite eliminar un objeto presente en el inventario.

    :args:
        - nombre: nombre del objeto que se quiere eliminar
        - collection: instancia de mongo.
    :returns:
        un Jsonresponse con un mensaje de exito o fallo en la eliminacion.
    """
    result = collection.delete_one({'nombre': nombre})
    if result.deleted_count == 0:
        return JSONResponse({'msg': 'Producto no encontrado'}, status_code=404)
    return {'mensaje': f'Producto "{nombre}" eliminado'}


@app.put(path='/actualizar-objeto/{nombre}',
        status_code=status.HTTP_200_OK,
        response_model=dict
        )
def actualizar_objeto(nombre: str, item: Inventario, collection=Depends(get_client)) -> JSONResponse:
    try:
        item_dict = item.model_dump()
        item_dict["estado"] = item.estado.value
        item_dict["tipo"] = item.tipo.value

        if isinstance(item.imagen, bytes):
            item_dict["imagen"] = item.imagen.decode('utf-8', errors='ignore')
        
        result = collection.update_one({"nombre": nombre}, {"$set": item_dict})
        if result.matched_count == 0:
            return JSONResponse({'msg': 'Producto no encontrado'}, status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse({'msg': 'Ocurrio un error inesperado al momento de actualizar el objeto.'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return JSONResponse({'msg': f'{nombre} actualizado exitosamente'}, status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    """
    Punto de entrada principal para ejecutar la aplicación con Uvicorn.
    """
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)
