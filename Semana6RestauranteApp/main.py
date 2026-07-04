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

def mostrar_menu():
    """
    Muestra el menú principal interactivo del sistema de restaurante.
    """
    print("\n==========================================================")
    print("      SISTEMA DE GESTIÓN DEL RESTAURANTE VACA & VACO"       )
    print("==========================================================")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar el menú completo")
    print("4. Modifica el precio de un producto")
    print("5. Salir del sistema")
    print("===========================================================")

def registrar_platillo(restaurante):
    print("\n=== REGISTRAR NUEVO PLATILLO ===")
    nombre = input("Ingrese el nombre del platillo: ")
    try:
        precio = float(input("Ingrese el precio: $"))
        calorias = int(input("Ingrese las calorías (kcal): "))
        
        nuevo_platillo = Platillo(nombre, precio, calorias)
        restaurante.agregar_producto(nuevo_platillo)
    except ValueError:
        print("Error: Precio o calorías inválidos. Registro cancelado.")

def registrar_bebida(restaurante):
    print("\n=== REGISTRAR NUEVA BEBIDA ===")
    nombre = input("Ingrese el nombre de la bebida: ")
    try:
        precio = float(input("Ingrese el precio: $"))
        volumen = int(input("Ingrese el volumen (ml): "))
        
        nueva_bebida = Bebida(nombre, precio, volumen)
        restaurante.agregar_producto(nueva_bebida)
    except ValueError:
        print("Error: Precio o volumen inválidos. Registro cancelado.")

def modificar_precio_interactivo(restaurante):
    print("\n=== MODIFICAR PRECIO DE PRODUCTO ===")
    if not restaurante.catalogo_productos:
        print("No hay productos en el catálogo.")
        return
        
    nombre_buscar = input("Ingrese el nombre del producto a modificar: ")
    encontrado = False
    
    for producto in restaurante.catalogo_productos:
        if producto.nombre.lower() == nombre_buscar.lower():
            encontrado = True
            try:
                print(f"Precio actual de {producto.nombre}: ${producto.obtener_precio():.2f}")
                nuevo_precio = float(input("Ingrese el nuevo precio: $"))
                producto.cambiar_precio(nuevo_precio)
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")
            break
            
    if not encontrado:
        print("Producto no encontrado en el catálogo.")

def main():
    # Instanciamos el servicio principal del restaurante
    mi_restaurante = Restaurante("Vaca & Vaco")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_platillo(mi_restaurante)
        elif opcion == "2":
            registrar_bebida(mi_restaurante)
        elif opcion == "3":
            mi_restaurante.mostrar_menu_completo()
        elif opcion == "4":
            modificar_precio_interactivo(mi_restaurante)
        elif opcion == "5":
            print("Saliendo del sistema... ¡Buen provecho!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

