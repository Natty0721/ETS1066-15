# append
# Example 1: Adding a student to a class roster
students = ["Alice", "Bob", "Charlie"]
students.append("David")
print(students)  # Output: ['Alice', 'Bob', 'Charlie', 'David']

# Example 2: Adding an item to a shopping cart
shopping_cart = ["Apples", "Bananas", "Milk"]
shopping_cart.append("Bread")
print(shopping_cart)  # Output: ['Apples', 'Bananas', 'Milk', 'Bread']

# Example 3: Recording a new bank transaction
transactions = [100, -50, 200, -30]
transactions.append(500)
print(transactions)  # Output: [100, -50, 200, -30, 500]


# extend() – Merging Two Lists

# Example 1: Merging two playlists
playlist1 = ["Song A", "Song B", "Song C"]
playlist2 = ["Song D", "Song E"]
playlist1.extend(playlist2)
print(playlist1)  # Output: ['Song A', 'Song B', 'Song C', 'Song D', 'Song E']

# Example 2: Adding new books to a library catalog
library_books = ["Book 1", "Book 2", "Book 3"]
new_books = ["Book 4", "Book 5"]
library_books.extend(new_books)
print(library_books)  # Output: ['Book 1', 'Book 2', 'Book 3', 'Book 4', 'Book 5']

# Example 3: Combining two project teams
team_A = ["Alice", "Bob"]
team_B = ["Charlie", "David"]
team_A.extend(team_B)
print(team_A)  # Output: ['Alice', 'Bob', 'Charlie', 'David']