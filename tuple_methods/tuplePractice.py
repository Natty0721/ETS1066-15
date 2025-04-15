# tuple.count() Method
# Eg 1 - Counting scores
scores = (90, 85, 90, 78)
print(scores.count(90))  # 2

# Eg 2 - Counting attendance records
attendance = ("Present", "Absent", "Present", "Present")
print(attendance.count("Present"))  # 3

# Eg 3 - Counting product codes
codes = ("P001", "P002", "P001", "P003")
print(codes.count("P001"))  # 2

# Eg 4 - Counting weather status
weather = ("Rain", "Sunny", "Rain", "Cloudy")
print(weather.count("Rain"))  # 2


# tuple.index() Method
# Eg 1 - Finding score position
scores = (70, 80, 90, 100)
print(scores.index(90))  # 2

# Eg 2 - Finding first absent
attendance = ("Present", "Absent", "Present", "Absent")
print(attendance.index("Absent"))  # 1

# Eg 3 - Finding city in travel list
cities = ("Addis", "Lalibela", "Gondar", "Bahir Dar")
print(cities.index("Gondar"))  # 2

# Eg 4 - First occurrence of item code
items = ("ID1", "ID2", "ID3", "ID2")
print(items.index("ID2"))  # 1
