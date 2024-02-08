number = 10

def guess_num(g, n):    #function checks if guess g is equal to number n
    if g == n:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry. That is incorrect.")
        hint(g, n)

def hint(g, n):
    if g > n:
        print("Your guess is higher than the number I'm thinking of.")
    if g < n:
        print("Your guess is lower than the number I'm thinking of.")

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

guess_num(guess, number)    #Initial check for the user's guess. If guess is incorrect, it will code will proceed to loop.

while guess != number:  #As long as the user's guess is incorrect, they be able to try again
    option = input("Enter 'q' to quit, or press ENTER to continue. ")   #option variable for user
    if option != 'q':   #As long as the user does not enter 'q', they will be able to try again
        guess = int(input("What number am I thinking of? "))
        guess_num(guess, number)
    else:   #If the user enters 'q', they are given the answer and the while loop ceases
        print(f"Okay. The number was {number}")
        break
