# -------------------------------
# STRING BASICS
# -------------------------------

s1 = "Hello"
s2 = 'World'
s3 = """This is a
multi-line string"""

print(s1)
print(s2)
print(s3)

# -------------------------------
# STRING INDEXING & SLICING
# -------------------------------

text = "PythonProgramming"

print(text[0])       # First character
print(text[-1])      # Last character
print(text[0:6])     # Python
print(text[6:])      # Programming
print(text[::2])     # Skip characters
print(text[::-1])    # Reverse string

# -------------------------------
# STRING CONCATENATION
# -------------------------------

a = "Hello"
b = "World"

print(a + " " + b)   # Hello World

# -------------------------------
# STRING REPEAT
# -------------------------------

print("Hi " * 3)

# -------------------------------
# STRING METHODS
# -------------------------------

msg = "  python is fun  "

print(msg.upper())       # PYTHON IS FUN
print(msg.lower())       # python is fun
print(msg.strip())       # remove spaces
print(msg.replace("fun", "awesome"))
print(msg.find("is"))    # index of substring

# -------------------------------
# CHECK FUNCTIONS
# -------------------------------

data = "Python123"

print(data.isalpha())    # False
print(data.isalnum())    # True
print(data.isdigit())    # False

# -------------------------------
# SPLIT & JOIN
# -------------------------------

sentence = "I love Python programming"

words = sentence.split(" ")
print(words)

joined = "-".join(words)
print(joined)

# -------------------------------
# STRING FORMATTING
# -------------------------------

name = "Rahul"
age = 20

print("My name is {} and age is {}".format(name, age))
print(f"My name is {name} and age is {age}")

# -------------------------------
# ESCAPE CHARACTERS
# -------------------------------

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python is awesome\"")

# -------------------------------
# STRING LOOPING
# -------------------------------

for char in "Python":
    print(char)

# -------------------------------
# COUNT & LENGTH
# -------------------------------

text = "banana"
print(len(text))
print(text.count("a"))

# -------------------------------
# CHECK SUBSTRING
# -------------------------------

if "thon" in "Python":
    print("Found")

# -------------------------------
# PALINDROME CHECK
# -------------------------------

word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# -------------------------------
# REMOVE VOWELS
# -------------------------------

string = "Hello World"
vowels = "aeiouAEIOU"

result = ""
for ch in string:
    if ch not in vowels:
        result += ch

print(result)

# -------------------------------
# STRING COMPARISON
# -------------------------------

print("abc" == "abc")
print("abc" > "abd")

# -------------------------------
# ASCII VALUES
# -------------------------------

print(ord("A"))   # ASCII value
print(chr(65))    # Character

# -------------------------------
# ADVANCED: STRING COMPRESSION
# -------------------------------

input_str = "aaabbcc"
compressed = ""

count = 1
for i in range(len(input_str)):
    if i < len(input_str)-1 and input_str[i] == input_str[i+1]:
        count += 1
    else:
        compressed += input_str[i] + str(count)
        count = 1

print(compressed)