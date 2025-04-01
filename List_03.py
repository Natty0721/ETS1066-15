# index() - Finding the Position of an Item in a List
# Example 1: Finding the position of a booked seat in a movie theater
seats = ["A1", "A2", "A3", "A4", "A5"]
seat_number = seats.index("A3")  # Finding where seat "A3" is

print("Seat A3 is at position:", seat_number)
# Output: Seat A3 is at position: 2

# Example 2: Finding the position of a specific subject in a semester course list
courses = ["Mathematics", "Physics", "Programming", "AI", "Robotics"]
course_position = courses.index("AI")

print("AI is the", course_position + 1, "course in the semester list")
# Output: AI is the 4th course in the semester list

# Example 3: Finding the position of a famous movie in a recommendation list
movies = ["Inception", "Interstellar", "Avengers", "Joker", "Titanic"]
movie_position = movies.index("Joker")

print("Joker is ranked", movie_position + 1, "on the recommendation list")
# Output: Joker is ranked 4 on the recommendation list

# Example 4: Finding where a player's name appears in a football squad
players = ["Messi", "Ronaldo", "Mbappe", "Neymar", "Haaland"]
player_position = players.index("Neymar")

print("Neymar is the", player_position + 1, "player in the squad list")
# Output: Neymar is the 4th player in the squad list


# 2. count() - Counting How Many Times an Element Appears
# Example 1: Counting how many times "Python" appears in a programming language list
languages = ["Python", "Java", "Python", "C++", "Python", "JavaScript"]
python_count = languages.count("Python")

print("Python appears", python_count, "times in the list")
# Output: Python appears 3 times in the list

# Example 2: Counting how many times a customer orders "Burger" in a fast-food system
orders = ["Burger", "Pizza", "Burger", "Pasta", "Burger", "Salad"]
burger_count = orders.count("Burger")

print("Burger was ordered", burger_count, "times")
# Output: Burger was ordered 3 times

# Example 3: Counting the number of times a student was absent in an attendance list
attendance = ["Present", "Absent", "Present", "Absent", "Present", "Present"]
absent_count = attendance.count("Absent")

print("The student was absent", absent_count, "times")
# Output: The student was absent 2 times

# Example 4: Counting how many times a word appears in a text
words = ["hello", "world", "hello", "python", "hello", "code"]
hello_count = words.count("hello")

print("The word 'hello' appears", hello_count, "times")
# Output: The word 'hello' appears 3 times


# 3. sort() - Sorting a List in Ascending or Descending Order
# Example 1: Sorting exam scores from lowest to highest
scores = [85, 92, 78, 90, 88, 76, 95]
scores.sort()

print("Sorted scores:", scores)
# Output: Sorted scores: [76, 78, 85, 88, 90, 92, 95]

# Example 2: Sorting a list of city names alphabetically
cities = ["New York", "Paris", "Tokyo", "London", "Sydney"]
cities.sort()

print("Cities sorted alphabetically:", cities)
# Output: Cities sorted alphabetically: ['London', 'New York', 'Paris', 'Sydney', 'Tokyo']

# Example 3: Sorting product prices from high to low
prices = [250, 100, 450, 300, 150]
prices.sort(reverse=True)  # Sorting in descending order

print("Prices sorted from high to low:", prices)
# Output: Prices sorted from high to low: [450, 300, 250, 150, 100]

# Example 4: Sorting names in a class list alphabetically
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
students.sort()

print("Sorted student names:", students)
# Output: Sorted student names: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
