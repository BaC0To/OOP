from class_folder.my_book import Book
import unittest

class TestMyBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")


    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)

    def tearDown(self):
        print("Running tearDown method...")
        del self.book_1
        del self.book_2
    
    def test_get_reading_time(self):
        print("Running test_get_reading_time...")
        expected_value1 = 304*1.5
        self.assertEqual(self.book_1.get_reading_time(), f'Estimated reading time: {expected_value1} minutes')
        expected_value2 = 447*1.5
        self.assertEqual(self.book_2.get_reading_time(), f'Estimated reading time: {expected_value2} minutes')

    def test_apply_selectable_discount(self):
        print("Running test_apply_selectable_discount...")
        expected_value1 = 13.6
        self.assertEqual(self.book_2.apply_selectable_discount(), f'Book new price: {expected_value1} after applied selectable discount of: {0.15}')
    
    def test_apply_fixed_discount(self):
        print("Running test_apply_fixed_discount...")
        expected_value1 = 13.5
        self.assertEqual(self.book_1.apply_fixed_discount(), f'Book new price: {expected_value1} after applied fixed discount of: {0.1}')
        expected_value2 = 14.4
        self.assertEqual(self.book_2.apply_fixed_discount(), f'Book new price: {expected_value2} after applied fixed discount of: {0.1}')
        
    
    @classmethod
    def tearDownClass(cls):
    	print("\ntearDownClass method: Runs after all tests...")

if __name__=='__main__':
            unittest.main()
            