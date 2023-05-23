class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def calculate_total_price(self) -> float:
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate
