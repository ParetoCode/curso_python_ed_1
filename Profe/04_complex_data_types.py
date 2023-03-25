##### LISTAS
# listas: -> indice, mutables

shopping_list = ['eggs', 'potatos', 'gummy bears']
                 # 0        #1          #2

# print(shopping_list)

assert shopping_list[0] == 'eggs'
assert shopping_list[1] == 'potatos'
assert shopping_list[2] == 'gummy bears'

# compramos huevos
shopping_list[0] = 'X'

# print(shopping_list)
size = len(shopping_list)
# print('Longitud antes del append', size)

shopping_list.append('bananas')
# print(shopping_list)

next_size = len(shopping_list)
# print('Longitud después del append', next_size)

####### TUPLAS
# tuplas: -> indice, NO mutables

prime_numbers = (2, 3, 5, 7)
                #0, 1, 2, 3  

# print(prime_numbers[0])
# prime_numbers[0] = 'whatever' DA ERROR


#### SET inmutables, no indice (ni orden), no se repiten

group_a = {'Joselyn', 'Victor', 'Jose', 'Joselyn'}
# print(group_a)

group_b = {'Jorge', 'Alberto', 'Ramón', 'Jose'}
# print(group_b)

common = group_a.intersection(group_b)
# print(common)

union = group_b.union(group_a)
# print(union)

### DICCIONARIOS no indice, no orden. clave y valor.

pareto_code_academy = {'group_a': ['Joselyn', 'Victor'],
                       'group_b': ['Jorge', 'Alberto'] }

print(pareto_code_academy['group_a'])
# print(pareto_code_academy['group_b'])
       