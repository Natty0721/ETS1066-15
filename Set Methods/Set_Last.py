# set.discard() Method
# Eg 1 - Discarding a finished task
tasks = {"Clean", "Cook", "Read"}
tasks.discard("Cook")
print(tasks)  # {'Clean', 'Read'}

# Eg 2 - Removing student from club
club = {"Sara", "Mekdes", "Abel"}
club.discard("Abel")
print(club)  # {'Sara', 'Mekdes'}

# Eg 3 - Safe discard of unknown value
items = {"Milk", "Sugar"}
items.discard("Salt")  # No error even if Salt doesn't exist
print(items)  # {'Milk', 'Sugar'}

# Eg 4 - Discard borrowed book
library = {"Bible", "Math", "Physics"}
library.discard("Physics")
print(library)  # {'Bible', 'Math'}


# set.pop() Method
# Eg 1 - Remove random fruit
fruits = {"Apple", "Banana", "Mango"}
fruits.pop()
print(fruits)  # Output varies

# Eg 2 - Pop a student from waiting list
waiting = {"Alex", "Betty", "Noah"}
waiting.pop()
print(waiting)  # Output may vary

# Eg 3 - Pop from sensor list
sensors = {"Temp", "Humidity", "Vibration"}
sensors.pop()
print(sensors)

# Eg 4 - Pop an order
orders = {"Order1", "Order2", "Order3"}
orders.pop()
print(orders)


# set.clear() Method
# Eg 1 - Clear task list
tasks = {"Wash", "Study", "Exercise"}
tasks.clear()
print(tasks)  # set()

# Eg 2 - Clear shopping cart
cart = {"Soap", "Shampoo", "Toothpaste"}
cart.clear()
print(cart)  # set()

# Eg 3 - Clear saved playlists
playlist = {"Jazz", "Gospel", "Rock"}
playlist.clear()
print(playlist)  # set()

# Eg 4 - Clear participant names
participants = {"Liya", "Yonas", "Marta"}
participants.clear()
print(participants)  # set()