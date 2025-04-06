# dict.items() Method
# Eg 1 - Student records
students = {"Sara": 90, "Mekdes": 85}
print(students.items())  # dict_items([('Sara', 90), ('Mekdes', 85)])

# Eg 2 - Library book counts
library = {"Bible": 3, "Math": 5}
print(library.items())  # dict_items([('Bible', 3), ('Math', 5)])

# Eg 3 - Product and price
shop = {"Bread": 25, "Milk": 15}
print(shop.items())  # dict_items([('Bread', 25), ('Milk', 15)])

# Eg 4 - Employee roles
employees = {"Marta": "Manager", "Yonas": "Engineer"}
print(employees.items())  # dict_items([('Marta', 'Manager'), ('Yonas', 'Engineer')])

# dict.pop() Method
# Eg 1 - Remove a student
students = {"Sara": 90, "Mekdes": 85}
print(students.pop("Sara"))  # 90
print(students)  # {'Mekdes': 85}

# Eg 2 - Remove a fruit
fruits = {"Apple": 3, "Banana": 5}
print(fruits.pop("Banana"))  # 5
print(fruits)  # {'Apple': 3}

# Eg 3 - Remove from a basket
basket = {"Mango": 2, "Pineapple": 1}
print(basket.pop("Mango"))  # 2
print(basket)  # {'Pineapple': 1}

# Eg 4 - Remove a contact
contacts = {"Alex": "0911223344", "Daniel": "0933001122"}
print(contacts.pop("Daniel"))  # 0933001122
print(contacts)  # {'Alex': '0911223344'}

# dict.update() Method
# Eg 1 - Update student scores
scores = {"Sara": 90}
scores.update({"Sara": 95})
print(scores)  # {'Sara': 95}

# Eg 2 - Add new subject
subjects = {"Math": 80}
subjects.update({"Science": 85})
print(subjects)  # {'Math': 80, 'Science': 85}

# Eg 3 - Update shop stock
stock = {"Bread": 20}
stock.update({"Bread": 15, "Milk": 10})
print(stock)  # {'Bread': 15, 'Milk': 10}

# Eg 4 - Update employee roles
employees = {"Marta": "Manager"}
employees.update({"Yonas": "Developer"})
print(employees)  # {'Marta': 'Manager', 'Yonas': 'Developer'}