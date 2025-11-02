from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, precio_base: float, cc: int):
        super().__init__(marca, modelo, precio_base)
        if cc <= 0:
            raise ValueError("El cilindraje debe ser mayor que 0")
        self._cc = cc

    @property
    def cc(self) -> int:
        return self._cc

    def impuesto(self) -> float:
        tasa = 0.05 if self.cc <= 250 else 0.09  # Tasa del 5% si cc <= 250, sino 9%
        return self.precio_base * tasa

    def ficha(self) -> str:
        return f"Moto       |  {super().ficha()}  |  {self.cc}   cc "