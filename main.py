from class_folder.my_book import Book


book1 = Book('Mein_Kampf','Uncle_Adi',666,100)

print(book1)
book1.apply_fixed_discount()
print(book1)
user_discount = float(input("Enter user discount: "))
book1.apply_selectable_discount(user_discount)
print(book1)