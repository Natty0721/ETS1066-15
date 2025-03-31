# append() 
# 1. Adding a new guest to a coffee ceremony
coffee_ceremony_guests = ["Alem", "Biniyam", "Habtamu"]
coffee_ceremony_guests.append("Dereje")  # Dereje arrives and joins
print(coffee_ceremony_guests)
# Output: ['Alem', 'Biniyam', 'Habtamu', 'Dereje']

# 2. Adding a new book to an Amharic literature reading list
amharic_books = ["Fikir Eske Mekabir", "Oromay", "Derasiw"]
amharic_books.append("Tobia")  # A new book is added
print(amharic_books)
# Output: ['Fikir Eske Mekabir', 'Oromay', 'Derasiw', 'Tobia']

# 3. Adding a new minibus taxi route
taxi_routes = ["Bole - Merkato", "Megenagna - Saris", "Piazza - Arat Kilo"]
taxi_routes.append("Mexico - Bethel")  # A new route is added
print(taxi_routes)
# Output: ['Bole - Merkato', 'Megenagna - Saris', 'Piazza - Arat Kilo', 'Mexico - Bethel']


# extend() 
# 1. Expanding an Ethiopian food menu
ethiopian_foods = ["Doro Wot", "Shiro", "Tibs"]
new_dishes = ["Kitfo", "Gomen", "Firfir"]
ethiopian_foods.extend(new_dishes)  # Adding more dishes
print(ethiopian_foods)
# Output: ['Doro Wot', 'Shiro', 'Tibs', 'Kitfo', 'Gomen', 'Firfir']

# 2. Merging two student lists for School
morning_students = ["Mekdes", "Yonas", "Tinsae"]
afternoon_students = ["Abel", "Saron", "Nahom"]
morning_students.extend(afternoon_students)
print(morning_students)
# Output: ['Mekdes', 'Yonas', 'Tinsae', 'Abel', 'Saron', 'Nahom']

# 3. Adding new artists to an Ethiopian music festival lineup
festival_artists = ["Teddy Afro", "Betty G", "Dawit Tsige"]
new_artists = ["Jano Band", "Tilahun Gessesse", "Michael Belayneh"]
festival_artists.extend(new_artists)
print(festival_artists)
# Output: ['Teddy Afro', 'Betty G', 'Dawit Tsige', 'Jano Band', 'Tilahun Gessesse', 'Michael Belayneh']


# insert() 
# 1. Placing a new athlete in the middle of a marathon ranking
ethiopian_runners = ["Haile Gebrselassie", "Kenenisa Bekele"]
ethiopian_runners.insert(1, "Derartu Tulu")  # Inserting in 2nd position
print(ethiopian_runners)
# Output: ['Haile Gebrselassie', 'Derartu Tulu', 'Kenenisa Bekele']

# 2. Adding a new university in the the middle of a list
universities = ["Addis Ababa University", "Hawassa University"]
universities.insert(1, "Bahir Dar University")
print(universities)
# Output: ['Addis Ababa University', 'Bahir Dar University', 'Hawassa University']

# 3. Inserting an important historical event in the Ethiopian timeline
ethiopian_history = ["Battle of Adwa", "Italian Occupation", "Modern Ethiopia"]
ethiopian_history.insert(1, "Zemene Mesafint")
print(ethiopian_history)
# Output: ['Battle of Adwa', 'Zemene Mesafint', 'Italian Occupation', 'Modern Ethiopia']
