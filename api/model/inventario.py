"""Clases que definen la estructura basica de los objetos que ingresara el usuario."""

#External libraries
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class EstadoEnum(str, Enum):
    """Representa los posibles estados del objeto en el inventario."""

    nuevo = 'nuevo'
    actualizado = 'actualizado'
    robado = 'robado'
    guardado = 'guardado'


class TipoEnum(str, Enum):
    """Representa los posibles tipos de objeots en el inventarios."""

    papeleri_amaterial = "Papelería y materiales "
    proteccion_personal = 'Protección personal'
    mantenimiento = 'Mantenimiento' 
    herramientas = 'Herramientas'
    consumibles_equipos = 'Consumibles equipos '
    componentes_electronicos = 'Componentes electrónicos'
    souvenirs = 'Souvenirs'


class Inventario(BaseModel):
    """Representacion del objeto que sera ingresado por los usuarios para guardar en el inventario"""
    
    nombre: str = Field(..., title="Nombre del producto", max_length=100)
    imagen: Optional[bytes] = None
    cantidad: int = Field(..., title="Cantidad disponible")
    ubicacion: str = Field(..., max_length=100)
    tipo: TipoEnum
    observaciones: Optional[str] = None
    serial: str = Field(..., title="Número de serie", max_length=50)
    estado: EstadoEnum
#    fecha: datetime = Field(default_factory=datetime)
