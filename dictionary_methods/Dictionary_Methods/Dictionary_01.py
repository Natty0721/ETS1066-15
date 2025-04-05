# dict.get(key) Method
# Eg 1 - Student scores
students = {"Sara": 90, "Mekdes": 85}
print(students.get("Sara"))           # 90
print(students.get("Natnael", "N/A")) # N/A

# Eg 2 - Phone book
phone_book = {"Alex": "0911223344", "Betty": "0933001122"}
print(phone_book.get("Alex"))                   # 0911223344
print(phone_book.get("Daniel", "Not Registered"))  # Not Registered

# Eg 3 - Products in stock
stock = {"Bread": 20, "Milk": 15}
print(stock.get("Milk"))                # 15
print(stock.get("Cheese", "Out of Stock")) # Out of Stock

# Eg 4 - Students attendance
attendance = {"Yonas": "Present", "Marta": "Absent"}
print(attendance.get("Marta"))           # Absent
print(attendance.get("Samuel", "No Record"))  # No Record

# dict.keys() Method
# Eg 1 - Student IDs
students = {"Sara": 1, "Mekdes": 2}
print(students.keys())  # dict_keys(['Sara', 'Mekdes'])

# Eg 2 - Book library
books = {"Bible": 12, "Physics": 3}
print(books.keys())  # dict_keys(['Bible', 'Physics'])

# Eg 3 - Flight details
flights = {"ET101": "Addis-Ababa", "ET202": "Lalibela"}
print(flights.keys())  # dict_keys(['ET101', 'ET202'])

# Eg 4 - Fruits list
fruits = {"Coconut": 2, "Apple": 5}
print(fruits.keys())  # dict_keys(['Cocunut', 'Apple'])

# dict.values() Method
# Eg 1 - Student marks
marks = {"Abel": 90, "Hanna": 88}
print(marks.values())  # dict_values([90, 88])

# Eg 2 - Book prices
books = {"History": 300, "Math": 250}
print(books.values())  # dict_values([300, 250])

# Eg 3 - Product quantity
products = {"Eggs": 50, "Butter": 10}
print(products.values())  # dict_values([50, 10])

# Eg 4 - Employees salary
salaries = {"Liya": 7000, "Bereket": 8500}
print(salaries.values())  # dict_values([7000, 8500])
