import json
import os # Se puede usar para verificar si el archivo existe
from pathlib import Path # Opcional: para gestión de rutas (Unidad 4)

NOMBRE_ARCHIVO = "inventario.json"

# --- Parte 1: Clase y Estructura de Datos ---

class Producto:
    """Define la estructura de un producto en el inventario."""
    def __init__(self, nombre: str, cantidad: int, precio: float):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para guardar en JSON."""
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

# --- Parte 2: Funciones de Persistencia (Unidad 4) ---

def cargar_inventario() -> list:
    """
    [Implementación obligatoria - Tarea para el Estudiante B / Issue #2]
    Carga el inventario desde el archivo JSON.
    DEBE CAPTURAR FileNotFoundError y devolver una lista vacía si el archivo no existe.
    """
    try:
        # 1. Implementar la lectura segura del archivo (with open() y json.load())
        # 2. Si el archivo existe, retornar la lista de productos
        # 3. Si ocurre FileNotFoundError, imprimir una advertencia y retornar []
        return [] # Implementación Pendiente
    except Exception as e:
        print(f"Error al cargar el inventario: {e}")
        return []

def guardar_inventario(inventario: list):
    """
    [Implementación obligatoria]
    Guarda la lista de inventario completa en el archivo JSON.
    """
    # 1. Implementar la escritura segura del archivo (with open() y json.dump())
    pass # Implementación Pendiente

# --- Parte 3: Funciones CRUD ---

def agregar_producto(inventario: list):
    """
    [Implementación obligatoria - Tarea para el Estudiante A / Issue #1]
    Solicita datos al usuario y los agrega al inventario.
    DEBE CAPTURAR ValueError si la Cantidad o el Precio no son numéricos.
    """
    print("\n--- AGREGAR PRODUCTO ---")
    # 1. Solicitar Nombre
    # 2. Solicitar Cantidad y Precio
    # 3. Implementar try-except para validar Cantidad y Precio (float/int)
    # 4. Crear el objeto Producto y agregarlo a 'inventario'
    # 5. Llamar a guardar_inventario()
    print("Funcionalidad de agregar producto pendiente.") # Implementación Pendiente

def mostrar_inventario(inventario: list):
    """
    [Implementación obligatoria - Tarea para el Estudiante B / Issue #2]
    Muestra la lista completa de productos.
    """
    print("\n--- INVENTARIO ACTUAL ---")
    if not inventario:
        print("El inventario está vacío.")
        return
    # 1. Recorrer la lista 'inventario' e imprimir los detalles de cada producto
    print("Funcionalidad de mostrar inventario pendiente.") # Implementación Pendiente

def editar_producto(inventario: list):
    """
    [Implementación obligatoria - Tarea para el Estudiante A / Issue #3]
    Busca un producto por nombre y permite modificar su cantidad/precio.
    DEBE CAPTURAR ValueError y manejar la lógica de "Producto no encontrado".
    """
    print("\n--- EDITAR PRODUCTO ---")
    # 1. Solicitar el nombre del producto a editar
    # 2. Buscar el producto en la lista 'inventario'
    # 3. Si se encuentra: solicitar nuevos datos y validar con try-except
    # 4. Si no se encuentra: imprimir mensaje "Producto no encontrado"
    # 5. Llamar a guardar_inventario()
    print("Funcionalidad de editar producto pendiente.") # Implementación Pendiente

# --- Parte 4: Bucle Principal del Programa ---

def main():
    """Bucle principal de la aplicación de consola."""
    inventario = cargar_inventario() # Cargar el inventario al iniciar
    
    while True:
        print("\n==================================")
        print(" GESTOR DE INVENTARIO SEGURO (GIS) ")
        print("==================================")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Editar producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            mostrar_inventario(inventario)
        elif opcion == '3':
            editar_producto(inventario)
        elif opcion == '4':
            print("Guardando datos y saliendo del Gestor de Inventario. ¡Adiós!")
            guardar_inventario(inventario)
            break
        else:
            # Capturar error de opción inválida (sin usar try-except)
            print("\n❌ Opción inválida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()