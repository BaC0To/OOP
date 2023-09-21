
from item import Item


#class inheritance
class MyKeyboard(Item):
   # child class attribute overrides parent class attribute
   pay_rate = 0.7

   def __init__(self, name: str, price: float, quantity=0):
       # Call to super functions to have access/methods
       super().__init__(
          name, price, quantity
       )
