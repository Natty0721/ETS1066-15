# The next method I choose to practice is "List Methods in Python"

A "list" in Python is like a shopping bag where you can keep different items together.
We can add, remove, or change items as needed.
List methods help us modify these lists efficiently.

# Let me show you with examples

1 append() - Adding One Item at the End
- Imagine you are buying groceries at a supermarket. You have a list of items. 
- you need, and while shopping, you remember you need "Berbere" 
- Instead of rewriting the whole list, you simply add "Berbere" to the end.

shopping_list = ["Injera", "Shiro", "Teff", "Coffee"]
shopping_list.append("Berbere")  # which is adding an item to the end of the list

# Let's print the updated list
print("Shopping List after append:", shopping_list)
# Output: ['Injera', 'Shiro', 'Teff', 'Coffee', 'Berbere']


# 2. extend() - Adding Multiple Items at the End
- Now, imagine you are preparing for an Ethiopian holiday feast.
- You remember that you also need "Doro Wot", "Kitfo", and "Tibs".
- Instead of adding one item at a time, you can add all of them at once.
holiday_foods = ["Doro Wot", "Kitfo", "Tibs"]
shopping_list.extend(holiday_foods)  # Extending the shopping list with multiple items

# Let's print the updated list
print("Shopping List after extend:", shopping_list)
# Output: ['Injera', 'Shiro', 'Teff', 'Coffee', 'Berbere', 'Doro Wot', 'Kitfo', 'Tibs']


# 3. insert() - Adding an Item at a Specific Position
- Let's say you are organizing your bookshelf, and you want to place the Bible at the first position because it's the most important book.
- The insert() method allows you to put an item in a specific position.

bookshelf = ["Mathematics", "Physics", "Programming"]
bookshelf.insert(0, "Bible")  # Inserting 'Bible' at the first position

# Let's print the updated list
print("Bookshelf after insert:", bookshelf)
# Output: ['Bible', 'Mathematics', 'Physics', 'Programming']

To summarize our today's list methods are
# append()  – Adds one item at the end of the list.
# extend()  – Adds multiple items at the end.
# insert()  – Adds an item at a specific position.