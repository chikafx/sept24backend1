"""lists"""


list_fruits= [
    'apple',
    'mango',
    "pineapple",
    'banana',
    'grape'
]



print(list_fruits[0])
print(type(list_fruits))

list_fruits[4]= True

print(list_fruits)

list_fruits[3]= 24/2/2024

print(list_fruits)

length=len(list_fruits)

print(length)

text= 'hi am kamso and i love to code'

print(len(text))

for i in text:
    print(i)

print(text.split('i'))

email="kamsoobi@gmail.com"

print(email.split('@'))


list_number=[1,2,3,4,5]
# brings out the index of the list
print(list_number[1])

print(list_number[2:])

list_fruits= [
    'apple',
    'mango',
    "pineapple",
    'banana',
    'grape'
]

list_fruits.append('cow')

print(list_fruits)

list_fruits.insert(0,'rice')
print(list_fruits)

list_fruits.append([list_number])
print(list_fruits)
 

list_cars=[
    "G-wagon",
    'Benz',
    'toyota',
    'corrolla'
]

list_cars.extend(list_number)

print(list_cars)

list_cars.remove('Benz')
print(list_cars)

list_cars.reverse()
print(list_cars)

list_fruits
print(list_fruits)


list_data=[
    1,2,3,4,5, [2,4,6,1], 6,[3,6,8,1]
]

list_data.sort

print(list_data)

list_data[5].sort()
list_data[7].sort()
print(list_data)



"""dictionary"""

data={
    'name': 'clara',
    'status':'resident',
}

print(data)
data["name"]= 'kamso'
data["status"]= True
print(data['name'])
print(data['status'])

nested={
    'full_name': 'Kamso Obi',
    'age': '27',
    'status': 'married',
    'address':{
        'street': '123 main street',
        'city': 'lagos',
        'code': [
            1000001,
            1200001,
            1300001,
        ]
    },
    'religion': 'christainity',
    'church':{
        'type':{
            'name':'catholic',
            'location': 'lagos',
            'address':{
                'street': '123 main street',
                'city' : 'lagos',
                'code':[
                    1000011,
                    1230000,
                    1032222,
                ]
            }
        }
    }
}
# print(nested)
print(nested['church']['type']['address']['code'][1])

test_1= [100101, 20202]
test_2 =[30303, 21321]


nested['address']['code'].extend(test_2)
nested['church']['type']['address']['code'].extend(test_1)
# nested['age']['status']['address']['code'].extend(test_1)
# print(nested['age']['status']['address']['code'])

print(nested)