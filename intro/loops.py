import random



# i = 1
# while i <=10:
#     print(i)
#     i+=1


while True:
    number= random.randint(1,15)

    user_guess =int(input('guess a number between 1 and 10:>>'))

    if user_guess==number:
        print('you guessed it')

        break

    else:
        print(f"sorry, the number was {number} try again!")