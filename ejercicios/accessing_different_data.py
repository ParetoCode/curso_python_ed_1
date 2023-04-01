# MUTABILIDAD

numbers = (2, 4, 5, 5)

# index = 0
# last_index = len(numbers)
# while index < len(numbers):
#     numbers[index] = numbers[index] * 2
#     index += 1

# print(numbers)

#### Bucle for list comprenhension pattern
multiplied_numbers = []
for number in numbers:
    multiplied_numbers.append(number * 2)

print(tuple(multiplied_numbers))
print(numbers)