# remove() - Removing a Specific Item by Value
# Example 1: Removing an outdated software from an installation list
installed_software = ["Chrome", "Firefox", "Zoom", "Flash Player"]
installed_software.remove("Flash Player")  # Flash Player is outdated

print("Updated software list:", installed_software)
# Output: ['Chrome', 'Firefox', 'Zoom']

# Example 2: Removing a sold-out product from an online store’s inventory
inventory = ["Laptop", "Tablet", "Smartphone", "Headphones"]
inventory.remove("Tablet")  # Tablets are out of stock

print("Updated inventory:", inventory)
# Output: ['Laptop', 'Smartphone', 'Headphones']

# Example 3: Removing a player from a basketball team after an injury
basketball_team = ["James", "Davis", "Curry", "Durant"]
basketball_team.remove("Davis")  # Davis is injured

print("Updated basketball team:", basketball_team)
# Output: ['James', 'Curry', 'Durant']

# Example 4: Removing a canceled flight from an airline's schedule
flight_schedule = ["Flight 101", "Flight 202", "Flight 303", "Flight 404"]
flight_schedule.remove("Flight 404")  # Flight 404 is canceled

print("Updated flight schedule:", flight_schedule)
# Output: ['Flight 101', 'Flight 202', 'Flight 303']


# 2. pop() - Removing an Item by Position
# Example 1: Removing the last song played from a music playlist
playlist = ["Song A", "Song B", "Song C", "Song D"]
last_song = playlist.pop()  # Last song played is removed

print("Last song removed:", last_song)
print("Updated playlist:", playlist)
# Output: Last song removed: Song D
# Updated playlist: ['Song A', 'Song B', 'Song C']

# Example 2: Removing a customer from a restaurant waitlist after being seated
restaurant_waitlist = ["Alice", "Bob", "Charlie", "David"]
seated_customer = restaurant_waitlist.pop(0)  # Alice gets seated first

print("Seated customer:", seated_customer)
print("Remaining waitlist:", restaurant_waitlist)
# Output: Seated customer: Alice
# Remaining waitlist: ['Bob', 'Charlie', 'David']

# Example 3: Removing the last product added to an online shopping cart
shopping_cart = ["Shoes", "Shirt", "Watch", "Backpack"]
removed_item = shopping_cart.pop()  # Customer removes the last added item

print("Removed item:", removed_item)
print("Updated shopping cart:", shopping_cart)
# Output: Removed item: Backpack
# Updated shopping cart: ['Shoes', 'Shirt', 'Watch']

# Example 4: Removing a dismissed employee from a company's active staff list
employee_list = ["John", "Emma", "Sophia", "Michael"]
dismissed_employee = employee_list.pop(2)  # Sophia resigned

print("Dismissed employee:", dismissed_employee)
print("Updated employee list:", employee_list)
# Output: Dismissed employee: Sophia
# Updated employee list: ['John', 'Emma', 'Michael']


# 3. clear() - Removing All Items from a List
# Example 1: Clearing all completed tasks from a to-do list
to_do_list = ["Send emails", "Finish report", "Call client", "Schedule meeting"]
to_do_list.clear()  # All tasks are done

print("To-do list after clear:", to_do_list)
# Output: []

# Example 2: Clearing an online shopping cart after checkout
shopping_cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
shopping_cart.clear()  # Checkout is completed

print("Shopping cart after clear:", shopping_cart)
# Output: []

# Example 3: Clearing a chat conversation history after deleting messages
chat_history = ["Hello!", "How are you?", "Let’s meet at 5 PM", "Okay!"]
chat_history.clear()  # Conversation history is cleared

print("Chat history after clear:", chat_history)
# Output: []

# Example 4: Clearing all entries from a leaderboard after a game reset
leaderboard = ["Player1", "Player2", "Player3", "Player4"]
leaderboard.clear()  # Game session ends, resetting scores

print("Leaderboard after clear:", leaderboard)
# Output: []
