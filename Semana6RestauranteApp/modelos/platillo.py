"""
Clase Platillo.
Hereda de Producto.
"""

# Importación de la clase padre Producto para herencia

from modelos.producto import Producto

class Platillo(Producto):
    # Clase hija que representa un platillo del restaurante. Aplica herencia y sobrescritura de métodos para el polimorfismo.
    def __init__(self, nombre, precio, calorias, disponible=True):
        # Inicializa un platillo reutilizando el constructor del padre e incorporando su propio atributo especializado.
        # Invocación al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, disponible)
        # Atributo específico de la clase Platillo
        self.calorias = calorias

    def mostrar_informacion(self):
        # Sobrescribe el método de la clase Producto para demostrar polimorfismo.
        print("\n=== DETALLE DE PLATILLO ===")
        # Reutilizamos el comportamiento base o accedemos a los atributos heredados
        print(f"Platillo: {self.nombre}")
        print(f"Precio  : ${self.obtener_precio():.2f}")
        print(f"Calorías: {self.calorias} kcal")
        print(f"Estado  : {'Disponible' if self.disponible else 'Agotado'}")


