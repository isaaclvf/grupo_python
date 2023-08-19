class Rectangle:
    def __init__(self, height: float, width: float) -> None:
        self._height = height
        self._width = width

    @property
    def height(self) -> float:
        return self._height
    
    @property.setter
    def height(self, new_height: float):
        if new_height <= 0 or not isinstance(new_height, float):
            raise ValueError()
        self._height = new_height

    @property
    def width(self) -> float:
        return self._width
    
    @property.setter
    def width(self, new_width: float):
        if new_width <= 0 or not isinstance(new_width, float):
            raise ValueError()
        self._width = new_width