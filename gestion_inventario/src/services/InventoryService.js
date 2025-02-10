// src/services/InventoryService.js

const API_BASE_URL = "http://localhost:8080"; // Ajusta este valor según tu configuración de Docker

// Listar todos los objetos
export async function getInventory() {
  const response = await fetch(`${API_BASE_URL}/listar-inventario`);
  if (!response.ok) {
    throw new Error("Error al obtener el inventario");
  }
  return response.json();
}

// Obtener un objeto por nombre
export async function getInventoryItem(nombre) {
  const response = await fetch(
    `${API_BASE_URL}/listar-objeto/${encodeURIComponent(nombre)}`
  );
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.msg || "Error al obtener el objeto");
  }
  return response.json();
}

// Agregar un nuevo objeto
export async function addInventoryItem(item) {
  const response = await fetch(`${API_BASE_URL}/agregar-objeto`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(item),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.msg || "Error al agregar objeto");
  }
  return response.json();
}

// Actualizar un objeto existente
export async function updateInventoryItem(nombre, item) {
  const response = await fetch(
    `${API_BASE_URL}/actualizar-objeto/${encodeURIComponent(nombre)}`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(item),
    }
  );
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.msg || "Error al actualizar objeto");
  }
  return response.json();
}

// Eliminar un objeto
export async function deleteInventoryItem(nombre) {
  const response = await fetch(
    `${API_BASE_URL}/eliminar-objeto/${encodeURIComponent(nombre)}`,
    {
      method: "DELETE",
    }
  );
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.msg || "Error al eliminar objeto");
  }
  return response.json();
}
