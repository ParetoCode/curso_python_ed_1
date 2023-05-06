school_data = {
    1 : {'name': 'Adri', 'age':7},
    2 : {'name': 'Emma', 'age':5}
}

high_school = {
    1: {'name': 'Adrián', 'marks': 10},
    2 :{'name': 'Emma G.', 'marks': 10.0}
}

school_data_keys = school_data.keys()

for id in school_data_keys:
    high_school[id]['age'] = school_data[id]['age'] + 5

assert high_school == { 1: {'name': 'Adrián', 'marks': 10, 'age': 12},
                        2 :{'name': 'Emma G.', 'marks': 10.0, 'age':10}
                        }

for id, value in school_data.items():
    high_school[id]['age'] = value.get('age', 0) + 5

assert high_school == { 1: {'name': 'Adrián', 'marks': 10, 'age': 12},
                        2 :{'name': 'Emma G.', 'marks': 10.0, 'age':10}
                        }