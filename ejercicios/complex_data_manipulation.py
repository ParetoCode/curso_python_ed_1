# SIMPLE

a = 1
b = a
a = 2

# print('a vale: ', a)
# print('b vale: ', b)

# COMPLEX

a = [1, 1]
b = a
a = [0, 1]

# print('a vale: ', a) # [0, 1]
# print('b vale: ', b) # [1, 1]

###

a = [1, 1]
b = a
a[0] = 0

print('a vale: ', a) # [0, 1]
print('b vale: ', b) # [1, 1]