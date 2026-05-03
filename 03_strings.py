text = input("Kuch likh: ")

print("\n--- STRING MAGIC ---")

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

print("Length:", len(text))

print("First character:", text[0])
print("Last character:", text[-1])

print("Reverse:", text[::-1])

word = input("\nEk word find kar: ")

if word in text:
    print("Mil gaya 😎")
else:
    print("Nahi mila 😢")

new_text = text.replace("a", "@")
print("Replace a with @:", new_text)