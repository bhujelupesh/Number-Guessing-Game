import random

secrete_number = random.randint(1,100)

print("---------Welcome to the Number Guessing Game---------")
print("The number I am guessing is in the range of 1 and 100")

while True:
    guess = int(input("Enter your guess:\n"))

    if guess == secrete_number:
        print("Congratulation you have guess the Number correctly")
        break

    elif guess > secrete_number:
        print("The number is less then the number you guesssing")

    else:
        print("The number is more then then you are thinking")  
