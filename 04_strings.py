text = "python is fun and coding is awesome"

print("Original:", text)

print("Upper:", text.upper())
print("Title:", text.title())

print("Length:", len(text))

print("Words:", text.split())

print("First word:", text.split()[0])
print("Last word:", text.split()[-1])

print("Reverse:", text[::-1])

print("Replace fun with cool:", text.replace("fun", "cool"))

print("Starts with python?", text.startswith("python"))
print("Ends with awesome?", text.endswith("awesome"))