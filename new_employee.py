
from datetime import date, datetime

class Employee:
    

    def __init__(self, first_name, last_name, birth_date:str, start_date:str,total_wrk_days = 0):
        self.first_name = first_name
        self.last_name = last_name
        self._birth_date = birth_date
        self.start_date = start_date
        self.total_wrk_days = total_wrk_days

    @property
    def birth_date(self): #converts an attribute to a read-only
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        date_object = datetime.strptime(value, '%d-%m-%Y').date()
        print(f'new_birthday {date_object}, type: {type(date_object)}')
        self._birth_date = str(date_object)

    
    def calc_total_work_days(self):
        today = date.today().strftime("%Y-%m-%d") # in string
        end_date = datetime.strptime(today, "%Y-%m-%d") # in DateTime Object
        start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
        self.total_wrk_days = abs(start_date - end_date).days
        return self.total_wrk_days
        
        
    def __repr__(self) -> str:
        return f"Employee's data: {self.first_name} {self.last_name}, born on: {self._birth_date}, started on: {self.start_date}, total workdays: {self.total_wrk_days}"



emp_1 = Employee('Vasil', 'Kirov', '1986-09-15', '2023-09-01')
#print(emp_1.birth_date)
#emp_1.birth_date = '1999-12-12'
#emp_1.birth_date = '2000-01-01'

#print(emp_1.birth_date)
#print(type(emp_1.birth_date))
#emp_1.birth_date = '01-01-2022'
print(repr(emp_1))
emp_1.total_wrk_days = 10
print(repr(emp_1))
emp_1.calc_total_work_days()
print(repr(emp_1))
