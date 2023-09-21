import csv
import json
import os
from pathlib import Path


CSV_FILENAME = 'items.csv'
JSON_FILENAME = 'other_items.json'

class Item:
    
    #class atrbutes
    pay_rate = 0.8 # The pay rate after 20% discount for all instances

    all = []
    
    #MagicMethod constructor
    def __init__(self, name: str, price: float, quantity=0):
       #Run validations to received args
       assert price >= 0, f'Price {price} is not greater than zero!'
       assert quantity >= 0, f'Quantity {quantity} is not greater than zero!'
       
       #dynamically assign an unique atrribute to an instance
       self.name = name
       self.price = price
       self.quantity = quantity

       #actions to execute
       Item.all.append(self)

    def calculate_total_price(self):
      return self.quantity * self.price
      

    def apply_discout(self):
       #method that ovverides the price attribute
       self.price = self.price * self.pay_rate

    
    @classmethod
    def instantiate_from_csv(cls):
        with open(Path(os.path.join(os.getcwd(), 'config_files',CSV_FILENAME)), 'r') as f:
           reader = csv.DictReader(f)
           items = list(reader)
        for item in items:
           Item(
              name = item.get('name'),
              price = float(item.get('price')),
              quantity = int(item.get('quantity'))
           )
    
    @classmethod
    def instantiate_from_json(cls):
       with open(Path(os.path.join(os.getcwd(), 'config_files',JSON_FILENAME)), 'r') as f:
          json_data = json.load(f)
          for item in json_data:
             """ print(item)
             name = item.get('name')
             price = float(item.get('price'))
             quantity = int(item.get('quantity'))
             print(f'Objects instantiated with: {name}, {price}, {quantity}') """
             Item(
                name = item.get('name'),
                price = item.get('price'),
                quantity = item.get('quantity')
             )
    @staticmethod
    def is_integer(num):
       if isinstance(num, float):
          # cout  out the floats that are .0 eg 7.0
          return num.is_integer()
       elif isinstance(num, int):
          return True
       else:
          return False

     # MagicMethon representing my objects 
    def __repr__(self):
       return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_json()
print(Item.all)
