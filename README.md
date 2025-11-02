# Ejercicio08 - Concesionario

Nombre de autor: Jhosep Diaz
Fecha: 2025-11-02

Descripción
-----------
Este proyecto implementa una pequeña aplicación de consola para gestionar vehículos (automóviles y motos).

Archivos principales
-------------------
- `main.py` — Punto de entrada del programa.
- `vehiculo.py` — Clase base Vehículo.
- `automovil.py` — Implementación de Automóvil.
- `moto.py` — Implementación de Moto.

Requisitos
---------
- Python 3.8 o superior.

Cómo ejecutar
-------------
Abrir PowerShell y situarse en la carpeta del proyecto. Por ejemplo:

```powershell
cd "c:\Users\User\Ejemplo-Concesionario"
python .\main.py
```

Funcionamiento
-------------
Al ejecutar `main.py` el programa crea una lista de ejemplo con objetos `Automovil` y `Moto` y recorre esa lista mostrando la información de cada vehículo (utiliza el método `__str__` de forma polimórfica). Además calcula el valor final de cada vehículo llamando a `precio_final()` y suma esos valores para mostrar en consola el valor total del inventario.
