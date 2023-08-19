from math import sqrt

class RightTriangle():
    def __init__(self, perpendicular: float, base: float) -> None:
        self._perpendicular = perpendicular
        self._base = base
        self._hypotenuse = self.__calculate_hypotenuse(perpendicular, base)

    @property
    def perpendicular(self):
        return self._perpendicular
    
    @property.setter
    def perpendicular(self, new_perpendicular):
        self._perpendicular = new_perpendicular
        self.__update_hypotenuse()

    @property
    def base(self):
        return self._base
    
    @property.setter
    def base(self, new_base):
        self._base = new_base
        self.__update_hypotenuse()

    def __calculate_hypotenuse(self, perpendicular: float, base: float) -> float:
        return sqrt(perpendicular**2 + base**2)
    
    def __update_hypotenuse(self):
        self._hypotenuse = self.__calculate_hypotenuse(self._perpendicular, self._base)