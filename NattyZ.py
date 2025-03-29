# f-strings (Formatted String Literals)
name = "Natnael"
age = 21
language = "Python"

print(f"My name is {name}, I am {age} years old, and I love {language}.")
# Output: "My name is Natnael, I am 21 years old, and I love Python."

price = 99.99
item = "Laptop"
print(f"The {item} costs ${price:.2f}.")
# Output: "The Laptop costs $99.99."

# len() - String Length
greeting = "Hello, Ethiopia!"
print(len(greeting))  
# Output: 16 (Counts characters including spaces and punctuation)

empty_string = ""
print(len(empty_string))  
# Output: 0 (Empty string has no characters)

long_text = "Python is powerful"
print(len(long_text))  
# Output: 19 (Counts all letters and spaces)

# encode() - Encoding Strings
text = "Hello, world!"
encoded_utf8 = text.encode("utf-8")
print(encoded_utf8)  
# Output: b'Hello, world!' (Byte representation in UTF-8)

emoji_text = "🔥 Python is amazing! 🔥"
encoded_utf16 = emoji_text.encode("utf-16")
print(encoded_utf16)  
# Output: Encoded byte data for UTF-16 format
