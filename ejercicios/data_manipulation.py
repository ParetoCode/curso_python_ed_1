first_number = 1
second_number = 2

sum_numbers = first_number + second_number

# es igual a primer numero mas segundo número

assert sum_numbers == 3

# es igual a la suma de primer y segundo numero mas la suma otra vez del primer numero

sum_numbers = sum_numbers + first_number
assert sum_numbers == 4

first_number = sum_numbers

sum_numbers = sum_numbers + first_number

assert sum_numbers == 8