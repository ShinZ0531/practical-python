class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
        
    @property
    def cost(self) -> float:
        return self.shares * self.price
    
    def sell(self, nshares) -> None:
        self.shares -= nshares
        
        
class MyStock(Stock):
    def __init__(self, name: str, shares: int, price: float, factor: str = ''):
        super().__init__(name, shares, price)
        self.factor = factor
    
    def panic(self) -> None:
        self.sell(self.shares)
        
    @property    
    def cost(self) -> float:
        # return 1.25 * self.shares * self.price
        actual_cost = super().cost
        return 1.25 * actual_cost