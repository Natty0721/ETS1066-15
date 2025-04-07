# dict.clear() Method
# Eg 1 - Clearing student list
students = {"Sara": 90, "Mekdes": 85}
students.clear()
print(students)  # {}

# Eg 2 - Clearing shopping cart
cart = {"Bread": 2, "Milk": 1}
cart.clear()
print(cart)  # {}

# Eg 3 - Resetting a scoreboard
scoreboard = {"Team A": 5, "Team B": 3}
scoreboard.clear()
print(scoreboard)  # {}

# Eg 4 - Erasing saved settings
settings = {"theme": "dark", "volume": "low"}
settings.clear()
print(settings)  # {}

# dict.copy() Method
# Eg 1 - Backup student grades
grades = {"Abel": 92, "Hanna": 88}
backup = grades.copy()
print(backup)  # {'Abel': 92, 'Hanna': 88}

# Eg 2 - Duplicating employee records
employees = {"Alex": "HR", "Sara": "Finance"}
new_employees = employees.copy()
print(new_employees)  # {'Alex': 'HR', 'Sara': 'Finance'}

# Eg 3 - Copying a settings template
template = {"font": "Arial", "size": 12}
user_settings = template.copy()
print(user_settings)  # {'font': 'Arial', 'size': 12}

# Eg 4 - Backup inventory data
inventory = {"Eggs": 100, "Milk": 50}
backup_inventory = inventory.copy()
print(backup_inventory)  # {'Eggs': 100, 'Milk': 50}

# dict.fromkeys() Method
# Eg 1 - Create subjects with default score
subjects = ["Math", "English", "Science"]
scores = dict.fromkeys(subjects, 0)
print(scores)  # {'Math': 0, 'English': 0, 'Science': 0}

# Eg 2 - Student attendance initialization
students = ["Liya", "Bereket", "Natnael"]
attendance = dict.fromkeys(students, "Absent")
print(attendance)  # {'Liya': 'Absent', 'Bereket': 'Absent', 'Natnael': 'Absent'}

# Eg 3 - Inventory items with zero stock
items = ["Sugar", "Salt", "Oil"]
stock = dict.fromkeys(items, 0)
print(stock)  # {'Sugar': 0, 'Salt': 0, 'Oil': 0}

# Eg 4 - Event RSVP list
guests = ["Betty", "Noah", "Yared"]
rsvp = dict.fromkeys(guests, False)
print(rsvp)  # {'Betty': False, 'Noah': False, 'Yared': False}