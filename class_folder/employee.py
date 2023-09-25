from datetime import datetime, date

class Employee:

    num_of_emps = 0
    raise_amount = 1

    def __init__(self, first: str, last: str, pay: int = 0):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'
        
        Employee.num_of_emps += 1

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        pass
    
    @classmethod
    def from_string(cls, emp_str:str):
        splitted_data = emp_str.split('-')
        first = splitted_data[0] 
        last = splitted_data[1] 
        pay = splitted_data[2]
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() in range(0,5):
            return True
        else:
            print('Luckily it is  not a workday')
            return False


        # MagicMethon representing my objects 
    def __repr__(self):
       return f"{self.__class__.__name__}('{self.first}', {self.last}, {self.pay}, {self.email})"


    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)




class Developer(Employee): # class inheritance
    
    
    raise_amount = 1.10
    def __init__(self, first: str, last: str, pay: int = 0, prog_lang: str = 'None'):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
class Manager(Employee):

    def __init__(self, first: str, last: str, pay: int = 0, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
             self.employees = employees
    
    def add_empoyee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_empoyee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)     
            
    def print_empoyees(self):
        for emp in self.employees:
            print('--->', emp.fullname())


    
#emp_1 = Employee('Test_FisrtName_1','Test_LastName_1')

emp_1_str = 'Vasil-Kirov-1234'
emp_1=Employee.from_string(emp_1_str)
