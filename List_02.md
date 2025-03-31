# My today's practice is on the following list methods

1. remove() - Removing a Specific Item by **Value**
- Imagine you are managing a list of Ethiopian taxi routes you use frequently. 
- But one day, you find out that the "Bole to Megenagna" route is no longer available, so you need to remove it from your list.

taxi_routes = ["Bole to Piassa", "Bole to Megenagna", "Sarbet to Mexico", "Arat Kilo to Stadium"]
taxi_routes.remove("Bole to Megenagna")  # Removing the unavailable route

print("Taxi Routes after remove:", taxi_routes)
# Output: ['Bole to Piassa', 'Sarbet to Mexico', 'Arat Kilo to Stadium']


2. pop() - Removing an Item  by **Position**
- Now, imagine you are selling concert tickets for a big Ethiopian music festival.  
- The first person in line gets their ticket, and you need to remove their name from the queue.

ticket_queue = ["Abebe", "Hana", "Yonas", "Lidya"]
served_customer = ticket_queue.pop(0)  # The first person gets their ticket

print("Served Customer:", served_customer)
print("Remaining Queue after pop:", ticket_queue)
# Output: Served Customer: Abebe
# Remaining Queue after pop: ['Hana', 'Yonas', 'Lidya']


3. clear() - Removing All Items from a List
- Imagine you are keeping track of students present in a Python class.  
- At the end of the session, you want to clear the attendance list for the next day.

attendance_list = ["Natnael", "Mekdes", "Samuel", "Bethelem"]
attendance_list.clear()  # Clearing the entire list

print("Attendance List after clear:", attendance_list)
# Output: []
