# join() String
text1 = ["Mechatronics", "Engineering"]
print(" ".join(text1))  # Output: "Mechatronics Engineering"

text2 = ["AI", "Machine Learning", "Deep Learning"]
print(" - ".join(text2))  # Output: "AI - Machine Learning - Deep Learning"

text3 = ["10", "20", "30", "40"]
print("|".join(text3))  # Output: "10|20|30|40"

# isalpha() String
text1 = "Robotics"
print(text1.isalpha())  # Output: True

text2 = "Automation123"
print(text2.isalpha())  # Output: False (Contains numbers)

text3 = "Embedded Systems"
print(text3.isalpha())  # Output: False (Contains a space)

# isdigit() String
text1 = "987654"
print(text1.isdigit())  # Output: True

text2 = "IoT2024"
print(text2.isdigit())  # Output: False (Contains letters)

text3 = "404 Not Found"
print(text3.isdigit())  # Output: False (Contains a space and text)
