"""
Clase Bebida. Hereda de la clase padre Producto.
"""
# Importación de la clase padre Producto para herencia
# from Semana6RestauranteApp.modelos.producto import Producto

from modelos.producto import Producto

class Bebida(Producto):
    # Clase hija que representa una bebida disponible. Aplica herencia y sobrescritura de métodos para el polimorfismo.
    def __init__(self, nombre, precio, volumen_ml, disponible=True):
        # Inicializa una bebida reutilizando el constructor del padre, ademas la invocación al constructor de la clase padre (Producto)
        super().__init__(nombre, precio, disponible)
        # Atributo propio y específico de la clase Bebida
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        # Sobrescribe el método de la clase Producto para demostrar polimorfismo.
        print("\n=== DETALLE DE BEBIDA ===")
        print(f"Bebida  : {self.nombre}")
        print(f"Precio  : ${self.obtener_precio():.2f}")
        print(f"Volumen : {self.volumen_ml} ml")
        print(f"Estado  : {'Disponible' if self.disponible else 'Agotado'}")

