# definición de Jorge:
'''
Un cacho de código que acepta variables y que funciona cuando lo llamas / activas
'''

def can_drive(ADULT_AGE, age, exam_is_passed):    
    if age >= ADULT_AGE and exam_is_passed:
        print('Puedes conducir')
    else:
        print('No puedes conducir')
    

can_drive(18, 19, True)

