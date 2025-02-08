# 📌 Documentación del Proyecto de Gestión de Inventario

## 📖 Descripción
Este proyecto es una API desarrollada en **FastAPI** para la gestión de inventario. Permite agregar, listar, actualizar y eliminar objetos de un inventario almacenado en una base de datos **MongoDB**.

---

## 🚀 Instalación y Ejecución

### 📂 **Requisitos previos**
- Python 3.12
- Docker y Docker Compose
- MongoDB
- Archivo `.env` con la variable `DBCONN` configurada para la conexión a MongoDB

### 📥 **Clonar el repositorio**
```sh
git clone <repositorio>
cd <repositorio>
```

### 🏗️ **Ejecutar con Docker Compose**
```sh
docker-compose up --build -d
```

### ▶️ **Ejecutar localmente**
Instalar dependencias:
```sh
pip install -r requirements.txt
```
Ejecutar la API:
```sh
python main.py
```

---

## 📌 Endpoints de la API

### 🔹 **Agregar un objeto**
**POST** `/agregar-objeto`

**Descripción:** Agrega un objeto al inventario.

**Cuerpo de la solicitud:**
```json
{
  "nombre": "Laptop HP",
  "imagen": "bytes",
  "cantidad": 10,
  "ubicacion": "Almacén 1",
  "tipo": "electrónico",
  "observaciones": "Nuevo ingreso",
  "serial": "HP12345",
  "estado": "nuevo",
  "fecha": "2025-02-07T12:00:00"
}
```

**Respuesta:**
```json
{
  "msg": "OK",
  "id": "654d3a1c9a1c"
}
```

---

### 🔹 **Listar todo el inventario**
**GET** `/listar-inventario`

**Descripción:** Obtiene la lista de todos los objetos del inventario.

**Respuesta:**
```json
[
  {
    "nombre": "Laptop HP",
    "imagen": "bytes",
    "cantidad": 10,
    "ubicacion": "Almacén 1",
    "tipo": "electrónico",
    "observaciones": "Nuevo ingreso",
    "serial": "HP12345",
    "estado": "nuevo",
    "fecha": "2025-02-07T12:00:00"
  }
]
```

---

### 🔹 **Buscar un objeto por nombre**
**GET** `/listar-objeto/{nombre}`

**Descripción:** Obtiene un objeto específico por su nombre.

**Respuesta si existe:**
```json
{
  "nombre": "Laptop HP",
  "cantidad": 10,
  "ubicacion": "Almacén 1",
  "tipo": "electrónico",
  "serial": "HP12345",
  "estado": "nuevo",
  "fecha": "2025-02-07T12:00:00"
}
```

**Respuesta si no existe:**
```json
{
  "msg": "Producto no encontrado"
}
```

---

### 🔹 **Actualizar un objeto**
**PUT** `/actualizar-objeto/{nombre}`

**Descripción:** Modifica un objeto ya existente en el inventario.

**Cuerpo de la solicitud:** *(mismo formato que POST)*

**Respuesta:**
```json
{
  "msg": "Laptop HP actualizado exitosamente"
}
```

---

### 🔹 **Eliminar un objeto**
**DELETE** `/eliminar-objeto/{nombre}`

**Descripción:** Elimina un objeto del inventario.

**Respuesta si se elimina:**
```json
{
  "mensaje": "Producto 'Laptop HP' eliminado"
}
```

**Respuesta si no existe:**
```json
{
  "msg": "Producto no encontrado"
}
```

---

## ⚙️ Configuración del entorno
### 📌 **MongoDB Connection**
En el archivo `.env`, agregar la conexión a la base de datos MongoDB:

---

## 📜 **Estructura del Proyecto**
```
📂 api/
 ├── 📜 main.py  # API principal con FastAPI
 ├── 📜 mongoclient.py  # Conexión a MongoDB
 ├── 📂 model/
 │   ├── 📜 inventario.py  # Modelo de datos con Pydantic
 ├── 📜 Dockerfile  # Configuración del contenedor Docker
 ├── 📜 docker-compose.yml  # Orquestación con Docker Compose
 ├── 📜 requirements.txt  # Dependencias de Python
```

---

## 🛠️ Tecnologías Utilizadas
- **Python 3.12**
- **FastAPI** (Framework web)
- **MongoDB** (Base de datos NoSQL)
- **Pydantic** (Validación de datos)
- **Docker & Docker Compose** (Contenedores)
- **Uvicorn** (Servidor ASGI)

---

## 📌 Licencia
Este proyecto está bajo la licencia **MIT**.
