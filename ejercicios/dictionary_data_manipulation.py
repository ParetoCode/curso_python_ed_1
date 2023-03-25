

matetematico = {
    'a' : [1, 1]
}

b = matetematico['a']

matetematico['a'].append(3)

print(b)


# value is simple

simple_dict = {
    'a': True
}

b = simple_dict['a']
simple_dict['a'] = False
print(b)