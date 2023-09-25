class Automobile:

    def __init__(self, make:str, model:str, mileage:int = 0) -> None:
        self.make = make
        self.model = model
        self.__mileage = mileage # super private

    @property
    # make it read only wiht 1 underscore, 2 underscores make it private
    def mileage(self):
        return self.__mileage

  


    # MagicMethon representing my objects 
    def __repr__(self):
       return f"{self.__class__.__name__}('{self.make}', {self.model}, {self.__mileage})"
    

car_1 = Automobile('Dacia', 'Duster', 1234)
print(repr(car_1))
print(car_1._Automobile__mileage) # show super private




