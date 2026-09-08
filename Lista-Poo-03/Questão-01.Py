import math

class Retangulo:
    def __init__(self, b: float, h: float):
        self._b = b if b > 0 else 1.0
        self._h = h if h > 0 else 1.0

    def SetBase(self, b: float) -> None:
        if b > 0:
            self._b = b

    def SetAltura(self, h: float) -> None:
        if h > 0:
            self._h = h  

    def GetBase(self) -> float:
        return self._b

    def GetAltura(self) -> float:
        return self._h  

    def CalcArea(self) -> float:
        return self._b * self._h

    def CalcDiagonal(self) -> float:
        return math.sqrt(self._b**2 + self._h**2)

    def ToString(self) -> str:
        return f"Retangulo [Base:{self._b}, Altura:{self._h}, Area:{self.CalcArea()}, Diagonal:{self.CalcDiagonal():.2f}]"

    def __str__(self) -> str:  
        return self.ToString()
