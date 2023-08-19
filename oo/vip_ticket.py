from ticket import Ticket

class VIPTicket(Ticket):
    def __init__(self, price: float, additional: float):
        super().__init__(price)
        self._additional = additional

    @property
    def additional(self) -> float:
        return self._additional
    
    def __str__(self) -> str:
        return f"R$ {(self._price + self._additional):.2f}"