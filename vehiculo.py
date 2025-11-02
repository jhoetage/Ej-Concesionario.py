from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, precio_base: float):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que 0")
        self._marca = marca
        self._modelo = modelo
        self._precio_base = precio_base

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @abstractmethod
    def impuesto(self) -> float:
        pass

    def precio_final(self) -> float:
        return self.precio_base + self.impuesto()

    def ficha(self) -> str:
        return f"{self.marca} {self.modelo} (${self.precio_base:.2f})"

    def __str__(self) -> str:
        return f"{self.ficha()}  |  Final: ${self.precio_final():.2f}"