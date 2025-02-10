// src/components/InventoryList.js
import React, { useState, useEffect } from "react";
import { getInventory, deleteInventoryItem } from "../services/InventoryService";

const InventoryList = ({ onEditItem, refreshFlag }) => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchItems = async () => {
    try {
      setLoading(true);
      const data = await getInventory();
      setItems(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchItems();
  }, [refreshFlag]);

  const handleDelete = async (nombre) => {
    try {
      await deleteInventoryItem(nombre);
      fetchItems();
    } catch (err) {
      console.error("Error al eliminar objeto", err);
    }
  };

  if (loading) return <p className="text-center text-gray-600">Cargando...</p>;
  if (error)
    return <p className="text-center text-red-500">Error: {error}</p>;

  return (
    <div className="max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Inventario</h2>
      {items.length === 0 ? (
        <p className="text-center text-gray-600">No hay objetos registrados.</p>
      ) : (
        <ul className="space-y-4">
          {items.map((item) => (
            <li
              key={item.nombre}
              className="border border-gray-200 rounded p-4 shadow-sm bg-white"
            >
              <h3 className="text-xl font-semibold text-gray-800">{item.nombre}</h3>
              <p className="text-gray-600">
                <strong>Cantidad:</strong> {item.cantidad}
              </p>
              <p className="text-gray-600">
                <strong>Ubicación:</strong> {item.ubicacion}
              </p>
              <p className="text-gray-600">
                <strong>Tipo:</strong> {item.tipo}
              </p>
              <p className="text-gray-600">
                <strong>Serial:</strong> {item.serial}
              </p>
              <p className="text-gray-600">
                <strong>Estado:</strong> {item.estado}
              </p>
              <div className="mt-4 flex space-x-2">
                <button
                  onClick={() => onEditItem(item)}
                  className="py-1 px-3 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
                >
                  Editar
                </button>
                <button
                  onClick={() => handleDelete(item.nombre)}
                  className="py-1 px-3 bg-red-600 text-white rounded hover:bg-red-700 transition-colors"
                >
                  Eliminar
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default InventoryList;
