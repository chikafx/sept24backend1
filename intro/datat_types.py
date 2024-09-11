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