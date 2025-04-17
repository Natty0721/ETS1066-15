# set.union() Method
# Eg 1 - Union of two friend groups
group1 = {"Sara", "Mekdes"}
group2 = {"Abel", "Yonas"}
all_friends = group1.union(group2)
print(all_friends)  # {'Sara', 'Mekdes', 'Abel', 'Yonas'}

# Eg 2 - Union of cities visited
trip1 = {"Addis", "Gondar"}
trip2 = {"Lalibela", "Bahir Dar"}
places = trip1.union(trip2)
print(places)

# Eg 3 - Union of two subject lists
subjects_sem1 = {"Math", "Physics"}
subjects_sem2 = {"Biology", "Chemistry"}
all_subjects = subjects_sem1.union(subjects_sem2)
print(all_subjects)

# Eg 4 - Union of two sports teams
team_A = {"Alex", "Marta"}
team_B = {"Samuel", "Alex"}
full_team = team_A.union(team_B)
print(full_team)


# set.intersection() Method
# Eg 1 - Common books in two libraries
library1 = {"Bible", "Math", "History"}
library2 = {"History", "English", "Bible"}
common_books = library1.intersection(library2)
print(common_books)  # {'Bible', 'History'}

# Eg 2 - Students in both clubs
club1 = {"Sara", "Liya", "Abel"}
club2 = {"Abel", "Yonas", "Sara"}
both_clubs = club1.intersection(club2)
print(both_clubs)

# Eg 3 - Mutual followers
my_followers = {"Betty", "Noah", "Selam"}
your_followers = {"Selam", "Natnael", "Betty"}
mutuals = my_followers.intersection(your_followers)
print(mutuals)

# Eg 4 - Shared subjects
grade10 = {"Math", "English", "Civics"}
grade11 = {"Biology", "Civics", "Math"}
shared = grade10.intersection(grade11)
print(shared)


# set.difference() Method
# Eg 1 - Unique items in cart1
cart1 = {"Soap", "Shampoo", "Brush"}
cart2 = {"Brush", "Toothpaste"}
unique_to_cart1 = cart1.difference(cart2)
print(unique_to_cart1)  # {'Soap', 'Shampoo'}

# Eg 2 - Cities I visited but you didn’t
my_trip = {"Addis", "Hawassa", "Dire Dawa"}
your_trip = {"Addis", "Gondar"}
only_mine = my_trip.difference(your_trip)
print(only_mine)

# Eg 3 - Tasks only I completed
my_tasks = {"Wash", "Cook", "Read"}
team_tasks = {"Wash", "Read"}
solo_tasks = my_tasks.difference(team_tasks)
print(solo_tasks)

# Eg 4 - Subjects I passed but you didn’t
my_passed = {"Math", "Physics", "Chemistry"}
your_passed = {"Math", "Biology"}
better_grades = my_passed.difference(your_passed)
print(better_grades)