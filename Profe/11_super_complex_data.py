school_data = {
    1 : {'name': 'Adri', 'details': {'age':7, 'actitud':'positive'}},
    2 : {'name': 'Emma', 'details': {'age':5, 'actitud':'rebel'}}
}

high_school = {
    1: {'name': 'Adrián', 'marks': 10},
    2 :{'name': 'Emma G.', 'marks': 10.0}
}

for id, value in school_data.items():
    high_school[id]['age'] = value['details']['age'] + 5
    high_school[id]['actitud'] = value['details']['actitud']

assert high_school == {
    1: {'name': 'Adrián', 'marks': 10, 'age':12, 'actitud': 'positive'},
    2 :{'name': 'Emma G.', 'marks': 10.0, 'age':10, 'actitud': 'rebel'}
}