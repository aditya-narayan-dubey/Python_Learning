numbers = [10, 25, 5, 99, 42]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
