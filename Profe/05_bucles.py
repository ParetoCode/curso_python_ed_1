prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 , 97]

print(len(prime_numbers))

# DRY -> DO NOT REPEAT YOURSELF
"""
index = 0
while index <= 24:
    prime_number = prime_numbers[index]
    print(prime_number)
    index = index + 1 # index += 1
"""

print('SAME THING BUT WITH BUCLE FOR')

# for -> para cada
# elemento
# in lista
for prime_number in prime_numbers:
    print(prime_number)