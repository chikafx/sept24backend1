datas = [
    {
        "name": "Kamso",
        "age": 21,
        "is_student": True,
        "duration": 4,
        "courses": ["Python", "Javascript", "React"],
        "address": {
            "street": "123 Main Street",
            "city": "Lekki",
            "state": "Lagos"
        }
    },
    {
        "name": "Ada",
        "age": 18,
        "is_student": False,
        "duration": 4,
        "courses": ["Python", "Javascript", "React"],
        "address": {
            "street": "123 Main Street",
            "city": "Lekki",
            "state": "Lagos"
        }
    },
    {
        "name": "Joe",
        "age": 16,
        "is_student": True,
        "duration": 5,
        "courses": ["Python", "Javascript", "React"],
        "address": {
            "street": "123 Main Street",
            "city": "Lekki",
            "state": "Lagos"
        }
    },
    {
        "name": "Ebube",
        "age": 22,
        "is_student": False,
        "duration": 4,
        "courses": ["Python", "Javascript", "React"],
        "address": {
            "street": "123 Main Street",
            "city": "Lekki",
            "state": "Lagos"
        }
    }
]


for i in datas:
    if i['is_student'] is False:
        print(f"{i['name']} is not an active student")

    else:
        print(f"{i['name']} is an active student")
        if i['age'] < 21:
            print(f"{i['name']} is not an adult")
        else:
            if i["age"] > 21:
                print(f"{i['name']} is an adult")
for i in datas:
            if i['duration'] is 4:
                print(f"{i['name']} is a full time student")
            else:
                 print(f"{i['name']} is a part time student")

for i in datas:
    courses = i['courses']
    if 'Python' in courses:
        print(f"{i['name']} is good at python")
        
