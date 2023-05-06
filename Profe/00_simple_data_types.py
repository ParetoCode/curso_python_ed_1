# ESTE COMENTARIO ES DE UNA LINEA

'''
ESTE COMENTARIO SON VARIAS
LINEAS
'''

# PERSONALEMENTE PREFIERO
# ESTE FORMATO PARA COMENTARIOS
# DE VARIAS LINEAS


# TIPOS DE DATO SENCILLO
## NUMERICOS
### ENTEROS
10
## "AZUCAR SINTACTICO" ENTEROS GRANDES 
10_000_000
10000000

assert 10_000_000 == 10000000

### FLOTANTE
10.5

## STRING -> "CADENA DE TEXTO"

'H'

'HOLA'

"HOLA"

'''HOLA
MUNDO
'''

"""HOLA
MUNDO
"""

## BOOLEAN -> BOOLEANO

True
False

## None
None


print(type(None))
print(type(('a')))
print(type(1))
print(type(1.4))
print(type(True))


## SECOND DAY: OPERATIONS

number = 3
print('number multiplicado por 2 es: ',number * 2)
print('number sumado 1 es: ', number + 1)
print('number menos 1 es: ', number - 1)
print('number dividido por 2 es: ', number / 2)


## Strings o texto

my_text = 'hola pareto'

capitalized_text = my_text.capitalize()

assert 'Hola pareto' == capitalized_text
assert 'hola pareto' == my_text

print(my_text)
print(capitalized_text)

assert my_text.startswith('hola')

greeting = 'Hola'
name = 'Joselyn'

final_text = greeting + ' ' + name
print(final_text)

number = 5
word = 'times'
how_many_times = f'{number} {word}  puedo añadir cosas'
print(how_many_times)
print(word*number)

