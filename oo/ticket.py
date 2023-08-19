class Ticket():
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self) -> float:
        return self._price
    
    def __str__(self) -> str:
        return f"R$ {self._price:.2f}"