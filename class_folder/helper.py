# when to use class/vs static methods

class Item:

    @staticmethod
    def is_integer():
        '''This should do sth that has a relationship with the class,
        but not sth that must be unique per instance
        '''
        pass


    @classmethod
    def instantiate_from_csv(cls):
        '''This should also do sth that has a relationship with the class,
        but usually, those are used to manipulate different structures of data to
        instatiate objects, like with the .CSV file'''
        pass