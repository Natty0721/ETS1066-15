# dict.items() Method
#Eg 1 - Student data
students = {"Sara": 90, "Mekdes": 85}
print(students.items())  # dict_items([('Sara', 90), ('Mekdes', 85)])

#Eg 2 - Product prices
products = {"Milk": 25, "Bread": 10}
print(products.items())  # dict_items([('Milk', 25), ('Bread', 10)])

#Eg 3 - Countries and capitals
countries = {"Ethiopia": "Addis Ababa", "Kenya": "Nairobi"}
print(countries.items())  # dict_items([('Ethiopia', 'Addis Ababa'), ('Kenya', 'Nairobi')])

#Eg 4 - Library records
library = {"Book1": "Borrowed", "Book2": "Available"}
print(library.items())  # dict_items([('Book1', 'Borrowed'), ('Book2', 'Available')])

# dict.pop() Method
# Eg 1 - Remove a student
students = {"Sara": 90, "Mekdes": 85}
students.pop("Sara")
print(students)  # {'Mekdes': 85}

# Eg 2 - Remove out-of-stock item
stock = {"Milk": 15, "Cheese": 0}
stock.pop("Cheese")
print(stock)  # {'Milk': 15}

# Eg 3 - Remove cancelled order
orders = {"Order1": "Delivered", "Order2": "Cancelled"}
orders.pop("Order2")
print(orders)  # {'Order1': 'Delivered'}

# Eg 4 - Remove employee
employees = {"Alex": "HR", "Hanna": "Tech"}
employees.pop("Alex")
print(employees)  # {'Hanna': 'Tech'}

# dict.update() Method
# Eg 1 - Update student score
students = {"Sara": 90}
students.update({"Sara": 95})
print(students)  # {'Sara': 95}

# Eg 2 - Add new product
products = {"Milk": 20}
products.update({"Bread": 10})
print(products)  # {'Milk': 20, 'Bread': 10}

# Eg 3 - Merge settings
default = {"theme": "light"}
user = {"theme": "dark", "font": "Arial"}
default.update(user)
print(default)  # {'theme': 'dark', 'font': 'Arial'}

# Eg 4 - Add new employees
team = {"Liya": "Designer"}
new_hires = {"Samuel": "Dev", "Betty": "Tester"}
team.update(new_hires)
print(team)  # {'Liya': 'Designer', 'Samuel': 'Dev', 'Betty': 'Tester'}