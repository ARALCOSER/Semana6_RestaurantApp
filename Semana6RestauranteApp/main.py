"""
Punto de entrada del sistema restaurante_app. Aquí se crean los objetos y se demuestra las propiedades de:
- Herencia
- Encapsulación, y
- Polimorfismo
"""
# Importación de clases desde los módulos correspondientes

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    # Punto de arranque de la aplicación de restaurante.
    # 1. Instanciar el servicio principal del restaurante
    mi_restaurante = Restaurante("vaca & Vaco")

    print("\n") 
    print("--- REGISTRANDO PRODUCTOS EN EL SISTEMA ---")
    
    # 2. Crear al menos dos objetos de tipo Platillo
    platillo1 = Platillo("Lomo a las finas Yerbas", 13.50, 650)
    platillo2 = Platillo("Parrillada Doble", 18.75, 720)

    # 3. Crear al menos dos objetos de tipo Bebida
    bebida1 = Bebida("Jugo de Mora Natural", 2.50, 400)
    bebida2 = Bebida("Vino sierra los Andes Malbec", 16.00, 180)

    # 4. Agregar los objetos creados al catálogo del Restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Muestra la información organizada en consola (Polimorfismo)
    mi_restaurante.mostrar_menu_completo()

    # 6. Muestra el correcto funcionamiento de la Encapsulación y Validación
    print("\n--- PRUEBA DE ENCAPSULACIÓN Y VALIDACIÓN ---")
    print(f"Precio actual de {platillo1.nombre}: ${platillo1.obtener_precio():.2f}")
    
    print("\nIntentando cambiar el precio a un valor negativo (-5.00):")
    platillo1.cambiar_precio(-5.00)  # Saltara el error controlado
    
    print("\nIntentando cambiar el precio a un valor válido (19.99):")
    platillo1.cambiar_precio(19.99)  # Debera actualizarse correctamente

    # Volvemos a mostrar el menú para verificar los cambios finales
    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    main()

