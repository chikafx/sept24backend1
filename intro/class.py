print("Hello world!")

print (type(2))
print (type(3.3))

print (type('clara'))

name= 'king'
print (name)
print (type(name))

age, height = 23, 5.5
print(age, height)
print(age, height, name)

status= "single"
# this is called the concatinating string
text= name + ' is ' + status

print(text)

# this is called an (f) string
new_text= f"{name} is {status}"

print(new_text)

age= "29"
status="married"
zodiac_sign="leo"
occupation="fullstack"
internship= "univelcity"

#this is called the {F} formatter
bio= f"""

my name is {name} i am currently {status}, i am {age}
my zodiac sign is {zodiac_sign} and my occupation{occupation}
and i am currently interning at {internship}

"""

print(bio)



name="king"

