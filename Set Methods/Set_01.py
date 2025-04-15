# set.add() Method
# Eg 1 - Add a student to a class list
students = {"Sara", "Mekdes"}
students.add("Abel")
print(students)  # {'Sara', 'Abel', 'Mekdes'}

# Eg 2 - Add a new city to visited list
visited = {"Addis", "Gondar"}
visited.add("Lalibela")
print(visited)  # {'Addis', 'Gondar', 'Lalibela'}

# Eg 3 - Add new tag to blog post
tags = {"Python", "Coding"}
tags.add("Tutorial")
print(tags)  # {'Python', 'Tutorial', 'Coding'}

# Eg 4 - Add course to student record
courses = {"Math", "Physics"}
courses.add("Biology")
print(courses)  # {'Math', 'Biology', 'Physics'}


# set.update() Method
# Eg 1 - Add multiple fruits
fruits = {"Apple"}
fruits.update(["Banana", "Orange"])
print(fruits)  # {'Banana', 'Orange', 'Apple'}

# Eg 2 - Merge user roles
roles = {"Admin"}
roles.update({"Editor", "Viewer"})
print(roles)  # {'Admin', 'Viewer', 'Editor'}

# Eg 3 - Add new devices to a network
devices = {"Printer"}
devices.update(["Scanner", "Camera"])
print(devices)  # {'Scanner', 'Camera', 'Printer'}

# Eg 4 - Update subjects list
subjects = {"English"}
subjects.update(["History", "Civics"])
print(subjects)  # {'Civics', 'History', 'English'}


# set.remove() Method
# Eg 1 - Remove a course
courses = {"Math", "Physics", "Biology"}
courses.remove("Biology")
print(courses)  # {'Math', 'Physics'}

# Eg 2 - Remove a registered guest
guests = {"Betty", "Noah", "Yared"}
guests.remove("Noah")
print(guests)  # {'Betty', 'Yared'}

# Eg 3 - Remove a hobby
hobbies = {"Reading", "Cycling", "Painting"}
hobbies.remove("Cycling")
print(hobbies)  # {'Reading', 'Painting'}

# Eg 4 - Remove a feature from app settings
features = {"Dark Mode", "Notifications", "Backup"}
features.remove("Backup")
print(features)  # {'Dark Mode', 'Notifications'}