if 4 > 1:
    print('4 es mayor que 1')
    print('y además esto')

if 4 < 1:
    print('esto no debe verse')
else:
    print('4 NO es menor que 1')

print('pasa lo que está fuera')

# Combinados

# and == además (todo tiene que ser True)

print(True and True and True and True)
print(True and True and False and True)

# or CON QUE UNO SEA CIERTO, es True

print(False or False or False or False)
print(False or False or True)

# con parentesis

truly_or_falsy = True and (True or (False and (True and True)))
                 # True and  #True
print(truly_or_falsy)     
