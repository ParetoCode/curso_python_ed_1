'''
2 variables:
edad:
examen de conducción:
Para que alguien conduzca tiene que:
- Ser mayor de edad
- Haber pasado el examen de conducción
''' 
ADULT_AGE = 18

def can_drive(ADULT_AGE, age, exam_is_passed):
    '''can be refactored, to return ifcase, check in the near future'''
    if age >= ADULT_AGE and exam_is_passed:
        return True
    return False

# adulto con test pasado, puede conducir
assert can_drive(ADULT_AGE, 19, True) == True

# No adulto con test pasado, no puede conducir
assert can_drive(ADULT_AGE, 14, True) == False

# Adulto sin test pasado, no puede conducir
assert can_drive(ADULT_AGE, 21, False) == False

# No adulto sin test pasado, no puede conducir
assert can_drive(ADULT_AGE, 14, False) == False

