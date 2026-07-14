import random

def guessing_no():
    num = random.randint(1,100)
    
    while True:
        try:

            guess_no = int(input("Enter the guessed numberbetween 1 and 100:"))

            if guess_no < num :
                print("your guess is too low")
            elif guess_no > num :
                print("Your guess is too high")
            else:
                print("super...You guessed correct number")        
    
        except ValueError:
            print("Please enter a valid number")
guessing_no()            