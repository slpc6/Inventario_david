# Documentación del Proyecto

## Introducción

Este proyecto es una aplicación de gestión de inventario que consta de un backend en Python y un frontend en React. La API permite administrar objetos en un inventario, y el frontend proporciona una interfaz amigable para los usuarios.

## Backend (API en Python)

### Instalación y Configuración

Instalar dependencias:

```Bash
pip install -r requirements.txt
```

Configurar la conexión a la base de datos en config.py.

Ejecutar la API:
```Bash
python main.py
```

## Rutas Principales

- GET /listar-inventario → Lista todos los objetos del inventario.

- GET /listar-objeto/<nombre> → Obtiene un objeto específico.

- POST /agregar-objeto → Agrega un nuevo objeto.

- PUT /actualizar-objeto/<nombre> → Actualiza un objeto existente.

- DELETE /eliminar-objeto/<nombre> → Elimina un objeto.

## Frontend (React + Vite)

### Instalación y Ejecución

Instalar dependencias:
```Bash
npm install
```
Ejecutar el frontend:
```Bash
npm run dev
```

## Caracteristicas

Es una SPA que proporcia un acceso visible y amable con el usuario a los metodos mencionados anteriormente en el API de la aplicacion.

Proporciona una interfaz interactuable para poder ver los objetos del inventario, agregar nuevos, modificar existentes y eliminarlos de ser necesario.

## Despliegue con Docker
Se ejecuta el archivo ```docker-compose.yaml``` con la siguiente intruccion para construir las imagenes y desplegar los servicios:

```bash
docker-compose --profile full up -d --build
```

Y para detener la ejecucion de la aplicacion se usa:
```bash
docker-compose --profile full down 
```

Ambos comando contenidos dentro del archivo ```run.sh``` que al ser invocado desde una terminal linux reiniciaran este proceso automaticamente.