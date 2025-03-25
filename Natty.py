# index ()
text1 = "Natnael Ayalew is a student"
print(text1.index("Ayalew"))  # Output: 8

text2 = "Python programming is fun"
print(text2.index("gram"))  # Output: 10

text3 = "Python 1234"
print(text3.index("robot"))  # Raises ValueError: substring not found

# startwith () 
text1 = "Natnael Ayalew"
print(text1.startswith("Natnael"))  # Output: True

text2 = "Python programming"
print(text2.startswith("Java"))  # Output: False

text3 = "Python 1234"
print(text3.startswith("Python"))  # Output: True

# endwith ()
text1 = "Natnael Ayalew"
print(text1.endswith("Ayalew"))  # Output: True

text2 = "Python programming"
print(text2.endswith("script"))  # Output: False

text3 = "Python 1234"
print(text3.endswith("1234"))  # Output: True
