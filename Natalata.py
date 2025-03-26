# lstrip() String
text1 = "   Mechatronics Engineering"
print(text1.lstrip())  # Output: "Mechatronics Engineering"

text2 = "***Python Programming***"
print(text2.lstrip("*"))  # Output: "Python Programming***"

text3 = "###Python 5678"
print(text3.lstrip("#"))  # Output: "Python 5678"

# rstrip() String
text1 = "Software Development   "
print(text1.rstrip())  # Output: "Software Development"

text2 = "###JavaScript Programming###"
print(text2.rstrip("#"))  # Output: "###JavaScript Programming"

text3 = "Machine Learning!!!!"
print(text3.rstrip("!"))  # Output: "Machine Learning"

# split() String
text1 = "Electrical Mechanical Civil"
print(text1.split())  # Output: ['Electrical', 'Mechanical', 'Civil']

text2 = "Data-Science-ML-AI"
print(text2.split("-"))  # Output: ['Data', 'Science', 'ML', 'AI']

text3 = "Python|Java|C++|Rust"
print(text3.split("|"))  # Output: ['Python', 'Java', 'C++', 'Rust']
