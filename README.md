# 🍽️ SISTEMA DE GESTIÓN DE RESTAURANTE VACA & VACO

## 👨‍🎓 Estudiante

RAMIRO ALCOSER ALLAICA

---

# 📖 Descripción

Este proyecto fue desarrollado en Python utilizando los principios fundamentales de la Programación Orientada a Objetos (POO).

El sistema permite administrar productos de un restaurante mediante una estructura basada en herencia, encapsulación y polimorfismo.

Se manejan dos tipos de productos:

- Platillos
- Bebidas

Todos ellos heredan de una clase principal llamada Producto.

---

# 🎯 Objetivos

Aplicar correctamente:

- Clases y objetos
- Constructores
- Herencia
- Encapsulación
- Polimorfismo
- Modularidad en Python

---

# 📁 Estructura del Proyecto

```text
restaurante_app/
│
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

---

# 🧬 Relación de Herencia

```text
Producto
├── Platillo
└── Bebida
```

La clase Producto actúa como clase padre.

Las clases Platillo y Bebida heredan sus atributos y métodos utilizando:

```python
super().__init__()
```

---

# 🔒 Encapsulación

Se encapsuló el atributo:

```python
__precio
```

Su acceso se realiza únicamente mediante:

```python
obtener_precio()
cambiar_precio()
```

Además, se valida que el precio nunca sea menor o igual a cero.

---

# 🔄 Polimorfismo

Las clases Platillo y Bebida sobrescriben:

```python
mostrar_informacion()
```

Esto permite que el mismo método produzca resultados diferentes dependiendo del objeto.

Ejemplo:

```python
for producto in self.productos:
    producto.mostrar_informacion()
```

---

# ⚙️ Tecnologías

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# ▶️ Ejecución

Ejecutar:

```bash
python main.py
```

---

# 💡 Reflexión

La Programación Orientada a Objetos permite diseñar sistemas más organizados, reutilizables y fáciles de mantener. La aplicación de herencia reduce la duplicación de código, la encapsulación protege los datos importantes y el polimorfismo proporciona flexibilidad para trabajar con diferentes tipos de objetos utilizando una misma interfaz.

---

# ✅ Conceptos demostrados

- Clases y objetos
- Constructor __init__()
- Herencia
- Encapsulación
- Polimorfismo
- Modularidad
- Uso de super()
- Métodos getter y setter
- Validación de datos
