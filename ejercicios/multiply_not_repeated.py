# Dada una tupla, de números enteros
# retornar como resultado una lista
# sin repetir ningun elemento multiplicados x 2


def multiply_not_repeated(origin_data):
    multiplied_numbers = []
    multiplied_data = []

    for number in origin_data:
        if number not in multiplied_numbers:
            multiplied_data.append(number * 2)
            multiplied_numbers.append(number)

    return multiplied_data


## test tupla sin elementos duplicados

def test_origin_data_without_repeated_numbers():
    # preparación
    numbers = (1, 3, 5)

    # actuación
    result = multiply_not_repeated(numbers)

    # assert
    assert result == [2, 6, 10]
    print('TEST 1 PASSED')

def test_origin_data_with_a_number_repeated():
    # arrange
    numbers = (1, 1, 2, 4)

    # act
    result = multiply_not_repeated(numbers)

    # assert
    assert result == [2 ,4, 8]
    print('TEST 2 PASSED')


test_origin_data_without_repeated_numbers()
test_origin_data_with_a_number_repeated()
