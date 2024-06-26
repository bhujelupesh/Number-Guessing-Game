import random

print("---------Welcome to the Number Guessing Game---------")
print("Select mode of the games you want to play")
print("1 - Easy Mode \n2 - Hard Mode")

mode = int(input("Enter your choice: "))

if mode == 1:
    secrete_number = random.randint(1,100)
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
            
elif mode == 2:
    secrete_number = random.randint(1,1000)
    print("The number I am guessing is in the range of 1 and 1000")
    print("You have 10 guesses: ")
    for i in range (10):
        guess = int(input(f"Enter your guess no {i+1}:\n"))

        if guess == secrete_number:
            print(f"Congratulation you have guess the Number correctly on your {i+1} guesses")
            break

        elif guess > secrete_number:
            print(f"The number is less then the number you guesssing and {9-i} guess remaining")

        else:
            print(f"The number is more then then you are thinking and {9-i} guess remaining")  
            
else:
    print("Invalid choice")
