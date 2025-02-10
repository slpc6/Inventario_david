// src/App.js
import React, { useState } from "react";
import InventoryForm from "./components/InventoryForm";
import InventoryList from "./components/InventoryList";
import InventoryEditForm from "./components/InventoryEditForm";
import { updateInventoryItem } from "./services/InventoryService";

const App = () => {
  const [refreshFlag, setRefreshFlag] = useState(false);
  const [itemToEdit, setItemToEdit] = useState(null);

  const handleItemAdded = () => {
    setRefreshFlag((prev) => !prev);
  };

  const handleEditItem = (item) => {
    setItemToEdit(item);
  };

  const handleUpdate = async (updatedItem) => {
    try {
      await updateInventoryItem(updatedItem.nombre, updatedItem);
      setItemToEdit(null);
      setRefreshFlag((prev) => !prev);
    } catch (err) {
      console.error("Error al actualizar objeto", err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-blue-600 text-white py-6 shadow">
        <div className="container mx-auto px-4">
          <h1 className="text-3xl font-bold">Gestión de Inventario</h1>
          <p className="mt-2 text-lg">Administra y controla tus objetos de manera sencilla</p>
        </div>
      </header>

      {/* Contenido */}
      <main className="container mx-auto px-4 py-8">
        {itemToEdit ? (
          <InventoryEditForm
            initialData={itemToEdit}
            onUpdate={handleUpdate}
            onCancel={() => setItemToEdit(null)}
          />
        ) : (
          <InventoryForm onItemAdded={handleItemAdded} />
        )}
        <InventoryList onEditItem={handleEditItem} refreshFlag={refreshFlag} />
      </main>
    </div>
  );
};

export default App;
