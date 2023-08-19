class Product:
    def __init__(self, description: str, price: float, store_name: str=""):
        self._description = description
        self._price = price
        self._store_name = store_name

    @property
    def description(self) -> str:
        return self._description
    
    @property
    def price(self) -> float:
        return self._price
    
    @property.setter
    def price(self, new_price: float):
        if new_price < 0 or not isinstance(new_price, float):
            raise ValueError()
        self._price = new_price

    @property
    def store_name(self) -> str:
        return self._store_name
    
    @property.setter
    def store_name(self, new_store_name: str):
        if not isinstance(new_store_name, str):
            raise ValueError()
        self._store_name = new_store_name