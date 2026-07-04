"""
Clase padre, Producto.
Representa un producto general del restaurante.
Demuestra encapsulación mediante el atributo privado __precio.
"""

class Producto:
    # Clase padre que representa un producto general del restaurante. Demuestra los principios de abstracción y encapsulación.
    def __init__(self, nombre, precio, disponible=True):
        # Inicializa los atributos comunes de un producto.
        self.nombre = nombre
        # Atributo encapsulado (privado) para proteger la integridad de los datos
        self.__precio = precio 
        self.disponible = disponible

    # Método de acceso para obtener el precio protegido
    def obtener_precio(self):
        # Devuelve el precio del producto.
        return self.__precio

    # Setter: Método de modificación con lógica de validación
    def cambiar_precio(self, nuevo_precio):
        # Actualiza el precio del producto validando que sea mayor a cero, pongo esta validacion para evitar precios negativos.
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"El precio de '{self.nombre}' se actualizó a ${nuevo_precio:.2f}")
        else:
            print("Error: El precio debe ser un valor numérico positivo mayor que cero.")

    def mostrar_informacion(self):
        # Muestra los datos básicos del producto. Este método será sobrescrito por las clases hijas.
        estado = "Disponible" if self.disponible else "Agotado"
        print(f"Producto: {self.nombre}")
        print(f"Precio  : ${self.__precio:.2f}")
        print(f"Estado  : {estado}")


