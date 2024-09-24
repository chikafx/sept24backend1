import random

# Write a program that prints the numbers from 10 to 1 in reverse order. When the countdown reaches 1, print "Liftoff!".

# explanation: a range takes 3 argument(start, stop and step): d step value is d increment btw each num

for i in range(10, 0, -1):
    print(i)
print("Liftoff!")


#  Q2: Write a program that checks each number between 1 and 20 to determine if it’s odd or even. Print “even” for even numbers and “odd” for odd numbers.
# explanation: we can use the modulus operator (%) to find the remainder of a division operation.

for num in range (1, 21):
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')


# Write a program that simulates a number guessing game. The program should choose a random number between 1 and 10, and the user has to guess it. If the guess is correct, print "You guessed it!". If the guess is too high or too low, print "Too high!" or "Too low!" respectively. The game should continue until the user guesses the correct number.

while True:
    number= random.randint(1,10)

    Pablo_guess=int(input('guess whats on my mind:----->'))

    if Pablo_guess==number:
        print('God save you!!')
    else:
        if Pablo_guess > 10:
            print('abeg joor, the number too high')
        else:
            if Pablo_guess<0:
                print('stop whinning me na, the number is too low')
            else:
                print(f"sorry baby the number is {number} try again")
    
    


    # else:
    #     if Pablo_guess >= number:
    #         print('Too high')
    #     else:   
    #         if Pablo_guess <= number:
    #             print('Too low')
    #         
        