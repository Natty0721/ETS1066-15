# count ()
text1 = "Natnael Ayalew Natnael Ayalew"
print(text1.count("Natnael"))  # Output: 2

text2 = "Python programming is fun, Python is powerful!"
print(text2.count("Python"))  # Output: 2

text3 = "Python 1234 Python 1234"
print(text3.count("1234"))  # Output: 2

# replace ()
text1 = "Natnael Ayalew"
print(text1.replace("Ayalew", "Mechatronics"))  # Output: Natnael Mechatronics

text2 = "Python programming"
print(text2.replace("Python", "Java"))  # Output: Java programming

text3 = "Python 1234"
print(text3.replace("1234", "5678"))  # Output: Python 5678

# strip ()
text1 = "   Natnael Ayalew   "
print(text1.strip())  # Output: "Natnael Ayalew" (removes extra spaces)

text2 = "###Python Programming###"
print(text2.strip("#"))  # Output: "Python Programming"

text3 = "   Python 1234   "
print(text3.strip())  # Output: "Python 1234"
