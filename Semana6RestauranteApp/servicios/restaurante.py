# Clase Restaurante. Gestiona los productos registrados.
"""
Clase Restaurante. Administra los productos registrados.
"""

class Restaurante:
    # Clase de servicio encargada de administrar el catálogo de productos y procesar la información de manera unificada.
    def __init__(self, nombre_establecimiento):
        # Inicializa el servicio con una lista vacía de productos.
        self.nombre_establecimiento = nombre_establecimiento
        self.catalogo_productos = []

    def agregar_producto(self, producto):
        # Recibe cualquier objeto que sea un Producto (o sus hijos) y lo añade a la lista.
        self.catalogo_productos.append(producto)
        print(f"✓ '{producto.nombre}' ha sido agregado al catálogo con éxito.")

    def mostrar_menu_completo(self):
        # Recorre el catálogo dinámico y ejecuta el método correspondiente. Aquí se evidencia directamente el POLIMORFISMO.
        print(f"\n=========================================")
        print(f"    MENÚ DEL RESTAURANTE: {self.nombre_establecimiento.upper()}")
        print(f"=========================================")
        
        if not self.catalogo_productos:
            print("El catálogo está vacío actualmente.")
            return

        print("\n--- Demostración de Polimorfismo en ejecución ---")
        for producto in self.catalogo_productos:
            # Python identifica en tiempo de ejecución el tipo de instancia (Platillo o Bebida) y ejecuta la versión del método 'mostrar_informacion' que le corresponde.
            producto.mostrar_informacion()

        print("\n") 
        
