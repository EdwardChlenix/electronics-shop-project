import csv




class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            return "Слишком длинное наименование"

    def calculate_total_price(self) -> float:
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\\Users\\User92\\PycharmProjects\\pythonProject\\electronics-shop-project\\src\\items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                #print(row['name'], row['price'], row['quantity'])
                Item(row['name'], row['price'], row['quantity'])

#Item.instantiate_from_csv()
#print(Item.all)

    @staticmethod
    def string_to_number(string):

        return int(string)



