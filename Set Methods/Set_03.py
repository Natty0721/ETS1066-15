# set.symmetric_difference() Method
# Eg 1 - Unique students in two classes
class_A = {"Sara", "Mekdes", "Abel"}
class_B = {"Abel", "Yonas", "Hanna"}
unique_students = class_A.symmetric_difference(class_B)
print(unique_students)  # {'Sara', 'Yonas', 'Hanna', 'Mekdes'}

# Eg 2 - Non-overlapping followers
my_followers = {"Liya", "Selam"}
your_followers = {"Selam", "Yonas"}
different_people = my_followers.symmetric_difference(your_followers)
print(different_people)  # {'Liya', 'Yonas'}

# Eg 3 - Exclusive books in libraries
lib1 = {"Bible", "Math", "Biology"}
lib2 = {"Math", "History", "English"}
exclusive_books = lib1.symmetric_difference(lib2)
print(exclusive_books)

# Eg 4 - Different tasks between two teams
team1_tasks = {"Design", "Test"}
team2_tasks = {"Test", "Deploy"}
unshared_tasks = team1_tasks.symmetric_difference(team2_tasks)
print(unshared_tasks)


# set.issubset() Method
# Eg 1 - Check if club is part of school
club_members = {"Sara", "Abel"}
all_students = {"Sara", "Abel", "Mekdes", "Yonas"}
print(club_members.issubset(all_students))  # True

# Eg 2 - Check subject requirement
core_subjects = {"Math", "English"}
grade10 = {"Math", "English", "Civics"}
print(core_subjects.issubset(grade10))  # True

# Eg 3 - Event guest list
invited = {"Alex", "Marta"}
attended = {"Marta", "Alex", "Liya"}
print(invited.issubset(attended))  # True

# Eg 4 - Access roles in a system
limited_roles = {"Viewer"}
all_roles = {"Admin", "Editor", "Viewer"}
print(limited_roles.issubset(all_roles))  # True


# set.issuperset() Method
# Eg 1 - Check if all students are registered
registered = {"Sara", "Abel", "Yonas", "Mekdes"}
new_students = {"Sara", "Abel"}
print(registered.issuperset(new_students))  # True

# Eg 2 - Check skill match
my_skills = {"Python", "Problem Solving", "Communication"}
required_skills = {"Python", "Communication"}
print(my_skills.issuperset(required_skills))  # True

# Eg 3 - Library check
library_books = {"Bible", "Physics", "Chemistry", "Math"}
borrowed_books = {"Bible", "Math"}
print(library_books.issuperset(borrowed_books))  # True

# Eg 4 - Parent set of club
school_group = {"Sara", "Liya", "Abel", "Mekdes"}
coding_club = {"Sara", "Abel"}
print(school_group.issuperset(coding_club))  # True
