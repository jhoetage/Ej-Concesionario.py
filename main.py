from typing import List
from vehiculo import Vehiculo
from automovil import Automovil
from moto import Moto

def main():
    # Crear lista de vehículos (polimorfismo)
    inventario: List[Vehiculo] = [
        Automovil("Toyota", "Yaris ", 40000, 5),
        Moto("Honda ", "CB190R", 20000, 190),
        Automovil("Mazda ", "3     ", 25000, 4),
        Moto("BMW   ", "G310R ", 34000, 350)
    ]

    # Mostrar información de cada vehículo
    total = 0.0
    for vehiculo in inventario:
        print(vehiculo)  # Usa __str__ polimórficamente
        total += vehiculo.precio_final()

    # Mostrar total del inventario
    print(f"\nValor total del inventario: ${total:.2f}")

if __name__ == "__main__":
    main()