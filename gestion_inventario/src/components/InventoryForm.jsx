// src/components/InventoryForm.js
import React, { useState } from "react";
import { addInventoryItem } from "../services/InventoryService";

const InventoryForm = ({ onItemAdded }) => {
  const [nombre, setNombre] = useState("");
  const [imagen, setImagen] = useState(null);
  const [cantidad, setCantidad] = useState(0);
  const [ubicacion, setUbicacion] = useState("");
  const [tipo, setTipo] = useState("Papelería y materiales ");
  const [observaciones, setObservaciones] = useState("");
  const [serial, setSerial] = useState("");
  const [estado, setEstado] = useState("nuevo");
  const [error, setError] = useState(null);

  // Convierte archivo a Base64
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagen(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newItem = {
      nombre,
      imagen,
      cantidad,
      ubicacion,
      tipo,
      observaciones,
      serial,
      estado,
    };
    try {
      await addInventoryItem(newItem);
      onItemAdded(); // Para refrescar el listado
      // Limpiar el formulario
      setNombre("");
      setImagen(null);
      setCantidad(0);
      setUbicacion("");
      setTipo("Papelería y materiales ");
      setObservaciones("");
      setSerial("");
      setEstado("nuevo");
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-xl mx-auto bg-white p-6 rounded shadow mb-8">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">Agregar Objeto</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Nombre del producto:</label>
        <input
          type="text"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          required
          maxLength={100}
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Imagen:</label>
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="mt-1 block w-full"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Cantidad:</label>
        <input
          type="number"
          value={cantidad}
          onChange={(e) => setCantidad(Number(e.target.value))}
          required
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Ubicación:</label>
        <input
          type="text"
          value={ubicacion}
          onChange={(e) => setUbicacion(e.target.value)}
          required
          maxLength={100}
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Tipo:</label>
        <select
          value={tipo}
          onChange={(e) => setTipo(e.target.value)}
          required
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        >
          <option value="Papelería y materiales ">Papelería y materiales</option>
          <option value="Protección personal">Protección personal</option>
          <option value="Mantenimiento">Mantenimiento</option>
          <option value="Herramientas">Herramientas</option>
          <option value="Consumibles equipos ">Consumibles equipos</option>
          <option value="Componentes electrónicos">Componentes electrónicos</option>
          <option value="Souvenirs">Souvenirs</option>
        </select>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Observaciones:</label>
        <textarea
          value={observaciones}
          onChange={(e) => setObservaciones(e.target.value)}
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        ></textarea>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Serial:</label>
        <input
          type="text"
          value={serial}
          onChange={(e) => setSerial(e.target.value)}
          required
          maxLength={50}
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        />
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700">Estado:</label>
        <select
          value={estado}
          onChange={(e) => setEstado(e.target.value)}
          required
          className="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:border-blue-300"
        >
          <option value="nuevo">Nuevo</option>
          <option value="actualizado">Actualizado</option>
          <option value="robado">Robado</option>
          <option value="guardado">Guardado</option>
        </select>
      </div>

      <button
        type="submit"
        className="w-full py-2 px-4 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
      >
        Agregar objeto
      </button>
    </form>
  );
};

export default InventoryForm;
