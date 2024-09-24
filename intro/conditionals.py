data = {
    'name': 'kamso',
    'age': 20,
    'is_student': True,
    'duration': 4,
    'courses':['python' 'javascript', 'react'],
    'address':{
        'street' : '125 main street',
        'city' : 'Lekki',
        'state' : 'lagos'
    }
}

if data['is_student']:
    print('yes, kamso is a student')

if data['age']>18:
    print('kamso is an adult')
    if data['age']>21:
        print('kamso is a major')
    else:
        if data['age']==21:
            print('kamso is a major adult but legally an adult')
        else:
            print('kamso is a minor')

if data['duration'] is 4:
    print('kamso is a full time student')
elif ['duration']<4:
    print('kamso is a part time student')

if data['address']['street'] == '123 main street':
    print('kamso lives in lekki')
else:
    print('kamso lives in the trenches')