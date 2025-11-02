from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, puertas: int):
        super().__init__(marca, modelo, precio_base)
        if puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor que 0")
        self._puertas = puertas

    @property
    def puertas(self) -> int:
        return self._puertas

    def impuesto(self) -> float:
        impto = self.precio_base * 0.08  # Impuesto base del 8%
        dscto = self.precio_base * 0.01 if self.puertas == 5 else 0  # Descuento del 1% si tiene 5 puertas
        return impto - dscto

    def ficha(self) -> str:
        return f"Automovil  |  {super().ficha()}  |  {self.puertas} puertas"