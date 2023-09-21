
from item import Item


CSV_FILENAME = 'items.csv'
JSON_FILENAME = 'other_items.json'



#class inheritance
class Phone(Item):
  

   def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):
       # Call to super functions to have access/methods
       super().__init__(
          name, price, quantity
       )
       #Run validations to received args
       
       assert broken_phones >= 0, f'Broken Phones {broken_phones} is not greater than zero!'

       #dynamically assign an unique atrribute to an instance
      
       self.broken_phones = broken_phones


