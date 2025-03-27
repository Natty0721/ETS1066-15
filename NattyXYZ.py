# isalnum() String
name1 = "Natnael2025"
print(name1.isalnum())  # Output: True (Only letters and numbers)

name2 = "Python 3.9"
print(name2.isalnum())  # Output: False (Contains space and period)

name3 = "CodeMaster123"
print(name3.isalnum())  # Output: True (Only letters and numbers)

# isspace() String
message1 = "   "  
print(message1.isspace())  # Output: True (Only whitespace)

message2 = "Hello World"
print(message2.isspace())  # Output: False (Contains letters)

message3 = "\n\t  "  
print(message3.isspace())  # Output: True (Newline and tab are also whitespace)

# format() String
intro = "Hi, my name is {} and I love {}."
print(intro.format("Natnael", "coding"))  
# Output: "Hi, my name is Natnael and I love coding."

price_info = "The {} costs ${:.2f}."
print(price_info.format("smartphone", 599.99))  
# Output: "The smartphone costs $599.99."

exam_score = "{} scored {} marks in {} class."
print(exam_score.format("Helen", 90, "Physics"))  
# Output: "Helen scored 90 marks in Physics class."