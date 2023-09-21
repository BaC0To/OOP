
class Book:

    pay_rate = 10/100

    def __init__(self,title: str, author: str, pages: int, price, discount: float = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.__price = price
        self.discount = discount

    @property
    # Property Decorator = Read-only Attribute
    def price(self):
       return self.__price
    
    def apply_fixed_discount(self):
        #method that ovverides the price attribute
        self.__price = self.__price - (self.__price * self.pay_rate)
        price_with_fixed_dscount = self.__price
        return f'Book new price: {price_with_fixed_dscount} after applied fixed discount of: {self.pay_rate}'
    
    def apply_selectable_discount(self):
    #method that ovverides the price attribute
        self.__price = self.__price - (self.__price * self.discount)
        price_with_selectable_dscount = self.__price
        return f'Book new price: {price_with_selectable_dscount} after applied selectable discount of: {self.discount}'
    
    def get_reading_time(self):
        reading_time = self.pages * 1.5
        return f'Estimated reading time: {reading_time} minutes'
    
    # MagicMethon representing my objects 
    def __repr__(self):
       return f"{self.__class__.__name__}('{self.title}', {self.author}, {self.pages}, {self.__price}, {self.discount})"
