"""Clases que definen la estructura basica de los objetos que ingresara el usuario."""

from pydantic import BaseModel, Field, conint
from datetime import datetime
from enum import Enum
from typing import Optional


class EstadoEnum(str, Enum):
    nuevo = 'nuevo'
    actualizado = 'actualizado'
    robado = 'robado'
    guardado = 'guardado'


class TipoEnum(str, Enum):
    papeleri_amaterial = "Papelería y materiales "
    proteccion_personal = 'Protección personal'
    mantenimiento = 'Mantenimiento' 
    herramientas = 'Herramientas'
    consumibles_equipos = 'Consumibles equipos '
    componentes_electronicos = 'Componentes electrónicos'
    souvenirs = 'Souvenirs'


class Inventario(BaseModel):
    nombre: str = Field(..., title="Nombre del producto", max_length=100)
    imagen: Optional[bytes] = None
    cantidad: int = Field(..., title="Cantidad disponible")
    ubicacion: str = Field(..., max_length=100)
    tipo: TipoEnum
    observaciones: Optional[str] = None
    serial: str = Field(..., title="Número de serie", max_length=50)
    estado: EstadoEnum
    fecha: datetime = Field(default_factory=datetime)
